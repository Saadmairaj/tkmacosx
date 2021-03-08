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

"""This file contains patches to support ColorVar with 
tkinter widgets and canvas items. Patches are decorators 
later used on tkmacosx widgets to support ColorVar."""

import tkinter


# {(self, option, tag): (var, cbname)}
_all_traces_colorvar = {}

_properties1 = (
    'activefill',
    'activeoutline',
    'disabledfill',
    'disabledoutline',
    'fill',
    'outline',
    'background',
    'activebackground',
    'activeforeground',
    'disabledbackground',
    'disabledforeground',
    'foreground'
)

_properties2 = (
    'fg',
    'foreground',
    'bg',
    'background',
    'activebackground',
    'activeforeground',
    'disabledforeground',
    'highlightbackground',
    'selectcolor',
    'highlightcolor',
    'selectforeground',
    'readonlybackground',
    'selectbackground',
    'insertbackground',
    'disabledbackground')


def _colorvar_patch_destroy(fn):
    """Internal function.\n
    Deletes the traces if any when widget is destroy."""

    def _patch(self):
        """Interanl function."""
        if self._tclCommands is not None:
            # Deletes the widget from the _all_traces_colorvar
            # and deletes the traces too.
            for key, value in dict(_all_traces_colorvar).items():
                if self == key[0]:
                    var, cbname = value
                    try:
                        var.trace_vdelete('w', cbname)
                    except tkinter.TclError:
                        pass
                    _all_traces_colorvar.pop(key)
        return fn(self)
    return _patch


def _colorvar_patch_configure(fn):
    """Internal function.\n
    Patch for Canvas items to support ColorVar functionality."""

    def _patch(self, cmd, cnf, kw):
        """Internal function."""
        if isinstance(cmd, tuple) and isinstance(self, tkinter.Canvas):
            tags = self.find('withtag', cmd[1])
            for tag in tags:
                for i in _properties1:
                    tmp_dict = cnf if cnf and i in cnf else kw
                    cnf_copy = dict(**tmp_dict) if tmp_dict else {}
                    if isinstance(cnf_copy.get(i), tkinter.Variable):
                        var = cnf_copy[i]
                        cbname = var.trace_variable(
                            'w', lambda a, b, c, cls=self, opt=i,
                            tagId=tag, var=var: cls._configure(
                                ('itemconfigure', tagId), {opt: var.get()}, None))
                        if (self, (i, tag)) in _all_traces_colorvar:
                            v, cb = _all_traces_colorvar.get((self, (i, tag)))
                            v.trace_vdelete('w', cb)
                            _all_traces_colorvar[(self, (i, tag))] = (
                                var, cbname)
                        else:
                            _all_traces_colorvar[(self, (i, tag))] = (
                                var, cbname)
                        tmp_dict[i] = var.get()
        return fn(self, cmd, cnf, kw)
    return _patch


def _colorvar_patch_options(fn):
    """Internal function.\n
    Patch for ColorVar to work with tkinter widgets."""

    def _patch(self, cnf, kw=None):
        """Internal function."""
        cnf = tkinter._cnfmerge(cnf)
        if kw:
            cnf = tkinter._cnfmerge((cnf, kw))

        for i in _properties2:
            if isinstance(cnf.get(i), tkinter.Variable):
                var = cnf[i]
                cbname = var.trace_variable(
                    'w', lambda a, b, c, i=i, var=var,
                    cls=self: cls.config({i: var.get()}))
                if (self, i) in _all_traces_colorvar:
                    v, cb = _all_traces_colorvar.get((self, i))
                    v.trace_vdelete('w', cb)
                    _all_traces_colorvar[(self, i)] = (var, cbname)
                else:
                    _all_traces_colorvar[(self, i)] = (var, cbname)
                cnf[i] = var.get()
        return fn(self, cnf, None)
    return _patch


def _create(self, itemType, args, kw):
    """Internal function."""
    args = tkinter._flatten(args)
    cnf = args[-1]
    if isinstance(cnf, (dict, tuple)):
        args = args[:-1]
    else:
        cnf = {}

    # Add the resources to the list to have ColorVar functionality.
    ckw = tkinter._cnfmerge((cnf, kw))
    var = None
    for i in _properties1:
        if isinstance(ckw.get(i), tkinter.Variable):
            var = ckw[i]
            _all_traces_colorvar[(self, (i, None))] = (var, None)
            if isinstance(cnf, dict) and i in cnf:
                cnf[i] = var.get()
            elif i in kw:
                kw[i] = var.get()

    # get unique tag id
    tagId = self.tk.getint(self.tk.call(
        self._w, 'create', itemType,
        *(args + self._options(cnf, kw))))

    for key, value in dict(_all_traces_colorvar).items():
        if isinstance(key[1], (tuple, list)):
            _, (opt, tag_id) = key
            var, cbname = value
            if tag_id is None and cbname is None:
                cbname = var.trace_variable(
                    'w', lambda a, b, c, cls=self, opt=opt,
                    tagId=tagId, var=var: cls._configure(
                        ('itemconfigure', tagId), {opt: var.get()}, None))
                _all_traces_colorvar[(self, (opt, tagId))] = (var, cbname)
                _all_traces_colorvar.pop((self, (opt, None)))
    return tagId


# initializing decorators here.
def patch():
    """Patch tkinter.Misc._options, tkinter.Misc.destroy, 
    tkinter.Misc._configure, tkinter.Canvas._create."""
    tkinter.Misc.destroy = _colorvar_patch_destroy(tkinter.Misc.destroy)
    tkinter.Misc._options = _colorvar_patch_options(tkinter.Misc._options)
    tkinter.Misc._configure = _colorvar_patch_configure(
        tkinter.Misc._configure)
    tkinter.Canvas._create = _create
