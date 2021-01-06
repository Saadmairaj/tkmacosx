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

import colour as C
import tkinter as _tk
import tkmacosx.variables as tkv

from tkinter import ttk
from tkinter import _cnfmerge


def delta(evt):
    """Modified delta to work with all platforms."""
    if evt.num == 5 or evt.delta < 0:
        return -1
    return 1


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


def check_function_equality(func1, func2):
    """Checks if two functions are same."""
    return func1.__code__.co_code == func2.__code__.co_code


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


def _on_press_color(cls=None, cnf={}, **kw):
    """Internal function. Do not call directly.\n
    Give gradient color effect used for activebackground.
    Returns ids"""
    kw = _cnfmerge((cnf, kw))
    cls = kw.get('cls', cls)
    w = cls.cnf.get('height', cls.winfo_width())
    h = cls.cnf.get('height', cls.winfo_height())
    tag = kw.get('tag', 'press')
    state = kw.get('state', 'normal' if cls.cnf.get(
                   'state') in ('active', 'pressed') else 'hidden')
    if not cls:
        raise ValueError('Counld not refer to any class instance "cls".')
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
    cr = cls.cnf['activebackground'] = kw.get(
        'color', cls.cnf.get('activebackground', 
        ("#4b91fe", "#055be5"))) # This is the default color for mac
    cls.delete(tag)
    ids = []
    if isinstance(cr, (tuple, list)) and None in cr:
        cr = list(cr)
        cr.remove(None)
        cr = cr[0]
    if not isinstance(cr, (tuple, list)):
        cr = (C.Color(cr), C.Color(cr))
    else:
        cr = (C.Color(cr[0]), C.Color(cr[1]))
    for i, j in enumerate(tuple(cr[0].range_to(cr[1], kw.get('height', h)))):
        ags = (0, i, kw.get('width', w), i)
        cnf = {'fill': j, 'tag': tag, 'state': state}
        ids.append(cls._create('line', ags, cnf))
    cls.tag_lower(tag)     # keep the tag last
    return tuple(ids)


def _info_button(master, cnf={}, **kw):
    """Internal Function.\n
    This function takes essentials parameters to give
    the approximate width and height accordingly. \n
    It creates a ttk button and use all the resources given
    and returns width and height of the ttk button, after taking
    width and height the button gets destroyed also the custom style."""
    kw = _tk._cnfmerge((cnf, kw))
    cnf = dict(**kw)    
    name = '%s.TButton' % master
    _style_tmp = ttk.Style()
    _style_tmp.configure(name, font=kw.pop('font', None))
    _style_tmp.configure(name, padding=(kw.pop('padx', 0), kw.pop('pady', 0)))
    tmp = ttk.Button(master, style=name, **kw)
    geo = [tmp.winfo_reqwidth(), tmp.winfo_reqheight()]
    # [issue-2] Need fix --- doesn't really delete the custom style
    del _style_tmp
    tmp.destroy()
    return geo


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
        color = list(float(i/65535.0)
                     for i in _tk._default_root.winfo_rgb(color))
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


class _Canvas(_tk.Widget):
    """Internal Class."""

    def __init__(self, master=None, cnf={}, **kw):
        _tk.Widget.__init__(self, master, 'canvas', cnf, kw)

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
        args = _tk._flatten(args)
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


