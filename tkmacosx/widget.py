#                       Copyright 2020 Saad Mairaj
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

import sys
if sys.version_info.major == 2:
    import Tkinter as _TK
elif sys.version_info.major == 3:
    import tkinter as _TK
from tkmacosx.basewidget import _Frame, _Canvas, Widget


class SFrame(_Frame):
    """### Scrollable Frame Widget.    
    (Only supports vertical scrolling)

    ### Agrs:
    Sames as tkinter Frame. These are some extra resources.
    1. `scrollbarwidth`: Set the width of scrollbar.
    2. `mousewheel`: Set mousewheel scrolling.

    ### How to use?
    Use it like a normal frame.

    ### Example:

        root = Tk()
        frame = SFrame(root, bg='pink')
        frame.pack()

        for i in range(100):
            Button(frame, text='Button %s'%i).pack()

        root.mainloop()
    """

    def __init__(self, master=None, **kw):
        self.scrollbarwidth = kw.pop('scrollbarwidth', 10)
        self.mousewheel = kw.pop('mousewheel', 1)
        self._canvas = _TK.Canvas(master=master, highlightthickness=0, width=kw.pop('width', 250),
                                  height=kw.pop('height', 250))
        _Frame.__init__(self, self._canvas, **kw)
        self.yScroll = _TK.Scrollbar(
            self._canvas, orient='vertical', width=self.scrollbarwidth)
        self.yScroll.place(relx=1, rely=0, anchor='ne', relheight=1)
        self.yScroll.configure(command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=self.yScroll.set)
        self._canvas.create_window(0, 0, anchor='nw', tags="window", window=self,
                                   width=self._canvas.winfo_reqwidth()-self.yScroll.winfo_reqwidth())
        self._canvas.bind("<Configure>", self._configure_height, add="+")
        self.bind_class(self, "<Configure>", self._configure_window, add="+")
        self._mouse_scrolling()
        self._geometryManager()

    def _mouse_scrolling(self):
        """Internal function."""
        if self.mousewheel:
            self.bind_class(self, '<Enter>', lambda _:
                            self.bind_all('<MouseWheel>', self._on_mouse_scroll))
            self.bind_class(self, '<Leave>', lambda _:
                            self.unbind_all('<MouseWheel>'))
        else:
            self.unbind_class(self, '<Enter>')
            self.unbind_class(self, '<Leave>')

    def _on_mouse_scroll(self, evt):
        """Internal function."""
        if evt.state == 0:
            self._canvas.yview_scroll(-1*(evt.delta), 'units')

    def _configure_height(self, evt):
        """Internal function."""
        if self.winfo_height() < self._canvas.winfo_height():
            self._canvas.itemconfig(
                "window", height=self._canvas.winfo_height(), anchor='nw')
        self._canvas.itemconfig(
            'window', width=self._canvas.winfo_width()-self.yScroll.winfo_width())

    def _configure_window(self, evt):
        """Internal function."""
        # this will update the position of scrollbar when scrolled from mousewheel.
        # fixes some bugs
        # makes scrolling more smoother
        self.update()
        self._canvas.configure(scrollregion=self._canvas.bbox('all'))

    def _geometryManager(self):
        """Internal function."""
        # Can be done in a loop with setatr but then it underlines with red when these
        # attributes are called as they're created at runtime.
        self.grid = self.grid_configure = self._canvas.grid_configure
        self.grid_forget = self._canvas.grid_forget
        self.grid_info = self._canvas.grid_info
        self.grid_remove = self._canvas.grid_remove
        self.pack = self.pack_configure = self._canvas.pack_configure
        self.pack_forget = self._canvas.pack_forget
        self.pack_info = self._canvas.pack_info
        self.place = self.place_configure = self._canvas.place_configure
        self.place_forget = self._canvas.place_forget
        self.place_info = self._canvas.place_info

    def configure(self, cnf=None, **kw):
        """Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.
        """
        kw = _TK._cnfmerge((cnf, kw))
        self._canvas['width'] = kw.pop('width', self._canvas['width'])
        self._canvas['height'] = kw.pop('height', self._canvas['height'])
        self.yScroll['width'] = kw.pop('scrollbarwidth', self.yScroll['width'])
        self.mousewheel = kw.pop('mousewheel', self.mousewheel)
        self._mouse_scrolling()
        return _Frame.configure(self, **kw)

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in ('scrollbarwidth', 'mousewheel'):
            return self.__dict__.get(key)
        return _Frame.cget(self, key)
    config = configure
    __getitem__ = cget


