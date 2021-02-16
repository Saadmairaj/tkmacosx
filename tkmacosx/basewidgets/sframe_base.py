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
from tkmacosx.utils import (_cnfmerge, _bind, delta, check_param)


SFRAME_PROPERTIES = [
    'avoidmousewheel', 'autohidescrollbar', 'autohidescrollbardelay',
    'background', 'borderwidth', 'canvas', 'class', 'colormap', 'container',
    'cursor', 'height', 'highlightbackground', 'highlightcolor',
    'highlightthickness', 'mousewheel', 'padx', 'pady', 'relief',
    'scrollbar', 'scrollbarwidth', 'takefocus', 'visual', 'width',
]


SFRAME_FEATURES = (
    'scrollbarwidth', 'mousewheel', 'autohidescrollbar', 'avoidmousewheel',
    'canvas', 'scrollbar', 'autohidescrollbardelay'
)


class _sframe_functions:

    def _auto_hide_scrollbar(self, evt=None):
        "Internal function"
        if not self.cnf['autohidescrollbar']:
            return
        self.after_cancel(self._after_ids.get(1, ' '))
        if ((isinstance(evt, tkinter.Event) and evt.x >= self['scrollbar'].winfo_x())
                or evt == 'show'):
            self['scrollbar'].place(relx=1, rely=0, anchor='ne', relheight=1)
            self['scrollbar'].lift()
        else:
            self._after_ids[1] = self.after(
                self['autohidescrollbardelay'], self['scrollbar'].place_forget)

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

    def _configure_height(self, evt):
        """Internal function."""
        width = self.cnf['canvas'].winfo_width(
        )-self.cnf['scrollbar'].winfo_width()
        self.cnf['canvas'].itemconfig('window', width=width)

    def _configure_window(self, evt):
        """Internal function."""
        # this will update the position of scrollbar when scrolled from mousewheel.
        # fixes some bugs
        # makes scrolling more smoother
        self.after_cancel(self._after_ids.get(0, ' '))
        self._after_ids[0] = self.after(
            1, lambda: self.cnf['canvas'].configure(
                scrollregion=self.cnf['canvas'].bbox('all')))

    def _geometryManager(self):
        """Internal function."""
        # Use set to support the following in both python 2 and python 3
        geo_methods = [m for m in (set(tkinter.Pack.__dict__) | set(tkinter.Grid.__dict__) |
                                   set(tkinter.Place.__dict__)) if m not in tkinter.Frame.__dict__]
        for m in geo_methods:
            if m[0] != '_' and 'config' not in m:
                setattr(self, m, getattr(self.cnf['canvas'], m))

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
            delay = 1
            if self['autohidescrollbardelay'] < 1000:
                delay = 1000 - self['autohidescrollbardelay']
            self.cnf['canvas'].yview_scroll(-1*delta(evt), 'units')
            self.after_cancel(self._after_ids.get(2, ' '))
            self._auto_hide_scrollbar('show')
            self._after_ids[2] = self.after(delay, self._auto_hide_scrollbar)

    def _set_configure(self, cnf):
        "Internal function."
        kw_copy = check_param(self, 'sframe',
                              {k: cnf.pop(k) for k in SFRAME_FEATURES if k in cnf})
        self.cnf['scrollbar']['width'] = kw_copy.pop(
            'scrollbarwidth', self.cnf['scrollbar']['width'])
        for key in kw_copy.copy():
            if key == 'avoidmousewheel':
                l = list(self.cnf[key])
                if isinstance(kw_copy[key], (tuple, list)):
                    l.extend(kw_copy.pop(key))
                else:
                    l.append(kw_copy.pop(key))
                self.cnf[key] = tuple(set(l))
            else:
                self.cnf[key] = kw_copy.pop(key, self.cnf.get(key))

        self.cnf['canvas']['width'] = cnf.pop(
            'width', self.cnf['canvas']['width'])
        self.cnf['canvas']['height'] = cnf.pop(
            'height', self.cnf['canvas']['height'])

        self._mouse_scrolling(self.cnf['mousewheel'])
        self._avoid_mousewheel(self.cnf['avoidmousewheel'])
        return cnf


