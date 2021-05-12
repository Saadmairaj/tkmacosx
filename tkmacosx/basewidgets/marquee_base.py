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
from tkmacosx.utils import (SYSTEM_DEFAULT, _cnfmerge, _bind, check_param)


MARQUEE_PROPERTIES = [
    'background', 'bg', 'borderwidth', 'bd', 'cursor', 'disabledforeground',
    'end_delay', 'foreground', 'font', 'fps', 'height', 'highlightbackground',
    'highlightcolor', 'highlightthickness', 'initial_delay', 'justify',
    'left_margin', 'relief', 'smoothness', 'state', 'takefocus', 'text', 'width',
]


class MarqueeBase(tkinter.Canvas):
    """Base class for Marquee."""

    def __init__(self, master=None, cnf={}, **kw):
        kw = _cnfmerge((cnf, kw))
        self._stop_state = False
        self.after_id = ' '
        cnf = dict(
            text=kw.pop('text', ''),
            font=kw.pop('font', 'TkDefaultFont'),
            fg=kw.pop('fg', kw.pop('foreground', SYSTEM_DEFAULT.fg)),
            fps=kw.pop('fps', 30),
            justify=kw.pop('justify', 'left'),
            left_margin=kw.pop('left_margin', 10),
            initial_delay=kw.pop('initial_delay', 1000),
            end_delay=kw.pop('end_delay', 1000),
            smoothness=kw.pop('smoothness', 1),  # 1 <= smooth < 1
            disabledforeground=kw.pop('disabledforeground', 'grey')
        )
        cnf['foreground'] = cnf['fg']
        cnf = {k: v for k, v in cnf.items() if v is not None}

        kw['bg'] = kw.get('bg', kw.get('background', SYSTEM_DEFAULT.bg))
        kw['height'] = kw.get('height', 24)
        kw['highlightthickness'] = kw.get('highlightthickness', 0)
        tkinter.Canvas.__init__(self, master=master, **kw)
        self.cnf = check_param(self, 'marquee', **cnf)
        self._set_text()
        _bind(self, className='configure',
              sequence='<Configure>', func=self._check)

    def _set_text(self, reset=False):
        TAG = 'text'
        itemconfig = lambda kw={}: tkinter.Canvas._configure(
            self, ('itemconfigure', TAG), None, kw)
        if reset or not self.find_withtag(TAG):
            COORD = (3, self.winfo_height()/2)
            ANCHOR = 'w'
            self.delete(TAG)
            self._create(
                'text', COORD, dict(anchor=ANCHOR, tag=TAG))

        # Configure text item
        for op in list(itemconfig()):
            if (op in self.cnf and
                    not ('foreground' in op or 'fg' in op)):
                itemconfig({op: self.cnf[op]})

        self.cnf['font'] = self.itemcget(TAG, 'font')
        self.cnf['justify'] = self.itemcget(TAG, 'justify')

        itemconfig(
            dict(state=self['state'],
                 disabledfill=self.cnf.get('disabledforeground'),
                 fill=self.cnf.get('foreground'))
        )

    def _set_height(self, evt=None):
        """Internal function."""
        bbox = self.bbox('text')
        height = bbox[3] - bbox[1] + 8
        if int(self['height']) == height:
            return
        tkinter.Canvas._configure(
            self, 'configure', {'height': height}, None)

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
            delay = self.cnf.get('initial_delay')  # INITITAL DELAY
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
            delay = self.cnf.get(
                'initial_delay') + self.cnf.get(
                    'end_delay')  # INITITAL DELAY
        else:
            # MOVE -1 PIXEL EVERYTIME
            self.tk.call((self._w, 'move') + (
                'text', -self.cnf.get('smoothness'), 0))
        self.after_id = self.after(delay, self._animate)

    def _configure(self, cmd, cnf, kw):
        """Internal function."""
        kw = _cnfmerge((cnf, kw))
        diff = set(self.keys()).difference(
            list(tkinter.Canvas._configure(
                self, cmd, None, None)))
        for i in diff:
            if i in kw:
                self.cnf.update(check_param(
                    self, 'marquee', {i: kw.pop(i)}))
        self._set_text()
        self._set_height()
        values = tkinter.Canvas._configure(self, cmd, None, kw)
        if values is not None and isinstance(values, dict):
            values.update(self.cnf.copy())
            for i in list(values.copy()):
                if i not in MARQUEE_PROPERTIES:
                    values.pop(i)
        return values

    def keys(self):
        """Return a list of all resource names of this widget."""
        return MARQUEE_PROPERTIES

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in self.cnf:
            val = self.cnf[key]
            if (('foreground' in key or 'fg' in key)
                    and isinstance(val, tkinter.Variable)):
                return val.get()
            return str(val)
        return tkinter.Canvas.cget(self, key)
    __getitem__ = cget

    def destroy(self):
        """Destroy this widget."""
        self.after_cancel(self.after_id)
        return tkinter.Canvas.destroy(self)
