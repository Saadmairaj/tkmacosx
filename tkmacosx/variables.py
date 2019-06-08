import tkinter as _TK
import re


# Modified Misc._options(...) to make ColorVar work with tkinter 
_all_traces_colorvar={}
def _options(self, cnf, kw = None):
    """Internal function."""
    if kw: 
        cnf = _TK._cnfmerge((cnf, kw))
    else: 
        cnf = _TK._cnfmerge(cnf)
    
    # ----------- Added the below block -------------
    # Add the resources to the list to have ColorVar functionality. 
    # It'll work as long as it's not an item of canvas or mark_tag of text.
    for i in ('fg','foreground','bg','background',
        'activebackground','activeforeground','disabledforeground',
        'highlightbackground','highlightcolor', 'selectforeground', 
        'readonlybackground', 'selectbackground', 'insertbackground', 
        'disabledbackground', ):        
        if isinstance(cnf.get(i), _TK.Variable):
            var = cnf[i]
            cbname = var.trace_add('write', lambda *a, i=i, 
                    cls=self: cls.config({i: var.get()}) )  
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
            if k[-1] == '_': k = k[:-1]
            if callable(v): v = self._register(v)
            elif isinstance(v, (tuple, list)):
                nv = []
                for item in v:
                    if isinstance(item, int):
                        nv.append(str(item))
                    elif isinstance(item, str):
                        nv.append(_TK._stringify(item))
                    else: break
                else: v = ' '.join(nv)
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
                r,g,b = self._root.winfo_rgb(value)
                c = (r/257, g/257, b/257)
                value = '#%02x%02x%02x' % (int(c[0]),int(c[1]),int(c[2]))
            except: 
                raise ValueError('Could not find right HEX for "{}".'.format(value)) 
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
        if not isinstance(value, dict): value = eval(value)
        if key: return value.get(key, d)
        else: return value


# ------------------ Testing ------------------

def demo_colorvar():
    import colors
    root = _TK.Tk()
    root.geometry('100x100')
    color = ColorVar()
    color_list = list(colors.OrderedHex)
    L = _TK.Label(root, textvariable=color, bg=color)
    L.place(relx=0.5, rely=0.5, anchor='center')
    def change_color(c=0):
        if c >= len(color_list): c=0
        color.set(color_list[c])
        root.after(70, change_color, c+1)
    change_color()
    root.mainloop()

if __name__ == "__main__":
    # demo_colorvar()

    from tkinter import *
    # from tkmacosx import DictVar

    root = Tk()

    dictionary = DictVar(value = {'width': 100, 'height': 200})

    print(type(dictionary.get()))
    print(dictionary.get())
    print(dictionary.get('width'))
    