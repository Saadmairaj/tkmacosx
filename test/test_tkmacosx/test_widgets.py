import unittest
import tkinter
import tkmacosx
import tkinter.ttk as ttk

from test.widget_tests import (add_standard_options, noconv,
                               StandardOptionsTests, ButtonOptionsTests,
                               IntegerSizeTests, PixelSizeTests,
                               AbstractWidgetTest)


def float_round(x):
    return float(round(x))


class AbstractToplevelTest(AbstractWidgetTest, PixelSizeTests):
    _conv_pad_pixels = noconv

    def test_configure_class(self):
        widget = self.create()
        self.assertEqual(widget['class'],
                         widget.__class__.__name__.title())
        self.checkInvalidParam(widget, 'class', 'Foo',
                               errmsg="can't modify -class option after widget is created")
        widget2 = self.create(class_='Foo')
        self.assertEqual(widget2['class'], 'Foo')

    def test_configure_colormap(self):
        widget = self.create()
        self.assertEqual(widget['colormap'], '')
        self.checkInvalidParam(widget, 'colormap', 'new',
                               errmsg="can't modify -colormap option after widget is created")
        widget2 = self.create(colormap='new')
        self.assertEqual(widget2['colormap'], 'new')

    def test_configure_container(self):
        widget = self.create()
        self.assertEqual(widget['container'], 0 if self.wantobjects else '0')
        self.checkInvalidParam(widget, 'container', 1,
                               errmsg="can't modify -container option after widget is created")
        widget2 = self.create(container=True)
        self.assertEqual(widget2['container'], 1 if self.wantobjects else '1')

    def test_configure_visual(self):
        widget = self.create()
        self.assertEqual(widget['visual'], '')
        self.checkInvalidParam(widget, 'visual', 'default',
                               errmsg="can't modify -visual option after widget is created")
        widget2 = self.create(visual='default')
        self.assertEqual(widget2['visual'], 'default')


class AbstractLabelTest(AbstractWidgetTest, IntegerSizeTests):
    _conv_pixels = noconv

    def test_configure_highlightthickness(self):
        widget = self.create()
        self.checkPixelsParam(widget, 'highlightthickness',
                              0, 1.3, 2.6, 6, -2, '10p')


class AbstractButtonTest(AbstractWidgetTest, PixelSizeTests):

    _ttk_parent = False
    _ttk_parent_with_style = False
    _ttk_style = "TFrame"
    _type = 'normal'

    def create(self, **kwargs):
        self._master = self.root
        if self._ttk_parent and self._ttk_parent_with_style:
            style = ttk.Style(self.root)
            self._ttk_style = "Custom.TFrame"
            style.configure(self._ttk_style, background="pink")
            self._master = ttk.Frame(self.root, style=self._ttk_style)
            self._master.pack()
        elif self._ttk_parent:
            self._master = ttk.Frame(self.root)
            self._master.pack()
        if self._type == 'normal':
            return tkmacosx.Button(self._master, **kwargs)
        if self._type == 'circle':
            return tkmacosx.CircleButton(self._master, **kwargs)

    def test_configure_state(self):
        widget = self.create()
        self.checkEnumParam(widget, 'state', 'active',
                            'disabled', 'normal', 'pressed')

    def test_configure_highlightbackground(self):
        widget = self.create()
        self.checkColorParam(widget, 'highlightbackground')

        widget['borderless'] = True
        for c in ('#ff0000', '#00ff00', '#0000ff', '#123456',
                  'red', 'green', 'blue', 'white', 'black', 'grey'):
            widget['highlightbackground'] = c
            self.assertNotEqual(widget['highlightbackground'], c)

        widget['borderless'] = False
        for c in ('#ff0000', '#00ff00', '#0000ff', '#123456',
                  'red', 'green', 'blue', 'white', 'black', 'grey'):
            widget['highlightbackground'] = c
            self.assertEqual(widget['highlightbackground'], c)


