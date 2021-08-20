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

import re
import sys
import colour
import tkinter
from tkinter import ttk
from tkmacosx.utils.check_parameter import Check_Common_Parameters, pixels_conv


STDOUT_WARNING = True


class _appearanceColor:
    """Internal class for button appearance colors.

    Return bg and fg appearance colors if on macos 
    and also compatible with macos."""

    _bg = None
    _fg = None
    _warning_msg_shown = False

    def _check(self, option):
        """Internal function"""
        try:
            tkinter._default_root
        except AttributeError:
            # for running unit tests.
            return False
        try:
            if tkinter._default_root and sys.platform == 'darwin':
                org = tkinter._default_root['bg']
                tkinter._default_root['bg'] = option
                tkinter._default_root['bg'] = org
                return True
        except Exception:
            if not self._warning_msg_shown and STDOUT_WARNING:
                print("WARNING: Appearance colors are either not"
                      "supported with this tkinter or the "
                      "colors doesn't exist on this Mac.")
                self._warning_msg_shown = True
        return False

    @property
    def bg(self):
        """Returns white or macos system window background 
        appearance colour"""
        if self._bg is None:
            self._bg = "white"
            if self._check("systemWindowBackgroundColor"):
                self._bg = "systemWindowBackgroundColor"
        return self._bg

    @property
    def fg(self):
        """Returns black or macos system text appearance colour"""
        if self._fg is None:
            self._fg = "black"
            if self._check("systemTextColor"):
                self._fg = "systemTextColor"
        return self._fg


SYSTEM_DEFAULT = _appearanceColor()


def _agsmerge(args):
    """Internal functions.\n
    Merges lists/tuples."""
    if not isinstance(args, (tuple, list)):
        return args
    a = []
    for i in args:
        if isinstance(i, (tuple, list)):
            a.extend(i)
        else:
            a.append(i)
    return a


def _bind(cls=None, *ags, **kw):
    """Internal function.\n
    Binds and unbinds sequences with any name given as className."""
    cls = cls or kw.pop('cls', ags.pop(0))
    if ags:
        return [_bind(cls=cls, **i) for i in ags]
    classname = kw['className'] + str(cls)
    bindtags = list(cls.bindtags())
    if classname in bindtags:
        bindtags.remove(classname)
    if kw.get('func'):
        _bind(cls, className=kw['className'], sequence=kw['sequence'])
        bindtags.append(classname)
        cls.bindtags(tuple(bindtags))
        return cls.bind_class(classname, sequence=kw['sequence'],
                              func=kw['func'], add=kw.get('add', '+'))
    cls.bindtags(tuple(bindtags))
    cls.unbind_class(classname, kw['sequence'])


def _cnfmerge(cnfs):
    """Internal function."""
    if isinstance(cnfs, (type(None), str, dict)):
        return cnfs
    cnf = {}
    for c in tkinter._flatten(cnfs):
        try:
            if isinstance(c, dict):
                cnf.update(c)
        except (AttributeError, TypeError) as msg:
            print("_cnfmerge: fallback due to:", msg)
            for k, v in c.items():
                cnf[k] = v
    return cnf


def _info_button(cls, cnf={}, **kw):
    """Internal Function.\n
    This function takes essentials parameters to give
    the approximate width and height accordingly. \n
    It creates a ttk button and use all the resources given
    and returns width and height of the ttk button, after taking
    width and height the button gets destroyed also the custom style."""
    kw = _cnfmerge((cnf, kw))
    if kw.get('bitmap'):
        tmp = tkinter.Button(cls, **kw)
    else:
        kw['style'] = '%s.TButton' % cls
        _style_tmp = ttk.Style(master=cls)
        _style_tmp.configure(kw['style'], font=kw.pop('font', None))
        _style_tmp.configure(kw['style'], padding=(
            kw.pop('padx', 0), kw.pop('pady', 0)))
        tmp = ttk.Button(cls, **kw)
        # [issue-2] Need fix --- doesn't really delete the custom style
        del _style_tmp
    geo = [tmp.winfo_reqwidth(), max(24, tmp.winfo_reqheight()-4)]
    tmp.destroy()
    return geo


