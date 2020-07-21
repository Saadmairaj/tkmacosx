# tkmacosx

This module provides some modified widgets of Tkinter which works better on macOS and some more useful functions and classes as well. For example Button of tkmacosx which looks and feels exactly like a native tkinter button can change its *background* and *foreground* color on a mac and can do much more.

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
<!-- https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/Button.gif -->
![](https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/sampleimage.png)

## Demonstration

```bash
python -m tkmacosx
```

<!-- ![](https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/demonstration.gif") -->


## Documentation of tkmacosx

### Button Widget

The tkmacosx `Button` widget is alternative to tkinter's Button that supports all features on a macos that were not possible with tkinter Button like background, relief, overrelief, activebackground, and some other features can be set.

- **Argument:**

    Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values. All the options are pretty much the same as Tkinter [Button](https://effbot.org/tkinterbook/button.htm). Here are the extra options of tkmacosx Button.

  - `activebackground`: What background color to use when the button is active. The default is system specific. Give tuple of two colors for gradient effect in active background.
  - `activebackground`: What foreground color to use when the button is active. The default is system specific.
  - `activeimage`: What Image to display when the button is active. No image to display by default.
  - `activebitmap`: What Bitmap to display when the button is active. No bitmap to display by default.
  - `bordercolor`: The color to use for the highlight border when the button does not have focus. The default is system specific. Same as **highlightbackground.**
  - `borderless`: Blend the button with it's parent's background results in a clean look with no square borders. It will change color automatically. The default is **False**.
  - `disabledbackground`: The color to use when the button is disabled. The default is system specific.
  - `focuscolor`: The color to use for the focus border when the button have focus. The default is system specific.
  - `focusthickness`: The width of the focus border. The default is system specific.
  - `state`: The button state: NORMAL, ACTIVE, PRESSED or DISABLED. Default is NORMAL.
  - `takefocus`: Indicates that the user can use the Tab key to move to this button. Default is an empty string, which means that the button accepts focus only if it has any keyboard bindings (default is on, in other words).
  - `overforeground`: Alternative foreground to use when the mouse is moved over the widget.
  - `overbackground`: Alternative background to use when the mouse is moved over the widget.

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

  ![](https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/Button.gif)

   <!-- <p align="center">
      <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/Button.gif">
   </p> -->

### SFrame Widget

The tkmacosx `SFrame` widget is just like a tkinter Frame but vertically scrollable.

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

  ![](https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/SFrame.gif)

   <!-- <p align="center">
      <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/SFrame.gif">
   </p> -->

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

  ![](https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/Colorscale.gif)

  <!-- <p align="center">
    <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/Colorscale.gif">
  </p> -->

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

  ![](https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/Marquee.gif)

  <!-- <p align="center">
    <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/Marquee.gif">
  </p> -->

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

  ![](https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/Colorvar.gif)

  <!-- <p align="center">
    <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/Colorvar.gif">
  </p> -->

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

- **0.1.4**
  - Added new feature `"gradient"` to `Colorscale` widget.
  - Added new features to `Button` widget.
  - Added new `stop`, `play` and `reset` methods to Marquee.
  - Added new feature `avoidmousewheel` to SFrame.
  - Fixed height not working with Button widget issue.
  - Fixed `foreground` argument not working in Button widget.
  - Fixed SFrame not autosizing according to widgets.
  - Redesign classes of widgets.
  - Removed large images.
  - Removed numpy and PIL dependencies.
  - Some other fixes and improvements.

- **0.1.3**
  - Fixed `can't invoke "bindtags" command` error.

- **0.1.2**
  - Added python 2.x support.
  - Fixed half HEX issues.

- **0.1.1**
  - Added `Marquee` widget.
  - `ColorVar` now works with `Canvas` items as well.
  - Fixed `ColorVar` not working with the foreground of `tkmacosx.Button`.
  - Fixed unnecessary `focus_set()` by `tkmacosx.Button`.
  - Fixed issues with __main__.py file.
  - Fixed issues with `SaveVar()`.

- **0.1.0**
  - Added `SaveVar()` funtion to save and load tkinter variable.
  - Fixed colors import issue.

- **0.0.8 & 0.0.9**
  - Fixed installation issues.

- **0.0.7**
  - Change `eval()` with `ast.literal_eval()` in DictVar Variable
  - Fixed colorscale issues.

- **0.0.6**
  - Added new style tkinter colorscale.

- **0.0.5**
  - Fixed a bug where `borderless` for multiple buttons does not work properly.
  - Improved __init__.py file.

- **0.0.4**
  - Fixed an import error.

- **0.0.3**
  - Added docstring.

- **0.0.2**
  - Fixed an error running command `python -m tkmacosx` .

- **0.0.1**
  - First import.
