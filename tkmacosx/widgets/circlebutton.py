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


class CircleButton(ButtonBase):
    """Circle button widget."""

    def __init__(self, master=None, cnf={}, **kw):
        """
        Circle shaped Button supports almost all options of a tkinter button 
        and have some few more useful options such as 'activebackground', overbackground', 
        'overforeground', 'activeimage', 'activeforeground', 'borderless' and much more. 

        To check all the configurable options for CircleButton run `print(CircleButton().keys())`.

        Example:
        ```
        import tkinter as tk
        import tkmacosx as tkm

        root = tk.Tk()
        cb = tkm.CircleButton(root, text='Hello')
        cb.pack()
        root.mainloop()
        ```
        """
        ButtonBase.__init__(self, 'circle', master, cnf, **kw)