def _on_press_color(cls=None, cnf={}, **kw):
    """Internal function. Do not call directly.\n
    Give gradient color effect used for activebackground.
    Returns ids"""
    kw = _cnfmerge((cnf, kw))
    cls = kw.get('cls', cls)
    w = cls.cnf.get('height', cls.winfo_width())
    h = cls.cnf.get('height', cls.winfo_height())
    tag = kw.get('tag', 'press')
    state = kw.get('state', 'normal' if cls.cnf.get('state')
                   in ('active', 'pressed') else 'hidden')
    if not cls:
        raise ValueError('Could not refer to any class instance "cls".')
    if kw.get('color') is None:
        kw.pop('color', None)
    width = cls.coords(tag) or 0
    if isinstance(width, (list, tuple)) and len(width) > 3:
        width = int(width[2])
    all_activebg_ids = cls.find('withtag', tag)
    cond1 = bool(h == len(all_activebg_ids))
    cond2 = bool(w == width)
    # [issue-1] Need a better approach for getting "cond3"
    cond3 = bool(kw.get('color', (False,)) == cls.cnf.get('activebackground'))
    if cond1 and cond2 and cond3 and not kw.get('force_create', False):
        return
    # This is the default accent color for mac.
    cr = cls.cnf['activebackground'] = kw.get(
        'color', cls.cnf.get('activebackground', ("#4b91fe", "#055be5")))
    cls.delete(tag)
    ids = []
    height = kw.get('height', h)
    if isinstance(cr, (tuple, list)) and None in cr:
        cr = list(cr)
        cr.remove(None)
        cr = cr[0]
    if not isinstance(cr, (tuple, list)):
        cr_list = (cr,) * height
    else:
        cr = (colour.Color(cr[0]), colour.Color(cr[1]))
        cr_list = tuple(
            cr[0].range_to(cr[1], height)
        )
    for i in range(height):
        ags = (0, i, kw.get('width', w), i)
        cnf = {'fill': cr_list[i], 'tag': tag, 'state': state}
        ids.append(cls._create('line', ags, cnf))
    cls.tag_lower(tag)     # keep the tag lowest
    return tuple(ids)


