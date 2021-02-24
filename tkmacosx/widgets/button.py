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

from tkmacosx.basewidgets.button_base import ButtonBase


class Button(ButtonBase):
    """Button widget."""

    def __init__(self, master=None, cnf={}, **kw):
        """Button for macos, supports almost all the features of tkinter button,

            - There are few extra features as compared to default Tkinter Button:
            - To check the list of all the resources. To get an overview about
                the allowed keyword arguments call the method `keys`. 
                    print(Button().keys())

        ### Examples:
        ```
        import tkinter as tk
        import tkmacosx as tkm
        import tkinter.ttk as ttk

        root = tk.Tk()
        root.geometry('200x200')
        tkm.Button(root, text='Mac OSX', bg='lightblue', fg='yellow').pack()
        tk.Button(root, text='Mac OSX', bg='lightblue', fg='yellow').pack()
        ttk.Button(root, text='Mac OSX').pack()
        root.mainloop()
        ```

        ### Get a cool gradient effect in activebackground color.
        ```
        import tkinter as tk
        import tkmacosx as tkm

        root = tk.Tk()
        root.geometry('200x200')
        tkm.Button(root, text='Press Me!!', activebackground=('pink','blue') ).pack()
        tkm.Button(root, text='Press Me!!', activebackground=('yellow','green') ).pack()
        tkm.Button(root, text='Press Me!!', activebackground=('red','blue') ).pack()
        root.mainloop()
        ```"""
        ButtonBase.__init__(self, 'normal', master, cnf, **kw)
