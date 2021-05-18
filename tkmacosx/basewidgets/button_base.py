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
import tkinter.ttk as ttk
from tkmacosx.utils import (SYSTEM_DEFAULT, STDOUT_WARNING,
                            _cnfmerge, _bind, _Canvas, check_param,
                            _info_button, _on_press_color, 
                            get_shade, check_function_equality)
import tkmacosx.utils.colorvar_patches as cp


BUTTON_PROPERTIES = [
    'activebackground', 'activeforeground', 'anchor', 'background', 
    'bd', 'bg', 'bitmap', 'borderwidth', 'command', 'compound', 'cursor', 
    'disabledforeground', 'fg', 'font', 'foreground', 'height', 
    'highlightbackground', 'highlightcolor', 'highlightthickness', 'image', 
    'justify', 'overrelief', 'padx', 'pady', 'relief', 'repeatdelay', 
    'repeatinterval', 'state', 'takefocus', 'text', 'textvariable', 
    'underline', 'width'
]


BUTTON_FEATURES = (
    'overbackground', 'overforeground', 'activeimage', 'activebitmap', 
    'anchor', 'bitmap', 'bordercolor', 'borderless', 'command', 'compound', 
    'disabledforeground', 'justify', 'disabledbackground', 'fg', 'font', 
    'foreground', 'height', 'image', 'overrelief', 'padx', 'pady', 'repeatdelay', 
    'repeatinterval', 'text', 'textvariable', 'underline', 'width', 'state', 
    'focusthickness', 'focuscolor', 'highlightbackground', 'activebackground', 
    'activeforeground'
)


BUTTON_ITEMS = (
    '_txt', '_bit', '_img', '_bd_color', '_border', '_tf'
)

BORDER_INTENSITY = 0.06

_warning_msg_shown = [False]