class Button(Widget):
    """ Button for macos, supports almost all the features of tkinter button,
    - Looks very similar to ttk Button.
    - There are few extra features as compared to default Tkinter Button:
    - To check the list of all the resources. To get an overview about
        the allowed keyword arguments call the method keys 
            print(Button().keys())

    ### Examples:
        import tkinter as tk
        import tkmacosx as tkm
        root = tk.Tk()
        root.geometry('200x200')
        tkm.Button(root, text='Mac OSX', bg='lightblue', fg='yellow').pack()
        tk.Button(root, text='Mac OSX', bg='lightblue', fg='yellow').pack()
        ttk.Button(root, text='Mac OSX').pack()
        root.mainloop()

    ### Get a cool gradient effect in activebackground color.
        import tkinter as tk
        import tkmacosx as tkm
        root = tk.Tk()
        root.geometry('200x200')
        tkm.Button(root, text='Press Me!!', activebackground=('pink','blue') ).pack()
        tkm.Button(root, text='Press Me!!', activebackground=('yellow','green') ).pack()
        tkm.Button(root, text='Press Me!!', activebackground=('red','blue') ).pack()
        root.mainloop()"""

    # all the instance of class Button will be stored in _button list.

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master=master, cnf=cnf, **kw)

    def invoke(self):
        """Invoke the command associated with the button.

        The return value is the return value from the command,
        or an empty string if there is no command associated with
        the button. This command is ignored if the button's state
        is disabled.
        """
        if self['state'] == 'normal':
            return self.cnf['command']() if self.cnf.get('command') else None


class Marquee(_TK.Canvas):
    """Use `Marquee` for creating scrolling text which moves from 
    right to left only if the text does not fit completely.

    ### Args:
    - `text`: Give a string to display.
    - `font`: Font of the text.
    - `fg`: Set foreground color of the text.
    - `fps`: Set fps(frames per seconds).
    - `left_margin`: Set left margin to make text move further to right before reset.
    - `initial_delay`: Delay before text start to move.
    - `end_delay`: Delay before text reset.
    - `smoothness`: Set the smoothness of the animation.

    ### Example: 
        root=tk.Tk()
        marquee = Marquee(root, text='This text will move from right to left if does not fit the window.')
        marquee.pack()
        root.mainloop()"""

    def __init__(self, master=None, cnf={}, **kw):
        kw = _TK._cnfmerge((cnf, kw))
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
        _TK.Canvas.__init__(self, master=master, **kw)
        self.create_text(3, 1, anchor='w', tag='text', text=self.cnf.get('text'),
                         font=self.cnf.get('font'), fill=self.cnf.get('fg'))
        self.bind_class(self, '<Configure>', self.check, '+')
        self.after_id = ' '

    def check(self, evt=None):
        "Sets the text properly in the frame."
        self.coords('text', 3, self.winfo_height()/2)
        text_width = self.bbox('text')[2]   # TEXT WIDTH
        frame_width = self.winfo_width()    # FRAME WIDTH
        if text_width + 1 < frame_width:
            self.after_cancel(self.after_id)
            self.coords('text', 3, self.winfo_height()/2)  # RESETS TEXT
            self.after_id = ' '
        elif self.after_id == ' ':
            delay = self.cnf.get('initial_delay')  # INITITAL DEALY
            self.after_id = self.after(delay, self.animate)

    def animate(self, evt=None):
        "Process text and move text."
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
            self.move('text', -self.cnf.get('smoothness'), 0)
        self.after_id = self.after(delay, self.animate)

    def configure(self, cnf={}, **kw):
        """Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.
        """
        kw = _TK._cnfmerge((cnf, kw))
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
        self.itemconfig('text', text=self.cnf.get('text'),
                        font=self.cnf.get('font'), fill=self.cnf.get('fg'))
        return _TK.Canvas.configure(self, **kw)

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in self.cnf.keys():
            return self.cnf['key']
        return _TK.Canvas.cget(self, key)
    __getitem__ = cget
    config = configure

    def destroy(self):
        """Destroy this widget."""
        self.after_cancel(self.after_id)
        return _TK.Canvas.destroy(self)

# ------------------ Testing ------------------


def demo_button():
    if sys.version_info.major == 2:
        import ttk
    elif sys.version_info.major == 3:
        from tkinter import ttk
    root = _TK.Tk()
    root.title('Mac OSX Button Demo')
    page_color = '#FFFFC6'
    root.geometry('300x400')
    root['bg'] = page_color
    _TK.Label(root, text='Can you tell the difference?', font=(
        '', 16, 'bold'), bg=page_color).pack(pady=(20, 5))
    Button(root, text='Press Me', disabledbackground='red').pack(pady=(0, 5))
    ttk.Button(root, text="Press Me").pack()
    _TK.Label(root, text='Change Background Color', font=(
        '', 16, 'bold'), bg=page_color).pack(pady=(20, 5))
    Button(root, text='Press Me', bg='pink',
           activebackground=('pink', 'blue')).pack()
    _TK.Label(root, text='Blend In', font=('', 16, 'bold'),
              bg=page_color).pack(pady=(20, 5))
    Button(root, text='Press Me', bg='yellow', activebackground=(
        'orange', 'lime'), borderless=1).pack()
    _TK.Label(root, text='Change bordercolor', font=(
        '', 16, 'bold'), bg=page_color).pack(pady=(20, 5))
    Button(root, text='Press Me', bg='red', fg='white',
           activebackground=('red', 'blue'), bordercolor='blue').pack()
    root.mainloop()


def demo_sframe():
    root = _TK.Tk()
    frame = SFrame(root, bg='pink')
    frame.pack()
    for i in range(50):
        Button(frame, text='Button %s' % i, borderless=1).pack()
    root.mainloop()


def demo_marquee():
    root = _TK.Tk()
    marquee = Marquee(
        root, text='This text will move from right to left if does not fit the window.')
    marquee.pack()
    root.mainloop()


if __name__ == "__main__":
    demo_sframe()
    demo_button()
    demo_marquee()
