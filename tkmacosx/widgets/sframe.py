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

from tkmacosx.basewidgets.sframe_base import SFrameBase


class SFrame(SFrameBase):
    "Sframe widget. (Scrollable frame)"

    def __init__(self, master=None, cnf={}, **kw):
        """### Scrollable Frame ButtonBase.    
        (Only supports vertical scrolling)

        Sames as tkinter Frame. These are some extra resources.
        - `scrollbarwidth`: Set the width of scrollbar.
        - `mousewheel`: Set mousewheel scrolling.
        - `avoidmousewheel`: Give widgets that also have mousewheel scrolling and is a child of SFrame \
            this will configure widgets to support their mousewheel scrolling as well. \
            For eg:- Text widget inside SFrame can have mousewheel scrolling as well as SFrame.

        Scrollbar of SFrame can be configured by calling `scrollbar_configure(**options)`. 
        To access methods of the scrollbar it can be called through the scrollbar instance `self['scrollbar']`.

        ### How to use?
        Use it like a normal frame.

        ### Example:
        ```
        root = Tk()
        frame = SFrame(root, bg='pink')
        frame.pack()

        for i in range(100):
            Button(frame, text='Button %s'%i).pack()

        root.mainloop()
        ```"""
        SFrameBase.__init__(self, master=master, cnf=cnf, **kw)
        self.scrollbar_configure = self['scrollbar'].configure
