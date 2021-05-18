<p align="center">
   <img width="550" alt="tkmacosx" src="https://user-images.githubusercontent.com/46227224/114270791-e8816f00-9a2b-11eb-911c-a736253b3de5.png">
</p>
<p align="center">
   <a href="https://pypi.org/project/tkmacosx/"><img src="https://img.shields.io/pypi/v/tkmacosx"></a>
   <a href="https://github.com/Saadmairaj/tkmacosx/actions/workflows/python-package.yml"><img src="https://github.com/Saadmairaj/tkmacosx/actions/workflows/python-package.yml/badge.svg"></a>
   <a href="https://lgtm.com/projects/g/Saadmairaj/tkmacosx/context:python"><img src="https://img.shields.io/lgtm/grade/python/g/Saadmairaj/tkmacosx.svg?logo=lgtm&logoWidth=18"></a>
   <a href="https://www.codefactor.io/repository/github/saadmairaj/tkmacosx"><img src="https://www.codefactor.io/repository/github/saadmairaj/tkmacosx/badge"></a>
   <a href="https://GitHub.com/Saadmairaj/tkmacosx/graphs/commit-activity"><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg"></a>
   <a href="https://pepy.tech/project/tkmacosx"><img src="https://pepy.tech/badge/tkmacosx"></a>
   <a href="https://app.fossa.com/projects/git%2Bgithub.com%2FSaadmairaj%2Ftkmacosx?ref=badge_small"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2FSaadmairaj%2Ftkmacosx.svg?type=small"></a>
   <a href="https://github.com/Saadmairaj/tkmacosx/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Saadmairaj/tkmacosx.svg"></a>
   <a href="https://github.com/Saadmairaj/tkmacosx/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/Saadmairaj/tkmacosx.svg"></a>
   <a href="https://conda.anaconda.org/saad_7"><img src="https://anaconda.org/saad_7/tkmacosx/badges/installer/conda.svg"></a>   
   <img src="https://img.shields.io/powershellgallery/p/Pester?color=blue">
</p>

This module provides some modified widgets of Tkinter which fixes many issues with widgets not working properly on macOS platform. For example Button of tkmacosx which looks and feels exactly like a native Tkinter button can change its _background_ and _foreground_ color and has a lot more functionality, Issues with Radiobutton are also fixed with this library. The library also offers some more useful functionality.