@add_standard_options(StandardOptionsTests, ButtonOptionsTests)
class ButtonTest(AbstractButtonTest, unittest.TestCase):
    OPTIONS = (
        'activebackground', 'activeforeground', 'activeimage',
        'activebitmap', 'anchor', 'background', 'bitmap', 'bordercolor',
        'borderless', 'borderwidth', 'command', 'compound', 'cursor', 'disabledbackground',
        'disabledforeground', 'font', 'focuscolor', 'focusthickness',
        'foreground', 'height', 'highlightbackground', 'highlightcolor',
        'highlightthickness', 'image', 'justify', 'overbackground',
        'overforeground', 'overrelief', 'padx', 'pady', 'relief',
        'repeatdelay', 'repeatinterval', 'state', 'takefocus', 'text',
        'textvariable', 'underline', 'width')

    _conv_pixels = round
    _ttk_parent = False
    _ttk_parent_with_style = False
    _type = 'normal'


@add_standard_options(StandardOptionsTests, ButtonOptionsTests)
class Button_ttk_Test(AbstractButtonTest, unittest.TestCase):
    OPTIONS = (
        'bordercolor', 'borderless', 'highlightbackground',
        'highlightcolor', 'highlightthickness')

    _conv_pixels = round
    _ttk_parent = True


@add_standard_options(StandardOptionsTests, ButtonOptionsTests)
class Button_ttk_with_style_Test(AbstractButtonTest, unittest.TestCase):
    OPTIONS = (
        'bordercolor', 'borderless', 'highlightbackground',
        'highlightcolor', 'highlightthickness')

    _conv_pixels = round
    _ttk_parent = True
    _ttk_parent_with_style = True


@add_standard_options(StandardOptionsTests, ButtonOptionsTests)
class CircleButtonTest(AbstractButtonTest, unittest.TestCase):
    OPTIONS = (
        'activebackground', 'activeforeground', 'activeimage',
        'activebitmap', 'anchor', 'background', 'bitmap', 'bordercolor',
        'borderless', 'borderwidth', 'command', 'compound', 'cursor', 'disabledbackground',
        'disabledforeground', 'font', 'focuscolor', 'focusthickness',
        'foreground', 'height', 'highlightbackground', 'highlightcolor',
        'highlightthickness', 'image', 'justify', 'overbackground',
        'overforeground', 'overrelief', 'padx', 'pady', 'relief', 'radius',
        'repeatdelay', 'repeatinterval', 'state', 'takefocus', 'text',
        'textvariable', 'underline', 'width')

    _conv_pixels = round
    _type = 'circle'

    def test_configure_radius(self):
        widget = self.create()
        self.checkIntegerParam(widget, 'radius', 402, -402, 0)


@add_standard_options(StandardOptionsTests, ButtonOptionsTests)
class CircleButton_ttk_Test(AbstractButtonTest, unittest.TestCase):
    OPTIONS = (
        'bordercolor', 'borderless', 'highlightbackground',
        'highlightcolor', 'highlightthickness')

    _conv_pixels = round
    _ttk_parent = True
    _type = 'circle'


@add_standard_options(StandardOptionsTests, ButtonOptionsTests)
class CirclButton_ttk_with_style_Test(AbstractButtonTest, unittest.TestCase):
    OPTIONS = (
        'bordercolor', 'borderless', 'highlightbackground',
        'highlightcolor', 'highlightthickness')

    _conv_pixels = round
    _ttk_parent = True
    _ttk_parent_with_style = True
    _type = 'circle'