class _button_properties:
    """Internal class.\n
    Contains modified properties of Button widget. Do not call directly."""

    # Utils
    def _bit_img(self, cmd, kw):
        tag = '_bit' if cmd == 'bitmap' else '_img'
        if kw.get(cmd, '') != '':
            state = 'disabled' if self.cnf.get('state') in (
                'disabled', 'disable') else 'normal'
            _opt = dict(state=state, **{i: kw.get(i, self.cnf.get(i))
                                    for i in ('anchor', cmd)})
            return (('itemconfigure', tag), _opt, None)
        self.delete(tag)
    
    def _active_bit_img(self, cmd, kw):
        tag = '_bit' if cmd == 'activebitmap' else '_img'
        name = cmd.rsplit('active')[-1]
        if self['state'] in ('pressed', 'active'):
            return (('itemconfigure', tag), {
                    name: self.cnf.get(cmd, '')}, None)

    def _item(self, cmd, kw):
        self.cnf['width'] = self.winfo_width()
        self.cnf['height'] = self.winfo_height()
        
        r1 = self._compound(self.cnf.get('compound'), self.cnf.get('width'), self.cnf.get('height'))
        r2 = {cmd: ((self.cnf['width']/2), self.cnf['height']/2)}
        return r1 or r2
    
    def _size_opts(self):
        _opt = {}
        for i in ('text', 'font', 'textvariable', 'image', 'bitmap',
                    'compound', 'padx', 'pady', 'activeimage',
                    'activebitmap'):
            cond1 = self.cnf.get(i, '') != ''
            if cond1 and i == 'activeimage':
                _opt['image'] = self.cnf[i]
            elif cond1 and i == 'activebitmap':
                _opt['bitmap'] = self.cnf[i]
            elif cond1:
                _opt[i] = self.cnf.get(i)
        return _opt

    # These are properties of button widget:
    def _border(self, kw):
        return [('itemconfigure', '_border'),
            {'outline': get_shade(self['bg'], 
                BORDER_INTENSITY, 'auto-120')}, None]
    
    def _bit(self, kw):
        return _button_properties._item(self, '_bit', kw)

    def _img(self, kw):
        return _button_properties._item(self, '_img', kw)

    def _txt(self, kw):
        return _button_properties._item(self, '_txt', kw)

    def activebackground(self, kw):
        color = None
        if kw.get('activebackground', '') != '':
            color = kw.get('activebackground', self.cnf.get('activebackground'))
        return [self, {'tag': '_activebg',
                        'width':  self.winfo_width(),
                        'height': self.winfo_height(),
                        'color': color}]
    
    def activeforeground(self, kw):
        if self['state'] in ('pressed', 'active'):
            return (('itemconfigure', '_txt'), {
                    'fill': self.cnf.get('activeforeground', 'white')}, None)
    
    def activebitmap(self, kw):
        return _button_properties._active_bit_img(self, 'activebitmap', kw)
    
    def activeimage(self, kw):
        return _button_properties._active_bit_img(self, 'activeimage', kw)

    def bitmap(self, kw):
        return _button_properties._bit_img(self, 'bitmap', kw)

    def borderless(self, kw):
        def _get_master_bg():
            """Internal function."""
            ttk_widget_types = tuple(
                getattr(ttk, i) for i in ttk.__all__ if isinstance(getattr(ttk, i), type))
            if isinstance(self.master, ttk_widget_types):
                try:
                    style = self.master['style'] or 'T' + self.master.__class__.__name__
                    ttk_bg = ttk.Style(self.master).lookup(style, "background")
                    return ttk_bg
                except tkinter.TclError:
                    if not _warning_msg_shown[0] and STDOUT_WARNING:
                        print('WARNING: "borderless" option is partially supported with ttk widgets. '
                            'Bordercolor/highlightbackground can be set manually '
                            'with "highlightbackground" or "bordercolor" options.\n')
                        _warning_msg_shown[0] = True
                    return self.cnf.get('bordercolor', self.cnf['highlightbackground'])
            return self.master['bg']

        _opt = {}
        if bool(kw.get('borderless')) or self.cnf.get('borderless'):
            if not check_function_equality(self.master.config, self._get_functions('borderless', kw)):
                self.master.config = self.master.configure = self._get_functions(
                    'borderless', kw)
            master_bg = _get_master_bg()
            self.cnf['highlightbackground'] = self.cnf['bordercolor'] = master_bg
            _opt[1] = [('itemconfigure', '_bd_color'), {'outline': master_bg}, None]
            _opt[2] = ['configure', {'highlightbackground': master_bg}, None]

        elif not bool(kw.get('borderless', True)) or not self.cnf.get('borderless'):
            if self.cnf.get('bordercolor') == _get_master_bg():
                self.cnf.pop('bordercolor', None)
                self.cnf.pop('highlightbackground', None)
            bd_color = self.cnf.get(
                'bordercolor', get_shade(self['bg'], 0.04, 'auto-120'))
            if bd_color == '':
                bd_color = get_shade(self['bg'], 0.04, 'auto-120')
            elif bd_color.lower() == 'default':
                bd_color = get_shade('white', 0.04, 'auto-120')
            self.cnf.update({'bordercolor': bd_color})
            self.cnf['highlightbackground'] = self.cnf['bordercolor'] = bd_color
            if self.itemcget('_bd_color', 'outline') != bd_color:
                _opt[1] = [('itemconfigure', '_bd_color'), {'outline': bd_color}, None]
                _opt[2] = ['configure', {'highlightbackground': bd_color}, None]
        return _opt
    bordercolor = highlightbackground = borderless

    def foreground(self, kw):
        return (('itemconfigure', '_txt'),
                {'fill': kw.get('foreground', self.cnf.get('foreground'))}, None)
    fg = foreground

    def focuscolor(self, kw):
        return (('itemconfigure', '_tf'),
                {'outline': kw.get('focuscolor', self.cnf.get('focuscolor'))}, None)
    
    def focusthickness(self, kw):
        _button_items.create_items(self, 'create', True, avoid=(
            '_txt', '_img', '_bit', '_bd_color', '_border'))
    
    def image(self, kw):
        return _button_properties._bit_img(self, 'image', kw)
    
    def overbackground(self, kw):
        _opt = []
        if kw.get('overbackground', '') != '':
            fn = self._get_functions('overbackground', kw)
            _opt = [self,
                    {'className': 'overbackground', 'sequence': '<Enter>',
                    'func': fn.get('<Enter>')},
                    {'className': 'overbackground', 'sequence': '<Leave>',
                    'func': fn.get('<Leave>')}]
            if self._mouse_state_condition():
                _Canvas._configure(self, 'configure', {'bg': kw.get('overbackground')}, None)
                _Canvas._configure(self, ('itemconfigure', '_border'), 
                    {'outline': get_shade(kw.get('overbackground'), 0.1, 'auto-120')}, None)
        elif kw.get('overbackground') == '':
            _opt = [self,
                    {'className': 'overbackground', 'sequence': '<Enter>'},
                    {'className': 'overbackground', 'sequence': '<Leave>'}, 
                    ('configure', {'bg': self._org_bg}, None), 
                    (('itemconfigure', '_border'), {'outline': 
                    get_shade(self._org_bg, 0.1, 'auto-120')}, None)]
        return _opt

    def overforeground(self, kw):
        _opt = []
        if kw.get('overforeground', '') != '':
            fn = self._get_functions('overforeground', kw)
            _opt = [self,
                    {'className': 'overforeground', 'sequence': '<Enter>',
                    'func': fn.get('<Enter>')},
                    {'className': 'overforeground', 'sequence': '<Leave>',
                    'func': fn.get('<Leave>')}]
            if self._mouse_state_condition():
                # [issue-3] doesn't change if overrelief is on.
                # [issue-3] (FIXED) using after with 0ms delay
                #           fixes the issue. To be safe delay is 1ms.
                self.after(1, lambda: _Canvas._configure(self,
                    ('itemconfigure', '_txt'), {'fill': kw.get('overforeground')}, None))
        elif kw.get('overforeground') == '':
            _opt = [self,
                    {'className': 'overforeground', 'sequence': '<Enter>'},
                    {'className': 'overforeground', 'sequence': '<Leave>'}]
            _opt.append((('itemconfigure', '_txt'),
                        {'fill': self.cnf.get('fg', 'black')}, None))
        return _opt

    def overrelief(self, kw):
        _opt = None
        if kw.get('overrelief', '') != '':
            if not self._rel[1]:
                self._rel = ('flat', False)
            if self._mouse_state_condition():
                self._configure(
                    'configure', {'_relief': kw.get('overrelief')}, None)
            fn = self._get_functions('overrelief', kw)
            _opt = (self,
                    {'className': 'overrelief', 'sequence': '<Enter>',
                        'func': fn.get('<Enter>')},
                    {'className': 'overrelief', 'sequence': '<Leave>',
                        'func': fn.get('<Leave>')})

        elif kw.get('overrelief') == '':
            _opt = (self,
                    {'className': 'overrelief', 'sequence': '<Enter>'},
                    {'className': 'overrelief', 'sequence': '<Leave>'},
                    ('configure', {'relief': self._rel[0]}, None))
        return _opt

    def size(self, kw):
        if self._type == 'circle' and kw.get('radius'):
            self.cnf['width'] = self.cnf['height'] = kw.get(
                'width', kw.get('height', int(kw['radius']*2)))
        if self._fixed_size['w'] and kw.get('width', True):
            kw['width'] = self.cnf['width']
        if self._fixed_size['h'] and kw.get('height', True):
            kw['height'] = self.cnf['height']
        self._fixed_size['w'] = True if kw.get('width', kw.get('radius')) is not None else False
        self._fixed_size['h'] = True if kw.get('height', kw.get('radius')) is not None else False
        W, H = _info_button(self, **_button_properties._size_opts(self))
        self.cnf['width'] = self.cnf.get('width') if self._fixed_size['w'] else W
        self.cnf['height'] = self.cnf.get('height') if self._fixed_size['h'] else H
        return ('configure', {'width': self.cnf['width'],
                              'height': self.cnf['height']}, None)
    
    def state(self, kw):
        _opt = {}
        if kw.get('state') in 'disabled':
            _opt[1] = ('configure', {'bg': self.cnf.get('disabledbackground'),
                                    'state': 'disabled'}, None)
            _opt[2] = (('itemconfigure', '_txt'), {
                            'disabledfill': kw.get('disabledforeground', 
                            self.cnf.get('disabledforeground')), 
                            'state': 'disabled'}, None)
            _opt[3] = (('itemconfigure', '_activebg'), {'state': 'hidden'}, None)
            _opt[5] = (('itemconfigure', '_img'), {'state': 'disabled'}, None)
            _opt[6] = (('itemconfigure', '_bit'), {'state': 'disabled'}, None)
        elif kw.get('state') == 'normal':
            _bg = self._org_bg
            if self._mouse_state_condition() and self.cnf.get('overbackground'):
                _bg = self.cnf['overbackground']
            _opt[1] = ('configure', {'bg': _bg, 'state': 'normal'}, None)
            _opt[2] = (('itemconfigure', '_txt'), {'state': 'normal', 
                            'fill': self.cnf.get('foreground', 'black')}, None)
            _opt[3] = (('itemconfigure', '_activebg'), {'state': 'hidden'}, None)
            _opt[4] = (('itemconfigure', '_border'), {'state': 'normal'}, None)
            _opt[5] = (('itemconfigure', '_img'), {
                            'image': self.cnf.get('image', '')}, None)
            _opt[6] = (('itemconfigure', '_bit'), {
                            'bitmap': self.cnf.get('bitmap', '')}, None)
        elif kw.get('state') in ('active', 'pressed'):
            _bg = self._org_bg
            if self._mouse_state_condition() and self.cnf.get('overbackground'):
                _bg = self.cnf['overbackground']
            _opt[1] = ('configure', {'bg': _bg, 'state': 'normal'}, None)
            _opt[2] = (('itemconfigure', '_txt'), {'state': 'normal', 
                            'fill': self.cnf.get('activeforeground', 'white')}, None)
            _opt[3] = (('itemconfigure', '_activebg'), {'state': 'normal'}, None)
            _opt[4] = (('itemconfigure', '_border'), {'state': 'hidden'}, None)
            _opt[5] = (('itemconfigure', '_img'), {
                            'image': self.cnf.get('activeimage', '')}, None)
            _opt[6] = (('itemconfigure', '_bit'), {
                            'bitmap': self.cnf.get('activebitmap', '')}, None)
        return _opt

    def takefocus(self, kw):
        _opt = None
        if self['takefocus'] and self['state'] in ('normal', 'active', 'pressed'):
            fn = self._get_functions('takefocus', kw)
            _opt = [self, {'className': 'takefocus', 'sequence':
                            '<FocusIn>', 'func': fn.get('<FocusIn>')},
                            {'className': 'takefocus', 'sequence':
                            '<FocusOut>', 'func': fn.get('<FocusOut>')}]

        elif not self['takefocus'] or self['state'] in 'disabled':
            _opt = [self,
                    {'className': 'takefocus', 'sequence': '<FocusIn>'},
                    {'className': 'takefocus', 'sequence': '<FocusOut>'},
                    (('itemconfigure', '_tf'), {'state': 'hidden'}, None)]
        return _opt

    def text(self, kw):
        if kw.get('textvariable', '') != '':
            kw['text'] = self.cnf['text'] = self.cnf['textvariable'].get()
            cbn = self.cnf['textvariable'].trace_variable('w',
                    self._get_functions('textvariable', kw).get('w'))
            self._var_cb = (self.cnf['textvariable'], cbn)

        elif kw.get('textvariable') == '' and self._var_cb:
            kw['text'] = self.cnf['text'] = self._var_cb[0].get()
            self.cnf.pop('textvariable', None)
            self._var_cb[0].trace_vdelete('w', self._var_cb[1])
            self._var_cb = []

        state = 'disabled' if self.cnf.get('state') in (
            'disabled', 'disable') else 'normal'
        fill = kw.get('fg', self.cnf.get('fg'))
        if self['state'] in ('pressed', 'active'):
            fill = self.cnf.get('activeforeground', 'white')
        _opt = dict(state=state, fill=fill,
                    disabledfill=kw.get(
                        'disabledforeground', self.cnf.get('disabledforeground')),
                    **{i: kw.get(i, self.cnf.get(i)) for i in ('text', 'anchor', 'font', 'justify')})
        return (('itemconfigure', '_txt'), _opt, None)