class _Canvas(tkinter.Widget):
    """Internal Class."""

    def __init__(self, master=None, cnf={}, **kw):
        tkinter.Widget.__init__(self, master, 'canvas', cnf, kw)

    def find(self, *args):
        """Internal function."""
        return self._getints(
            self.tk.call((self._w, 'find') + args)) or ()

    def bbox(self, *args):
        """Return a tuple of X1,Y1,X2,Y2 coordinates for a rectangle
        which encloses all items with tags specified as arguments."""
        return self._getints(
            self.tk.call((self._w, 'bbox') + args)) or None

    def coords(self, *args):
        """Return a list of coordinates for the item given in ARGS."""
        return [self.tk.getdouble(x) for x in
                self.tk.splitlist(
            self.tk.call((self._w, 'coords') + args))]

    def _create(self, itemType, args, kw):  # Args: (val, val, ..., cnf={})
        """Internal function."""
        args = tkinter._flatten(args)
        cnf = args[-1]
        if isinstance(cnf, (dict, tuple)):
            args = args[:-1]
        else:
            cnf = {}
        return self.tk.getint(self.tk.call(
            self._w, 'create', itemType,
            *(args + self._options(cnf, kw))))

    def delete(self, *args):
        """Delete items identified by all tag or ids contained in ARGS."""
        self.tk.call((self._w, 'delete') + args)

    def itemcget(self, tagOrId, option):
        """Return the resource value for an OPTION for item TAGORID."""
        return self.tk.call(
            (self._w, 'itemcget') + (tagOrId, '-'+option))

    def check_tag(self, cmd, tag, safe_create=False, avoid=[]):
        """Internal function.\n
        If `cmd="check"` and the tag does not exist then
        the tag is created, but if `cmd="create"` and
        safe_create=True this will delete the tag if exists
        and creates a new tag  with same settings."""
        c = True
        if cmd == 'check':
            c = False
        if cmd not in ('create', 'check'):
            raise ValueError(
                '%s is not a valid command! Takes -create, -check' % cmd)
        cond1 = bool(not self.find('withtag', tag) or c)
        cond2 = bool(tag not in avoid)
        if safe_create and cond1 and cond2:
            self.delete(tag)
        return cond1 and cond2

    def tag_lower(self, *args):
        """Lower an item TAGORID given in ARGS
        (optional below another item)."""
        self.tk.call((self._w, 'lower') + args)

    def tag_raise(self, *args):
        """Raise an item TAGORID given in ARGS
        (optional above another item)."""
        self.tk.call((self._w, 'raise') + args)

    def rounded_rect(self, ags=(), *args, **kw):
        """Internal function."""
        x, y, w, h, c = _agsmerge((ags, args))
        ids = []
        cnf = dict(kw)
        for i in ('extent', 'start', 'style'):
            cnf.pop(i, None)
        for i in ('joinstyle', 'smooth', 'slinesteps'):
            kw.pop(i, None)
        points = (  # Arc points:-
            (x, y, x+2*c, y+2*c),
            (x, y+h-2*c, x+2*c, y+h),
            (x+w-2*c, y+h-2*c, x+w, y+h),
            (x+w-2*c, y, x+w, y+2*c),
            # Polygon points:-
            (x+c, y, x+w-c, y),
            (x+c, y+h, x+w-c, y+h),
            (x, y+c, x, y+h-c),
            (x+w, y+c, x+w, y+h-c))

        for i, point in enumerate(points):
            if i <= 3:
                kw['start'] = 90*(i+1)
                ids.append(self._create('arc', point, kw))
            else:
                ids.append(self._create('polygon', point, cnf))
        return tuple(ids)

    def _rounded(self, ags=(), *args, **kw):
        """Internal function."""
        x1, y1, x2, y2, c = _agsmerge((ags, args))
        ids = []
        points = (  # Arc points:-
            (x2-c-1, y1, x2-1, y1+c),
            (x1, y1, x1+c, y1+c),
            (x1, y2-c-1, x1+c, y2-1),
            (x2-c, y2-c, x2-1, y2-1),
            # Rectangle points:-
            (x1+c/2, y1, x2-c/2, y2),
            (x1, y1+c/2, x2, y2-c/2))

        kw['start'], kw['outline'] = 0, ''
        for i, point in enumerate(points):
            if i <= 3:
                ids.append(self._create('arc', point, kw))
                kw['start'] += 90
            else:
                kw.pop('start', None)
                kw['width'] = 0
                ids.append(self._create('rectangle', point, kw))
        return tuple(ids)


def check_appearance(cmd='defaults read -g AppleInterfaceStyle'):
    """### Checks DARK/LIGHT mode of macos. Returns Boolean.
    #### Args:
    - `cmd`: Give commands. Like to check DARK/LIGHT mode \
            the command is `'defaults read -g AppleInterfaceStyle'` .
    """
    import subprocess
    cmd = 'defaults read -g AppleInterfaceStyle'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
    return bool(p.communicate()[0])


def check_function_equality(func1, func2):
    """Checks if two functions are same."""
    return func1.__code__.co_code == func2.__code__.co_code


def check_light_dark(value, intensity=110, light_value="white", dark_value="black"):
    """Tells if the given RGB or HEX code is lighter or darker color.

    Args:
        value [str, tuple]: Give sequence of RBG values and hexcode.
        intensity (int): The measurable amount of a brightness.
        light_value (any): Value returned if lighter. Default is white.
        dark_value (any): Value returned if darker. Default is black.

    Return:
        any: light_value/dark_value"""
    if isinstance(value, str) and value.startswith('#'):
        value = hex_to_rgb(value)
    if (value[0]*0.299 + value[1]*0.587 + value[2]*0.114) > intensity:
        return dark_value
    return light_value


def check_param(master, name, cnf={}, **kw):
    "Internal function. Used to validate options of the widget."
    kw = _cnfmerge((cnf, kw))
    cm = Check_Common_Parameters(master)
    return cm(name, kw)


def delta(evt):
    """Modified delta to work with all platforms."""
    if evt.num == 5 or evt.delta < 0:
        return -1
    return 1


