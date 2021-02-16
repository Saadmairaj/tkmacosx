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

import tkinter

# patch to make tkinter.Variable with multiple options of widgets.
from tkmacosx.utils.colorvar_patches import patch
patch()


class ColorVar(tkinter.Variable):
    """Value holder for HEX color. Default is white"""

    _default = "white"

    def __init__(self, master=None, value=None, name=None):
        """Construct a color variable. (bg, fg, ..)

        MASTER can be given as master widget.
        VALUE is an optional value (defaults to "")
        NAME is an optional Tcl name (defaults to PY_VARnum).

        If NAME matches an existing variable and VALUE is omitted
        then the existing value is retained.
        """
        tkinter.Variable.__init__(self, master, value, name)

    def set(self, value):
        """Set the variable to VALUE."""
        self._root.winfo_rgb(value)
        return self._tk.globalsetvar(self._name, value)
    initialize = set

    def get(self):
        """Return value of variable color."""
        value = self._tk.globalgetvar(self._name)
        self._root.winfo_rgb(value)
        return str(value)