class _button_items:
    """Internal class.

    Checks and creates (text, image, bitmap, border, 
    bordercolor, takefocus ring*) items."""

    # Utils
    def _active_state(self, val):
        """Internal function."""
        _kw = dict( fill=self.cnf.get('foreground', 'black'),
                    img=self.cnf.get('image', ''),
                    bit=self.cnf.get('bitmap', ''),
                    state='normal')
        if self['state'] in ('pressed', 'active'):
            return dict(fill=self.cnf.get('activeforeground', 'white'),
                        img=self.cnf.get('activeimage', _kw['img']),
                        bit=self.cnf.get('activebitmap', _kw['bit']),
                        state='hidden')[val]
        return _kw[val]
    
    def _bit_img_main(self, opt, *ags, **kw):
        kw['tag'] = '_img' if opt == 'image' else '_bit'
        if (self.cnf.get(opt) != '' or 
                self.cnf.get(str('active'+opt), '') != '' ):
            return self._create(
                opt, (0, 0), {'tag': kw['tag'], 
                opt: _button_items._active_state(self, kw['tag'][1:])})

    # These are main items (function names = item tag name.)
    def _txt(self, *ags, **kw):
        "Text item."
        txt_id = self._create(
            'text', (0, 0), {'text': None, 'tag': '_txt', 
            'fill': _button_items._active_state(self, 'fill')})
        self.cnf['font'] = self.cnf.get('font', self.itemcget(txt_id, 'font'))
        return txt_id

    def _bit(self, *ags, **kw):
        "Bitmap items (bitmap and activebitmap)."
        return _button_items._bit_img_main(self,'bitmap', *ags, **kw)
    
    def _img(self, *ags, **kw):
        "Image item (image and activeimage)."
        return _button_items._bit_img_main(self, 'image', *ags, **kw)
    
    def _bd_color(self, *ags, **kw):
        "Border color item."
        bd_color = self.cnf.get('bordercolor', get_shade(self['bg'], 0.04, 'auto-120'))
        if self._type == 'circle':
            pad = 2
            width = r = int(self.cnf.get('width', 87)/2)  # radius = x = y (in pixels)
            _bd_points = (pad-width, pad-width, r*2+width-pad, r*2+width-pad)
            kw_bd_color = {
                'tag': '_bd_color', 
                'state': _button_items._active_state(self, 'state'),
                'width': width*2,'outline': bd_color}
            return self._create('oval', _bd_points, kw_bd_color)
        _bd_points = (0, -1, self.cnf.get('width', 87), 
                        self.cnf.get('height', 24)+3, 7)  # was 6
        return self.rounded_rect(
            _bd_points, width=6, tag='_bd_color', 
            style='arc', outline=bd_color)
    
    def _border(self, *ags, **kw):
        "Border item."
        bo_color = get_shade(self['bg'], BORDER_INTENSITY, 'auto-120')
        if self._type == 'circle':
            pad = 2
            r = int(self.cnf.get('width', 87)/2)  # radius = x = y
            _bo_points = (pad, pad, r*2-(pad+1), r*2-(pad+1))
            return self._create('oval', _bo_points, {
                'tag': '_border', 'outline': self.cnf.get('bordercolor', bo_color) })
        h = 4
        if int(self['highlightthickness']):
            h += 1
        _bo_points = (2, 2, self.cnf.get('width', 87)-5, self.cnf.get('height', 24)-h, 4)  # was 3
        return self.rounded_rect(
            _bo_points, width=1, outline=bo_color, smooth=1, 
            tag='_border', style='arc', 
            state=_button_items._active_state(self,'state'))
    
    def _tf(self, *ags, **kw):
        "Takefocus highlight ring."
        if self.cnf.get('focusthickness') == 0:
            return
        if self._type == 'circle':
            pad = 1
            width = self.cnf.get('focusthickness', 2)
            r = int(self.cnf.get('width', 87)/2)  # radius = x = y
            _tk_points = (pad+width, pad+width, r*2-width-pad, r*2-width-pad)
            return self._create('oval', _tk_points, {
                    'tag': '_tf', 'width': width,
                    'outline': self.cnf.get('focuscolor', '#81b3f4'), 
                    'state': 'hidden'})

        # takefocuswidth can be changed.
        # Focus line is not on point the line is off when thickness is changed.
        s = w = self.cnf.get('focusthickness', 2)
        diff1 = diff2 = (int(self['highlightthickness'])*2) + (s*2)
        if diff2 == (s*2):
            diff2 -= 1
        
        if s == 1:
            s = 2
            diff2 = (int(self['highlightthickness'])*2) + (s*2)
            diff1 = diff2 + 1
        
        _tk_points = (s+int(self['highlightthickness']),
                        s+int(self['highlightthickness']),
                        self.cnf.get('width',  87)-diff1,
                        self.cnf.get('height', 24)-diff2, 4)
        return self.rounded_rect(
            _tk_points, width=w, style='arc', 
            outline=self.cnf.get('focuscolor', '#81b3f4'), 
            tag='_tf', state='hidden')
    
    # Main function
    def create_items(self, cmd, safe_create=False, **kw):
        _id = []
        for i in BUTTON_ITEMS:
            if self.check_tag(cmd, i, safe_create, kw.get('avoid', [])):
                fn = getattr(_button_items, i)
                _id.append(fn(self, cmd=cmd, safe_create=safe_create, **kw))
        return _id


