import tkinter
from tkinter import TclError, Variable


UNITS = {
    'c': 72 / 2.54,     # centimeters
    'i': 72,            # inches
    'm': 72 / 25.4,     # millimeters
    'p': 1,             # points
}


def pixels_conv(value):
    return float(value[:-1]) * UNITS[value[-1:]]


class widget_options:

    button = {
        'boolean': ('borderless', ),
        'color': ('activebackground', 'activeforeground', 'bordercolor',
                  'disabledbackground', 'disabledforeground', 'foreground', 'fg',
                  'overforeground', 'overbackground', 'focuscolor', 'highlightbackground'),
        'enum': ('anchor', 'compound', 'state', 'justify', 'overrelief'),
        'integer': ('focusthickness', 'repeatinterval', 'repeatdelay', 'underline', 'radius'),
        'pixel': ('highlightthickness', 'padx', 'pady', 'width', 'height'),
        'not_exist': ('activeimage', 'image', 'font'),
    }

    colorscale = {
        'boolean': ('showinfo', 'mousewheel'),
        'enum': ('orient', 'value'),
        'integer': ('showinfodelay', ),
    }

    marquee = {
        'color': ('fg', 'foreground', 'disabledforeground'),
        'enum': ('justify', ),
        'integer': ('end_delay', 'fps', 'initial_delay', 'smoothness', 'left_margin'),
        'not_exist': ('font', ),
    }

    sframe = {
        'boolean': ('autohidescrollbar', 'mousewheel'),
        'integer': ('autohidescrollbardelay', ),
        'widget': ('canvas', 'scrollbar'),
    }

    @classmethod
    def get_options(cls, widget, name):
        return getattr(cls, widget, None)[name]

    @classmethod
    def get_keys(cls, widget):
        return list(getattr(cls, widget, None).keys())


class Check_Common_Parameters:

    enum_para = {
        'anchor': ('n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'center'),
        'compound': ('bottom', 'center', 'left', 'none', 'right', 'top'),
        'state': ('active', 'disabled', 'normal', 'pressed'),
        'justify': ('left', 'right', 'center'),
        'overrelief': ('flat', 'groove', 'raised', 'ridge', 'solid', 'sunken', ''),
        'orient': ('horizontal', 'vertical'),
        'value': ('rgb', 'hex'),
    }

    def __init__(self, master):
        self.master = master

    def __call__(self, widget, kw):
        for i in widget_options.get_keys(widget):
            fn = getattr(self, i)
            fn(widget, kw)
        return kw

    def boolean(self, widget, kw):
        for i in widget_options.get_options(widget, self.boolean.__name__):
            if i in kw:
                if kw[i] in (False, 0, 'false', 'no', 'off'):
                    kw[i] = 0
                elif kw[i] in (True, 1, 'true', 'yes', 'on'):
                    kw[i] = 1
                else:
                    raise TclError(
                        'expected boolean value but got "%s"' % kw[i])

    def color(self, widget, kw):
        for i in widget_options.get_options(widget, self.color.__name__):
            if i in kw and kw[i] != '':
                if i == 'activebackground' and isinstance(kw[i], (list, tuple)):
                    for c in kw[i]:
                        self.master.winfo_rgb(c)
                elif not isinstance(kw[i], Variable):
                    self.master.winfo_rgb(kw[i])

    def enum(self, widget, kw):
        op_list = widget_options.get_options(widget, self.enum.__name__)
        for k, v in self.enum_para.items():
            if (k in op_list and k in kw
                and kw[k] not in v
                and not (k == 'compound'
                                 and str(kw[k]).lower() in 'none'
                                 and kw[k] != '')
                ):
                err = 'ambiguous' if kw[k] == '' else 'bad'
                name = 'justification' if k == 'justify' else k
                if 'overrelief' == k:
                    v = v[:-1]
                    name = 'relief'
                raise TclError(
                    '%s %s "%s": must be %s%s or %s' % (
                        err, name, kw[k], ', '.join(v[:-1]),
                        ',' if len(v) > 2 else '', v[-1]))

    def integer(self, widget, kw):
        for i in widget_options.get_options(widget, self.integer.__name__):
            if i in kw:
                if kw[i] == '' or '.' in str(kw[i]) or not str(kw[i]).lstrip("-").isnumeric():
                    raise TclError('expected integer but got "%s"' % kw[i])

    def not_exist(self, widget, kw):
        for i in widget_options.get_options(widget, self.not_exist.__name__):
            image_cond = ('image' in i and i in kw and
                          isinstance(kw[i], str) and kw[i] != '')
            font_cond = 'font' in kw and kw['font'] == ''
            if i in kw and (image_cond or font_cond):
                name = 'image' if i == 'activeimage' else i
                raise TclError('%s "%s" doesn\'t exist' % (name, kw[i]))

    def pixel(self, widget, kw):
        for i in widget_options.get_options(widget, self.pixel.__name__):
            if i in kw:
                if '.' in str(kw[i]):
                    kw[i] = round(float(kw[i]))
                if isinstance(kw[i], str):
                    if kw[i][-1] in UNITS and kw[i][:-1].isnumeric():
                        kw[i] = round(pixels_conv(kw[i]))
                if not isinstance(kw[i], (int, float)):
                    raise TclError('bad screen distance "%s"' % kw[i])

    def widget(self, widget, kw):
        for i in widget_options.get_options(widget, self.widget.__name__):
            if i in kw:
                name = i.capitalize()
                if not isinstance(kw[i], getattr(tkinter, name)):
                    raise TclError(
                        'expected tkinter.%s instance but got "%s"' % (name, kw[i]))
