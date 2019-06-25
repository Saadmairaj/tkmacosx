'''
Newer style colorchoosers for tkinter module.

Version: 0.1.0
'''

import tkinter as tk
from tkmacosx.basewidget import _Canvas
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import font
import numpy as np
import os


class Colorscale(_Canvas):
    """
    ## Color Scale.
    This is ColorScale alternate to tkinter's colorchooser. 

    ### Args: 
    - `value`: Get either 'RGB' or 'HEX'.
    - `command`: callback function with an argument.
    - `orient`: Set the orientation.
    - `mousewheel`: Set mousewheel to scroll marker.
    - `variable`: Give tkinter variable (`StringVar`).
    - `showinfo`: Shows hex or rbg while selecting color.
    - `showinfodelay`: Delay before the showinfo disappears (in ms).
    """

    def __init__(self, master=None, cnf={}, **kw):
        kw = tk._cnfmerge((cnf, kw))
        self.cnf = {
            'value'         :    kw.pop('value', 'rgb'),
            'command'       :    kw.pop("command", None),
            'orient'        :    kw.pop('orient', 'vertical'),
            'mousewheel'    :    kw.pop("mousewheel", True),
            'variable'      :    kw.pop('variable', None),
            'showinfo'      :    kw.pop('showinfo', True),
            'showinfodelay' :    kw.pop('showinfodelay', 1500),
        }
        kw['width'] = kw.get("width",  250 if 'ver' in self.cnf['orient'] else 30)
        kw['height'] = kw.get("height", 30 if 'ver' in self.cnf['orient'] else 250)
        kw['highlightthickness'] = kw.get('highlightthickness', 0)
        tk.Canvas.__init__(self, master=master, **kw)
        self.xy_axis = int(self.winfo_width()/3)
        self._size = (0,0)

        self.np_im = np.load(os.path.dirname
                (os.path.abspath(__file__))+"/images/colorscale.npy")
        self.image_id = self._image(0, 0, anchor='nw')

        # Binds
        self.bind_class(self, '<Button-1>', self.move_marker, '+')
        self.bind_class(self, "<B1-Motion>", self.move_marker, '+')
        self.set_mousewheel()
        self.bind_class(self, '<Configure>', self.on_resize, '+')
    
    def set_mousewheel(self):
        '''Intenal function. Sets mousewheel scrolling.'''
        def on_mousewheel(evt=None):
            "Internal function."
            if evt.delta <= -1 and bool(self.xy_axis < self.winfo_width() \
                or self.xy_axis < self.winfo_height()):
                self.xy_axis += 1
                self.move_marker(evt, mw=self.xy_axis)
            if evt.delta >= 1 and self.xy_axis > 1:
                self.xy_axis -= 1
                self.move_marker(evt, mw=self.xy_axis)

        if self.cnf['mousewheel']:
            self.bind("<MouseWheel>", on_mousewheel)
        else: self.unbind("<MouseWheel>")

    def on_resize(self, evt):
        '''Internal function.'''
        if evt.width == self._size[0] and evt.height == self._size[1]: return
        self._size = (evt.width, evt.height)
        self._im = Image.fromarray(self.np_im).rotate(0 if 'ver' in
                            self.cnf['orient'] else 270, expand=1).resize(
                            (evt.width, evt.height))
        self.pixels = self._im.load()
        self._im = ImageTk.PhotoImage(self._im)
        self.itemconfig(self.image_id, image=self._im)
        
        self.delete('marker')
        self.delete('borderline1')
        self.delete('borderline2')
        self.rounded_rect(1, 1, evt.width-2, evt.height-2, 1, width=2, 
            fill='#81b3f4', tag1='borderline1', tag2='borderline2')
        self.rounded_rect(
            evt.width/3 if 'ver' in self.cnf['orient'] else 2,
            2 if 'ver' in self.cnf['orient'] else evt.height/3,
            5 if 'ver' in self.cnf['orient'] else evt.width-4,
            evt.height-4 if 'ver' in self.cnf['orient'] else 5,
            2, width=2, fill="black", tag="marker")
        
    def configure(self, cnf={}, **kw):
        """Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.
        """
        cnf = tk._cnfmerge((cnf, kw))
        for k in cnf.copy():
            if k in self.cnf.keys():
                self.cnf[k] = cnf.pop(k)
        self.set_mousewheel()
        rv = super().configure(**cnf) 
        if rv is not None:
            rv.update(self.cnf)
            return rv
    config = configure

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in self.cnf.keys():
            return self.cnf[key]
        return super().cget(key)
    __getitem__=cget

    def Release(self, evt=None):
        "Internal function."
        self.delete("info")
        self.delete("markerbg")

    def RGB2HEX(self, R, G, B):
        "Internal function. Use to convert RGB to HEX"
        return '#%02x%02x%02x' % (R, G, B)

    def move_marker(self, evt, mw=None):
        "Internal function."
        if mw:
            evt.x = mw if 'ver' in self.cnf['orient'] else 10
            evt.y = 10 if 'ver' in self.cnf['orient'] else mw

        self.after_cancel(getattr(self, '_remove_id', ' '))
        self._remove_id = self.after(self.cnf['showinfodelay'], self.Release)

        if (evt.x > 0 and evt.y > 0 and evt.x < self.winfo_width() and evt.y < self.winfo_height()):
            if not mw:
                self.xy_axis = evt.x
            RGB = self.pixels[evt.x, evt.y][:-1]
            hexcode = self.RGB2HEX(RGB[0], RGB[1], RGB[2])
            maker_color = 'black' if (
                RGB[0]*0.299 + RGB[1]*0.587 + RGB[2]*0.114) > 110 else 'white'
            
            self.itemconfig('borderline1', outline=hexcode)
            self.itemconfig('borderline2', fill=hexcode)

            if self.cnf['value'] == "rgb":
                spacer = 50
                spacbg = 40
                text = str(RGB)
                self.callback(RGB)
            elif self.cnf['value'] == "hex":
                spacer = 35
                spacbg = 25
                text = hexcode
                self.callback(hexcode)

            self.delete("marker")
            self.Release()

            self.rounded_rect(
                evt.x if 'ver' in self.cnf['orient'] else 2,
                2 if 'ver' in self.cnf['orient'] else evt.y,
                5 if 'ver' in self.cnf['orient'] else self.winfo_width()-4,
                self.winfo_height()-4 if 'ver' in self.cnf['orient'] else 5,
                2, width=2, fill=maker_color, tag="marker")

            if bool(evt.x < self.winfo_width()-100 or evt.y < self.winfo_height()-100) and self['showinfo']:
                self._rounded(
                    evt.x+spacer-spacbg if 'ver' in self.cnf['orient'] else self.winfo_width()/2-6,
                    self.winfo_height()/2-6 if 'ver' in self.cnf['orient'] else evt.y+spacer-spacbg,
                    evt.x+spacer+spacbg if 'ver' in self.cnf['orient'] else self.winfo_width()/2+7,
                    self.winfo_height()/2+7 if 'ver' in self.cnf['orient'] else evt.y+spacer+spacbg,
                    6, fill=maker_color, tag="markerbg")
                self._text(
                    evt.x+spacer if 'ver' in self.cnf['orient'] else self.winfo_width()/2,
                    self.winfo_height()/2 if 'ver' in self.cnf['orient'] else evt.y+spacer,
                    angle=0 if 'ver' in self.cnf['orient'] else 90,
                    text=text, font=Font(size=10), tag="info", fill=hexcode)
            elif self['showinfo']:
                self._rounded(
                    evt.x-spacer-spacbg if 'ver' in self.cnf['orient'] else self.winfo_width()/2-6,
                    self.winfo_height()/2-6 if 'ver' in self.cnf['orient'] else evt.y-spacer-spacbg,
                    evt.x-spacer+spacbg if 'ver' in self.cnf['orient'] else self.winfo_width()/2+7,
                    self.winfo_height()/2+7 if 'ver' in self.cnf['orient'] else evt.y-spacer+spacbg,
                    6, fill=maker_color, tag="markerbg")
                self._text(
                    evt.x-spacer if 'ver' in self.cnf['orient'] else self.winfo_width()/2,
                    self.winfo_height()/2 if 'ver' in self.cnf['orient'] else evt.y-spacer,
                    angle=0 if 'ver' in self.cnf['orient'] else 90,
                    text=text, font=Font(size=10), tag="info", fill=hexcode)

    def callback(self, val):
        "Internal function."
        if self.cnf['variable']:
            self.cnf['variable'].set(val)
        if self.cnf['command']:
            return self.cnf['command'](val)

    def keys(self):
        """Return a list of all resource names of this widget."""
        return list(self.config().keys())


# ------------------------------------ #
#           Testing and demo           #
# ------------------------------------ #

def demo_colorscale():
    root = tk.Tk()
    root.config({"bg": "black"})
    root.title("Tkinter Color Bar")
    CS = Colorscale(root, value='hex')
    CS.pack(side="bottom", padx=3, pady=3)
    root.mainloop()
    return "break"

if __name__ == "__main__":
    demo_colorscale()