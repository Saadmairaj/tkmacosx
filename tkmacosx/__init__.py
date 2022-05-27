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

"""
This module provides some modified widgets of Tkinter which works better on macos
and some more useful functions and classes as well. For example Button of tkmacosx which 
looks and feels exactly like a native tkinter button can change its background 
and foreground colors.

Read more about tkmacosx in detail on
https://github.com/Saadmairaj/tkmacosx#tkmacosx
"""

__version__ = '1.0.5'
__author__ = 'Saad Mairaj'

from tkmacosx.variables import ColorVar, DictVar, SaveVar
from tkmacosx.widgets import Button, CircleButton, Colorscale, Radiobutton, Marquee, SFrame
from tkmacosx.utils import (check_appearance, check_light_dark,
                            delta, hex_to_rgb, get_shade, gradient)