class _button_functions:
    """Internal class.\n
    Function class for Button widget. Do not call directly."""

    def _mouse_state_condition(self):
        """Internal function.\n
        True if state is normal and cursor is on the widget."""
        con1 = bool(self.cnf.get('state') not in 'disabled')
        con2 = bool(self.winfo_containing(*self.winfo_pointerxy()) == self)
        return con1 and con2
    
    def _make_dictionaries(self, cnf={}, kw={}):
        """Internal function.\n
        Merges kw into cnf and removes None values."""
        kw['bordercolor'] = kw['highlightbackground'] = kw.get(
            'bordercolor', kw.get('highlightbackground'))
        kw = {k: v for k, v in kw.items() if v is not None}
        cnf.update(kw)
        cnf = {k: v for k, v in cnf.items() if v is not None}
        cnf['fg'] = cnf['foreground'] = kw.get(
            'foreground', kw.get('fg', cnf.get('fg', 'black')))
        if cnf.get('textvariable', '') != '':
            cnf['text'] = cnf['textvariable'].get()
        if kw.get('activebackground'):
            cnf.pop('activebackground')
        return cnf, kw

    def _set_trace(self, kw):
        """Internal function."""
        for i in ('activeforeground', 'activebackground', 'bordercolor', 
                  'disabledbackground', 'disabledforeground', 'foreground', 
                  'fg', 'focuscolor', 'highlightbackground', 'overbackground', 
                  'overforeground'):
            if isinstance(kw.get(i), tkinter.Variable):
                var = kw[i]
                cbname = var.trace_variable('w', lambda a, b, c, i=i, var=var,
                                cls=self: cls.config({i: var.get()}))
                if (self, i) in cp._all_traces_colorvar:
                    v, cb = cp._all_traces_colorvar.get((self, i))
                    v.trace_vdelete('w', cb)
                    cp._all_traces_colorvar[(self, i)] = (var, cbname)
                else:
                    cp._all_traces_colorvar[(self, i)] = (var, cbname)
                kw[i] = var.get()
        return kw

    def _get_functions(self, cmds, kw={}):
        """Internal function.\n
        Contains all the required functions."""

        def _borderless_support(cnf={}, **kw):
            _return = self.master._configure('configure', cnf, kw)
            kw = _cnfmerge((cnf, kw))
            if kw.get('bg') or kw.get('background'):
                for i in self._buttons:
                    if i['borderless']:
                        i.cnf['highlightbackground'] = i.cnf['bordercolor'] = i.master['bg']
                        _Canvas._configure(i, ('itemconfigure', '_bd_color'), {
                            'outline': i.master['bg']}, None)
                        _Canvas._configure(i, 'configure', {
                            'highlightbackground': i.master['bg']}, None)
            return _return

        def if_state(fn):
            """Runs function only if state is normal."""
            def wrapper(*a, **k):
                if self.cnf.get('state') not in 'disabled':
                    return fn(*a, **k)
            return wrapper

        def over_img_bit(seq, key):
            """Resets coords for text with overimage/overbitmap."""
            if self.cnf['state'] in ('active', 'pressed'):
                return
            tag = '_img' if key == 'image' else '_bit'
            if seq == 'enter':
                _Canvas._configure(self, ('itemconfigure', tag), 
                                   {key: kw.get('over'+key)}, None)
            elif seq == 'leave':
                _Canvas._configure(self, ('itemconfigure', tag), 
                                   {key: self.cnf.get(key, '')}, None)
            self._set_coords(self._get_options(
                                ('_txt', '_img', '_bit'), self.cnf))
        
        def overbg(seq):
            """Implement overbackground properly."""
            if seq == 'enter':
                _Canvas._configure(self, 'configure', {'bg': kw.get('overbackground')}, None)
                _Canvas._configure(self, ('itemconfigure', '_border'), 
                    {'outline': get_shade(kw.get('overbackground'), 0.1, 'auto-120')}, None)
            elif seq == 'leave':
                self._configure('configure', {'bg': self._org_bg}, None)
        
        def overfg(seq):
            """Handle overforeground, 
            foreground and activeforeground."""
            if self.cnf['state'] in ('active', 'pressed'):
                return
            if seq == 'enter':
                _Canvas._configure(self, ('itemconfigure', '_txt'), 
                    {'fill': self.cnf.get('overforeground', 'black')}, None)
            elif seq == 'leave':
                _Canvas._configure(self, ('itemconfigure', '_txt'), 
                    {'fill': self.cnf.get('fg', 'black')}, None)

        binds = {
            'overrelief': {'<Enter>': if_state(lambda _: self._configure(
                                'configure', {'_relief': kw.get('overrelief')})),
                           '<Leave>': if_state(lambda _: self._configure(
                                'configure', {'_relief': self._rel[0]}))},

            # [issue-3] doesn't change if overrelief is on.
            # [issue-3] (FIXED) using after with 0ms delay fixes the issue. To be safe delay is 1ms.
            'overforeground': {'<Enter>': if_state(lambda _: self.after(1, overfg, 'enter')),
                               '<Leave>': if_state(lambda _: overfg('leave'))},
            
            'overbackground': {'<Enter>': if_state(lambda _: overbg('enter')), 
                               '<Leave>': if_state(lambda _: overbg('leave')) },

            'overimage': {'<Enter>': if_state(lambda _: over_img_bit('enter', 'image')),
                            '<Leave>': if_state(lambda _: over_img_bit('leave', 'image'))},

            'overbitmap': {'<Enter>': if_state(lambda _: over_img_bit('enter', 'bitmap')),
                             '<Leave>': if_state(lambda _: over_img_bit('leave', 'bitmap'))},

            'takefocus': {'<FocusIn>': lambda _: _Canvas._configure(self, (
                            'itemconfigure', '_tf'), {'state': 'normal'}, None),
                          '<FocusOut>': lambda _: _Canvas._configure(self, (
                            'itemconfigure', '_tf'), {'state': 'hidden'}, None)},
        }

        other_functions = {
            'borderless': _borderless_support,

            'textvariable': {'w': lambda *a: _Canvas._configure(self, (
                            'itemconfigure', '_txt'), {'text': self.cnf.get(
                                                       'textvariable').get()}, None)},

            '_activebg': lambda: _on_press_color(*self._get_options(
                                                 'activebackground', self.cnf)),
        }
        funcs = _cnfmerge((binds, other_functions))
        if isinstance(cmds, (list, tuple)):
            value = funcs.copy()
            for i in cmds:
                value = value.get(i, {})
            return value
        return funcs.get(cmds, {})

    def _get_options(self, cmd, cnf={}, **kw):
        """Internal function."""
        kw = _cnfmerge((cnf, kw))
        # If more than one commands are given.
        # returns Union[list, dict, tuple(list, dict)]
        if isinstance(cmd, (list, tuple)):
            opts = None
            ags, cnf = [], {}
            for i in cmd:
                opts = self._get_options(i, kw)
                if isinstance(opts, (list, tuple)):
                    ags.append(opts)
                elif isinstance(opts, dict):
                    cnf.update(opts)
            if isinstance(opts, (list, tuple)) and isinstance(opts, dict):
                return ags, cnf
            return ags or cnf

        if cmd in _button_properties.__dict__:
            return getattr(_button_properties, cmd)(self, kw)

    def _set_coords(self, cnf={}, **kw):
        """Internal function.\n
        Set Coordinates of the items."""
        kw = _cnfmerge((cnf, kw))
        r = [self.coords(tag, *kw[tag]) for tag in
                ('_txt', '_img', '_bit', '_bd_color',
                 '_border', '_tf') if kw.get(tag)]
        for i in ('_txt', '_bit', '_img'):
            if self.coords(i):
                self._set_anchor(self.cnf['anchor'], i)
        return r

    def _set_configure(self, options):
        """Internal function.\n
        Configures and binds according to the given options."""
        if options and isinstance(options, dict):
            return [self._set_configure(i) for i in options.values()]
        if not (options and isinstance(options[1], dict)):
            return

        con1 = bool(isinstance(options[0], tuple))
        if options[0] == 'configure' or (con1 and len(options[0]) > 1):
            # itemconfigure and configure
            for i in ('_txt', '_bit', '_img'):
                if self.coords(i) and options[1].get('anchor'):
                    self._set_anchor(options[1].pop('anchor', 'center'), i)
            _Canvas._configure(self, *options)

        if isinstance(options[0], tkinter.Misc):
            if isinstance(options[-1], (tuple, list)):
                # binds, itemconfigure and configure
                binds, conf = options[:-2], options[-1]
                _Canvas._configure(self, *conf)
                return _bind(*binds)
            if options[1].get('tag') == '_activebg':
                return _on_press_color(*options)    # _on_press_color
            return _bind(*options)  # binds

    def _configure1(self, cnf={}, **kw):
        """Internal Function.
        This function configure all the resources of 
        the Widget and save it to the class dict."""
        self.cnf, kw = self._make_dictionaries(
            self.cnf, self._set_trace(
                check_param(self, 'button', _cnfmerge((cnf, kw)))
            )
        )
        # Checks the items
        _button_items.create_items(self, 'check')
        # >.<
        for opt in ('overbackground', 'activebitmap', 'activeimage',
                    'bitmap', 'fg', 'bordercolor', 'borderless', 'image',
                    'overrelief', 'foreground', 'state', 'overforeground',
                    'focuscolor', 'focusthickness', 'activebackground', 
                    'activeforeground', 'compound'):
            if kw.get(opt) is not None:
                self._set_configure(self._get_options(opt, kw))
                if ((opt == 'state' and kw.get('compound', self.cnf.get('compound')))
                    or opt == 'compound'):
                    self._set_coords(**self._get_options(('_txt', '_img', '_bit'), kw))
        # Size
        if bool({'text', 'font', 'textvariable', 'image', 'bitmap', 'compound',
                 'padx', 'pady', 'width', 'height', 'activeimage', 'radius',
                 'activebitmap',}.intersection(set(kw))):
            self._set_configure(self._get_options('size', kw))
        # Text
        if {'text', 'anchor', 'font', 'justify', 'textvariable'}.intersection(set(kw)):
            self._set_configure(self._get_options('text', kw))
        # Takefocus
        cond1 = bool(self.itemcget('_tf', 'state') != 'hidden' and
                     self['state'] not in 'disabled')
        cond2 = bool(self.itemcget('_tf', 'state') != self['state'])
        if cond1 or cond2:
            self._set_configure(self._get_options('takefocus', kw))
        # Line border: This will darken the border around the button.
        if get_shade(self['bg'], BORDER_INTENSITY, 'auto-120') != self.itemcget('_border', 'outline'):
            self._set_configure(self._get_options('_border', kw))

    def _focus_in_out(self, intensity):
        """Internal function.\n
        Focus in and focus out effect maker."""
        self._main_win = self.winfo_toplevel()
        if not self._main_win.winfo_exists():
            return

        def _chngIn(evt):
            """Internal function."""
            try:
                if self.focus_get() is None:
                    self._tmp_bg = self['bg']
                    # [BUG] winfo_rgb doesn't read mac system colors.
                    color1 = self.winfo_rgb(self['highlightbackground'])
                    color1 = [int((int(i/257) + 255)/2) for i in color1]
                    color1 = '#%02x%02x%02x' % (color1[0], color1[1], color1[2])
                    color2 = get_shade(color1, intensity, 'auto-120')
                    _Canvas._configure(self, 'configure', {'bg': color1}, None)
                    _Canvas._configure(self, ('itemconfigure', '_border'),
                            {'outline': color2}, None)
                if self.focus_get():
                    if getattr(self, '_tmp_bg', False):
                        _Canvas._configure(self, 'configure',{'bg': self._tmp_bg}, None)
                    color = get_shade(self['bg'], intensity, 'auto-120')
                    _Canvas._configure(self, ('itemconfigure', '_border'),
                             {'outline': color}, None)
            except KeyError: 
                pass

        _bind(self._main_win, 
              {'className': 'focus%s' % str(self),
               'sequence': '<FocusIn>', 'func': _chngIn},
              {'className': 'focus%s' % str(self),
               'sequence': '<FocusOut>', 'func': _chngIn})
        return self._main_win

    def _relief(self, cnf, kw={}):
        """Internal function.\n
        Make overrelief and Relief work together."""
        kw = _cnfmerge((cnf, kw))
        cond1 = kw.get('overrelief', self.cnf.get('overrelief', '')) != ''
        if kw.get('relief') is not None and cond1:
            self._rel = (kw['relief'], True)
        if kw.get('_relief') is not None and kw.get('relief') is not None:
            self._rel = (kw['relief'], True)
            kw.pop('_relief', None)
        elif kw.get('_relief'):
            kw['relief'] = kw.pop('_relief')
        return kw

    def _set_size(self, evt=None):
        """Internal function.\n
        This will resize everything that is in the button"""
        if evt.width == self._size[0] and evt.height == self._size[1]:
            return
        # [issue-9] (NOT FIXED) On resizing the window the circlebutton doesn't resize properly, 
        #           current fix doesn't work properly.
        if self._type == 'circle' and evt.width != evt.height:
            if evt.width > evt.height:
                evt.width = evt.height
                # tkinter.Canvas.config(self, width=evt.width)
            else:
                evt.height = evt.width
                # tkinter.Canvas.config(self, height=evt.width)
            self.cnf['radius'] = evt.width
        self._size = (self.cnf['width'], self.cnf['height']) = (evt.width, evt.height)
        self.delete('_activebg')
        for i in self._after_IDs:
            self.after_cancel(self._after_IDs[i])
        _button_items.create_items(
            self, 'create', avoid=('_txt', '_img', '_bit'), safe_create=True)
        self._set_coords(self._get_options(('_txt', '_img', '_bit'), self.cnf))
        self._after_IDs[1] = self.after(1, self._get_functions('_activebg'))
        for t in ('_img', '_bit', '_txt', '_bd_color', '_border', '_tf'):
            self.tag_raise(t)
        self._after_IDs[2] = self.after(1, self._configure1)
        cur_focus = self.master.focus_get()
        if cur_focus and self.master != cur_focus and cur_focus != self:
            cur_focus.focus()
        else:
            self.master.focus()
            # [issue-7] Need a better fix to get focus back to the button if it has it previously
            if cur_focus == self:
                # [issue-7] (fixed) using after with 1ms delay solves the issue.
                self._after_IDs[3] = self.after(1, self.focus)

    def _active(self, value):
        """Internal function.\n 
        Do not call directly. Changes appearance when active."""

        def check_active_img_bit(op=''):
            tag = '_bit' if 'bit' in op else '_img'
            if self['activeimage'] != '':
                _Canvas._configure(self, ('itemconfigure', tag), 
                    {'image': self[op+'image']}, None)
            elif self['activebitmap'] != '':
                 _Canvas._configure(self, ('itemconfigure', tag), 
                    {'bitmap': self[op+'bitmap']}, None)

        if value in ('on_press', 'on_enter') or value is True:
            if self['state'] != 'pressed' :
                if value == 'on_press': 
                    self.cnf['_state'] = self.cnf['state']
                self.cnf['state'] = 'active'
                _Canvas._configure(self, ('itemconfigure', '_activebg'), 
                                   {'state': 'normal'}, None)
            _Canvas._configure(self, ('itemconfigure', '_border'), 
                               {'state': 'hidden'}, None)
            _Canvas._configure(self, ('itemconfigure', '_txt'), 
                               {'fill': self['activeforeground']}, None)
            check_active_img_bit('active')

        elif value in ('on_leave', 'on_release') or value is False:  # When not active (False)
            if self['state'] != 'pressed':
                if self.cnf.get('_state'): 
                    self.cnf['state'] = self.cnf['_state']
                if value == 'on_release':
                    self.cnf.pop('_state', None)
                    if self['state'] == 'active': 
                        self['state'] = 'normal'
                _Canvas._configure(self, ('itemconfigure', '_activebg'), 
                                   {'state': 'hidden'}, None)
                _Canvas._configure(self, ('itemconfigure', '_border'), 
                                   {'state': 'normal'}, None)
                fill = self['fg']
                if self._mouse_state_condition() and self['overforeground'] != '':
                    fill = self['overforeground']
                _Canvas._configure(self, ('itemconfigure', '_txt'), 
                                   {'fill': fill}, None)
                check_active_img_bit()

        self._set_coords(self._get_options(('_txt', '_img', '_bit'), self.cnf))

    def _on_press(self, *ags):
        """Internal function. When button is pressed <Button-1>"""
        self._rpin = None
        self._rpinloop = True

        def cmd(*a):
            """trigger function callback."""
            _bind(self, className='button_command', sequence='<ButtonRelease-1>')
            if self.cnf.get('repeatdelay', 0) and self.cnf.get('repeatinterval', 0) and self._rpinloop:
                self._rpin = self.after(self.cnf.get('repeatinterval', 0), cmd)
            if self.cnf.get('command'):
                self.cnf['command']() 

        def on_enter(*a):
            """Internal function.\n
            Enables when pressed and cursor
            is moved back on button."""
            self._active('on_enter')
            if self.cnf.get('repeatdelay', 0) and self.cnf.get('repeatinterval', 0):
                self._rpinloop = True
                cmd()
            _bind(self, className='button_command', sequence='<ButtonRelease-1>',
                  func=lambda *a: self.after(0, cmd), add='+')

        def on_leave(*a):
            """Internal function.\n
            Disables/Cancels when pressed and cursor
            is moved away from the button."""
            self._active('on_leave')                
            if self.cnf.get('repeatdelay', 0) and self.cnf.get('repeatinterval', 1):
                self._rpinloop = False
                self.after_cancel(self._rpin)
            _bind(self, className='button_command', sequence='<ButtonRelease-1>')

        if self['state'] not in 'disabled':
            self.focus_set()
            self._active('on_press')            
            if self.cnf.get('repeatdelay', 0) and self.cnf.get('repeatinterval', 1):
                self._rpin = self.after(self.cnf.get('repeatdelay', 0), cmd)
            _bind(self, {'className': 'on_press_enter', 'sequence': '<Enter>', 'func': on_enter},
                  {'className': 'on_press_leave', 'sequence': '<Leave>', 'func': on_leave},
                  {'className': 'button_command', 'sequence': '<ButtonRelease-1>', 'func': cmd})

    def _on_release(self, *ags):
        """Internal function. When button is released <ButtonRelease-1>"""
        if self['state'] in 'disabled': 
            return
        self._active('on_release')
        self._rpinloop = False
        if getattr(self, '_rpin', None): 
            self.after_cancel(self._rpin)
        _bind(self, {'className': 'on_press_enter', 'sequence': '<Enter>'},
              {'className': 'on_press_leave', 'sequence': '<Leave>'},
              {'className': 'button_command', 'sequence': '<ButtonRelease-1>'})

    def _compound(self, flag, width, height):
        """Internal function.\n
        Use `compound = 'left'/'right'/'top'/'bottom'` to configure."""
        _PiTag = ''
        if self.cnf.get('image', self.cnf.get('activeimage')):
            _PiTag = '_img'
        elif self.cnf.get('bitmap', self.cnf.get('activebitmap')):
            _PiTag = '_bit'
        _im_size = self.bbox(_PiTag)
        _txt_size = self.bbox('_txt')
        if _im_size and _txt_size:
            W_im = _im_size[2] - _im_size[0]
            H_im = _im_size[3] - _im_size[1]
            W_txt = _txt_size[2] - _txt_size[0]
            H_txt = _txt_size[3] - _txt_size[1]
            if flag == 'bottom':
                width = (width/2, width/2)
                height = (height/2-H_im/2, height/2+H_txt/2)
            elif flag == 'top':
                width = (width/2, width/2)
                height = (height/2+H_im/2, height/2-H_txt/2)
            elif flag == 'right':
                width = (width/2-W_im/2, width/2+W_txt/2)
                height = (height/2, height/2)
            elif flag == 'left':
                width = (width/2+W_im/2, width/2-W_txt/2)
                height = (height/2, height/2)        
            if isinstance(height, tuple):
                return {'_txt': (width[0], height[0]),
                            _PiTag: (width[1], height[1])}

    def _set_anchor(self, anchor, item):
        """Internal function.\n
        Sets the anchor position from (n, ne, e, se, s, sw, w, nw, or center)."""
        if self.cnf.get('compound') is not None:
            return
        bbox = self.bbox(item) or [0, 0, 0, 0]
        item_width = bbox[2] - bbox[0]
        item_height = bbox[3] - bbox[1]
        default_padx = 2 + int(item_width/2)
        default_pady = 0 + int(item_height/2)
        width = self.cnf['width'] = self.winfo_width()
        height = self.cnf['height'] = self.winfo_height()

        # Center
        x = width / 2
        y = height / 2

        if anchor in ('n', 'nw', 'ne'):
            x = int(width/2)
            y = default_pady + 0
            if anchor == 'nw':
                x = default_padx + 0
            elif anchor == 'ne':
                x = default_padx + (width - item_width) - 4
        
        elif anchor in ('s', 'sw', 'se'):
            x = int(width/2)
            y = default_pady + (height - item_height)
            if anchor == 'sw':
                x = default_padx + 0
            elif anchor == 'se':
                x = default_padx + (width - item_width) - 4
        
        elif anchor == 'e':
            x = default_padx + (width - item_width) - 4
                
        elif anchor == 'w':
            x = default_padx + 0
        return self.coords(item, x, y)


