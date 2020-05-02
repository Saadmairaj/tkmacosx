# tkmacosx

This module provides some modified widgets of Tkinter which works better on macOS and some more useful functions and classes as well. For example Button of tkmacosx which looks and feels exaclty like a native tkinter button can change its *background* and *foreground* colors on a mac.

## Installation

```bash
pip install tkmacosx
```

## Usage

```python
from tkinter import *
from tkmacosx import SFrame, Button

root = Tk()
frame = SFrame(root, bg='pink')
frame.pack()

for i in range(50):
    b = Button(frame, text='Button %s'%i, borderless=1)
    b.pack()

root.mainloop()
```

## Demonstration

```bash
python -m tkmacosx
```

## Widgets

### Button Widget

The tkmacosx `Button` widget is similar to defualt tkinter `Button` but supports all arguments of on a macos inclucding some extra features.

- **Argument:**

    Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values. All the options are pretty much the same as Tkinter [Button](https://effbot.org/tkinterbook/button.htm). Here are the extra options of tkmacosx Button.

  - `activebackground`: Background color to use when the button is active. Give tuple of two colors for gradient effect in active background.
  - `activeimage`: Image to use when the button is active.
  - `activebitmap`: Bitmap to use when the button is active.
  - `bordercolor`: The color of the button border.
  - `borderless`: Blend the button with it's parent's background results in a clean look with no square borders. It will change color automatically.
  - `disabledbackground`: The color to use when the button is disabled.

- **Usage:**

   ```python
   from tkinter import *
   from tkmacosx import Button

   root = Tk()

   B1 = Button(root, text='Mac OSX', bg='lightblue', fg='yellow', borderless=1)
   B1.pack()

   root.mainloop()
   ```

### SFrame Widget

The tkmacosx `SFrame` widget is just like a tkinter Frame but vertically scrollable.

- **Arguments:**

   Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values. All the options are pretty much the same as Tkinter [Frame](https://effbot.org/tkinterbook/frame.htm). Here are the extra options of tkmacosx SFrame.

  - `scrollbarwidth`: Set the width of scrollbar.
  - `mousewheel`: Set mousewheel scrolling.
  
- **Usage:**

   ```python
   from tkinter import *
   from tkmacosx import SFrame

   root = Tk()
   frame = SFrame(root, bg='pink')
   frame.pack()

   for i in range(50):
      Button(frame, text='Button %s'%i).pack()

   root.mainloop()
   ```

### Colorscale

Colorscale is a new style color selector which is an alternate to tkinter's colorchooser.

- **Arguments:**

  - `value`: Get either 'RGB' or 'HEX'.
  - `command`: callback function with an argument.
  - `orient`: Set the orientation.
  - `mousewheel`: Set mousewheel to scroll the marker.
  - `variable`: Give tkinter variable (`StringVar`).
  - `showinfo`: Shows hex or rbg while selecting color.
  - `showinfodelay`: Delay before the showinfo disappears (in ms).

- **Usage:**

    ```python
   from tkinter import *
   from tkmacosx import Colorscale

   root = Tk()
   CS = Colorscale(root, value='hex')
   CS.pack(side="bottom", padx=3, pady=3)

   root.mainloop()
   ```

## Variables

### ColorVar Variable

ColorVar of tkmacosx set same color to each widget it is assigned to. As ColorVar is a tkinter variable wrapper so it will change the color of widgets whenever the change is made to ColorVar instances. ColorVar takes HEX values or all the color names which tkinter supports and the `get()` method returns only the HEX value. It will work with all of the following keyword arguments of diffenert widgets. ***'fg', 'foreground', 'bg', 'background', 'activebackground', 'activeforeground', 'disabledforeground', 'highlightbackground', 'highlightcolor', 'selectforeground', 'readonlybackground', 'selectbackground', 'insertbackground', 'disabledbackground'*** *(might work with more but have not tested).*
  
- **Usage:**

   ```python
   from tkinter import Tk, Label
   from tkmacosx import colors, ColorVar

   root = Tk()
   root.geometry('100x100')

   color = ColorVar()
   color_list = list(colors.OrderedHex)
   L = Label(root, textvariable=color, bg=color)
   L.place(relx=0.5, rely=0.5, anchor='center')

   def change_color(c=0):
      if c >= len(color_list): c=0
      color.set(color_list[c])
      root.after(70, change_color, c+1)

   change_color()
   root.mainloop()
   ```

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

## Changelog

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
