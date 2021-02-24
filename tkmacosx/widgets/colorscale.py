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


from tkmacosx.basewidgets.colorscale_base import (ColorscaleBase, HEX, RGB)


class Colorscale(ColorscaleBase):
    "Colorscale widget."

    def __init__(self, master=None, cnf={}, **kw):
        """
        ## Color Scale.
        This is ColorScale alternate to colorchooser of tkinter. 

        ### Args: 
        - `value`: Get either 'RGB' or 'HEX'.
        - `command`: callback function with an argument.
        - `orient`: Set the orientation.
        - `mousewheel`: Set mousewheel to scroll marker.
        - `variable`: Give tkinter variable (`StringVar`).
        - `showinfo`: Shows hex or rbg while selecting color.
        - `gradient`: Take tuple of two colors or default.
        - `showinfodelay`: Delay before the showinfo disappears (in ms).
        """
        ColorscaleBase.__init__(self, master=master, cnf=cnf, **kw)