@add_standard_options(StandardOptionsTests, PixelSizeTests)
class ColorscaleTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (
        'borderwidth', 'cursor', 'command', 'gradient', 'height',
        'highlightbackground', 'highlightcolor', 'highlightthickness',
        'mousewheel', 'orient', 'relief', 'showinfo', 'showinfodelay',
        'state', 'takefocus', 'value', 'variable', 'width',
    )
    _conv_pixels = round
    _keep_orig = False
    default_orient = 'vertical'

    def create(self, **kwargs):
        return tkmacosx.Colorscale(self.root, **kwargs)

    def test_configure_gradient(self):
        widget = self.create()
        self.checkParams(
            widget, 'gradient', ('red', 'black'), 'default', ('#333', '#fff'))
        self.checkInvalidParam(widget, 'gradient', 'spam',
                               errmsg='expected sequence of two color values but got "spam"')
        self.checkInvalidParam(widget, 'gradient', ('spam', 'red'),
                               errmsg='unknown color name "spam"')
        self.checkInvalidParam(widget, 'gradient', ('#ff3123', 'spam'),
                               errmsg='unknown color name "spam"')

    def test_configure_mousewheel(self):
        widget = self.create()
        self.checkBooleanParam(widget, 'mousewheel')

    def test_configure_showinfo(self):
        widget = self.create()
        self.checkBooleanParam(widget, 'showinfo')

    def test_configure_state(self):
        widget = self.create()
        self.checkEnumParam(widget, 'state', 'disabled', 'normal',
                            errmsg='bad state value "{}": must be normal or disabled')

    def test_configure_showinfodelay(self):
        widget = self.create()
        self.checkIntegerParam(widget, 'showinfodelay', 0, 100, -100)

    def test_configure_value(self):
        widget = self.create()
        self.checkEnumParam(widget, 'value', 'rgb', 'hex')

    def test_configure_variable(self):
        widget = self.create()
        var = tkmacosx.ColorVar(self.root)
        self.checkVariableParam(widget, 'variable', var)


@add_standard_options(StandardOptionsTests, PixelSizeTests)
class MarqueeTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (
        'background', 'borderwidth', 'cursor', 'disabledforeground',
        'end_delay', 'foreground', 'font', 'fps', 'height', 'highlightbackground',
        'highlightcolor', 'highlightthickness', 'initial_delay', 'justify',
        'left_margin', 'relief', 'smoothness', 'state', 'takefocus', 'text', 'width',
    )

    _conv_pixels = round
    _stringify = True
    _keep_orig = False

    def create(self, **kwargs):
        kwargs['bg'] = kwargs.get('bg', kwargs.get('background', 'black'))
        kwargs['fg'] = kwargs.get('fg', kwargs.get('foreground', 'white'))
        return tkmacosx.Marquee(self.root, **kwargs)

    def test_configure_state(self):
        widget = self.create()
        self.checkEnumParam(widget, 'state', 'disabled', 'normal',
                            errmsg='bad state value "{}": must be normal or disabled')

    def test_configure_end_delay(self):
        widget = self.create()
        self.checkIntegerParam(widget, 'end_delay', 0, 100, '10')

    def test_configure_fps(self):
        widget = self.create()
        self.checkIntegerParam(widget, 'fps', 30, 60, 120, '30')

    def test_configure_initial_delay(self):
        widget = self.create()
        self.checkIntegerParam(widget, 'initial_delay', 0, 100, '10')

    def test_configure_left_margin(self):
        widget = self.create()
        self.checkIntegerParam(widget, 'left_margin', 0, 100, -100, '20')

    def test_configure_smoothness(self):
        widget = self.create()
        self.checkIntegerParam(widget, 'smoothness', 0, 1, 5, 6, -4, '20')

    def test_reset(self):
        widget = self.create()
        widget['text'] = 'Testing text functions'*4
        coords = widget.coords('text')
        widget['initial_delay'] = 0
        widget['end_delay'] = 0
        widget.reset()
        self.assertEqual(coords, widget.coords('text'))

    def test_play(self):
        widget = self.create()
        widget['text'] = 'Testing text functions'*4
        widget.stop(True)
        initial_coords = widget.coords('text')
        widget['initial_delay'] = 0
        widget['end_delay'] = 0
        coords = widget.coords('text')
        widget.play()
        self.assertNotEqual(coords, widget.coords('text'))
        widget.play(True)
        coords = widget.coords('text')
        coords[0] += 1
        self.assertEqual(initial_coords, coords)

    def test_stop(self):
        widget = self.create()
        widget['text'] = 'Testing text functions'*4
        initial_coords = widget.coords('text')
        widget['initial_delay'] = 0
        widget['end_delay'] = 0
        coords = widget.coords('text')
        widget.stop()
        self.assertEqual(coords, widget.coords('text'))
        widget.stop(True)
        self.assertEqual(initial_coords, coords)


