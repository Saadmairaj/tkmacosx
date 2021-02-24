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
from tkmacosx.utils import (_cnfmerge, _bind)

RADIOBUTTON_PROPERTIES = [
    'activebackground', 'activeforeground', 'anchor',
    'background', 'bitmap', 'borderwidth', 'command', 'compound',
    'cursor', 'disabledforeground', 'font', 'foreground', 'height',
    'highlightbackground', 'highlightcolor', 'highlightthickness',
    'image', 'indicatoron', 'justify', 'offrelief', 'overrelief',
    'padx', 'pady', 'relief', 'selectcolor', 'selectimage', 'state',
    'takefocus', 'text', 'textvariable', 'tristateimage', 'tristatevalue',
    'underline', 'value', 'variable', 'width', 'wraplength'
]


RADIOBUTTON_TEXT_PROPERTIES = (
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
    'wraplength'
)


class _radiobutton_functions:

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
            if (isinstance(self._cnf['variable'], tkinter.StringVar)
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
                tkinter.Radiobutton._configure(
                    self, 'configure', {'selectcolor': self._cnf['selectcolor']}, None)
            return
        self._indi_lb['bg'] = self['bg']
        if wid != self:
            tkinter.Radiobutton._configure(
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
        tkinter.Radiobutton._configure(self, 'configure', kw, None)
        lb = getattr(self, '_indi_lb', False)
        if lb and lb.winfo_exists():
            lb._configure('configure', kw, None)

    def _on_press(self, evt=None):
        """Internal function. \n
        When widget is pressed <Button-1>."""
        def cmd(evt):
            self._bind_handler(className='button_command',
                               sequence='<ButtonRelease-1>')
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
            self._bind_handler(className='button_command',
                               sequence='<ButtonRelease-1>', func=cmd)

        def on_leave(evt):
            """Internal function.\n
            Disables/Cancels when pressed 
            and cursor is moved away from 
            the widget."""
            self._state('on_leave')
            if self._if_selected():
                self._change_selector_color(evt.widget, 'checked')
            self._bind_handler(className='button_command',
                               sequence='<ButtonRelease-1>')

        if self['state'] not in 'disabled':
            self._state('on_press')
            self._change_selector_color(evt.widget, 'unchecked')
            self._bind_handler(
                {'className': 'on_press_enter',
                    'sequence': '<Enter>', 'func': on_enter},
                {'className': 'on_press_leave',
                    'sequence': '<Leave>', 'func': on_leave},
                {'className': 'button_command',
                    'sequence': '<ButtonRelease-1>', 'func': cmd}
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
        self._indi_lb = tkinter.Label(self)
        for i in RADIOBUTTON_TEXT_PROPERTIES:
            self._indi_lb[i] = self[i]
        self._indi_lb.pack(expand=1, fill='both')

        if self._if_selected():
            self._indi_lb['bg'] = self['selectcolor']

        self._bind_handler(
            {'className': "on_press", "sequence": "<Button-1>"},  # Unbinds if any
            {'className': "on_release", "sequence": "<ButtonRelease-1>"},  # Unbinds if any
            {'className': "on_press", "sequence": "<Button-1>", "func": self._on_press},
            {'className': "on_release", "sequence": "<ButtonRelease-1>",
                "func": self._on_release},
        )

    def _revert(self):
        """Internal function.\n
        Un-patch the radio button when `indicatoron` is set to 1."""
        self._indi_lb.destroy()
        self.propagate(1)

    def _set_configure(self, cnf={}):
        """Internal function."""
        self._trace_fix(cnf)
        for p in list(self._cnf):
            self._cnf[p] = cnf.get(p, self._cnf[p])
        lb = getattr(self, '_indi_lb', False)
        if self._check_setit(cnf):
            if lb and lb.winfo_exists():
                for i in cnf:
                    if i in RADIOBUTTON_TEXT_PROPERTIES:
                        self._indi_lb[i] = cnf[i]
            else:
                self._setit()
        elif lb:
            self._revert()

    def _trace_fix(self, kw={}):
        """Internal function."""
        for i in ('background', 'foreground', 'fg', 'bg'):
            if kw.get(i) and isinstance(kw.get(i), tkinter.Variable):
                key = 'background' if i[0] == 'b' else 'foreground'
                kw[i].trace_add(
                    'write', lambda *a, var=kw[i], k=key:
                        self._cnf.update({k: var.get()}))


class RadiobuttonBase(tkinter.Radiobutton, _radiobutton_functions):
    _radiobuttons = []

    def __init__(self, master=None, cnf={}, **kw):
        kw = _cnfmerge((kw, cnf))
        self._trace_fix(kw)
        tkinter.Radiobutton.__init__(self, master, kw)
        self._radiobuttons.append(self)
        self._cnf = dict(
            variable=kw.get('variable'),
            selectcolor=self['selectcolor'],
            foreground=self['foreground'],
            background=self['background'],
        )

        # Set the patch if indicatoron is set to 0.
        if self._check_setit():
            self._setit()

        self._bind_handler(
            {'className': "on_press", "sequence": "<Button-1>", "func": self._on_press},
            {'className': "on_release", "sequence": "<ButtonRelease-1>",
                "func": self._on_release},
        )

    def _configure(self, cmd, cnf, kw):
        """Internal function."""
        self._set_configure(_cnfmerge((cnf, kw)))
        return super()._configure(cmd, cnf, kw)

    def deselect(self):
        """Put the button in off-state."""
        self._change_selector_color(None, 'unchecked')
        return super().deselect()

    def select(self):
        """Put the button in on-state."""
        self._clear_unchecked()
        self._change_selector_color(None, 'checked')
        return super().select()