class ButtonBase(_Canvas, _button_functions):
    """Internal class used for tkinter macos Buttton"""

    _buttons = []  # list of all buttons

    def __init__(self, _type=None, master=None, cnf={}, **kw):
        kw = self._set_trace(_cnfmerge((cnf, kw)))
        kw = {k: v for k, v in kw.items() if v is not None}
        self._type = _type  # button type (circle, normal)
        self._after_IDs = {} # _after_IDs
        self._fixed_size = {'w': False, 'h': False}
        self._var_cb = None
        self.cnf = {}
        
        cnf = {}
        for i in kw.copy().keys():
            if i in BUTTON_FEATURES:
                cnf[i] = kw.pop(i, None)

        cnf['fg'] = cnf['foreground'] = cnf.get('fg', cnf.get('foreground', SYSTEM_DEFAULT.fg))
        cnf['anchor'] = cnf.get('anchor', 'center')
        cnf['justify'] = cnf.get('justify', 'center')
        cnf['borderless'] = cnf.get('borderless', False)
        cnf['disabledforeground'] = cnf.get('disabledforeground', 'grey')
        cnf['disabledbackground'] = cnf.get('disabledbackground', 'grey')
        cnf['state'] = cnf.get('state', 'normal')
        cnf['activeforeground'] = cnf.get('activeforeground', 'white')
        cnf['activebackground'] = cnf.get('activebackground', ("#4b91fe", "#055be5"))
        cnf['focuscolor'] = cnf.get('focuscolor', '#81b3f4')
        cnf['focusthickness'] = cnf.get('focusthickness', 2)
        cnf['compound'] = cnf.get('compound', None)
        cnf['padx'] = cnf.get('padx', 1)
        cnf['pady'] = cnf.get('pady', 1)
        cnf['repeatdelay'] = cnf.get('repeatdelay', 0)
        cnf['repeatinterval'] = cnf.get('repeatinterval', 1)
        cnf['wraplength'] = cnf.get('wraplength', 0)
        cnf['underline'] = cnf.get('underline', -1)

        for i in ('activebitmap', 'activeimage', 'bitmap', 'command', 
                  'image', 'overbackground', 'overforeground', 'overrelief', 
                  'text', 'textvariable'):
            cnf[i] = cnf.get(i, '')

        if self._type == 'circle':
            cnf['radius'] = int(kw.pop('radius', 35)) 
            ra = int(cnf['radius']*2 + 4)
            kw['width'] = kw['height'] = kw.get('width', kw.get('height', ra))
        else:
            kw['width'] = kw.get('width', 87)
            kw['height'] = kw.get('height', 24)

        kw['takefocus'] = kw.get('takefocus', 1)
        kw['bg'] = kw.pop('bg', kw.pop('background', SYSTEM_DEFAULT.bg))
        kw['highlightthickness'] = kw.get('highlightthickness', 0)

        _Canvas.__init__(self, master=master, **kw)
        self.cnf = check_param(self, 'button', **cnf)
        self.cnf['bordercolor'] = self.cnf['highlightbackground'] = self.cnf.get(
            'bordercolor', self.cnf.get('highlightbackground', get_shade(self['bg'], 0.04, 'auto-120')))

        self._buttons.append(self)
        self._size = (self.winfo_width(), self.winfo_height())
        _button_items.create_items(self, 'create', safe_create=True)
        self._org_bg = self['bg']
        if kw.get('relief') is not None:
            self._rel = (kw['relief'], True)
        else:
            self._rel = ('flat', False)

        _bind(self,
              {'className': 'button_release',
                  'sequence': '<ButtonRelease-1>', 'func': self._on_release},
              {'className': 'button_press',
                  'sequence': '<Button-1>', 'func': self._on_press},
              {'className': 'set_size', 'sequence': '<Configure>', 'func': self._set_size})

        self._focus_in_out(BORDER_INTENSITY)
        self._configure1(self.cnf)

    def _configure(self, cmd, cnf=None, kw=None):
        'Internal function to configure the inherited class'
        kw = self._relief(cnf, kw)
        cnf = {}
        for i in list(kw):
            if ((i in BUTTON_FEATURES)
                or (i == 'radius' and self._type == 'circle')):
                cnf[i] = kw.pop(i, None)
        _return = _Canvas._configure(self, cmd, None, kw)
        if kw.get('bg') or kw.get('background'):
            self._org_bg = self['bg']
        self._configure1(cnf)
        if _return is not None and isinstance(_return, dict):
            _return.update(self.cnf)
            _return['compound'] = self.cnf.get('compound', 'none')
            for k in list(_return):
                if k not in self.keys():
                    _return.pop(k)
        return _return

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        need_string = ('textvariable', 'image', 'activeimage')
        need_int = ('borderwidth', 'bd', 'highlightthickness')
        if key == 'radius' and self._type == 'circle':
            return self.cnf.get('radius')
        if key in BUTTON_FEATURES:
            if key in need_string and self.cnf.get(key):
                return str(self.cnf.get(key))
            if key == 'command' and self.cnf.get(key) is None:
                return 'none'
            return self.cnf.get(key)
        value = _Canvas.cget(self, key)
        if key in need_int:
            return int(value)
        return value
    __getitem__ = cget

    def keys(self):
        """Return a list of all resource names of this widget."""
        return sorted(
            set([*BUTTON_PROPERTIES, *BUTTON_FEATURES])
        )
    
    def invoke(self):
        """Invoke the command associated with the button.

        The return value is the return value from the command,
        or an empty string if there is no command associated with
        the button. This command is ignored if the button's state
        is disabled.
        """
        if (self['state'] not in ('disable', 'disabled') 
                and self.cnf.get('command')):
            return self.cnf['command']()

    @cp._colorvar_patch_destroy
    def destroy(self):
        """Destroy this and all descendants widgets. This will
        end the application of this Tcl interpreter."""
        if self._main_win.winfo_exists():
            _bind(self._main_win,
                {'className': 'focus%s' % str(self), 'sequence': '<FocusIn>'},
                {'className': 'focus%s' % str(self), 'sequence': '<FocusOut>'})
        for i in self._after_IDs:
            self.after_cancel(self._after_IDs[i])
        if self.cnf.get('textvariable', '') != '':
            self.configure(textvariable='')
        if self in self._buttons:
            self._buttons.remove(self)
        return _Canvas.destroy(self)