#                       Copyright 2021 Saad Mairaj
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import pickle
import tkinter


def SaveVar(var, master=None, value=None, name=None, filename='data.pkl'):
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
            tmpdict = pickle.load(open1)  # load saved dictionary data.
            # Block of code to check for the right value.
            if tmpdict.get(str(var)):
                old, default = tmpdict.get(str(var))
                new = var.get()
                if new != default:
                    var.set(new)
                elif not startup[0]:
                    var.set(default)
                else:
                    var.set(old)
            tmpdict.update({str(var): (var.get(), defaultval)})
            open1.close()
        except FileNotFoundError:
            tmpdict = {}
            tmpdict[str(var)] = (var.get(), defaultval)

        open2 = open(filename, 'wb')
        pickle.dump(tmpdict, open2)
        startup[0] = False
        open2.close()

    startup = [True]
    if not(filename.endswith('.pickle') or filename.endswith('.pkl')) \
            and not filename.startswith('.'):
        filename = filename+'.pkl'
    var = var(master=master, value=value, name=name)
    defaultval = var.get()  # get a default value of the variable
    update_val()
    for mode, cbname in (var.trace_vinfo()):
        if mode[0] == 'w' and update_val.__name__ in cbname:
            try:
                var.trace_vdelete('w', cbname)
            except tkinter.TclError:
                pass
    var.trace_variable('w',  update_val)
    return var
