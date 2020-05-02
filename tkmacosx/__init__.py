"""
This module provides some modified widgets of Tkinter which works better on macos
and some more useful functions and classes as well. For example Button of tkmacosx which 
looks and feels exaclty like a native tkinter button can change its background 
and foreground colors.

Read more about tkmacosx in detail on
https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx.
"""

from tkmacosx.basewidget import check_appearence, get_shade
from tkmacosx.variables import ColorVar, DictVar, demo_colorvar, SaveVar, demo_savevar
from tkmacosx.widget import Button, SFrame, demo_sframe, demo_button
from tkmacosx.colors import Hex, OrderedHex
from tkmacosx.colorscale import Colorscale, demo_colorscale

if __name__ == "__main__":
    demo_sframe()
    demo_button()
    demo_colorvar()
    demo_colorscale()