**Read more about all the classes and methods in the [tkmacosx documentation](https://github.com/Saadmairaj/tkmacosx#demonstration).**

Table of Contents

1. [Requirements](https://github.com/Saadmairaj/tkmacosx#requirements)
2. [Installation](https://github.com/Saadmairaj/tkmacosx#installation)
3. [Demonstration](https://github.com/Saadmairaj/tkmacosx#demonstration)
4. [Documentation](https://github.com/Saadmairaj/tkmacosx#documentation)
   - [4.1. Button Widget](https://github.com/Saadmairaj/tkmacosx#button-widget)
   - [4.2. CircleButton Widget](https://github.com/Saadmairaj/tkmacosx#circlebutton-widget)
   - [4.3. SFrame Widget](https://github.com/Saadmairaj/tkmacosx#sframe-widget)
   - [4.4. Colorscale Widget](https://github.com/Saadmairaj/tkmacosx#colorscale-widget)
   - [4.5. Marquee Widget](https://github.com/Saadmairaj/tkmacosx#marquee-widget)
   - [4.6. Radiobutton Widget](https://github.com/Saadmairaj/tkmacosx#radiobutton-widget)
   - [4.7. ColorVar Variable](https://github.com/Saadmairaj/tkmacosx#colorvar-variable)
   - [4.8. DictVar Variable](https://github.com/Saadmairaj/tkmacosx#dictvar-variable)
   - [4.9. SaveVar](https://github.com/Saadmairaj/tkmacosx#savevar)
   - [4.10. get_shade](https://github.com/Saadmairaj/tkmacosx#get_shade)
   - [4.11. check_appearance](https://github.com/Saadmairaj/tkmacosx#check_appearance)
   - [4.12. check_light_dark](https://github.com/Saadmairaj/tkmacosx#check_light_dark)
   - [4.13. gradient](https://github.com/Saadmairaj/tkmacosx#gradient)
5. [Changelog](https://github.com/Saadmairaj/tkmacosx#changelog)
6. [License](https://github.com/Saadmairaj/tkmacosx#license)

## Requirements

- Python 3

Python packages:

- tkinter _(included in the python distribution)_
- [colour](https://pypi.org/project/colour/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [tkmacosx](https://pypi.org/project/tkmacosx/) with the following command:

```bash
pip install tkmacosx
```

If you would like to get the latest master or branch from github, you could also:

```bash
pip install git+https://github.com/Saadmairaj/tkmacosx
```

Or even select a specific revision _(branch/tag/commit)_:

```bash
pip install git+https://github.com/Saadmairaj/tkmacosx@master
```

Similarly, for tag specify [tag](https://github.com/Saadmairaj/tkmacosx/tags) with `@v0.x.x`. For example to download tag v0.1.0 from Git use:

```bash
pip install git+https://github.com/Saadmairaj/tkmacosx@v0.1.0
```

If you use **[Anaconda](https://www.anaconda.com/products/individual) environment** then you could run:

[![Anaconda-Server Badge](https://anaconda.org/saad_7/tkmacosx/badges/version.svg)](https://anaconda.org/saad_7/tkmacosx)
[![Anaconda-Server Badge](https://anaconda.org/saad_7/tkmacosx/badges/downloads.svg)](https://anaconda.org/saad_7/tkmacosx)
[![Anaconda-Server Badge](https://anaconda.org/saad_7/tkmacosx/badges/platforms.svg)](https://anaconda.org/saad_7/tkmacosx)

```bash
conda install -c saad_7 tkmacosx
```

## Demonstration

```bash
python -m tkmacosx
```

Run the above command in the terminal or command line after installing tkmacosx to see working and almost all the configurable options of different widgets of tkmacosx.

<p align='center'><img src="https://user-images.githubusercontent.com/46227224/114269362-4742ea80-9a24-11eb-810f-eaa85b68fcf0.gif" height="600"></p>

Also if you want to style your button to stand out, scroll down to bottom of the window opened from the above command and randomise or configure button to different styles.

## Documentation

### Button Widget

The tkmacosx `Button` widget is alternative to tkinter's Button that supports all features on a macos that were not possible with tkinter Button like background, relief, overrelief, activebackground, and some other features can be set. There is a blue focus ring that tells if the button has the focus or not to disable or hide the focus ring, either set `takefocus=0` or `focuscolor=''`.

- Configurable options for a button widget. Syntax: `Button(root, options=value, ...)`

  | Options               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _activebackground_    | What background color to use when the button is active. The default is system specific. Give tuple of two colors for gradient effect in active background.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | _activeforeground_    | What foreground color to use when the button is active. The default is system specific.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | _activeimage_         | What Image to display when the button is active. No image to display by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  | _activebitmap_        | What Bitmap to display when the button is active. No bitmap to display by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | _anchor_              | Where the text is positioned on the button. For example, `anchor=tk.NE` would position the text at the top right corner of the button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | _bordercolor_         | The color to use for the highlight border when the button does not have focus. The default is system-specific. Same as highlightbackground.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | _borderless_          | Blend the button with its parent's background results in a clean look with no square borders. It will change color automatically. The default is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | _bd or borderwidth_   | Width of the border around the outside of the button. The default is two pixels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  | _bg or background_    | Normal background color.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | _command_             | Function or method to be called when the button is clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | _cursor_              | Selects the cursor to be shown when the mouse is over the button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | _disabledforeground_  | The color to use when the button is disabled. The default is system specific.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | _focuscolor_          | The color to use for the focus border when the button have focus. The default is system specific.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | _focusthickness_      | The width of the focus border _(pixels)_. The default is system specific.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | _fg or foreground_    | Normal foreground (text) color.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | _font_                | Text font to be used for the button's label.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | _height_              | The height of the button. The size is given in _pixels for both text and images._                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | _highlightbackground_ | Color of the focus highlight when the widget does not have focus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | _highlightcolor_      | The color of the focus highlight when the widget has focus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | _highlightthickness_  | Thickness of the focus highlight.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | _image_               | Image to be displayed on the button (instead of text).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | _justify_             | How to show multiple text lines: `tk.LEFT` to left-justify each line; `tk.CENTER` to center them; or `tk.RIGHT` to right-justify.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | _overbackground_      | Alternative background to use when the mouse is moved over the widget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | _overforeground_      | Alternative foreground to use when the mouse is moved over the widget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | _overrelief_          | The relief style to be used while the mouse is on the button; the default relief is `tk.RAISED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  | _padx_                | Additional padding left and right of the text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | _pady_                | Additional padding above and below the text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | _relief_              | Specifies the relief type for the button. The default relief is `tk.RAISED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | _repeatdelay_         | See `repeatinterval`, below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | _repeatinterval_      | Normally, a button fires only once when the user releases the mouse button. If you want the button to fire at regular intervals as long as the mouse button is held down, set this option to a number of milliseconds to be used between repeats, and set the `repeatdelay` to the number of milliseconds to wait before starting to repeat. _For example, if you specify “ `repeatdelay=500`, `repeatinterval=100` ” the button will fire after half a second, and every tenth of a second thereafter, until the user releases the mouse button. If the user does not hold the mouse button down at least `repeatdelay` milliseconds, the button will fire normally._ |
  | _state_               | Set this option to `"disabled"` to gray out the button and make it unresponsive. Has the value `"active"` when the mouse is over it. Keep the button pressed with `"pressed"`. Default is `"normal"`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | _takefocus_           | Normally, keyboard focus does visit buttons, and a space character acts as the same as a mouse click, “pushing” the button. You can set the takefocus option to zero to prevent focus from visiting the button.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | _text_                | Text displayed on the button. Use internal newlines to display multiple text lines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | _textvariable_        | An instance of `StringVar()` that is associated with the text on this button. If the variable is changed, the new value will be displayed on the button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | _width_               | The width of the button. The size is given in _pixels for both text and images._                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

- Methods on `Button` objects:

  | Methods     | Description                                                                                                                                   |
  | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
  | _.invoke()_ | Calls the button's command callback, and returns what that function returns. Has no effect if the button is disabled or there is no callback. |

- **Example:**

  ```python
  from tkinter import Tk
  from tkmacosx import Button

  root = Tk()
  root.geometry('200x150')
  B0 = Button(root, text='Button')
  B0.pack(padx=20, pady=(20,0))
  B1 = Button(root, text='Button', bg='#ADEFD1',
              fg='#00203F', borderless=1)
  B1.pack(padx=20, pady=10)
  B2 = Button(root, text='Button', bg='#E69A8D',
              fg='#5F4B8B', borderless=1,
              activebackground=('#AE0E36', '#D32E5E'),
              activeforeground='#E69A8D')
  B2.pack()
  root.mainloop()
  ```

   <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269000-f29e7000-9a21-11eb-9e10-ebd299c2ef7b.gif">
   </p>

- Few sample of different styles of button that can be configured.

<p align="center">
   <img src="https://user-images.githubusercontent.com/46227224/114268774-8d964a80-9a20-11eb-9122-8ee9292d4738.gif">
   <img src="https://user-images.githubusercontent.com/46227224/114268991-de5a7300-9a21-11eb-9f88-3145a6250f4d.gif">
   <img src="https://user-images.githubusercontent.com/46227224/114268987-d8649200-9a21-11eb-9668-6d5766414475.gif">
</p>

```python
# Options to get button in the first image.
b1 = Button(root, text='Button', activeforeground= '#EE3B3B', overrelief='flat', relief='flat', borderwidth=2,
    highlightthickness=1, font=font.Font(family='SignPainter', size=30, weight='bold', slant='roman'),
    focuscolor='#556B2F',highlightbackground='#CD5555', foreground='#1F1F1F', background='#7A7A7A',
    overbackground='#000000', overforeground='#00C78C', activebackground=('#BA55D3', '#D4D4D4'), borderless=1)

# Options to get button in the second image.
b2 = Button(root, text='Button', activeforeground= '#B5B5B5', overrelief='raised', relief='sunken', borderwidth=2,
    highlightthickness=4, font=font.Font(family='Brush Script MT', size=30, weight='bold', slant='roman'),
    focuscolor='#CD3700', highlightbackground='#AAAAAA', foreground='#6B6B6B', background='#BDBDBD',
    overbackground='#7A67EE', overforeground='#404040', activebackground=('#FF34B3', '#C1CDC1'), borderless=1)

# Options to get button in the third image.
b3 = Button(root, text='Button', activeforeground= '#FFDAB9', overrelief='flat', relief='raised', borderwidth=1,
    highlightthickness=3, font=font.Font(family='Helvetica', size=30, weight='bold', slant='roman', underline=1),
    focuscolor='#F5DEB3', highlightbackground='#8A360F',foreground='#FFC0CB', background='#708090',
    overbackground='#53868B', overforeground='#CCCCCC', activebackground=('#808069', '#C67171'), borderless=1)
```

---

### CircleButton Widget

**_BETA-Disclaimer:_** _Please note that this is a BETA version. Issues can be reported [here](https://github.com/Saadmairaj/tkmacosx/issues/new/choose)._

Circle shaped tkinter Button can contain text or images, and you can associate a Python function or method with each button. There is a blue focus ring that tells if the button has the focus or not to disable or hide the focus ring, either set `takefocus=0` or `focuscolor=''`. The CircleButton widget supports all the configurable options of tkmacosx [Button](#button-widget).

- Configurable options for a button widget. Syntax: `CircleButton(root, options=value, ...)`
  All the options are pretty much the same as tkmacosx [Button](#button-widget). Other options:

  | Options  | Description                                                                                                               |
  | -------- | ------------------------------------------------------------------------------------------------------------------------- |
  | _radius_ | Set the size of the button using radius _(in pixels)_. If width or height are given then radius value gets cancelled out. |

- Methods on `CircleButton` objects:

  | Methods     | Description                                                                                                                                   |
  | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
  | _.invoke()_ | Calls the button's command callback, and returns what that function returns. Has no effect if the button is disabled or there is no callback. |

- **Example:**

```python
from tkinter import *
from tkmacosx import CircleButton

root = Tk()
B0 = CircleButton(root, text='Button')
B0.grid(row=0)
B1 = CircleButton(root, text='Button', bg='#ADEFD1',
            fg='#00203F', borderless=1)
B1.grid(row=0, column=1)
B2 = CircleButton(root, text='Button', bg='#E69A8D',
            fg='#5F4B8B', borderless=1,
            activebackground=('#AE0E36', '#D32E5E'),
            activeforeground='#E69A8D')
B2.grid(row=0, column=2)
root.mainloop()
```

   <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269031-24afd200-9a22-11eb-9c23-17c6d560600a.gif">
   </p>

---

### SFrame Widget

The tkmacosx `SFrame` widget is just like a tkinter Frame but can be vertically scrolled. The SFrame supports intelligent mousewheel scrolling where it let you use mousewheel with other children widgets also having mousewheel scrolling without interfering with other widgets scrolling, a list of widgets having mousewheel scrolling can be passed to `avoidmousewheel` argument _(ex: `avoidmousewheel=(text1, text2, sframe)` or just one `avoidmousewheel=text2`)._

- Configurable options for a sframe widget. Syntax: `SFrame(root, options=value, ...)`

  | Options | Description |
  |----------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | _avoidmousewheel_ | Give widgets that also having the mousewheel scrolling and is a child of _SFrame_, this option will configure widgets to support their mousewheel scrolling as well and not interfere with _SFrame_ mousewheel scrolling. _For example: Text widget inside SFrame can have mousewheel scrolling as well as SFrame._ |
  | _autohidescrollbar_ | Auto hides the scrollbar when not in use or when the cursor is not around the scrollbar location. The scrollbar will reappear when mousewheel scrolling is used or the cursor is moved over the scrollbar location. Default is False. |
  | _autohidescrollbardelay_ | Time taken for the scrollbar to hide after reappearing. |
  | _bg or background_ | The frame's background color. |
  | _bd or borderwidth_ | Width of the frame's border. The default is 0 (no border). |
  | _cursor_ | The cursor used when the mouse is within the frame widget. |
  | _height_ | The vertical dimension of the new frame. This will be ignored unless you also call `.grid_propagate(0)` on the frame. |
  | _highlightbackground_ | Color of the focus highlight when the frame does not have focus. |
  | _highlightcolor_ | Color is shown in the focus highlight when the frame has the focus. |
  | _highlightthickness_ | The thickness of the focus highlight. |
  | _mousewheel_ | Set mousewheel scrolling. The default is `False` |
  | _padx_ | Normally, a Frame fits tightly around its contents. To add _N_ pixels of horizontal space inside the frame, set `padx=N`. |
  | _pady_ | Used to add vertical space inside a frame. See _padx_ above. |
  | _relief_ | The default relief for a frame is _tk.FLAT_, which means the frame will blend in with its surroundings. To put a border around a frame, set its borderwidth to a positive value and set its relief to one of the standard relief types. |
  | _scrollbarwidth_ | Set the width of scrollbar. |
  | _takefocus_ | Normally, frame widgets are not visited by input focus. However, you can set `takefocus=1` if you want the frame to receive keyboard input. To handle such input, you will need to create bindings for keyboard events. |
  | _width_ | The horizontal dimension of the new frame. This value be ignored unless you also call `.grid_propagate(0)` on the frame |

- **Example:**

  ```python
  from tkinter import *
  from tkmacosx import SFrame, Button

  root = Tk()
  root.geometry('350x300')
  frame = SFrame(root, bg='#333')
  text = Text(frame, background='#5F4B8B',
              width=35, height=10, foreground='white')
  text.pack(pady=(0,20))

  frame2 = SFrame(frame, bg='#E69A8D', scrollbarwidth=3)
  frame2.pack(pady=20)

  frame.config(avoidmousewheel=(text, frame2))
  frame.pack(expand=1, fill='both')
  for i in range(50):
     Button(frame2, text='Button %s'%i).pack()
     text.insert('end', 'Text Line: %s\n'%i)

  root.mainloop()
  ```

   <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269044-37c2a200-9a22-11eb-89b2-ccbe1c0cef83.gif">
   </p>

---

### Colorscale Widget

Colorscale is a new style color selector which is an alternate to tkinter's colorchooser.

- Configurable options for a Colorscale widget. Syntax: `Colorscale(root, options=value, ...)`

  | Options               | Description                                                                                                                                                                                                                                                                                       |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _bd or borderwidth_   | Width of the border around the outside of the _Colorscale_. The default is two pixels.                                                                                                                                                                                                            |
  | _command_             | A function or method with a parameter that is called when the slider is moved or scrolled and an argument is paased to the callback. The callback can be a function, bound method, or any other callable Python object. If this option is not used, nothing will happen when the slider is moved. |
  | _cursor_              | Cursor used in the _Colorscale_.                                                                                                                                                                                                                                                                  |
  | _gradient_            | Takes tuple of two colors. Two colors are required to form a gradient (`sequence[FROM, TO]`, For example: A tuple of `tuple('white', 'black')` will create a _Colorscale_ from _WHITE_ to _BLACK_ color). By default is complete color gradient.                                                  |
  | _height_              | Size of the _Colorscale_ in the Y dimension.                                                                                                                                                                                                                                                      |
  | _highlightbackground_ | Color of the focus highlight when the widget does not have focus.                                                                                                                                                                                                                                 |
  | _highlightcolor_      | Color is shown in the focus highlight.                                                                                                                                                                                                                                                            |
  | _highlightthickness_  | The thickness of the focus highlight. The default value is 1.                                                                                                                                                                                                                                     |
  | _mousewheel_          | Move the slider with mousewheel with _True._ By default the option is set _False._                                                                                                                                                                                                                |
  | _orient_              | Set the orientation _(VERTICAL, HORIZONTAL)_. By default is VERTICAL.                                                                                                                                                                                                                             |
  | _relief_              | The relief style of the _Colorscale_. Default is tk.FLAT.                                                                                                                                                                                                                                         |
  | _showinfo_            | Shows hex or rbg while selecting color.                                                                                                                                                                                                                                                           |
  | _showinfodelay_       | Delay before the show info disappears _(in ms)_.                                                                                                                                                                                                                                                  |
  | _takefocus_           | Normally, focus will cycle through this widget with the tab key only if there are keyboard bindings set for it (see Section 54, “Events”for an overview of keyboard bindings). If you set this option to 1, the focus will always visit this widget. Set it to '' to get the default behavior.    |
  | _value_               | Get either 'RGB' or 'HEX'. By deafult is hex.                                                                                                                                                                                                                                                     |
  | _variable_            | Associates a Tkinter variable (usually a _tk.StringVar_, _tkm.ColorVar_). If the slider is moved the value of the variable changes as well.                                                                                                                                                       |
  | _width_               | Size of the _Colorscale_ in the X dimension.                                                                                                                                                                                                                                                      |

- **Example:**

  ```python
  from tkinter import *
  from tkmacosx import Colorscale, ColorVar

  root = Tk()
  root['bg'] = '#333'
  bgvar = ColorVar(value='#333')
  fgvar = ColorVar(value='white')
  Label(root, text="I am a Label, Hello! :-)",bg=bgvar, fg=fgvar).pack(pady=10)
  Colorscale(root, value='hex', variable=bgvar, mousewheel=1).pack(padx=20)
  Colorscale(root, value='hex', variable=bgvar, mousewheel=1,
          gradient=('pink', 'purple')).pack(pady=10)
  Colorscale(root, value='hex', variable=fgvar, mousewheel=1,
          gradient=('lightgreen', 'orange')).pack()
  Colorscale(root, value='hex', variable=fgvar, mousewheel=1,
          gradient=('white', '#89ABE3')).pack(pady=10)

  root.mainloop()
  ```

   <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269070-55900700-9a22-11eb-8de5-38885fad5cf8.gif">
   </p>

---

### Marquee Widget

Use `Marquee` for creating scrolling text which moves from right to left only if the text does not fit completely on the window.

- Configurable options for a Marquee widget. Syntax: `Marquee(root, options=value, ...)`

  | Options               | Description                                                                                                                                                                           |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _bg or background_    | The background color of the marquee area.                                                                                                                                             |
  | _bd or borderwidth_   | Width of the border around the marquee. The default value is two pixels.                                                                                                              |
  | _cursor_              | Cursor that appears when the mouse is over this marquee.                                                                                                                              |
  | _disabledforeground_  | The color to use when the button is disabled. The default is systemspecific.                                                                                                          |
  | _end_delay_           | Time to wait before reseting at the end of movement. Default is 1000 ms.                                                                                                              |
  | _font_                | If you are displaying text in this marquee with the text option, the font option specifies in what font that text will be displayed.                                                  |
  | _fg or foreground_    | If you are displaying text in this marquee, this option specifies the color of the text.                                                                                              |
  | _fps_                 | Set fps(frames per seconds) indirectly is the speed of text movement. Default is 30.                                                                                                  |
  | _height_              | The height of the _Marquee_ is in pixels. If this option is not set, the _Marquee_ will be sized to fit its contents.                                                                 |
  | _highlightbackground_ | Color of the focus highlight when the widget does not have focus.                                                                                                                     |
  | _highlightcolor_      | The color of the focus highlight when the widget has focus.                                                                                                                           |
  | _highlightthickness_  | The thickness of the focus highlight.                                                                                                                                                 |
  | _initial_delay_       | Time to wait before starting the movement of the text. Default is 1000 ms.                                                                                                            |
  | _justify_             | Specifies how multiple lines of text will be aligned with respect to each other: _tk.LEFT_ for flush left, _tk.CENTER_ for centered (the default), or _tk.RIGHT_ for right-justified. |
  | _left_margin_         | Text to keep moving to right after last character is displayed before reseting.                                                                                                       |
  | _smoothness_          | Millisecond delay in movement of each frame. Default is 1 ms.                                                                                                                         |
  | _state_               | By default, a _Marquee_ widget is in the _tk.NORMAL_ state. Set this option to _tk.DISABLED_ to make it unresponsive to mouse events.                                                 |
  | _relief_              | Specifies the appearance of a decorative border around the _Marquee_. The default is _tk.FLAT_; for other values.                                                                     |
  | _takefocus_           | Normally, focus does not cycle through _Marquee_ widgets. If you want this widget to be visited by the focus, set `takefocus=1`.                                                      |
  | _text_                | To display one or more lines of text in a _Marquee_ widget, set this option to a string containing the text. Internal newlines ('\n') will force a line break.                        |
  | _width_               | The width of the _Marquee_ is in pixels. If this option is not set, the _Marquee_ will be sized to fit its contents.                                                                  |

- Methods on `Marquee` widget objects:

  | Methods              | Description                                                                                                                                   |
  | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
  | _.reset()_           | Resets the position of the text to default.                                                                                                   |
  | _.stop(reset: bool)_ | Stops the moving text to the current position. Set parameter `reset=True` to stop the movement and reset the position of the text to default. |
  | _.play(reset: bool)_ | Plays the stopped text from the current position. Set parameter `reset=True` to play from the default position.                               |

- **Example:**

  ```python
  from tkinter import *
  from tkmacosx import Marquee

  text1 = """This text will move from right to left \
  if does not fit the window."""
  text2 = """Please hover over the text to move it. \
  This text will move only if the cursor hovers over \
  the text widget."""

  root = Tk()
  root['bg'] = '#333'
  Marquee(root, bg='#FEE715', fg='#101820', text=text1).pack(pady=10)
  m = Marquee(root, fg='#FEE715', bg='#101820', text=text2)
  m.pack(pady=(0,10), padx=10)
  m.stop(True)
  m.bind('<Enter>', lambda _: m.play())
  m.bind('<Leave>', lambda _: m.stop())
  root.mainloop()
  ```

   <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269092-70fb1200-9a22-11eb-99f0-08f87078ff53.gif">
   </p>

---

### Radiobutton Widget

Radiobutton of tkmacosx are fixed from multiple issues i.e. background color not showing properly when `indicator=0`, _activebackground_, _activeforeground_ options not working, few other issues are fixed in tkmacosx Radiobutton. Radiobuttons are sets of related widgets that allow the user to select only one of a set of choices. Each radiobutton consists of two parts, the _indicator_ and the _label_.

- Configurable options for a Colorscale widget. Syntax: `Radiobutton(root, options=value, ...)`

  | Options               | Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | _activebackground_    | The background color when the mouse is over the radiobutton.                                                                                                                                                                                                                                                                                                                                                                         |
  | _activeforeground_    | The foreground color when the mouse is over the radiobutton.                                                                                                                                                                                                                                                                                                                                                                         |
  | _anchor_              | If the widget inhabits a space larger than it needs, this option specifies where the radiobutton will sit in that space. The default is `anchor=tk.CENTER`. For other positioning options. For example, if you set `anchor=tk.NE`, the radiobutton will be placed in the top right corner of the available space.                                                                                                                    |
  | _bg or background_    | The normal background color behind the indicator and label.                                                                                                                                                                                                                                                                                                                                                                          |
  | _bitmap_              | To display a monochrome image on a radiobutton, set this option to a bitmap.                                                                                                                                                                                                                                                                                                                                                         |
  | _bd or borderwidth_   | The size of the border around the indicator part itself. Default is two pixels.                                                                                                                                                                                                                                                                                                                                                      |
  | _command_             | A procedure to be called every time the user changes the state of this radiobutton.                                                                                                                                                                                                                                                                                                                                                  |
  | _compound_            | If you specify both text and a graphic (either a bitmap or an image), this option specifies where the graphic appears relative to the text. Possible values are _tk.NONE_ (the default value), _tk.TOP_, _tk.BOTTOM_, _tk.LEFT_, _tk.RIGHT_, and _tk.CENTER_. For example, `compound=tk.BOTTOM` would position the graphic below the text. If you specify `compound=tk.NONE`, the graphic is displayed but the text (if any) is not. |
  | _cursor_              | If you set this option to a cursor name, the mouse cursor will change to that pattern when it is over the radiobutton.                                                                                                                                                                                                                                                                                                               |
  | _disabledforeground_  | The foreground color used to render the text of a disabled radiobutton. The default is a stippled version of the default foreground color.                                                                                                                                                                                                                                                                                           |
  | _font_                | The font used for the text.                                                                                                                                                                                                                                                                                                                                                                                                          |
  | _fg or foreground_    | The color used to render the text.                                                                                                                                                                                                                                                                                                                                                                                                   |
  | _height_              | The number of lines (not pixels) of text on the radiobutton. Default is 1.                                                                                                                                                                                                                                                                                                                                                           |
  | _highlightbackground_ | The color of the focus highlight when the radiobutton does not have focus.                                                                                                                                                                                                                                                                                                                                                           |
  | _highlightcolor_      | The color of the focus highlight when the radiobutton has the focus.                                                                                                                                                                                                                                                                                                                                                                 |
  | _highlightthickness_  | The thickness of the focus highlight. Default is 1. Set `highlightthickness=0` to suppress the display of the focus highlight.                                                                                                                                                                                                                                                                                                       |
  | _image_               | To display a graphic image instead of text for this radiobutton, set this option to an image object. The image appears when the radiobutton is not selected; compare selectimage, below.                                                                                                                                                                                                                                             |
  | _inidicatoron_        | Normally a radiobutton displays its indicator. If you set this option to zero, the indicator disappears, and the entire widget becomes a “push-push” button that looks raised when it is cleared and sunken when it is set. You may want to increase the borderwidth value to make it easier to see the state of such a control.                                                                                                     |
  | _justify_             | If the text contains multiple lines, this option controls how the text is justified: _tk.CENTER_ (the default), _tk.LEFT_, or _tk.RIGHT_.                                                                                                                                                                                                                                                                                            |
  | _offrelief_           | If you suppress the indicator by asserting `indicatoron=False`, the offrelief option specifies the relief style to be displayed when the radiobutton is not selected. The default values is _tk.RAISED_.                                                                                                                                                                                                                             |
  | _overrelief_          | Specifies the relief style to be displayed when the mouse is over the radiobutton.                                                                                                                                                                                                                                                                                                                                                   |
  | _padx_                | How much space to leave to the left and right of the radiobutton and text. Default is 1.                                                                                                                                                                                                                                                                                                                                             |
  | _pady_                | How much space to leave above and below the radiobutton and text. Default is 1.                                                                                                                                                                                                                                                                                                                                                      |
  | _relief_              | By default, a radiobutton will have _tk.FLAT_ relief, so it doesn't stand out from its background. You can also use `relief=tk.SOLID`, which displays a solid black frame around the radiobutton.                                                                                                                                                                                                                                    |
  | _selectcolor_         | The color of the radiobutton when it is set. Default is red.                                                                                                                                                                                                                                                                                                                                                                         |
  | _selectimage_         | If you are using the image option to display a graphic instead of text when the radiobutton is cleared, you can set the selectimage option to a different image that will be displayed when the radiobutton is set.                                                                                                                                                                                                                  |
  | _state_               | The default is `state=tk.NORMAL`, but you can set `state=tk.DISABLED` to gray out the control and make it unresponsive. If the cursor is currently over the radiobutton, the state is _tk.ACTIVE_.                                                                                                                                                                                                                                   |
  | _takefocus_           | By default, the input focus will pass through a radiobutton. If you set `takefocus=0`, focus will not visit this radiobutton.                                                                                                                                                                                                                                                                                                        |
  | _text_                | The label displayed next to the radiobutton. Use newlines ('\n') to display multiple lines of text.                                                                                                                                                                                                                                                                                                                                  |
  | _textvariable_        | If you need to change the label on a radiobutton during execution, create a StringVar to manage the current value, and set this option to that control variable. Whenever the control variable's value changes, the radiobutton's annotation will automatically change to that text as well.                                                                                                                                         |
  | _underline_           | With the default value of -1, none of the characters of the text label are underlined. Set this option to the index of a character in the text (counting from zero) to underline that character.                                                                                                                                                                                                                                     |
  | _value_               | When a radiobutton is turned on by the user, its control variable is set to its current valueoption. If the control variable is an IntVar, give each radiobutton in the group a different integer value option. If the control variable is a StringVar, give each radiobutton a different string value option.                                                                                                                       |
  | _variable_            | The control variable that this radiobutton shares with the other radiobuttons in the group. This can be either an _IntVar_ or a _StringVar_.                                                                                                                                                                                                                                                                                         |
  | _width_               | The default width of a radiobutton is determined by the size of the displayed image or text. You can set this option to a number of characters ( not pixels) and the radiobutton will always have room for that many characters.                                                                                                                                                                                                     |
  | _wraplength_          | Normally, lines are not wrapped. You can set this option to a number of characters and all lines will be broken into pieces no longer than that number.                                                                                                                                                                                                                                                                              |

- Methods on `Radiobutton` widget objects:

  | Methods       | Description                                                                                                                   |
  | ------------- | ----------------------------------------------------------------------------------------------------------------------------- |
  | _.deselect()_ | Clears (turns off) the radiobutton.                                                                                           |
  | _.flash()_    | Flashes the radiobutton a few times between its active and normal colors, but leaves it the way it started.                   |
  | _.invoke()_   | You can call this method to get the same actions that would occur if the user clicked on the radiobutton to change its state. |
  | _.select()_   | Sets (turns on) the radiobutton.                                                                                              |

- **Example:**

  ```python
  import tkinter as tk
  import tkmacosx as tkm

  root = tk.Tk()
  var = tk.IntVar()

  r1 = tkm.Radiobutton(root, text='Radiobutton1', value=1,
                       variable=var, indicatoron=0, padx=20)
  r2 = tkm.Radiobutton(root, text='Radiobutton2', value=2,
                       variable=var, indicatoron=0, padx=20)
  r3 = tkm.Radiobutton(root, text='Radiobutton3', value=3,
                       variable=var, indicatoron=0, padx=20)

  r1.pack(pady=10)
  r2.pack(padx=10)
  r3.pack(pady=10)

  root.mainloop()
  ```

    <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269117-925bfe00-9a22-11eb-9959-86210d9c24f5.gif">
    </p>

---

### ColorVar Variable

ColorVar of tkmacosx set same color to each widget it is assigned to. As ColorVar is a tkinter variable wrapper so it will change the color of widgets whenever the change is made to ColorVar instances. ColorVar takes HEX values and all the color names which tkinter supports but the `get()` method returns only the HEX value. It will work with all of the following keyword arguments of different widgets _(eg:- `Canvas`, `Frame`, `Button`, `Label`, Canvas items, ...)_. **_'fg', 'foreground', 'bg', 'background', 'activebackground', 'activeforeground', 'disabledforeground', 'highlightbackground', 'highlightcolor', 'selectforeground', 'readonlybackground', 'selectbackground', 'insertbackground', 'disabledbackground', 'activefill', 'activeoutline', 'disabledfill','disabledoutline', 'fill', 'outline'_** _(might work with more but have not tested)._

- Configurable options for a ColorVar variable. Syntax: `ColorVar(root, options=value, ...)`

  | Options | Description                                                                                                                                                   |
  | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _value_ | The value is an optional value (defaults to "").                                                                                                              |
  | _name_  | The name is an optional Tcl name (defaults to PY*VARnum). If \_name* matches an existing variable and _value_ is omitted then the existing value is retained. |

- Methods on `ColorVar` variable objects:

  | Methods            | Description                                                                                                                                                |
  | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _.get()_           | Returns the current value of the variable.                                                                                                                 |
  | _.set(value: str)_ | Changes the current value of the variable. If any widget options are slaved to this variable, those widgets will be updated when the main loop next idles. |

- **Example:**

  ```python
  from tkinter import Tk, Label
  from tkmacosx import ColorVar, Button, gradient

  root = Tk()
  root['bg'] = '#333'
  root.geometry('200x200')

  def change_color(c=0):
     if c >= len(color_list): c=0
     color.set(color_list[c])
     root.after(50, change_color, c+1)

  color = ColorVar()
  color_list = gradient(200)
  L = Label(root, textvariable=color, bg='#333', fg=color)
  L.pack(fill='x', expand=1, padx=10, pady=10)
  B = Button(root, textvariable=color, bg=color, borderless=1, activeforeground=color)
  B.pack(fill='x', expand=1, padx=10, pady=10)

  change_color()
  root.mainloop()
  ```

   <p align="center">
      <img src="https://user-images.githubusercontent.com/46227224/114269131-b0c1f980-9a22-11eb-8f2a-13575329f71c.gif">
   </p>

---

### DictVar Variable

DictVar of tkmacosx stores python dictionary. It is very similar to tkinter `StringVar` with few modifications to it. `DictVar.get()` returns an instance of `dict` type whereas StringVar returns `str` type also DictVar method `get()` is a bit different `get(key=None, d=None)` get a key from `get()` method if `key=None` it will return the complete dictionary.

- Configurable options for a DictVar variable. Syntax: `DictVar(root, options=value, ...)`

  | Options | Description                                                                                                                                                   |
  | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _value_ | The value is an optional value (defaults to {}).                                                                                                              |
  | _name_  | The name is an optional Tcl name (defaults to PY*VARnum). If \_name* matches an existing variable and _value_ is omitted then the existing value is retained. |

- Methods on `DictVar` variable objects:

  | Methods                            | Description                                                                                                                                                |
  | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _.get(key: any=None, d: any=None)_ | Returns the current value of the variable. To get a specific value of dictionary use `key`, give a default value to `d` if the `key` is not available.     |
  | _set(value: str)_                  | Changes the current value of the variable. If any widget options are slaved to this variable, those widgets will be updated when the main loop next idles. |

- **Example:**

  ```python
  from tkinter import *
  from tkmacosx import DictVar

  root = Tk()
  dictionary = DictVar(value = {'width': 100, 'height': 200})

  print(type(dictionary.get()))
  print(dictionary.get())
  print(dictionary.get('width'))
  ```

---

### SaveVar

SaveVar of tkmacosx will let you save and load values of tkinter variables (`StringVar`, `IntVar`, ..). SaveVar uses pickle module to save values of variables into a file and when the program is executed next time, it will load the same values as they were last time. If the content of the .py file changes, it might not load correct values to the assigned variables. To avoid this issue use `name` argument to refer to the exact assigned values later.

- Configurable options for a SaveVar function. Syntax: `SaveVar(var, master=None, value=None, name=None, filename='data.pkl')`

  | Parameters | Description                                                                                                                            |
  | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- |
  | _var_      | Give the `tkinter.Variable` class like (`tk.StringVar`, `tk.IntVar`)                                                                   |
  | _master_   | Parent widget.                                                                                                                         |
  | _value_    | The value is an optional value (Given variable's default value).                                                                       |
  | _name_     | Set a name to group variables or to refer to assigned value when loaded.                                                               |
  | _filename_ | Set the name of the save file. (To make the file invisible in the directory start the name of the file with "." like ".cache-savevar") |

- **Example:**

  ```python
  from tkinter import *
  from tkmacosx import SaveVar

  root = Tk()
  var1 = SaveVar(StringVar, root, 'Enter Username', 'Var1', '.cache-savevar')
  var2 = SaveVar(StringVar, root, 'Enter Password', 'Var2', '.cache-savevar')
  Entry(root, textvariable=var1).pack()
  Entry(root, textvariable=var2).pack()
  root.mainloop()
  ```

---

### get_shade

- Configurable options for a get_shade function. Syntax: `get_shade(color, shade, mode='auto')`

  | Parameters | Description                                                                                                                                                                                                                                                                               |
  | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _color_    | Give a color as either HEX or name of the color.                                                                                                                                                                                                                                          |
  | _shade_    | The amount of change required. Takes float between 0.0 to 1.0 eg: `shade=0.225`.                                                                                                                                                                                                          |
  | _mode_     | Use mode for more control over the shade of the color. Use `mode='-'` for darker shade, use `mode='+'` for lighter shade, use `mode='auto'` to automatically decide the shade _(the deafult)_. To change the intensity of shade checking use `mode='auto-110` where 110 is the intensity. |

---

### check_appearance

Checks DARK/LIGHT mode of macOS and returns boolean value. Other settings can also be checked with this function just by passing a different command line argument to check a particular setting to `cmd` parameter of `check_appearance`.

- Configurable options for a check_appearance function. Syntax: `check_appearance(cmd='defaults read -g AppleInterfaceStyle')`.

  | Parameters | Description                                                                                                     |
  | ---------- | --------------------------------------------------------------------------------------------------------------- |
  | _cmd_      | Give commands. _For example: To check DARK/LIGHT mode the command is `'defaults read -g AppleInterfaceStyle'.`_ |

---

### check_light_dark

Tells if the given RGB or HEX code is lighter or darker shade of color. Returns `"black"` for darker shade and `"white"` for lighter shade.

- Configurable options for a check_light_dark function. Syntax: `check_light_dark(value, intensity=110)`.

  | Parameters  | Description                                                  |
  | ----------- | ------------------------------------------------------------ |
  | _value_     | Give sequence of RBG values or hexcode.                      |
  | _intensity_ | The measurable amount of a brightness. By deafult it is 110. |

---

### gradient

This function returns sequences of rainbow colors hexcodes in order.

- Configurable options for a gradient function. Syntax: `gradient(iteration)`.

  | Parameters  | Description              |
  | ----------- | ------------------------ |
  | _iteration_ | Length of the sequences. |

## Changelog

- [**v1.0.2**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v1.0.2)

  - Fix unknown color name "systemWindowBackgroundColor" ([#20](https://github.com/Saadmairaj/tkmacosx/issues/20))
  - Partial "borderless" button option support for ttk widgets ([#19](https://github.com/Saadmairaj/tkmacosx/issues/19))
  - Exclude test package in setup.py

- [**v1.0.1**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v1.0.1)

  - Fix widgets not auto-switch light/dark mode. ([#18](https://github.com/Saadmairaj/tkmacosx/issues/18))
  - Fix Button not working with ttk widgets. ([#19](https://github.com/Saadmairaj/tkmacosx/issues/19))

- [**v1.0.0**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v1.0.0)

  - Add Tests.
  - Add "-selectcolor" option to ColorVar list.
  - Reorganise tkmacosx package files into multiple packages.
  - Reorganise button items to a separate class.
  - Fix `Misc._configure()` returning 'NoneType'. ([#12](https://github.com/Saadmairaj/tkmacosx/issues/12))
  - Fix text misalignment when changed dynamically under certain situations.
  - Fix -activebackground" not accepting mac deafult system colors names.
  - Fix button appearance when toplevel is out of focus.
  - Fix `focusthickness=0` glitch of button.
  - Fix ColorVar not working with -focuscolor of button.
  - Fix unknown option "-bitmap". error
  - Fix "-width", "-height" have effect on 0 value.
  - Fix Marquee `cget()` issues.
  - Fix "-activebackground" not changing with Variable.
  - Fix ColorVar not working with few Button options.
  - Fix lag when Button is configured.
  - Fix an error with `Button.destroy()`. ([#17](https://github.com/Saadmairaj/tkmacosx/issues/17))

- [**v0.1.6**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.1.6)

  - Add new feature, _set image as background_ in Button widget.
  - Add new functions (_hex_to_rgb, check_light_dark_).
  - Add XView to Marquee widget.
  - Add Radiobutton widget and fix selectcolor issue. ([#11](https://github.com/Saadmairaj/tkmacosx/issues/11))
  - Reorganize properties of BaseButton class.
  - Fix broken links.
  - Fix anchor of Button widget. ([#7](https://github.com/Saadmairaj/tkmacosx/issues/7))
  - Fix focusring appearing for all CircleButton.
  - Fix activebackground and activeforeground of Radiobutton.
  - Remove colors.py file
  - Remove support for python 2.x.
  - Remove unnecessary code from multiple files.
  - Remove Information.md file.
  - Remove tkmacosx/README.md file.

- [**v0.1.5**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.1.5)

  - Add new [CircleButton Widget](#circlebutton-widget) widget.
  - Fix `["key"]` to `[key]` in Marquee.
  - Fix Colorvar not working with item of canvas in 0.1.4.
  - Fix Marquee.play(reset=True) to reset and play the text from beginning.
  - Fix focusthickness of button not working when set to 1.
  - Fix Image not showing when button is active.
  - Fix Text/Image/Bitmap bleed off the button widget.
  - Fix width or height of button widget not working with compound argument.

- [**v0.1.4**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.1.4)

  - Add new feature `"gradient"` to `Colorscale` widget.
  - Add new features to `Button` widget.
  - Add new `stop`, `play` and `reset` methods to Marquee.
  - Add new feature `avoidmousewheel` to SFrame.
  - Fix height not working with Button widget issue.
  - Fix `foreground` argument not working in Button widget.
  - Fix SFrame not autosizing according to widgets.
  - Redesign classes of widgets.
  - Remove large images.
  - Remove numpy and PIL dependencies.
  - Some other fixes and improvements.

- [**v0.1.3**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.1.3)

  - Fix `can't invoke "bindtags" command` error. ([#3](https://github.com/Saadmairaj/tkmacosx/issues/3))

- [**v0.1.2**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.1.2)

  - Add python 2.x support.
  - Fix half HEX issues. ([#6](https://github.com/Saadmairaj/tkmacosx/issues/6))

- [**v0.1.1**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.1.1)

  - Add `Marquee` widget.
  - `ColorVar` now works with `Canvas` items as well.
  - Fix `ColorVar` not working with the foreground of `tkmacosx.Button`.
  - Fix unnecessary `focus_set()` by `tkmacosx.Button`.
  - Fix issues with **main**.py file.
  - Fix issues with `SaveVar()`.

- [**v0.1.0**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.1.0)

  - Add `SaveVar()` function to save and load tkinter variable.
  - Fix colors import issue.

- [**v0.0.9**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.0.9)

  - Fix installation issues.

- **v0.0.8**

  - Fix installation issues.

- [**v0.0.7**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.0.7)

  - Change `eval()` with `ast.literal_eval()` in DictVar Variable
  - Fix colorscale issues.

- [**v0.0.6**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.0.6)

  - Add new style tkinter colorscale.

- [**v0.0.5**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.0.5)

  - Fix a bug where `borderless` for multiple buttons does not work properly.
  - Improve **init**.py file.

- [**v0.0.4**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.0.4)

  - Fix an import error.

- [**v0.0.3**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.0.3)

  - Add docstring.

- [**v0.0.2**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.0.2)

  - Fix an error running command `python -m tkmacosx`.

- [**v0.0.1**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.0.1)
  - Initial release.

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method of this repository before making a change.

Please make sure to update tests as appropriate.

## License

[Apache](https://github.com/Saadmairaj/tkmacosx/blob/master/LICENSE)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSaadmairaj%2Ftkmacosx.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FSaadmairaj%2Ftkmacosx?ref=badge_large)
