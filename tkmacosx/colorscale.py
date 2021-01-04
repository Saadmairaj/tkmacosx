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

'''
Newer style colorchoosers for tkinter module.
'''

import re
import colour
import tkinter as _tk
import tkmacosx.basewidget as tkb

from tkinter import font
from tkinter.font import Font


HEX = 'hex'
RGB = 'rgb'


def gradient(iteration):
    """This function returns a list of HSL values
    of all the colors in an order."""

    ops = {'+': lambda c, step: min(1.0, c + step),
           '-': lambda c, step: max(0.0, c - step)}

    index = 0
    operation = '+'
    iteration = max(0, iteration-2)
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


def check_light_dark(value, intensity=110):
    """Tells if the given RGB or HEX code is lighter or darker color.

    Args:
        value [str, tuple]: Give sequence of RBG values and hexcode.
        intensity (int): The measurable amount of a brightness.
    
    Return:
        str('white') / str('black')"""
    if isinstance(value, str) and value.startswith('#'):
        value = hex_to_rgb(value)
    if (value[0]*0.299 + value[1]*0.587 + value[2]*0.114) > intensity:
        return 'black'
    return 'white'


class Colorscale(tkb._Canvas):
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
    - `gradient`: Take tuple of two colors or default.
    - `showinfodelay`: Delay before the showinfo disappears (in ms).
    """

    _features = ('value', 'command', 'orient', 'mousewheel', 'variable', 'showinfo',
                 'showinfodelay', 'gradient',)  # add more features

    def __init__(self, master=None, cnf={}, **kw):
        kw = {k: v for k, v in _tk._cnfmerge(
            (cnf, kw)).items() if v is not None}
        self.cnf = {k: kw.pop(k, None)
                    for k in kw.copy() if k in self._features}

        self.cnf['value'] = self.cnf.get('value', 'hex')
        self.cnf['orient'] = self.cnf.get('orient', 'vertical')
        self.cnf['gradient'] = self.cnf.get('gradient', 'default')
        self.cnf['showinfo'] = self.cnf.get('showinfo', True)
        self.cnf['showinfodelay'] = self.cnf.get('showinfodelay', 1500)

        kw['width'] = kw.get(
            "width", 250 if 'ver' in self.cnf['orient'] else 30)
        kw['height'] = kw.get(
            "height", 30 if 'ver' in self.cnf['orient'] else 250)
        kw['highlightthickness'] = kw.get('highlightthickness', 0)
        tkb._Canvas.__init__(self, master=master, cnf={}, **kw)

        # Protected members of the class
        self._size = (0, 0)
        self._marker_color = 'black'
        self._xy = int((self.winfo_reqwidth() if 'ver' in
                        self['orient'] else self.winfo_reqheight()) / 3)

        binds = [{'className': 'set_size', 'sequence': '<Configure>', 'func': self._set_size},
                 {'className': 'b1_on_motion', 'sequence': '<B1-Motion>',
                     'func': self._move_marker},
                 {'className': 'b1_press', 'sequence': '<Button-1>', 'func': self._move_marker}]
        tkb._bind(self, *binds)
        self._set_mousewheel()

    def _set_size(self, evt=None):
        """Internal function."""
        if evt.width == self._size[0] and evt.height == self._size[1]:
            return
        self._size = (evt.width, evt.height)
        self._create_items('create', safe_create=True)

    def _callback(self, color):
        """Internal function."""
        if self.cnf.get('command'):
            self.cnf['command'](color)
        if self.cnf.get('variable'):
            self.cnf['variable'].set(color)

    def _create_items(self, cmd, safe_create=False, **kw):
        """Internal function.\n
        Checks and creates (text, marker, 
        showinfo, gradient lines) items."""

        def check_tag(tag):
            return self.check_tag(cmd, tag, safe_create, kw.get('avoid', []))

        ids = []

        if check_tag('gradient'):
            w, h = self.winfo_width(), self.winfo_height()
            iteration = w if 'ver' in self.cnf['orient'] else h
            color_list = gradient(iteration)
            if isinstance(self.cnf.get('gradient'), (list, tuple)):
                c1 = colour.Color(self.cnf.get('gradient')[0])
                c2 = colour.Color(self.cnf.get('gradient')[1])
                color_list = c1.range_to(c2, iteration)
            elif isinstance(self.cnf.get('gradient'), str) \
                    and self.cnf.get('gradient') != 'default':
                c = colour.Color(self.cnf.get('gradient'))
                color_list = c.range_to(c, iteration)

            for count, c in enumerate(color_list):
                ags = (count, -1, count, h)
                if self.cnf['orient'] == 'horizontal':
                    ags = (-1, count, w, count)
                ids.append(self._create('line', ags, {
                           'fill': c, 'tag': 'gradient'}))

        if check_tag('borderline'):
            w, h = self.winfo_width(), self.winfo_height()
            borderline_points = kw.get('borderline_points',
                                       (1, 1, self.winfo_width()-2,
                                        self.winfo_height()-2, 0))
            ids.append(self.rounded_rect(borderline_points, width=2,
                                         outline='#81b3f4', tag='borderline',
                                         style='arc'))

        if check_tag('marker'):
            _def_val = (2, self._xy, self.winfo_width()-4, 5, 2)
            if self['orient'] == 'vertical':
                _def_val = (self._xy, 2, 5, self.winfo_height()-4, 2)
            marker_points = kw.get('marker_points', _def_val)
            ids.append(self.rounded_rect(marker_points, width=2,
                                         outline=self._marker_color,
                                         tag="marker", style='arc'))

        if check_tag('markerbg') and kw.get('markerbg_points') is not None:
            markerbg_points = kw.get('markerbg_points')
            cnf = kw.get('markerbg_cnf')
            ids.append(self._rounded(markerbg_points, **cnf))

        if check_tag('info') and kw.get('info_points') is not None:
            info_points = kw.get('info_points')
            cnf = kw.get('info_cnf')
            ids.append(self._create('text', info_points, cnf))

        return ids

    def _release(self, evt=None):
        """Internal function."""
        self.delete('info', 'markerbg')

    def _move_marker(self, evt, mw=None):
        """Internal function."""
        spacer, spacbg = 35, 25

        def diff_orient_val():
            """Internal function."""
            if self['orient'] == 'vertical':
                return dict(
                    evtx=mw,
                    evty=10,
                    _xy=evt.x,
                )
            return dict(
                evtx=10,
                evty=mw,
                _xy=evt.y,
            )

        if mw:
            evt.x = diff_orient_val()['evtx']
            evt.y = diff_orient_val()['evty']

        self.after_cancel(getattr(self, '_remove_id', ' '))
        self._remove_id = self.after(self.cnf['showinfodelay'], self._release)

        cond_x = bool(evt.x > 0 and evt.x < self.winfo_width())
        cond_y = bool(evt.y > 0 and evt.y < self.winfo_height())
        cond_state = bool(self['state'] not in 'disabled')

        if not (cond_x and cond_y and cond_state):
            return

        if not mw:
            self._xy = diff_orient_val()['_xy']

        c_id = self.find('overlapping', evt.x, evt.y, evt.x, evt.y)
        text = hexcode = self.itemcget(c_id[0], 'fill')
        rgb = [int(i/65535.0*255.0) for i in self.winfo_rgb(hexcode)]
        self._marker_color = check_light_dark(rgb)

        self._configure(('itemconfigure', 'borderline'),
                        {'outline': hexcode}, None)
        self._callback(hexcode)

        if self.cnf['value'] == "rgb":
            spacer, spacbg = 65, 55
            text = ' | '.join([v+':'+str(f)
                               for f, v in zip(rgb, ('R', 'G', 'B'))])
            self._callback(rgb)

        ver_cond = evt.x < self.winfo_width() - (spacbg+spacer) \
            and self['orient'] == 'vertical'
        hor_cond = evt.y < self.winfo_height() - (spacbg+spacer) \
            and self['orient'] == 'horizontal'

        markerbg_points, info_points = (), ()

        if bool(ver_cond or hor_cond) and self['showinfo']:
            markerbg_points = (self.winfo_width()/2-6, evt.y+spacer - spacbg,
                               self.winfo_width()/2+7, evt.y+spacer + spacbg, 6)
            info_points = ((self.winfo_width()/2, evt.y+spacer))

            if self.cnf['orient'] == 'vertical':
                markerbg_points = (evt.x+spacer - spacbg, self.winfo_height()/2-6,
                                   evt.x+spacer + spacbg, self.winfo_height()/2+7, 6)
                info_points = ((evt.x + spacer, self.winfo_height()/2))

        elif self['showinfo']:
            markerbg_points = (self.winfo_width()/2-6, evt.y-spacer - spacbg,
                               self.winfo_width()/2+7, evt.y-spacer + spacbg, 6)
            info_points = ((self.winfo_width()/2, evt.y-spacer))

            if self.cnf['orient'] == 'vertical':
                markerbg_points = (evt.x-spacer - spacbg, self.winfo_height()/2-6,
                                   evt.x-spacer + spacbg, self.winfo_height()/2+7, 6)
                info_points = ((evt.x - spacer, self.winfo_height()/2))

        markerbg_cnf = {'fill': self._marker_color, 'tag': 'markerbg'}
        info_cnf = {'angle': 0 if 'ver' in self.cnf['orient'] else 90,
                    'text': text, 'font': Font(size=10), 'tag': "info", 'fill': hexcode}

        self._create_items('create', safe_create=True, avoid=('gradient', 'borderline'),
                           info_points=info_points, markerbg_points=markerbg_points,
                           info_cnf=info_cnf, markerbg_cnf=markerbg_cnf)
        return True

    def _set_mousewheel(self, evt=None):
        """Internal function.\n
        Sets mousewheel scrolling."""

        def on_mousewheel(evt=None):
            "Internal function."
            ver_cond = self._xy < self.winfo_width() \
                and self['orient'] == 'vertical'
            hor_cond = self._xy < self.winfo_height() \
                and self['orient'] == 'horizontal'
            if tkb.delta(evt) <= -1 and (ver_cond or hor_cond):
                self._xy += 1
                if not self._move_marker(evt, mw=self._xy):
                    self._xy -= 1
            if tkb.delta(evt) >= 1 and self._xy > 1:
                self._xy -= 1
                if not self._move_marker(evt, mw=self._xy):
                    self._xy += 1

        if self.cnf.get('mousewheel'):
            tkb._bind(self, className='mousewheel',
                      sequence='<MouseWheel>', func=on_mousewheel)
            tkb._bind(self, className='mousewheel_x11',
                      sequence='<Button-4>', func=on_mousewheel)
            tkb._bind(self, className='mousewheel_x11',
                      sequence='<Button-5>', func=on_mousewheel)
        else:
            tkb._bind(self, className='mousewheel',
                      sequence='<MouseWheel>')
            tkb._bind(self, className='mousewheel_x11',
                      sequence='<Button-4>')
            tkb._bind(self, className='mousewheel_x11',
                      sequence='<Button-5>')

    def _configure(self, cmd, cnf=None, kw=None):
        """Internal function."""
        kw1 = _tk._cnfmerge((cnf, kw))
        self.cnf.update(
            {k: kw.pop(k, None) for k in kw1.copy() if k in self._features})
        self.cnf = {k: v for k, v in self.cnf.copy().items() if v is not None}
        _return = tkb._Canvas._configure(self, cmd, None, kw1)
        if _tk._cnfmerge((cnf, kw)).get('gradient'):
            self._create_items('create', safe_create=True,
                               avoid=('borderline', 'marker',
                                      'markerbg', 'info'))
        self._set_mousewheel()
        if _return and isinstance(_return, dict):
            _return.update(self.cnf)
        return _return

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in self.cnf.keys():
            return self.cnf.get(key)
        return tkb._Canvas.cget(self, key)
    __getitem__ = cget

    def keys(self):
        """Return a list of all resource names of this widget."""
        return list(sorted(self.config() + self._features))

    def destroy(self):
        """Destroy this widget."""
        self.after_cancel(getattr(self, '_remove_id', ' '))
        return tkb._Canvas.destroy(self)
