import re
import ast
import pickle as pkl
import tkinter as _TK


# Modified Misc._options(...) to make ColorVar work with tkinter
_all_traces_colorvar = {}


def _options(self, cnf, kw=None):
    """Internal function."""
    if kw:
        cnf = _TK._cnfmerge((cnf, kw))
    else:
        cnf = _TK._cnfmerge(cnf)

    # ----------- Added the below block -------------
    # Add the resources to the list to have ColorVar functionality.
    # It'll work as long as it's not an item of canvas or mark_tag of text.
    for i in ('fg', 'foreground', 'bg', 'background',
              'activebackground', 'activeforeground', 'disabledforeground',
              'highlightbackground', 'highlightcolor', 'selectforeground',
              'readonlybackground', 'selectbackground', 'insertbackground',
              'disabledbackground', ):
        if isinstance(cnf.get(i), _TK.Variable):
            var = cnf[i]
            cbname = var.trace_add('write', lambda *a, i=i,
                                   cls=self: cls.config({i: var.get()}))
            if (self, i) in _all_traces_colorvar:
                v, cb = _all_traces_colorvar.get((self, i))
                v.trace_remove('write', cb)
                _all_traces_colorvar[(self, i)] = (var, cbname)
            else:
                _all_traces_colorvar[(self, i)] = (var, cbname)
            cnf[i] = var.get()
    # -----------------------------------------------
    res = ()
    for k, v in cnf.items():
        if v is not None:
            if k[-1] == '_':
                k = k[:-1]
            if callable(v):
                v = self._register(v)
            elif isinstance(v, (tuple, list)):
                nv = []
                for item in v:
                    if isinstance(item, int):
                        nv.append(str(item))
                    elif isinstance(item, str):
                        nv.append(_TK._stringify(item))
                    else:
                        break
                else:
                    v = ' '.join(nv)
            res = res + ('-'+k, v)
    return res


_TK.Misc._options = _options


class ColorVar(_TK.Variable):
    """Value holder for HEX color. Default is white"""

    _default = "white"
    _rgbstring = re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$')

    def __init__(self, master=None, value=None, name=None):
        """Construct a color variable. (bg, fg, ..)

        MASTER can be given as master widget.
        VALUE is an optional value (defaults to "")
        NAME is an optional Tcl name (defaults to PY_VARnum).

        If NAME matches an existing variable and VALUE is omitted
        then the existing value is retained.
        """
        super(ColorVar, self).__init__(master, value, name)

    def set(self, value=''):
        """Set the variable to VALUE."""
        if value.startswith('#'):
            if not bool(self._rgbstring.match(value)):
                raise ValueError('{} is not a vaild HEX.'.format(value))
        elif isinstance(value, str):
            try:
                r, g, b = self._root.winfo_rgb(value)
                c = (r/257, g/257, b/257)
                value = '#%02x%02x%02x' % (int(c[0]), int(c[1]), int(c[2]))
            except:
                raise ValueError(
                    'Could not find right HEX for "{}".'.format(value))
        return self._tk.globalsetvar(self._name, value)
    initialize = set

    def get(self):
        """Return value of variable color."""
        value = self._tk.globalgetvar(self._name)
        if isinstance(value, str):
            return value
        return str(value)


class DictVar(_TK.Variable):
    """
    #### Value holder for Dictionaries.
    Get a specific value by getting the key from this \
    `get(self, key=None, d=None)` method if exists in the dictionary. \n
    if `key=None` it will returrn the complete dictionory.
    """
    _default = {}

    def __init__(self, master=None, value=None, name=None):
        """Construct a string variable.

        MASTER can be given as master widget.
        VALUE is an optional value (defaults to {})
        NAME is an optional Tcl name (defaults to PY_VARnum).

        If NAME matches an existing variable and VALUE is omitted
        then the existing value is retained.
        """
        _TK.Variable.__init__(self, master, value, name)

    def get(self, key=None, d=None):
        """Return value of variable as string."""
        value = self._tk.globalgetvar(self._name)
        if not isinstance(value, dict):
            value = ast.literal_eval(value)
        if key:
            return value.get(key, d)
        else:
            return value


def SaveVar(var: _TK.Variable, master=None, value=None, name=None, filename='data.pkl') \
        -> (_TK.Variable):
    """Save tkinter variable data in a pickle file and load the 
    same value when the program is executed next time. 

    #### If the content of the file changes, it might not load correct values \
        to the assigned variables. To avoid this issue use `name` to \
        refer to the exact assigned values later.

    ### Args:
    - `var`: Give the `tkinter.Variable` class like (`tk.StringVar`, `tk.IntVar`).
    - `master`: Parent widget.
    - `value`: Set value.
    - `name`: Set a name to group variables or to refer to assigned value when loaded.
    - `filename`: Set the name of the save file. (To make the file invisible in the \
            directory start the name of the file with "." like ".cache-savevar")

    ### Return:
    - returns the tk.Variable instance passed to `var` argument.

    ### Example:
        root = tk.Tk()
        var1 = SaveVar(tk.StringVar,'Enter Username','Var1','.cache-savevar')
        var2 = SaveVar(tk.StringVar,'Enter Password','Var2','.cache-savevar')
        tk.Entry(root,textvariable=var1).pack()
        tk.Entry(root,textvariable=var2).pack()
        root.mainloop()"""

    def update_val(*args):
        """Internal function for updating the value for variable"""
        try:    # try/except , if the file doesn't exists.
            open1 = open(filename, 'rb')
            tmpdict = pkl.load(open1)  # load saved dictionary data.
            # Block of code to check for the right value.
            if tmpdict.get(str(var)):
                old, default = tmpdict.get(str(var))
                new = var.get()
                if new != default:
                    var.set(new)
                elif new == default and not startup[0]:
                    var.set(default)
                else:
                    var.set(old)
            tmpdict.update({str(var): (var.get(), defaultval)})
            open1.close()
        except Exception as e:
            tmpdict = {}
            tmpdict[str(var)] = (var.get(), defaultval)

        open2 = open(filename, 'wb')
        pkl.dump(tmpdict, open2)
        startup[0] = False
        open2.close()

    startup = [True]
    if not(filename.endswith('.pickle') or filename.endswith('.pkl')) \
            and not filename.startswith('.'):
        filename = filename+'.pkl'
    var = var(master=master, value=value, name=name)
    defaultval = var.get()  # get a default value of the variable
    update_val()
    var.trace_add('write',  update_val)
    return var


# ------------------ Testing ------------------

def demo_colorvar():
    import tkmacosx.colors as colors
    root = _TK.Tk()
    root.geometry('100x100')
    color = ColorVar()
    color_list = list(colors.OrderedHex)
    L = _TK.Label(root, textvariable=color, bg=color)
    L.place(relx=0.5, rely=0.5, anchor='center')

    def change_color(c=0):
        if c >= len(color_list) and root.winfo_exists():
            c = 0
        color.set(color_list[c])
        root.after(100, change_color, c+1)
    change_color()
    root.mainloop()


def demo_savevar():
    root = _TK.Tk()
    var1 = SaveVar(_TK.StringVar, root, 'Enter Username',
                   'Var1', '.cache-savevar')
    var2 = SaveVar(_TK.StringVar, root, 'Enter Password',
                   'Var2', '.cache-savevar')
    _TK.Entry(root, textvariable=var1).pack()
    _TK.Entry(root, textvariable=var2).pack()
    root.mainloop()


if __name__ == "__main__":
    demo_colorvar()
    demo_savevar()
