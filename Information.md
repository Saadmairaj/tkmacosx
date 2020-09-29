# tkmacosx

[![GitHub license](https://img.shields.io/github/license/Saadmairaj/tkmacosx.svg)](https://github.com/Saadmairaj/tkmacosx/blob/master/LICENSE)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Saadmairaj/tkmacosx.svg)](https://github.com/Saadmairaj/tkmacosx/issues)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Saadmairaj/tkmacosx/graphs/commit-activity)
[![PyPI version shields.io](https://img.shields.io/pypi/v/tkmacosx)](https://pypi.org/project/tkmacosx/)
[![Downloads](https://pepy.tech/badge/tkmacosx)](https://pepy.tech/project/tkmacosx)
[![Downloads](https://pepy.tech/badge/tkmacosx/month)](https://pepy.tech/project/tkmacosx/month)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#documentation-of-tkmacosx)
![Platform macos](https://camo.githubusercontent.com/88b2a6b3c5b17c76a81f26679c90eb0e35d58a20/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d4d61632d626c75652e737667)
![Platform linux](https://camo.githubusercontent.com/d770098cca195092547eb2141c36b0b37abe70c2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d4c696e75782d626c75652e737667)
![Platform windows](https://camo.githubusercontent.com/237ee2d8b515525d5b003c578459830c94de3285/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d57696e646f77732d626c75652e737667)

This module provides some modified widgets of Tkinter which works better on macOS and some more useful functions and classes as well. For example Button of tkmacosx which looks and feels exactly like a native tkinter button can change its _background_ and _foreground_ color on a mac and can do much more.

**Read more about all the classes and methods of tkmacosx on [tkmacosx documentation](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#documentation-of-tkmacosx).**

- [Button Widget](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#button-widget)
- [CircleButton Widget](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#circlebutton-widget)
- [SFrame Widget](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#sframe-widget)
- [Colorscale Widget](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#colorscale-widget)
- [Marquee Widget](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#marquee-widget)
- [ColorVar Variable](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#colorvar-variable)
- [DictVar Variable](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#dictvar-variable)
- [SaveVar](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#savevar)
- [get_shade](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#get_shade)
- [check_appearance](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#check_appearance)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [tkmacosx](https://pypi.org/project/tkmacosx/).

```bash
pip install tkmacosx
```

Or install the latest repo

```bash
pip install git+https://github.com/Saadmairaj/tkmacosx#egg=tkmacosx
```

## Usage

```python
from tkinter import *
from tkmacosx import Button, ColorVar, Marquee, Colorscale

root = Tk()
var = ColorVar(value='pink')
root['bg'] = var
m = Marquee(root, left_margin=30, bg= var, initial_delay=2000,
            text='Welcome to tkmacosx!! Slide the slider to change color :)')
m.pack(pady=(10,0))
b = Button(root, text='Button', borderless=1, fg=var, bg='black')
b.pack(pady=10)
c = Colorscale(root, variable=var, value='hex', height=25, mousewheel=0)
c.pack(pady=(0,10))

root.mainloop()
```

<p align="center"><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/sampleimage.png" height="250"></p>

## Demonstration

```bash
python -m tkmacosx
```

Run the above command in the terminal or command line after installing tkmacosx to see working and almost all the configurable options of different widgets of tkmacosx. Also if you want to style your button to stand out, scroll down to bottom and randomise or configure button to different styles your program.

Few sample of different styles of button.

<p align="center"><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/samplebutton1.gif"></p>

```python
Button(root, text='Button', activeforeground= '#EE3B3B', overrelief='flat', relief='flat', borderwidth=2,
    highlightthickness=1, font=font.Font(family='SignPainter', size=30, weight='bold', slant='roman'),
    focuscolor='#556B2F',highlightbackground='#CD5555', foreground='#1F1F1F', background='#7A7A7A',
    overbackground='#000000', overforeground='#00C78C', activebackground=('#BA55D3', '#D4D4D4'), borderless=1)
```

<p align="center"><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/samplebutton2.gif"></p>

```python
Button(root, text='Button', activeforeground= '#B5B5B5', overrelief='raised', relief='sunken', borderwidth=2,
    highlightthickness=4, font=font.Font(family='Brush Script MT', size=30, weight='bold', slant='roman'),
    focuscolor='#CD3700', highlightbackground='#AAAAAA', foreground='#6B6B6B', background='#BDBDBD',
    overbackground='#7A67EE', overforeground='#404040', activebackground=('#FF34B3', '#C1CDC1'), borderless=1)
```

<p align="center"><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/samplebutton3.gif"></p>

```python
Button(root, text='Button', activeforeground= '#FFDAB9', overrelief='flat', relief='raised', borderwidth=1,
    highlightthickness=3, font=font.Font(family='Helvetica', size=30,weight='bold', slant='roman', underline=1),
    focuscolor='#F5DEB3', highlightbackground='#8A360F',foreground='#FFC0CB', background='#708090',
    overbackground='#53868B', overforeground='#CCCCCC', activebackground=('#808069', '#C67171'), borderless=1)
```

## Documentation of tkmacosx

### Button Widget

The tkmacosx `Button` widget is alternative to tkinter's Button that supports all features on a macos that were not possible with tkinter Button like background, relief, overrelief, activebackground, and some other features can be set.

- **Argument:**

    Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values. All the options are pretty much the same as Tkinter [Button](https://effbot.org/tkinterbook/button.htm). Here are the extra options of tkmacosx Button.

  - `activebackground`: What background color to use when the button is active. The default is system specific. Give tuple of two colors for gradient effect in active background.
  - `activeforeground`: What foreground color to use when the button is active. The default is system specific.
  - `activeimage`: What Image to display when the button is active. No image to display by default.
  - `activebitmap`: What Bitmap to display when the button is active. No bitmap to display by default.
  - `bordercolor`: The color to use for the highlight border when the button does not have focus. The default is system specific. Same as **highlightbackground.**
  - `borderless`: Blend the button with it's parent's background results in a clean look with no square borders. It will change color automatically. The default is **False**.
  - `disabledbackground`: The color to use when the button is disabled. The default is system specific.
  - `focuscolor`: The color to use for the focus border when the button have focus. The default is system specific.
  - `focusthickness`: The width of the focus border. The default is system specific.
  - `height`: The height of the button. The size is given in **pixels**.
  - `state`: The button state: NORMAL, ACTIVE, PRESSED or DISABLED. Default is NORMAL.
  - `takefocus`: Indicates that the user can use the Tab key to move to this button. Default is an empty string, which means that the button accepts focus only if it has any keyboard bindings (default is on, in other words).
  - `overforeground`: Alternative foreground to use when the mouse is moved over the widget.
  - `overbackground`: Alternative background to use when the mouse is moved over the widget.
  - `width`: The width of the button. The size is given in **pixels**.

- **Usage:**

   ```python
   from tkinter import *
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

   <p align="center"><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/Button.gif"></p>

### CircleButton Widget

***BETA-Disclaimer:*** *Please note that this is a BETA version. Issues can be reported [here](https://github.com/Saadmairaj/tkmacosx/issues/new/choose).*

Circle shaped tkinter Button can contain text or images, and you can associate a Python function or method with each button. There is a blue focus ring that tells if the button has the focus or not to disable or hide the focus ring, either set `takefocus=0` or `focuscolor=''`. The CircleButton widget supports all the configurable options of tkmacosx [Button](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#button-widget).

- **Argument:**
    Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values. All the options are pretty much the same as tkmaocsx [Button](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#button-widget).

  - `radius`: Set the size of the button using radius **(in pixels)**. If width or height are given then radius value gets cancelled out.

- **Usage:**

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

   <p align="center"><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/CircleButton.gif"></p>

### SFrame Widget

The tkmacosx `SFrame` widget is just like a tkinter Frame but can be vertically scrolled. The SFrame supports intelligent mousewheel scrolling where it let you use mousewheel with other children widgets also having mousewheel scrolling without interfering with other widgets scrolling, a list of widgets having mousewheel scrolling can be passed to `avoidmousewheel` argument *(ex: `avoidmousewheel=(text1, text2, sframe)` or just one `avoidmousewheel=text2`).*

- **Arguments:**

   Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values. All the options are pretty much the same as Tkinter [Frame](https://effbot.org/tkinterbook/frame.htm). Here are the extra options of tkmacosx SFrame.

  - `scrollbarwidth`: Set the width of scrollbar.
  - `mousewheel`: Set mousewheel scrolling.
  - `avoidmousewheel`: Give widgets that also have mousewheel scrolling and is a child of SFrame this will configure widgets to support their mousewheel scrolling as well. For eg:- Text widget inside SFrame can have mousewheel scrolling as well as SFrame.
  
- **Usage:**

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

   <p align="center"><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/SFrame.gif"></p>

### Colorscale Widget

Colorscale is a new style color selector which is an alternate to tkinter's colorchooser.

- **Arguments:**

  - `value`: Get either 'RGB' or 'HEX'. By deafult is hex.
  - `command`: A function or method with a parameter that is called when the slider is moved or scrolled and an argument is paased to the callback. The callback can be a function, bound method, or any other callable Python object. If this option is not used, nothing will happen when the slider is moved.
  - `orient`: Set the orientation (vertical, horizontal). By default is vertical.
  - `mousewheel`: Move the slider with mousewheel with True. By default the option is set False.
  - `variable`: Associates a Tkinter variable (usually a `StringVar`, `ColorVar`). If the slider is moved the value of variable changes as well.
  - `showinfo`: Shows hex or rbg while selecting color.
  - `showinfodelay`: Delay before the show info disappears (in ms).
  - `gradient`: Takes tuple of two colors. Two colors are required to form a gradient. By default is complete color gradient.

- **Usage:**

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
    <img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/Colorscale.gif">
  </p>

### Marquee Widget

Use `Marquee` for creating scrolling text which moves from right to left only if the text does not fit completely on the window.

- **Arguments:**

  - `text`: Give a string to display.
  - `font`: Font of the text.
  - `fg`: Set foreground color of the text.
  - `fps`: Set fps(frames per seconds).
  - `left_margin`: Set left margin to make text move further to right before reset.
  - `initial_delay`: Delay before text start to move. *(in ms)*
  - `end_delay`: Delay before text reset. *(in ms)*
  - `smoothness`: Set the smoothness of the animation.

- **Usage:**

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
    <img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/Marquee.gif">
  </p>

### ColorVar Variable

ColorVar of tkmacosx set same color to each widget it is assigned to. As ColorVar is a tkinter variable wrapper so it will change the color of widgets whenever the change is made to ColorVar instances. ColorVar takes HEX values and all the color names which tkinter supports but the `get()` method returns only the HEX value. It will work with all of the following keyword arguments of different widgets *(eg:- `Canvas`, `Frame`, `Button`, `Label`, Canvas items, ...)*. ***'fg', 'foreground', 'bg', 'background', 'activebackground', 'activeforeground', 'disabledforeground', 'highlightbackground', 'highlightcolor', 'selectforeground', 'readonlybackground', 'selectbackground', 'insertbackground', 'disabledbackground', 'activefill', 'activeoutline', 'disabledfill','disabledoutline', 'fill', 'outline'*** *(might work with more but have not tested).*
  
- **Usage:**

   ```python
   from tkinter import Tk, Label
   from tkmacosx import colors, ColorVar, Button, gradient

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
    <img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/Colorvar.gif">
  </p>

### DictVar Variable

DictVar of tkmacosx stores python dictionary. It is very similar to tkinter `StringVar` with few modifications to it. `DictVar.get()` returns an instance of `dict` type whereas StringVar returns `str` type also DictVar method `get()` is a bit different `get(key=None, d=None)` get a key from `get()` method if `key=None` it will return the complete dictionary.

- **Usage:**

   ```python
   from tkinter import *
   from tkmacosx import DictVar

   root = Tk()
   dictionary = DictVar(value = {'width': 100, 'height': 200})

   print(type(dictionary.get()))
   print(dictionary.get())
   print(dictionary.get('width'))
   ```

### SaveVar

SaveVar of tkmacosx will let you save and load values of tkinter variables (`StringVar`, `IntVar`, ..). SaveVar uses pickle module to save values of variables into a file and when the program is executed next time, it will load the same values as they were last time. If the content of the .py file changes, it might not load correct values to the assigned variables. To avoid this issue use `name` argument to refer to the exact assigned values later.

- **Arguments:**

  - `var`: Give the `tkinter.Variable` class like (`tk.StringVar`, `tk.IntVar`).
  - `master`: Parent widget.
  - `value`: Set value.
  - `name`: Set a name to group variables or to refer to assigned value when loaded.
  - `filename`: Set the name of the save file. (To make the file invisible in the directory start the name of the file with "." like ".cache-savevar")

- **Usage:**

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

### get_shade

Darken or Lighten a shade of color.

- **Arguments:**

  - `color`: Give a color as either HEX or name of the color.
  - `shade`: The amount of change required. Takes float. eg: shade=0.225.
  - `mode`: `'-'` for darker shade, `'+'` for lighter shade, `'auto-110'` automatically decide lighter or darker. Where 110 is the intensity.

### check_appearance

Checks DARK/LIGHT mode of macOS and returns boolean value. Other settings can also be checked with this function just by passing a different command line argument to check a particular setting to `cmd` parameter of `check_appearance`.

- **Arguments:**

  - `cmd`: Give commands. Like to check DARK/LIGHT mode the command is `'defaults read -g AppleInterfaceStyle'`

## Changelog

- **0.1.5**
  - Add new [CircleButton Widget](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#circlebutton-widget) widget.
  - Fix ["key"] to [key] in Marquee.
  - Fix Colorvar not working with item of canvas in 0.1.4.
  - Fix Marquee.play(reset=True) to reset and play the text from begining.
  - Fix focusthickness of button not working when set to 1.
  - Fix Image not showing when button is active.
  - Fix Text/Image/Bitmap bleed off the button widget.
  - Fix width or height of button widget not working with compound argument.

- **0.1.4**
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

- **0.1.3**
  - Fix `can't invoke "bindtags" command` error.

- **0.1.2**
  - Add python 2.x support.
  - Fix half HEX issues.

- **0.1.1**
  - Add `Marquee` widget.
  - `ColorVar` now works with `Canvas` items as well.
  - Fix `ColorVar` not working with the foreground of `tkmacosx.Button`.
  - Fix unnecessary `focus_set()` by `tkmacosx.Button`.
  - Fix issues with __main__.py file.
  - Fix issues with `SaveVar()`.

- **0.1.0**
  - Add `SaveVar()` funtion to save and load tkinter variable.
  - Fix colors import issue.

- **0.0.8 & 0.0.9**
  - Fix installation issues.

- **0.0.7**
  - Change `eval()` with `ast.literal_eval()` in DictVar Variable
  - Fix colorscale issues.

- **0.0.6**
  - Add new style tkinter colorscale.

- **0.0.5**
  - Fix a bug where `borderless` for multiple buttons does not work properly.
  - Improve __init__.py file.

- **0.0.4**
  - Fix an import error.

- **0.0.3**
  - Add docstring.

- **0.0.2**
  - Fix an error running command `python -m tkmacosx` .

- **0.0.1**
  - First import.