def hex_to_rgb(hx, hsl=False):
    """Converts a HEX code into RGB or HSL.
    Args:
        hx (str): Takes both short as well as long HEX codes.
        hsl (bool): Converts the given HEX code into HSL value if True.
    Return:
        Tuple of length 3 consisting of either int or float values.
    Raise:
        ValueError: If given value is not a valid HEX code."""
    if re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$').match(hx):
        div = 255.0 if hsl else 0
        if len(hx) <= 4:
            return tuple(int(hx[i]*2, 16) / div if div else
                         int(hx[i]*2, 16) for i in (1, 2, 3))
        return tuple(int(hx[i:i+2], 16) / div if div else
                     int(hx[i:i+2], 16) for i in (1, 3, 5))
    raise ValueError(f'"{hx}" is not a valid HEX code.')


def get_shade(color, shade, mode='auto'):
    """### Darken or Lighten a shade of color.
    #### Args:
    1. `color`: Give a color as either HEX or name of the color.
    2. `shade`: The amount of change required. Takes float \
                between 0.0 to 1.0 eg: shade=0.225.
    3. `mode`:
        - `'-'` for darker shade.
        - `'+'` for lighter shade.
        - `'auto-110'` automatically decide lighter or \
                       darker. where 110 is the intensity.

    return hexcode"""
    op = {'+': lambda x, y: float(x+y),
          '-': lambda x, y: float(x-y)}
    if isinstance(color, str):
        try:
            color = list(float(i/65535.0)
                         for i in tkinter._default_root.winfo_rgb(color))
        except AttributeError:
            # Raise AttributeError when running tests.
            color = list(colour.Color(color).get_rgb())
    if 'auto' in mode:
        intensity = (110.0 if len(mode) <= 4 else float(
            mode.split('-')[1])) / 1000.0
        color_intensity = float(
            color[0]*0.299 + color[1]*0.587 + color[2]*0.114)
        mode = '-' if color_intensity > intensity else '+'
        if color_intensity > intensity*2 or color_intensity < intensity/2:
            shade += shade
    if mode not in op:
        raise ValueError(
            'Invalid mode "{}", Takes only "-" or "+"'. format(mode))
    for index, c in enumerate((op[mode](c, shade) for c in color)):
        if c > 1.0:
            c = 1.0
        elif c < 0.0:
            c = 0.0
        color[index] = int(c*255.0)
    return '#%02x%02x%02x' % (color[0], color[1], color[2])


def get_hex(color, master=None):
    """
    Get hex code from tkinter named colors

    Args:
        color (str): Valid colour name
        master (tkinter.Widget, optional): To get systemDeafult hex,
            give master or it will raise an error. Defaults to None.

    Returns:
        str: Full size HEX code
    """
    if color == "systemWindowBackgroundColor":
        color = "#ebeceb"
        if check_appearance():
            color = "#333133"
    if master is None:
        c = colour.Color(color)
        return c.hex
    c = [int((int(i/257) + 255)/2) for i in master.winfo_rgb(color)]
    return '#%02x%02x%02x' % (c[0], c[1], c[2])


def gradient(iteration):
    """This function returns a list of HSL values
    of all the colors in an order."""

    ops = {'+': lambda c, step: min(1.0, c + step),
           '-': lambda c, step: max(0.0, c - step)}

    index = 0
    operation = '+'
    iteration = max(1, iteration-2)
    rgb, _list = [1.0, 0.0, 0.0], []
    combo = ((2, 1, 0), (2, 0, 1), (0, 2, 1), (0, 1, 2), (1, 0, 2), (1, 2, 0))
    step = float(len(combo)) / float(iteration)
    _list.append('#%02x%02x%02x' % (round(rgb[0]*255),
                                    round(rgb[1]*255), round(rgb[2]*255)))
    for i in range(iteration):
        if (rgb[combo[index][1]] == 1.0 and operation == '+') or \
           (rgb[combo[index][1]] == 0.0 and operation == '-'):
            operation = '-' if operation == '+' else '+'
            index += 1
        rgb[combo[index][1]] = ops[operation](rgb[combo[index][1]], step)
        _list.append('#%02x%02x%02x' % (round(rgb[0]*255),
                                        round(rgb[1]*255), round(rgb[2]*255)))
    _list.append('#%02x%02x%02x' % (round(1.0*255),
                                    round(0.0*255), round(0.0*255)))
    return _list


__all__ = [
    'check_appearance',
    'check_light_dark',
    'delta',
    'get_shade',
    'gradient'
]
