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

import ast
import tkinter


class DictVar(tkinter.Variable):
    """
    #### Value holder for Dictionaries.
    Get a specific value by getting the key from this \
    `get(self, key=None, d=None)` method if exists in the dictionary. \n
    if `key=None` it will return the complete dictionary.
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
        tkinter.Variable.__init__(self, master, value, name)

    def get(self, key=None, d=None):
        """Return value of variable as string."""
        value = self._tk.globalgetvar(self._name)
        if not isinstance(value, dict):
            value = ast.literal_eval(value)
        if key:
            return value.get(key, d)
        return value
