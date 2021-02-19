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

from tkmacosx.basewidgets.marquee_base import MarqueeBase


class Marquee(MarqueeBase):
    """Marquee widget."""

    def __init__(self, master=None, cnf={}, **kw):
        """Use `Marquee` for creating scrolling text which moves from 
        right to left only if the text does not fit completely.

        ### Args:
        - `text`: Give a string to display.
        - `font`: Font of the text.
        - `fg`: Set foreground color of the text.
        - `fps`: Set fps(frames per seconds).
        - `left_margin`: Set left margin to make text move further in right direction before reset.
        - `initial_delay`: Delay before text start to move.
        - `end_delay`: Delay before text reset.
        - `smoothness`: Set the smoothness of the animation.

        ### Example: 
        ```
        root=tk.Tk()
        marquee = Marquee(root, 
                        text='This text will move from right to left if does not fit the window.')
        marquee.pack()
        root.mainloop()
        ```

        ### To move the text when cursor is over the text then follow the below example.
        ```
        text = "Please hover over the text to move it. "
               "This text will move only if the cursor "
               "hovers over the text widget."
        root = tk.Tk()
        m = tkm.Marquee(root, bg='lightgreen', text=text)
        m.pack()
        m.stop(True)
        m.bind('<Enter>', lambda _: m.play())
        m.bind('<Leave>', lambda _: m.stop())
        root.mainloop()
        ```"""
        MarqueeBase.__init__(self, master=master, cnf=cnf, **kw)

    def reset(self):
        """Reset the text postion."""
        self._reset(True)
        self._stop_state = False

    def stop(self, reset=False):
        """Stop the text movement."""
        if reset:
            self.reset()
        self._stop_state = True
        self.after_cancel(self.after_id)
        self.after_id = ' '

    def play(self, reset=False):
        """Play/continue the text movement."""
        if not self._stop_state and not reset:
            return
        self._stop_state = False
        if reset:
            self.reset()
        self._animate()
