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

import colour
import tkinter
from tkinter.font import Font
from tkmacosx.utils import (_cnfmerge, _bind, _Canvas, check_param,
                            check_light_dark, delta, gradient)

HEX = 'hex'
RGB = 'rgb'

COLORSCALE_PROPERTIES = [
    'borderwidth', 'cursor', 'command', 'gradient', 'height',
    'highlightbackground', 'highlightcolor', 'highlightthickness',
    'mousewheel', 'orient', 'relief', 'showinfo', 'showinfodelay',
    'state', 'takefocus', 'value', 'variable', 'width'
]

COLORSCALE_FEATURES = (
    'value', 'command', 'orient', 'mousewheel', 'variable', 'showinfo',
    'showinfodelay', 'gradient'
)


class ColorscaleBase(_Canvas):
    "Base class for Colorscale widget."

    def __init__(self, master=None, cnf={}, **kw):
        kw = {k: v for k, v in _cnfmerge(
            (cnf, kw)).items() if v is not None}
        cnf = {k: kw.pop(k, None)
               for k in kw.copy() if k in COLORSCALE_FEATURES}

        cnf['command'] = cnf.get('command', '')
        cnf['gradient'] = cnf.get('gradient', 'default')
        cnf['mousewheel'] = cnf.get('mousewheel', False)
        cnf['orient'] = cnf.get('orient', 'vertical')
        cnf['showinfo'] = cnf.get('showinfo', True)
        cnf['showinfodelay'] = cnf.get('showinfodelay', 1500)
        cnf['value'] = cnf.get('value', 'hex')
        cnf['variable'] = cnf.get('variable', '')

        kw['width'] = kw.get(
            "width", 250 if 'ver' in cnf['orient'] else 30)
        kw['height'] = kw.get(
            "height", 30 if 'ver' in cnf['orient'] else 250)
        kw['highlightthickness'] = kw.get('highlightthickness', 0)
        _Canvas.__init__(self, master=master, cnf={}, **kw)

        self.cnf = self._check_param(**cnf)
        self._size = (0, 0)
        self._marker_color = 'black'
        self._xy = int((self.winfo_reqwidth() if 'ver' in
                        self.cnf['orient'] else self.winfo_reqheight()) / 3)

        binds = [
            {'className': 'set_size', 'sequence': '<Configure>', 'func': self._set_size},
            {'className': 'b1_on_motion', 'sequence': '<B1-Motion>',
                'func': self._check_marker},
            {'className': 'b1_press', 'sequence': '<Button-1>',
                'func': self._check_marker}
        ]
        _bind(self, *binds)
        self._set_mousewheel()

    def _check_param(self, cnf={}, **kw):
        kw = _cnfmerge((cnf, kw))
        if 'gradient' in kw:
            if kw['gradient'] != 'default':
                cond = isinstance(kw['gradient'], (list, tuple))
                if not cond or (cond and len(kw['gradient']) <= 1):
                    raise tkinter.TclError(
                        'expected sequence of two color values but got "%s"'
                        % kw['gradient'])
                for c in kw['gradient']:
                    self.winfo_rgb(c)
        kw = check_param(self, 'colorscale', kw)
        return kw

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
    
    def _move_marker(self, evt):
        spacer, spacbg = 35, 25
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

    def _check_marker(self, evt, mw=None):
        """Internal function."""
        diff_orient_val = {
            'vertical': dict(evtx=mw, evty=10, _xy=evt.x),
            'horizontal': dict(evtx=10, evty=mw, _xy=evt.y)}
        
        self.after_cancel(getattr(self, '_remove_id', ' '))
        self._remove_id = self.after(self.cnf['showinfodelay'], self._release)

        if mw:
            evt.x = diff_orient_val[self['orient']]['evtx']
            evt.y = diff_orient_val[self['orient']]['evty']
        else:
            self._xy = diff_orient_val[self['orient']]['_xy']

        cond_x = bool(evt.x > 0 and evt.x < self.winfo_width())
        cond_y = bool(evt.y > 0 and evt.y < self.winfo_height())
        cond_state = bool(self['state'] not in 'disabled')

        if not (cond_x and cond_y and cond_state):
            return
        return self._move_marker(evt)
        

    def _set_mousewheel(self, evt=None):
        """Internal function.\n
        Sets mousewheel scrolling."""

        def on_mousewheel(evt=None):
            "Internal function."
            ver_cond = self._xy < self.winfo_width() \
                and self['orient'] == 'vertical'
            hor_cond = self._xy < self.winfo_height() \
                and self['orient'] == 'horizontal'
            if delta(evt) <= -1 and (ver_cond or hor_cond):
                self._xy += 1
                if not self._check_marker(evt, mw=self._xy):
                    self._xy -= 1
            if delta(evt) >= 1 and self._xy > 1:
                self._xy -= 1
                if not self._check_marker(evt, mw=self._xy):
                    self._xy += 1

        if self.cnf.get('mousewheel'):
            _bind(self, className='mousewheel',
                  sequence='<MouseWheel>', func=on_mousewheel)
            _bind(self, className='mousewheel_x11',
                  sequence='<Button-4>', func=on_mousewheel)
            _bind(self, className='mousewheel_x11',
                  sequence='<Button-5>', func=on_mousewheel)
        else:
            _bind(self, className='mousewheel',
                  sequence='<MouseWheel>')
            _bind(self, className='mousewheel_x11',
                  sequence='<Button-4>')
            _bind(self, className='mousewheel_x11',
                  sequence='<Button-5>')

    def _configure(self, cmd, cnf=None, kw=None):
        """Internal function."""
        kw1 = _cnfmerge((cnf, kw))

        for i in list(kw1):
            if i in COLORSCALE_FEATURES:
                self.cnf.update(
                    self._check_param({i: kw1.pop(i)})
                )

        values = _Canvas._configure(self, cmd, None, kw1)
        if _cnfmerge((cnf, kw)).get('gradient'):
            self._create_items('create', safe_create=True,
                               avoid=('borderline', 'marker',
                                      'markerbg', 'info'))
        self._set_mousewheel()
        if values and isinstance(values, dict):
            values.update(self.cnf)
            for k in list(values):
                if k not in COLORSCALE_PROPERTIES:
                    values.pop(k)
        return values

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in self.cnf.keys():
            if key == 'variable':
                return str(self.cnf[key])
            return self.cnf.get(key)
        value = _Canvas.cget(self, key)
        if key in ('height', 'width', 'highlightthickness',
                   'borderwidth', 'bd'):
            return int(value)
        return value
    __getitem__ = cget

    def keys(self):
        """Return a list of all resource names of this widget."""
        return COLORSCALE_PROPERTIES

    def destroy(self):
        """Destroy this widget."""
        self.after_cancel(getattr(self, '_remove_id', ' '))
        return _Canvas.destroy(self)