class SFrameBase(tkinter.Frame, _sframe_functions):
    """Base Class for SFrame."""

    def __init__(self, master=None, cnf={}, **kw):
        kw = _cnfmerge((cnf, kw))
        kw['class_'] = kw.get('class_', 'Sframe')
        self._after_ids = {}
        self._over_scrollbar = False
        cnf = {}
        cnf['scrollbarwidth'] = kw.pop('scrollbarwidth', 10)
        cnf['mousewheel'] = kw.pop('mousewheel', True)
        cnf['avoidmousewheel'] = kw.pop('avoidmousewheel', ())
        cnf['autohidescrollbar'] = kw.pop('autohidescrollbar', False)
        cnf['autohidescrollbardelay'] = kw.pop('autohidescrollbardelay', 1000)
        cnf['canvas'] = kw.pop(
            'canvas', tkinter.Canvas(master=master, highlightthickness=0,
                                     width=kw.pop('width', 250), height=kw.pop('height', 250)))
        cnf['scrollbar'] = kw.pop(
            'scrollbar', tkinter.Scrollbar(cnf['canvas'], orient='vertical',
                                           width=cnf.get('scrollbarwidth')))
        tkinter.Frame.__init__(self, cnf['canvas'], **kw)
        self.cnf = check_param(self, 'sframe', **cnf)
        self.cnf['canvas']['bg'] = self['bg']

        if not self.cnf['autohidescrollbar']:
            self.cnf['scrollbar'].place(
                relx=1, rely=0, anchor='ne', relheight=1)

        self.cnf['scrollbar'].configure(command=self.cnf['canvas'].yview)
        self.cnf['canvas'].configure(yscrollcommand=self.cnf['scrollbar'].set)
        self.cnf['canvas'].create_window(
            0, 0, anchor='nw', tags="window", window=self,
            width=self.cnf['canvas'].winfo_reqwidth()-self.cnf['scrollbar'].winfo_reqwidth())
        self.cnf['canvas'].bind("<Configure>", self._configure_height, add="+")

        _bind(self, className='configure',
              sequence='<Configure>', func=self._configure_window)
        _bind(self, className='auto_hide_motion',
              sequence='<Motion>', func=self._auto_hide_scrollbar)
        _bind(
            self['scrollbar'], className='auto_hide_motion', sequence='<Enter>',
            func=lambda _: self._auto_hide_scrollbar('show'))
        _bind(
            self['scrollbar'], className='auto_hide_motion', sequence='<Leave>',
            func=self._auto_hide_scrollbar)

        self._mouse_scrolling(self.cnf['mousewheel'])
        self._avoid_mousewheel(self.cnf.get('avoidmousewheel'))
        self._geometryManager()

    def _configure(self, cmd, cnf=None, kw=None):
        cnf = self._set_configure(_cnfmerge((cnf, kw)))
        _return = tkinter.Frame._configure(self, cmd, None, cnf)
        if kw.get('bg', kw.get('background')):
            self.cnf['canvas']['bg'] = self['bg']
        if isinstance(_return, dict):
            _return.update(self.cnf)
            for k in list(_return):
                if k not in SFRAME_PROPERTIES:
                    _return.pop(k)
        return _return

    def keys(self):
        """Return a list of all resource names of this widget."""
        return SFRAME_PROPERTIES

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in ('width', 'height'):
            return int(self.cnf['canvas'][key])
        if key == 'avoidmousewheel' and len(self.cnf.get(key)) == 1:
            return self.cnf[key][0]
        if key == 'scrollbarwidth':
            return int(self['scrollbar'].cget('width'))
        if key in SFRAME_FEATURES:
            return self.cnf.get(key)
        return tkinter.Frame.cget(self, key)
    __getitem__ = cget