@add_standard_options(StandardOptionsTests)
class RadiobuttonTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (
        'activebackground', 'activeforeground', 'anchor',
        'background', 'bitmap', 'borderwidth', 'command', 'compound',
        'cursor', 'disabledforeground', 'font', 'foreground', 'height',
        'highlightbackground', 'highlightcolor', 'highlightthickness',
        'image', 'indicatoron', 'justify', 'offrelief', 'overrelief',
        'padx', 'pady', 'relief', 'selectcolor', 'selectimage', 'state',
        'takefocus', 'text', 'textvariable', 'tristateimage', 'tristatevalue',
        'underline', 'value', 'variable', 'width', 'wraplength'
    )

    def create(self, **kwargs):
        return tkmacosx.Radiobutton(self.root, **kwargs)

    def test_configure_value(self):
        widget = self.create()
        self.checkParams(widget, 'value', 1, 2.3, '', 'any string')


@add_standard_options(StandardOptionsTests)
class SFrameTest(AbstractToplevelTest, unittest.TestCase):
    OPTIONS = (
        'avoidmousewheel', 'autohidescrollbar', 'autohidescrollbardelay',
        'background', 'borderwidth', 'canvas', 'class', 'colormap', 'container',
        'cursor', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness',
        'mousewheel', 'padx', 'pady', 'relief', 'scrollbar', 'scrollbarwidth', 'takefocus',
        'visual', 'width'
    )

    def create(self, **kwargs):
        return tkmacosx.SFrame(self.root, **kwargs)

    def test_configure_autohidescrollbar(self):
        widget = self.create()
        self.checkBooleanParam(widget, 'autohidescrollbar')

    def test_configure_autohidescrollbardelay(self):
        widget = self.create()
        self.checkIntegerParam(
            widget, 'autohidescrollbardelay', 0, 100, 500, '1000')

    def test_configure_avoidmousewheel(self):
        widget = self.create()
        widget_list = tuple([tkmacosx.Colorscale(widget) for i in range(10)])
        self.checkParam(widget, 'avoidmousewheel', widget_list[0])
        widget['avoidmousewheel'] = widget_list
        for w in widget_list:
            self.assertIn(w, widget['avoidmousewheel'])

    def test_configure_canvas(self):
        widget = self.create()
        canvas = tkinter.Canvas(widget)
        wrong_widget = tkinter.Frame(widget)
        self.checkParam(widget, 'canvas', canvas)
        self.checkInvalidParam(widget, 'canvas', wrong_widget,
                               errmsg='expected tkinter.Canvas instance but got "%s"'
                               % wrong_widget)
        self.checkInvalidParam(widget, 'canvas', 10,
                               errmsg='expected tkinter.Canvas instance but got "10"')
        self.checkInvalidParam(widget, 'canvas', 'spam',
                               errmsg='expected tkinter.Canvas instance but got "spam"')

    def test_configure_mousewheel(self):
        widget = self.create()
        self.checkBooleanParam(widget, 'mousewheel')

    def test_configure_scrollbar(self):
        widget = self.create()
        scrollbar = tkinter.Scrollbar(widget)
        wrong_widget = tkinter.Frame(widget)
        self.checkParam(widget, 'scrollbar', scrollbar)
        self.checkInvalidParam(widget, 'scrollbar', wrong_widget,
                               errmsg='expected tkinter.Scrollbar instance but got "%s"'
                               % wrong_widget)
        self.checkInvalidParam(widget, 'scrollbar', 10,
                               errmsg='expected tkinter.Scrollbar instance but got "10"')
        self.checkInvalidParam(widget, 'scrollbar', 'spam',
                               errmsg='expected tkinter.Scrollbar instance but got "spam"')

    def test_configure_scrollbarwidth(self):
        widget = self.create()
        self.checkPixelsParam(
            widget, 'scrollbarwidth', 402, 403.4, 404.6, -402, 0, '5i')