class _button_properties:
    """Internal class.\n
    Contains modified properties of Button widget. Do not call directly."""

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
        if not self.cnf.get('width'):
            self.cnf['width'] = self.winfo_width()
        if not self.cnf.get('height'):
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
                {'outline': get_shade(self['bg'], 0.1, 'auto-120')}, None]
    
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
        _opt = {}
        if bool(kw.get('borderless')) or self.cnf.get('borderless'):
            if not check_function_equality(self.master.config, self._get_functions('borderless', kw)):
                self.master.config = self.master.configure = self._get_functions(
                    'borderless', kw)
            self.cnf['highlightbackground'] = self.cnf['bordercolor'] = self.master['bg']
            _opt[1] = [('itemconfigure', '_bd_color'), {'outline': self.master['bg']}, None]
            _opt[2] = ['configure', {'highlightbackground': self.master['bg']}, None]
        elif not bool(kw.get('borderless', True)) or not self.cnf.get('borderless'):
            if self.cnf.get('bordercolor') == self.master['bg']:
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
        self._create_items('create', True, avoid=(
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
        self._fixed_size['w'] = True if kw.get('width', kw.get('radius')) else False
        self._fixed_size['h'] = True if kw.get('height', kw.get('radius')) else False
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
        if int(self['takefocus']) and self['state'] in ('normal', 'active', 'pressed'):
            fn = self._get_functions('takefocus', kw)
            _opt = [self, {'className': 'takefocus', 'sequence':
                            '<FocusIn>', 'func': fn.get('<FocusIn>')},
                            {'className': 'takefocus', 'sequence':
                            '<FocusOut>', 'func': fn.get('<FocusOut>')}]

        elif not int(self['takefocus']) or self['state'] in 'disabled':
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


class _button_functions:
    """Internal class.\n
    Function class for Button widget. Do not call directly."""

    _buttons = []  # list of all buttons
    _features = ('overbackground', 'overforeground', 'activeimage', 'activebitmap', 
                 'anchor', 'bitmap', 'bordercolor', 'borderless', 'command', 'compound', 
                 'disabledforeground', 'justify', 'disabledbackground', 'fg', 'font', 
                 'foreground', 'height', 'image', 'overrelief', 'padx', 'pady', 'repeatdelay', 
                 'repeatinterval', 'text', 'textvariable', 'underline', 'width', 'state', 
                 'focusthickness', 'focuscolor', 'highlightbackground', 'activebackground', 
                 'activeforeground')

    def _mouse_state_condition(self):
        """Internal function.\n
        True if state is normal and cursor is on the widget."""
        con1 = bool(self.cnf.get('state') not in 'disabled')
        con2 = bool(self.winfo_containing(*self.winfo_pointerxy()) == self)
        return con1 and con2

    def _make_dictionaries(self, cnf={}, kw={}):
        """Internal function.\n
        Merges kw into cnf and removes None values."""
        kw['bordercolor'] = kw['highlightbackground'] = kw.get('bordercolor', kw.get('highlightbackground'))
        kw = {k: v for k, v in kw.items() if v is not None}
        cnf.update(kw)
        cnf = {k: v for k, v in cnf.items() if v is not None}
        cnf['fg'] = cnf['foreground'] = kw.get('foreground', kw.get('fg', cnf.get('fg', 'black')))
        if cnf.get('textvariable', '') != '':
            cnf['text'] = cnf['textvariable'].get()
        if kw.get('activebackground'):
            cnf.pop('activebackground')
        return cnf, kw

    def _set_trace(self, kw):
        """Internal function."""
        for i in ('overforeground', 'foreground', 'fg', 'activeforeground'):
            if isinstance(kw.get(i), _tk.Variable):
                var = kw[i]
                cbname = var.trace_variable('w', lambda a, b, c, i=i, var=var,
                                cls=self: cls.config({i: var.get()}))
                if (self, i) in tkv._all_traces_colorvar:
                    v, cb = tkv._all_traces_colorvar.get((self, i))
                    v.trace_vdelete('w', cb)
                    tkv._all_traces_colorvar[(self, i)] = (var, cbname)
                else:
                    tkv._all_traces_colorvar[(self, i)] = (var, cbname)
                kw[i] = var.get()
        return kw

    def _create_items(self, cmd, safe_create=False, **kw):
        """Internal function.\n
        Checks and creates (text, image, bitmap, border, 
        bordercolor, takefocus ring*) items."""

        def check_tag(tag):
            """Internal function."""
            return self.check_tag(cmd, tag, safe_create, kw.get('avoid', []))
        
        def active_state(val):
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

        ids = []
        cond_image = bool(
            self.cnf.get('image', self.cnf.get('activeimage', '')) != '')
        cond_bitmap = bool(
            self.cnf.get('bitmap', self.cnf.get('activebitmap', '')) != '')

        # Text item.
        if check_tag('_txt') and self.cnf.get('text'):
            ids.append(self._create('text', (0, 0), {
                    'text': None, 'tag': '_txt', 'fill': active_state('fill')}))
        
        # Image item (image and activeimage).
        if check_tag('_img') and cond_image:
            ids.append(self._create('image', (0, 0), {
                    'tag': '_img', 'image': active_state('img')}))
        
        # Bitmap items (bitmap and activebitmap).
        elif check_tag('_bit') and cond_bitmap:
            ids.append(self._create('bitmap', (0, 0), {
                    'tag': '_bit', 'bitmap': active_state('bit')}))
        
        # Border color item.
        bd_color = self.cnf.get('bordercolor', get_shade(self['bg'], 0.04, 'auto-120'))
        if check_tag('_bd_color') and self._type == 'circle':
            pad = 2
            width = r = int(self.cnf.get('width', 87)/2)  # radius = x = y (in pixels)
            _bd_points = (pad-width, pad-width, r*2+width-pad, r*2+width-pad)
            kw_bd_color = {
                'tag': '_bd_color', 
                'state': active_state('state'),
                'width': width*2,'outline': bd_color}
            ids.append(self._create('oval', _bd_points, kw_bd_color))
        elif check_tag('_bd_color'):
            _bd_points = (0, -1, self.cnf.get('width', 87), self.cnf.get('height', 24)+3, 7)  # was 6
            ids.append(self.rounded_rect(
                _bd_points, width=6, tag='_bd_color', style='arc', outline=bd_color))
        
        # Border item.
        bo_color = get_shade(self['bg'], 0.1, 'auto-120')
        if check_tag('_border') and self._type == 'circle':   
            pad = 2
            r = int(self.cnf.get('width', 87)/2)  # radius = x = y
            _bo_points = (pad, pad, r*2-(pad+1), r*2-(pad+1))
            ids.append(self._create('oval', _bo_points, {
                'tag': '_border', 'outline': self.cnf.get('bordercolor', bo_color) }))
        elif check_tag('_border'):
            h = 4
            if int(self['highlightthickness']):
                h += 1
            _bo_points = (2, 2, self.cnf.get('width', 87)-5, self.cnf.get('height', 24)-h, 4)  # was 3
            ids.append(self.rounded_rect(
                _bo_points, width=1, outline=bo_color, smooth=1, tag='_border', 
                style='arc', state=active_state('state')))
        
        # Takefocus highlight ring.
        if check_tag('_tf') and self._type == 'circle':
            pad = 1
            width = self.cnf.get('focusthickness', 2)
            r = int(self.cnf.get('width', 87)/2)  # radius = x = y
            _tk_points = (pad+width, pad+width, r*2-width-pad, r*2-width-pad)
            ids.append(self._create('oval', _tk_points, {
                'tag': '_tf', 'width': width, 
                'outline': self.cnf.get('focuscolor', '#81b3f4'), 
                'state': 'hidden'}))
                
        elif check_tag('_tf'):
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
            ids.append(self.rounded_rect(
                _tk_points, width=w, style='arc', 
                outline=self.cnf.get('focuscolor', '#81b3f4'), 
                tag='_tf', state='hidden'))
        return tuple(ids)

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
        if not options:
            return
        if isinstance(options, dict):
            return [self._set_configure(i) for i in options.values()]
        if len(options) > 1 and isinstance(options[1], dict):
            con1 = bool(isinstance(options[0], tuple))
            if options[0] == 'configure' or (con1 and len(options[0]) > 1):
                # itemconfigure and configure
                for i in ('_txt', '_bit', '_img'):
                    if self.coords(i) and options[1].get('anchor'):
                        self._set_anchor(options[1].pop('anchor', 'center'), i)
                _Canvas._configure(self, *options)
            if isinstance(options[0], _tk.Misc):
                if isinstance(options[-1], (tuple, list)):
                    # binds, itemconfigure and configure
                    binds, conf = options[:-2], options[-1]
                    for i in ('_txt', '_bit', '_img'):
                        if i in self.find('all') and conf.get('anchor'):
                            self._set_anchor(conf.pop('anchor', 'center'), i)
                    _Canvas._configure(self, *conf)
                    return _bind(*binds)
                if options[1].get('tag') == '_activebg':
                    return _on_press_color(*options)    # _on_press_color
                return _bind(*options)  # binds

    def _configure1(self, cnf={}, **kw):
        """Internal Function.
        This function configure all the resources of 
        the Widget and save it to the class dict."""
        self.cnf, kw = self._make_dictionaries(self.cnf, 
                            self._set_trace(_cnfmerge((cnf, kw))))
        # Checks the items
        self._create_items('check')
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
        if get_shade(self['bg'], 0.1, 'auto-120') != self.itemcget('_border', 'outline'):
            self._set_configure(self._get_options('_border', kw))

    def _focus_in_out(self, intensity):
        """Internal function.\n
        Focus in and focus out effect maker."""
        main_win = self.winfo_toplevel()

        def _chngIn(evt):
            """Internal function."""
            try:
                if self.focus_get() is None:
                    color = get_shade(self['bg'], intensity, 'auto-120')
                    _Canvas._configure(self, ('itemconfigure', '_border'),
                            {'outline': color}, None)
                c1 = get_shade(self['bg'], intensity, 'auto-120')
                c2 = self.itemcget('_border', 'outline')
                if self.focus_get() and c1 == c2:
                    color = get_shade(self['bg'], 0.1, 'auto-120')
                    _Canvas._configure(self, ('itemconfigure', '_border'),
                             {'outline': color}, None)
            # [issue-8] (Fixed) tkinter issue with combobox (w = w.children[n])
            except KeyError: 
                pass

        _bind(main_win, 
              {'className': 'focus%s' % str(self),
               'sequence': '<FocusIn>', 'func': _chngIn},
              {'className': 'focus%s' % str(self),
               'sequence': '<FocusOut>', 'func': _chngIn})
        return main_win

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
                # _tk.Canvas.config(self, width=evt.width)
            else:
                evt.height = evt.width
                # _tk.Canvas.config(self, height=evt.width)
            self.cnf['radius'] = evt.width
        self._size = (self.cnf['width'], self.cnf['height']) = (evt.width, evt.height)
        self.delete('_activebg')
        # [issue-6] (Fixed) Need fix (laggy on resizing) --> workaround: cancel if still resizing
        for i in self._after_IDs:
            self.after_cancel(self._after_IDs[i])
        self._create_items('create', avoid=('_txt', '_img', '_bit'), safe_create=True)
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
                               {'fill': self.cnf.get('activeforeground', 'white')}, None)
            _Canvas._configure(self, ('itemconfigure', '_img'), 
                            {'image': self.cnf.get('activeimage', self.cnf.get('image', ''))}, None)
            _Canvas._configure(self, ('itemconfigure', '_bit'), 
                            {'bitmap': self.cnf.get('activebitmap', self.cnf.get('bitmap', ''))}, None)

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
                fill = self.cnf.get('fg', 'black')
                if self._mouse_state_condition() and self.cnf.get('overforeground'):
                    fill = self.cnf['overforeground']
                _Canvas._configure(self, ('itemconfigure', '_txt'), 
                                   {'fill': fill}, None)
                _Canvas._configure(self, ('itemconfigure', '_img'), 
                                {'image': self.cnf.get('image', '')}, None)
                _Canvas._configure(self, ('itemconfigure', '_bit'), 
                                {'bitmap': self.cnf.get('bitmap', '')}, None)
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
            elif flag is not None:
                raise _tk.TclError(
                    'bad compound flag "{}", must be -none, -top, -bottom, -left, or -right'\
                        .format(flag))
            if isinstance(height, tuple):
                if _im_size is None:
                    return {'_txt': (width[0], height[0])}
                return {'_txt': (width[0], height[0]),
                            _PiTag: (width[1], height[1])}

    def _set_anchor(self, anchor, item):
        """Internal function.\n
        Sets the anchor position from (n, ne, e, se, s, sw, w, nw, or center)."""
        if self.cnf.get('compound') is not None:
            return
        bbox = self.bbox(item)
        item_width = bbox[2] - bbox[0]
        item_height = bbox[3] - bbox[1]
        default_padx = 2 + int(item_width/2)
        default_pady = 0 + int(item_height/2)
        width = self.cnf.get('width', self.winfo_reqwidth())
        height = self.cnf.get('height', self.winfo_reqheight())

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
            
        elif anchor != 'center':
            raise _tk.TclError(
                'bad anchor position "{}": must be n, ne, e, se, s, sw, w, nw, or center'.format(anchor))

        return self.coords(item, x, y)


class ButtonBase(_Canvas, _button_functions):
    """Internal class used for tkinter macos Buttton"""

    def __init__(self, _type=None, master=None, cnf={}, **kw):
        kw = self._set_trace(_cnfmerge((cnf, kw)))
        kw = {k: v for k, v in kw.items() if v is not None}
        self._type = _type  # button type (circle, normal)
        self._after_IDs = {} # _after_IDs
        self._fixed_size = {'w': False, 'h': False}
        self._var_cb = None
        self.cnf = {}
        for i in kw.copy().keys():
            if i in self._features:
                self.cnf[i] = kw.pop(i, None)

        self.cnf['fg'] = self.cnf['foreground'] = self.cnf.get('fg', self.cnf.get('foreground', 'black'))
        self.cnf['anchor'] = self.cnf.get('anchor', 'center')
        self.cnf['borderless'] = self.cnf.get('borderless', False)
        self.cnf['disabledforeground'] = self.cnf.get('disabledforeground', 'grey')
        self.cnf['state'] = self.cnf.get('state', 'normal')
        self.cnf['activeforeground'] = self.cnf.get('activeforeground', 'white')

        if self._type == 'circle':
            self.cnf['radius'] = int(kw.pop('radius', 35)) 
            ra = int(self.cnf['radius']*2 + 4)
            kw['width'] = kw['height'] = kw.get('width', kw.get('height', ra))
        else:
            kw['width'] = kw.get('width', 87)
            kw['height'] = kw.get('height', 24)

        kw['takefocus'] = kw.get('takefocus', 1)
        kw['bg'] = kw.pop('bg', kw.pop('background', 'white'))
        kw['highlightthickness'] = kw.get('highlightthickness', 0)

        _Canvas.__init__(self, master=master, **kw)
        self.cnf['bordercolor'] = self.cnf['highlightbackground'] = self.cnf.get(
            'bordercolor', self.cnf.get('highlightbackground', get_shade(self['bg'], 0.04, 'auto-120')))

        self._buttons.append(self)
        self._size = (self.winfo_width(), self.winfo_height())
        self._create_items('create', safe_create=True)
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

        self._focus_in_out(0.04)
        self._configure1(self.cnf)

    def _configure(self, cmd, cnf=None, kw=None):
        'Internal function to configure the inherited class'
        kw = self._relief(cnf, kw)
        cnf = {}
        for i in list(kw):
            if ((i in self._features)
                or (i == 'radius' and self._type == 'circle')):
                cnf[i] = kw.pop(i, None)
        _return = _Canvas._configure(self, cmd, None, kw)
        if kw.get('bg') or kw.get('background'):
            self._org_bg = self['bg']
        self._configure1(cnf)
        if _return is not None and isinstance(_return, dict):
            _return.update(self.cnf)
        return _return

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key == 'radius' and self._type == 'circle':
            return self.cnf.get('radius')
        if key in self._features:
            return self.cnf.get(key)
        return _Canvas.cget(self, key)
    __getitem__ = cget

    def keys(self):
        """Return a list of all resource names of this widget."""
        _return = _Canvas.keys(self)
        _return.extend(self._features)
        return sorted(list(set(_return)))

    @tkv._colorvar_patch_destroy
    def destroy(self):
        """Destroy this and all descendants widgets. This will
        end the application of this Tcl interpreter."""
        main_win = self.winfo_toplevel()
        _bind(main_win, 
              {'className': 'focus%s' % str(self), 'sequence': '<FocusIn>'},
              {'className': 'focus%s' % str(self), 'sequence': '<FocusOut>'})
        if self.cnf.get('textvariable', '') != '':
            self.configure(textvariable='')
        if self in self._buttons:
            self._buttons.remove(self)
        return _Canvas.destroy(self)


class SFrameBase(_tk.Frame):
    """Base Class for SFrame."""

    _features = ('scrollbarwidth', 'mousewheel',
                 'avoidmousewheel', 'canvas', 'scrollbar')

    def __init__(self, master=None, cnf={}, **kw):
        kw = _cnfmerge((cnf, kw))
        self.cnf = {}
        self._after_ids = {}
        self.cnf['scrollbarwidth'] = kw.pop('scrollbarwidth', 10)
        self.cnf['mousewheel'] = kw.pop('mousewheel', True)
        self.cnf['avoidmousewheel'] = kw.pop('avoidmousewheel', ())
        self.cnf['canvas'] = kw.pop('canvas', _tk.Canvas(master=master, 
                                                         highlightthickness=0,
                                                         width=kw.pop('width', 250), 
                                                         height=kw.pop('height', 250)))
        self.cnf['scrollbar'] = kw.pop('scrollbar', _tk.Scrollbar(self.cnf['canvas'],
                                                                  orient='vertical', 
                                                                  width=self.cnf['scrollbarwidth']))
        _tk.Frame.__init__(self, self.cnf['canvas'], **kw)
        self.cnf['canvas']['bg'] = self['bg']
        self.cnf['scrollbar'].place(relx=1, rely=0, anchor='ne', relheight=1)
        self.cnf['scrollbar'].configure(command=self.cnf['canvas'].yview)
        self.cnf['canvas'].configure(yscrollcommand=self.cnf['scrollbar'].set)
        self.cnf['canvas'].create_window(0, 0, anchor='nw', tags="window", window=self,
                                         width=self.cnf['canvas'].winfo_reqwidth()-\
                                               self.cnf['scrollbar'].winfo_reqwidth())
        self.cnf['canvas'].bind("<Configure>", self._configure_height, add="+")
        _bind(self, className='configure',
              sequence='<Configure>', func=self._configure_window)
        self._mouse_scrolling(self.cnf['mousewheel'])
        self._avoid_mousewheel(self.cnf.get('avoidmousewheel'))
        self._geometryManager()

    def _avoid_mousewheel(self, widgets):
        """Internal function.\n
        Use this to have multiple scrollable 
        widgets inside of SFrame."""

        def set_widget(wid):
            """Internal function.\n
            Binds <Enter> and <Leave> to the widget 
            to enable/disable mousewheel scrolling."""
            binds = [{'className': 'mw_state_sframe', 'sequence':
                   '<Leave>', 'func': lambda _: self._mouse_scrolling(True)}]
            if not isinstance(wid, SFrameBase):
                binds.append({'className': 'mw_state_sframe', 'sequence': 
                    '<Enter>', 'func': lambda _: self._mouse_scrolling(False)})
            _bind(wid, *binds)
    
        if isinstance(widgets, (list, tuple)):
            for widget in widgets:
                set_widget(widget)
        else:
            set_widget(widgets)

    def _mouse_scrolling(self, state):
        """Internal function."""
        def enable_mousewheel(evt=None):
            """Internal function."""
            self.bind_all('<MouseWheel>', self._on_mouse_scroll)

        def disable_mousewheel(evt=None):
            """Internal function."""
            self.unbind_all('<MouseWheel>')

        if state:
            _bind(self,
                  {'className': 'mousewheel_state', 'sequence':
                   '<Enter>', 'func': enable_mousewheel},
                  {'className': 'mousewheel_state', 'sequence':
                   '<Leave>', 'func': disable_mousewheel})
            enable_mousewheel()
        else:
            _bind(self,
                  {'className': 'mousewheel_state', 'sequence': '<Enter>'},
                  {'className': 'mousewheel_state', 'sequence': '<Leave>'})
            disable_mousewheel()

    def _on_mouse_scroll(self, evt):
        """Internal function."""
        if self.winfo_height() < self.cnf['canvas'].winfo_height(): 
            return 
        if evt.state == 0:
            self.cnf['canvas'].yview_scroll(-1*delta(evt), 'units')

    def _configure_height(self, evt):
        """Internal function."""
        width = self.cnf['canvas'].winfo_width()-self.cnf['scrollbar'].winfo_width()
        self.cnf['canvas'].itemconfig('window', width=width)

    def _configure_window(self, evt):
        """Internal function."""
        # this will update the position of scrollbar when scrolled from mousewheel.
        # fixes some bugs
        # makes scrolling more smoother
        self.after_cancel(self._after_ids.get(0, ' '))
        self._after_ids[0] = self.after(1, lambda: self.cnf['canvas'].configure(
                scrollregion=self.cnf['canvas'].bbox('all')))

    def _geometryManager(self):
        """Internal function."""
        # Use set to support the following in both python 2 and python 3
        geo_methods = [m for m in (set(_tk.Pack.__dict__) | set(_tk.Grid.__dict__) |
                       set(_tk.Place.__dict__)) if m not in _tk.Frame.__dict__]
        for m in geo_methods:
            if m[0] != '_' and 'config' not in m:
                setattr(self, m, getattr(self.cnf['canvas'], m))

    def _configure(self, cmd, cnf=None, kw=None):
        kw = _tk._cnfmerge((cnf, kw))
        self.cnf['scrollbar']['width'] = kw.pop(
            'scrollbarwidth', self.cnf['scrollbar']['width'])
        for key in kw.copy():
            if key in self._features:
                self.cnf[key] = kw.pop(key, self.cnf.get(key))
        self.cnf['canvas']['width'] = kw.pop(
            'width', self.cnf['canvas']['width'])
        self.cnf['canvas']['height'] = kw.pop(
            'height', self.cnf['canvas']['height'])
        self._mouse_scrolling(self.cnf['mousewheel'])
        self._avoid_mousewheel(self.cnf['avoidmousewheel'])
        _return = _tk.Frame._configure(self, cmd, {}, kw)
        if kw.get('bg', kw.get('background')):
            self.cnf['canvas']['bg'] = self['bg']
        if isinstance(_return, dict):
            _return.update(self.cnf)
        return _return

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in self._features:
            return self.cnf.get(key)
        return _tk.Frame.cget(self, key)
    __getitem__ = cget


class MarqueeBase(_tk.Canvas):
    """Base class for Marquee."""

    def __init__(self, master=None, cnf={}, **kw):
        kw = _cnfmerge((cnf, kw))
        self._stop_state = False
        self.cnf = dict(
            text=kw.pop('text', ''),
            font=kw.pop('font', None),
            fg=kw.pop('fg', 'black') if kw.get(
                'fg') else kw.pop('foreground', 'black'),
            fps=kw.pop('fps', 30),
            left_margin=kw.pop('left_margin', 10),
            initial_delay=kw.pop('initial_delay', 1000),
            end_delay=kw.pop('end_delay', 1000),
            smoothness=kw.pop('smoothness', 1),  # 1 <= smooth < 1
        )
        kw['height'] = kw.get('height', 24)
        kw['highlightthickness'] = kw.get('highlightthickness', 0)
        _tk.Canvas.__init__(self, master=master, **kw)
        self._create('text', (3, 1), dict(anchor='w', tag='text', text=self.cnf.get('text'),
                                          font=self.cnf.get('font'), fill=self.cnf.get('fg')))
        _bind(self, className='configure',
                  sequence='<Configure>', func=self._check)
        self.after_id = ' '
    
    def _set_height(self, evt=None):
        """Internal function."""
        bbox = self.bbox('text')
        height = bbox[3] - bbox[1] + 8
        if int(self['height']) == height: 
            return
        _tk.Canvas._configure(self, 'configure', {'height': height}, None)

    def _reset(self, force_reset=False):
        """Internal function.\n
        Resets the text position, do not call directly."""
        if self.after_id == ' ' and not force_reset:
            return
        self.after_cancel(self.after_id)
        self.coords('text', 3, self.winfo_height()/2)  # RESETS TEXT
        self.after_id = ' '

    def _check(self, evt=None):
        """Internal function.\n
        Sets the text properly in the frame."""
        self._set_height()
        self.coords('text', 3, self.winfo_height()/2)
        text_width = self.bbox('text')[2]   # TEXT WIDTH
        frame_width = self.winfo_width()    # FRAME WIDTH
        if text_width + 1 < frame_width:
            self._reset()
        elif self.after_id == ' ':
            delay = self.cnf.get('initial_delay')  # INITITAL DEALY
            self.after_id = self.after(delay, self._animate)

    def _animate(self, evt=None):
        """Internal function.\n
        Process text and move text."""
        if self._stop_state: 
            return
        self._set_height()
        text_width = self.bbox('text')[2]   # TEXT WIDTH
        frame_width = self.winfo_width()    # FRAME WIDTH
        delay = int(self.cnf.get('smoothness')*1000 / self.cnf.get('fps'))
        if text_width + 1 + self.cnf.get('left_margin') < frame_width:
            self.after(self.cnf.get('end_delay'), self.coords,
                       'text', 3, self.winfo_height()/2)  # RESETS TEXT
            delay = self.cnf.get('initial_delay') + \
                self.cnf.get('end_delay')  # INITITAL DEALY
        else:
            # MOVE -1 PIXEL EVERYTIME
            self.tk.call((self._w, 'move') + (
                'text', -self.cnf.get('smoothness'), 0))
        self.after_id = self.after(delay, self._animate)

    def _configure(self, cmd, cnf=None, kw=None):
        """Internal function."""
        kw = _cnfmerge((cnf, kw))
        self.cnf = dict(
            text=kw.pop('text', self.cnf.get('text')),
            font=kw.pop('font', self.cnf.get('font')),
            fg=kw.pop('fg', self.cnf.get('fg')) if kw.get('fg')
            else kw.pop('foreground', self.cnf.get('foreground')),
            fps=kw.pop('fps', self.cnf.get('fps')),
            left_margin=kw.pop('left_margin', self.cnf.get('left_margin')),
            initial_delay=kw.pop(
                'initial_delay', self.cnf.get('initial_delay')),
            end_delay=kw.pop('end_delay', self.cnf.get('end_delay')),
            smoothness=kw.pop('smoothness', self.cnf.get('smoothness')),
        )
        _tk.Canvas._configure(self, ('itemconfigure','text'), dict(text=self.cnf.get('text'),
                        font=self.cnf.get('font'), fill=self.cnf.get('fg')), None)
        self._set_height()
        return _tk.Canvas._configure(self, cmd, kw, None)

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in self.cnf.keys():
            return self.cnf[key]
        return _tk.Canvas.cget(self, key)
    __getitem__ = cget

    def destroy(self):
        """Destroy this widget."""
        self.after_cancel(self.after_id)
        return _tk.Canvas.destroy(self)


class _radiobutton_functions:
    _properties = (
        'activebackground',
        'activeforeground',
        'anchor',
        'background',
        'bd',
        'bg',
        'cursor',
        'disabledforeground',
        'fg',
        'font',
        'foreground',
        'justify',
        'state',
        'text',
        'textvariable',
        'underline',
        'wraplength',
    )

    def _check_setit(self, kw={}):
        """Internal function.\n
        Checks if indicator patch needed or not."""
        cond1 = kw.get('indicator', kw.get('indicatoron', self['indicator']))
        if (not cond1 and
                not (kw.get('bitmap', self['bitmap']) or 
                     kw.get('image', self['image']))):
            return True
        return False
    
    def _if_selected(self):
        """Internal function.\n
        Checks if the radiobutton is selected or not."""
        if self._cnf['variable'] is not None:
            if (isinstance(self._cnf['variable'], _tk.StringVar) 
                    and isinstance(self['value'], int)):
                return self._cnf['variable'].get() == str(self['value'])
            return self._cnf['variable'].get() == self['value']
        return True
    
    def _change_selector_color(self, wid, mode):
        """Internal function."""
        lb = getattr(self, '_indi_lb', False)
        if not lb or not lb.winfo_exists():
            return
        if mode == 'checked':
            self._indi_lb['bg'] = self._cnf['selectcolor']
            if wid != self:
                _tk.Radiobutton._configure(
                    self, 'configure', {'selectcolor': self._cnf['selectcolor']}, None)
            return
        self._indi_lb['bg'] = self['bg']
        if wid != self:
            _tk.Radiobutton._configure(
                self, 'configure', {'selectcolor': self['bg']}, None)
    
    def _bind_handler(self, *ags, **kw):
        """Internet function.\n
        Don't call this function directly."""
        _bind(self, *ags, **kw)
        lb = getattr(self, '_indi_lb', False)
        if lb and lb.winfo_exists():
            _bind(lb, *ags, **kw)
    
    def _internal_configure(self, **kw):
        """Internal function.\n
        Don't call this function directly. 
        Configure both radiobutton and the label."""
        _tk.Radiobutton._configure(self, 'configure', kw, None)
        lb = getattr(self, '_indi_lb', False)
        if lb and lb.winfo_exists():
            lb._configure('configure', kw, None)

    def _on_press(self, evt=None):
        """Internal function. \n
        When widget is pressed <Button-1>."""
        def cmd(evt):
            self._bind_handler(className='button_command', sequence='<ButtonRelease-1>')
            self._state('on_release')
            self._clear_unchecked()
            self._change_selector_color(evt.widget, 'checked')
            self.tk.call(self._w, 'select')
            if evt.widget != self:
                self.invoke()
            
        def on_enter(evt):
            """Internal function.\n
            Enables when pressed and cursor
            is moved back on widget."""
            self._state('on_enter')
            if self._if_selected():
                self._change_selector_color(evt.widget, 'unchecked')
            self._bind_handler(className='button_command', sequence='<ButtonRelease-1>', func=cmd)

        def on_leave(evt):
            """Internal function.\n
            Disables/Cancels when pressed 
            and cursor is moved away from 
            the widget."""
            self._state('on_leave')
            if self._if_selected():
                self._change_selector_color(evt.widget, 'checked')
            self._bind_handler(className='button_command', sequence='<ButtonRelease-1>')
        
        if self['state'] not in 'disabled':
            self._state('on_press')
            self._change_selector_color(evt.widget, 'unchecked')
            self._bind_handler(
                {'className': 'on_press_enter', 'sequence': '<Enter>', 'func': on_enter},
                {'className': 'on_press_leave', 'sequence': '<Leave>', 'func': on_leave},
                {'className': 'button_command', 'sequence': '<ButtonRelease-1>', 'func': cmd}
            )

    def _on_release(self, evt):
        """Internal function. \n
        When button is released <ButtonRelease-1>."""
        if self['state'] not in 'disabled':
            self._bind_handler(
                {'className': 'on_press_enter', 'sequence': '<Enter>'},
                {'className': 'on_press_leave', 'sequence': '<Leave>'},
                {'className': 'button_command', 'sequence': '<ButtonRelease-1>'}
            )

    def _clear_unchecked(self, evt=None):
        """Internal function."""
        for i in self._radiobuttons:
            lb = getattr(i, '_indi_lb', False)
            if (lb and lb.winfo_exists()
                and i._cnf['variable'] == self._cnf['variable']
                    and i != self and self._cnf['variable']):
                lb['bg'] = i['bg']
    
    def _state(self, mode):
        """Internal function."""
        if mode in ('on_enter', 'on_press'):
            self._internal_configure(
                state='active',
                background=self['activebackground'],
                foreground=self['activeforeground'],
            )
        elif mode in ('on_leave', 'on_release'):
            self._internal_configure(
                state='normal', 
                background=self._cnf['background'], 
                foreground=self._cnf['foreground']
            )

    def _setit(self):
        """Internal function.
        Sets the radio button with the patch."""
        self.propagate(0)
        self._indi_lb = _tk.Label(self)
        for i in self._properties:
            self._indi_lb[i] = self[i]
        self._indi_lb.pack(expand=1, fill='both')

        if self._if_selected():
            self._indi_lb['bg'] = self['selectcolor']
        
        self._bind_handler(
            {'className': "on_press", "sequence": "<Button-1>"}, # Unbinds if any
            {'className': "on_release", "sequence": "<ButtonRelease-1>"}, # Unbinds if any
            {'className': "on_press", "sequence": "<Button-1>", "func": self._on_press},
            {'className': "on_release", "sequence": "<ButtonRelease-1>", "func": self._on_release},
        )

    def _revert(self):
        """Internal function.\n
        Un-patch the radio button when `indicatoron` is set to 1."""
        self._indi_lb.destroy()
        self.propagate(1)

    def _set_configure(self, cnf={}):
        """Internal function."""        
        for p in list(self._cnf): 
            self._cnf[p] = cnf.get(p, self._cnf[p])
        lb = getattr(self, '_indi_lb', False)
        if self._check_setit(cnf):
            if lb and lb.winfo_exists():
                for i in cnf:
                    if i in self._properties:
                        self._indi_lb[i] = cnf[i]
            else:
                self._setit()
        elif lb:
            self._revert() 


class RadiobuttonBase(_tk.Radiobutton, _radiobutton_functions):
    _radiobuttons = []

    def __init__(self, master=None, cnf={}, **kw):
        """Construct a radiobutton widget with the parent MASTER.

        Valid resource names: activebackground, activeforeground, anchor,
        background, bd, bg, bitmap, borderwidth, command, cursor,
        disabledforeground, fg, font, foreground, height,
        highlightbackground, highlightcolor, highlightthickness, image,
        indicatoron, justify, padx, pady, relief, selectcolor, selectimage,
        state, takefocus, text, textvariable, underline, value, variable,
        width, wraplength."""
        kw = _cnfmerge((kw, cnf))
        _tk.Radiobutton.__init__(self, master, kw)
        self._radiobuttons.append(self)
        self._cnf = dict(
            variable = kw.get('variable'),
            selectcolor = self['selectcolor'],
            foreground = self['foreground'],
            background = self['background'],
        )
        
        # Set the patch if indicatoron is set to 0.
        if self._check_setit():
            self._setit()
        
        self._bind_handler(
            {'className': "on_press", "sequence": "<Button-1>", "func": self._on_press},
            {'className': "on_release", "sequence": "<ButtonRelease-1>", "func": self._on_release},
        )
    
    def _configure(self, cmd, cnf, kw):
        """Internal function."""
        _radiobutton_functions._set_configure(self, _cnfmerge((cnf, kw)))
        super()._configure(cmd, cnf, kw)

    def deselect(self):
        """Put the button in off-state."""
        self._change_selector_color(None, 'unchecked')
        return super().deselect()
        
    def select(self):
        """Put the button in on-state."""
        self._clear_unchecked()
        self._change_selector_color(None, 'checked')
        return super().select()
    