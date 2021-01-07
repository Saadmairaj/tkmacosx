# tkmacosx

[![PyPI version shields.io](https://img.shields.io/pypi/v/tkmacosx)](https://pypi.org/project/tkmacosx/)
[![CodeFactor](https://www.codefactor.io/repository/github/saadmairaj/tkmacosx/badge)](https://www.codefactor.io/repository/github/saadmairaj/tkmacosx)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Saadmairaj/tkmacosx/graphs/commit-activity)
[![Downloads](https://static.pepy.tech/personalized-badge/tkmacosx?period=total&units=international_system&left_color=lightgrey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/tkmacosx)
[![Downloads](https://static.pepy.tech/personalized-badge/tkmacosx?period=month&units=none&left_color=grey&right_color=blue&left_text=Downloads/Month)](https://pepy.tech/project/tkmacosx)
[![GitHub license](https://img.shields.io/github/license/Saadmairaj/tkmacosx.svg)](https://github.com/Saadmairaj/tkmacosx/blob/master/LICENSE)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Saadmairaj/tkmacosx.svg)](https://github.com/Saadmairaj/tkmacosx/issues?q=is%3Aissue+is%3Aclosed)
[![Anaconda-Server Badge](https://anaconda.org/saad_7/tkmacosx/badges/installer/conda.svg)](https://conda.anaconda.org/saad_7)
![PowerShell Gallery](https://img.shields.io/powershellgallery/p/Pester?color=blue)

This module provides some modified widgets of Tkinter which fixes many issues with widgets not working properly on macOS platform. For example Button of tkmacosx which looks and feels exactly like a native Tkinter button can change its _background_ and _foreground_ color and has a lot more functionality, Issues with Radiobutton are also fixed with this library. The library also offers some more useful functionality.

**Read more about all the classes and methods in the [tkmacosx documentation](#documentation).**

Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Demonstration](#demonstration)
4. [Documentation](#documentation)
   - [4.1. Button Widget](#button-widget)
   - [4.2. CircleButton Widget](#circlebutton-widget)
   - [4.3. SFrame Widget](#sframe-widget)
   - [4.4. Colorscale Widget](#colorscale-widget)
   - [4.5. Marquee Widget](#marquee-widget)
   - [4.6. Radiobutton Widget](#radiobutton-widget)
   - [4.7. ColorVar Variable](#colorvar-variable)
   - [4.8. DictVar Variable](#dictvar-variable)
   - [4.9. SaveVar](#savevar)
   - [4.10. get_shade](#get_shade)
   - [4.11. check_appearance](#check_appearance)
   - [4.12. check_light_dark](#check_light_dark)
   - [4.13. gradient](#gradient)
5. [Changelog](#changelog)
6. [License](#license)

## Requirements

- Python 3

Python packages:

- tkinter *(included in the python distribution)*
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

Or even select a specific revision *(branch/tag/commit)*:

```bash
pip install git+https://github.com/Saadmairaj/tkmacosx@master
```

Similarly, for tag specify [tag](https://github.com/Saadmairaj/tkmacosx/tags) with `@v0.x.x`. For example to download tag v0.1.0 from Git use:

```bash
pip install git+https://github.com/Saadmairaj/tkmacosx@v0.1.0
```

If you use [Anaconda](https://www.anaconda.com/products/individual) environment then you could run:

```bash
conda install -c saad_7 tkmacosx 
```

## Demonstration

```bash
python -m tkmacosx
```

Run the above command in the terminal or command line after installing tkmacosx to see working and almost all the configurable options of different widgets of tkmacosx.

<p align='center'><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/demonstration.gif" height="500"></p>

Also if you want to style your button to stand out, scroll down to bottom of the window opened from the above command and randomise or configure button to different styles.

## Documentation

### Button Widget

The tkmacosx `Button` widget is alternative to tkinter's Button that supports all features on a macos that were not possible with tkinter Button like background, relief, overrelief, activebackground, and some other features can be set. There is a blue focus ring that tells if the button has the focus or not to disable or hide the focus ring, either set `takefocus=0` or `focuscolor=''`.

- Configurable options for a button widget. Syntax: `Button(root, options=value, ...)`

    | Options               	| Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            	|
    |-----------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *activebackground*    	| What background color to use when the button is active. The default is system specific. Give tuple of two colors for gradient effect in active background.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             	|
    | *activeforeground*    	| What foreground color to use when the button is active. The default is system specific.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                	|
    | *activeimage*         	| What Image to display when the button is active. No image to display by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       	|
    | *activebitmap*        	| What Bitmap to display when the button is active. No bitmap to display by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     	|
    | *anchor*              	| Where the text is positioned on the button. For example, `anchor=tk.NE` would position the text at the top right corner of the button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 	|
    | *bordercolor*         	| The color to use for the highlight border when the button does not have focus. The default is system-specific. Same as highlightbackground.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            	|
    | *borderless*          	| Blend the button with its parent's background results in a clean look with no square borders. It will change color automatically. The default is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                	|
    | *bd or borderwidth*   	| Width of the border around the outside of the button. The default is two pixels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       	|
    | *bg or background*    	| Normal background color.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	|
    | *command*             	| Function or method to be called when the button is clicked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            	|
    | *cursor*              	| Selects the cursor to be shown when the mouse is over the button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      	|
    | *disabledforeground*  	| The color to use when the button is disabled. The default is system specific.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          	|
    | *focuscolor*          	| The color to use for the focus border when the button have focus. The default is system specific.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      	|
    | *focusthickness*      	| The width of the focus border *(pixels)*. The default is system specific.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              	|
    | *fg or foreground*    	| Normal foreground (text) color.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        	|
    | *font*                	| Text font to be used for the button's label.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           	|
    | *height*              	| The height of the button. The size is given in *pixels for both text and images.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      	|
    | *highlightbackground* 	| Color of the focus highlight when the widget does not have focus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      	|
    | *highlightcolor*      	| The color of the focus highlight when the widget has focus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            	|
    | *highlightthickness*  	| Thickness of the focus highlight.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      	|
    | *image*               	| Image to be displayed on the button (instead of text).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 	|
    | *justify*             	| How to show multiple text lines: `tk.LEFT` to left-justify each line; `tk.CENTER` to center them; or `tk.RIGHT` to right-justify.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      	|
    | *overbackground*      	| Alternative background to use when the mouse is moved over the widget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 	|
    | *overforeground*      	| Alternative foreground to use when the mouse is moved over the widget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 	|
    | *overrelief*          	| The relief style to be used while the mouse is on the button; the default relief is `tk.RAISED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       	|
    | *padx*                	| Additional padding left and right of the text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         	|
    | *pady*                	| Additional padding above and below the text.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           	|
    | *relief*              	| Specifies the relief type for the button. The default relief is `tk.RAISED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           	|
    | *repeatdelay*         	| See `repeatinterval`, below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           	|
    | *repeatinterval*      	| Normally, a button fires only once when the user releases the mouse button. If you want the button to fire at regular intervals as long as the mouse button is held down, set this option to a number of milliseconds to be used between repeats, and set the `repeatdelay` to the number of milliseconds to wait before starting to repeat. *For example, if you specify “ `repeatdelay=500`, `repeatinterval=100` ” the button will fire after half a second, and every tenth of a second thereafter, until the user releases the mouse button. If the user does not hold the mouse button down at least `repeatdelay` milliseconds, the button will fire normally.* 	|
    | *state*               	| Set this option to `"disabled"` to gray out the button and make it unresponsive. Has the value `"active"` when the mouse is over it. Keep the button pressed with `"pressed"`. Default is `"normal"`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  	|
    | *takefocus*           	| Normally, keyboard focus does visit buttons, and a space character acts as the same as a mouse click, “pushing” the button. You can set the takefocus option to zero to prevent focus from visiting the button.                                                                                                                                                                                                                                                                                                                                                                                                                                                        	|
    | *text*                	| Text displayed on the button. Use internal newlines to display multiple text lines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    	|
    | *textvariable*        	| An instance of `StringVar()` that is associated with the text on this button. If the variable is changed, the new value will be displayed on the button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	|
    | *width*               	| The width of the button. The size is given in *pixels for both text and images.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       	|

- Methods on `Button` objects:

    | Methods     	| Description                                                                                                                                   	|
    |-------------	|-----------------------------------------------------------------------------------------------------------------------------------------------	|
    | *.invoke()* 	| Calls the button's command callback, and returns what that function returns. Has no effect if the button is disabled or there is no callback. 	|             

- **Example:**

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

   <p align="center">
      <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/Button.gif">
   </p>
 
 - Few sample of different styles of button that can be configured.

<p align="center"><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/samplebutton1.gif">
            <img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/samplebutton2.gif">
            <img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/samplebutton3.gif">
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

***BETA-Disclaimer:*** *Please note that this is a BETA version. Issues can be reported [here](https://github.com/Saadmairaj/tkmacosx/issues/new/choose).*

Circle shaped tkinter Button can contain text or images, and you can associate a Python function or method with each button. There is a blue focus ring that tells if the button has the focus or not to disable or hide the focus ring, either set `takefocus=0` or `focuscolor=''`. The CircleButton widget supports all the configurable options of tkmacosx [Button](#button-widget).

- Configurable options for a button widget. Syntax: `CircleButton(root, options=value, ...)`
    All the options are pretty much the same as tkmacosx [Button](#button-widget). Other options:
    
    | Options  	| Description                                                                                                               	|
    |----------	|---------------------------------------------------------------------------------------------------------------------------	|
    | *radius* 	| Set the size of the button using radius *(in pixels)*. If width or height are given then radius value gets cancelled out. 	|

- Methods on `CircleButton` objects:

    | Methods     	| Description                                                                                                                                   	|
    |-------------	|-----------------------------------------------------------------------------------------------------------------------------------------------	|
    | *.invoke()* 	| Calls the button's command callback, and returns what that function returns. Has no effect if the button is disabled or there is no callback. 	|
             

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
      <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/CircleButton.gif">
   </p>

---

### SFrame Widget

The tkmacosx `SFrame` widget is just like a tkinter Frame but can be vertically scrolled. The SFrame supports intelligent mousewheel scrolling where it let you use mousewheel with other children widgets also having mousewheel scrolling without interfering with other widgets scrolling, a list of widgets having mousewheel scrolling can be passed to `avoidmousewheel` argument *(ex: `avoidmousewheel=(text1, text2, sframe)` or just one `avoidmousewheel=text2`).*

- Configurable options for a sframe widget. Syntax: `SFrame(root, options=value, ...)`

    | Options               	| Description                                                                                                                                                                                                                                    	|
    |-----------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *avoidmousewheel*     	| Give widgets that also having the mousewheel scrolling and is a child of *SFrame*, this option will configure widgets to support their mousewheel scrolling as well and not interfere with *SFrame* mousewheel scrolling. *For example: Text widget inside SFrame can have mousewheel scrolling as well as SFrame.* 	|
    | *bg or background*    	| The frame's background color.                                                                                                                                                                                                                  	|
    | *bd or borderwidth*   	| Width of the frame's border. The default is 0 (no border).                                                                                                                                                                                     	|
    | *cursor*              	| The cursor used when the mouse is within the frame widget.                                                                                                                                                                                     	|
    | *height*              	| The vertical dimension of the new frame. This will be ignored unless you also call `.grid_propagate(0)` on the frame.                                                                                                                          	|
    | *highlightbackground* 	| Color of the focus highlight when the frame does not have focus.                                                                                                                                                                               	|
    | *highlightcolor*      	| Color is shown in the focus highlight when the frame has the focus.                                                                                                                                                                            	|
    | *highlightthickness*  	| The thickness of the focus highlight.                                                                                                                                                                                                          	|
    | *mousewheel*          	| Set mousewheel scrolling. The default is `False`                                                                                                                                                                                               	|
    | *padx*                	| Normally, a Frame fits tightly around its contents. To add *N* pixels of horizontal space inside the frame, set `padx=N`.                                                                                                                      	|
    | *pady*                	| Used to add vertical space inside a frame. See *padx* above.                                                                                                                                                                                   	|
    | *relief*              	| The default relief for a frame is *tk.FLAT*, which means the frame will blend in with its surroundings. To put a border around a frame, set its borderwidth to a positive value and set its relief to one of the standard relief types.        	|
    | *scrollbarwidth*      	| Set the width of scrollbar.                                                                                                                                                                                                                    	|
    | *takefocus*           	| Normally, frame widgets are not visited by input focus. However, you can set `takefocus=1` if you want the frame to receive keyboard input. To handle such input, you will need to create bindings for keyboard events.                        	|
    | *width*               	| The horizontal dimension of the new frame. This value be ignored unless you also call `.grid_propagate(0)` on the frame                                                                                                                        	|

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
      <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/SFrame.gif">
   </p>

---

### Colorscale Widget

Colorscale is a new style color selector which is an alternate to tkinter's colorchooser.

- Configurable options for a Colorscale widget. Syntax: `Colorscale(root, options=value, ...)`

    | Options               	| Description                                                                                                                                                                                                                                                                                       	|
    |-----------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *bd or borderwidth*   	| Width of the border around the outside of the *Colorscale*. The default is two pixels.                                                                                                                                                                                                            	|
    | *command*             	| A function or method with a parameter that is called when the slider is moved or scrolled and an argument is paased to the callback. The callback can be a function, bound method, or any other callable Python object. If this option is not used, nothing will happen when the slider is moved. 	|
    | *cursor*              	| Cursor used in the *Colorscale*.                                                                                                                                                                                                                                                                  	|
    | *gradient*            	| Takes tuple of two colors. Two colors are required to form a gradient (`sequence[FROM, TO]`, For example: A tuple of `tuple('white', 'black')` will create a *Colorscale* from *WHITE* to *BLACK* color). By default is complete color gradient.                                                  	|
    | *height*              	| Size of the *Colorscale* in the Y dimension.                                                                                                                                                                                                                                                      	|
    | *highlightbackground* 	| Color of the focus highlight when the widget does not have focus.                                                                                                                                                                                                                                 	|
    | *highlightcolor*      	| Color is shown in the focus highlight.                                                                                                                                                                                                                                                            	|
    | *highlightthickness*  	| The thickness of the focus highlight. The default value is 1.                                                                                                                                                                                                                                     	|
    | *mousewheel*          	| Move the slider with mousewheel with *True.* By default the option is set *False.*                                                                                                                                                                                                                	|
    | *orient*              	| Set the orientation *(VERTICAL, HORIZONTAL)*. By default is VERTICAL.                                                                                                                                                                                                                             	|
    | *relief*              	| The relief style of the *Colorscale*. Default is tk.FLAT.                                                                                                                                                                                                                                         	|
    | *showinfo*            	| Shows hex or rbg while selecting color.                                                                                                                                                                                                                                                           	|
    | *showinfodelay*       	| Delay before the show info disappears *(in ms)*.                                                                                                                                                                                                                                                  	|
    | *takefocus*           	| Normally, focus will cycle through this widget with the tab key only if there are keyboard bindings set for it (see Section 54, “Events”for an overview of keyboard bindings). If you set this option to 1, the focus will always visit this widget. Set it to '' to get the default behavior.    	|
    | *value*               	| Get either 'RGB' or 'HEX'. By deafult is hex.                                                                                                                                                                                                                                                     	|
    | *variable*            	| Associates a Tkinter variable (usually a *tk.StringVar*, *tkm.ColorVar*). If the slider is moved the value of the variable changes as well.                                                                                                                                                       	|
    | *width*               	| Size of the *Colorscale* in the X dimension.                                                                                                                                                                                                                                                      	|

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
      <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/Colorscale.gif">
   </p>

---

### Marquee Widget

Use `Marquee` for creating scrolling text which moves from right to left only if the text does not fit completely on the window.

- Configurable options for a Marquee widget. Syntax: `Marquee(root, options=value, ...)`

    | Options               	| Description                                                                                                                                                                           	|
    |-----------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *bg or background*    	| The background color of the marquee area.                                                                                                                                             	|
    | *bd or borderwidth*   	| Width of the border around the marquee. The default value is two pixels.                                                                                                              	|
    | *cursor*              	| Cursor that appears when the mouse is over this marquee.                                                                                                                              	|
    | *font*                	| If you are displaying text in this marquee with the text option, the font option specifies in what font that text will be displayed.                                                  	|
    | *fg or foreground*    	| If you are displaying text in this marquee, this option specifies the color of the text.                                                                                              	|
    | *height*              	| The height of the *Marquee* is in pixels. If this option is not set, the *Marquee* will be sized to fit its contents.                                                                 	|
    | *highlightbackground* 	| Color of the focus highlight when the widget does not have focus.                                                                                                                     	|
    | *highlightcolor*      	| The color of the focus highlight when the widget has focus.                                                                                                                           	|
    | *highlightthickness*  	| The thickness of the focus highlight.                                                                                                                                                 	|
    | *justify*             	| Specifies how multiple lines of text will be aligned with respect to each other: *tk.LEFT* for flush left, *tk.CENTER* for centered (the default), or *tk.RIGHT* for right-justified. 	|
    | *relief*              	| Specifies the appearance of a decorative border around the *Marquee*. The default is *tk.FLAT*; for other values.                                                                     	|
    | *state*               	| By default, a *Marquee* widget is in the *tk.NORMAL* state. Set this option to *tk.DISABLED* to make it unresponsive to mouse events.                                                 	|
    | *takefocus*           	| Normally, focus does not cycle through *Marquee* widgets. If you want this widget to be visited by the focus, set `takefocus=1`.                                                      	|
    | *text*                	| To display one or more lines of text in a *Marquee* widget, set this option to a string containing the text. Internal newlines ('\n') will force a line break.                        	|
    | *width*               	| The width of the *Marquee* is in pixels. If this option is not set, the *Marquee* will be sized to fit its contents.                                                                  	|

- Methods on `Marquee` widget objects:

    | Methods              	| Description                                                                                                                                   	|
    |----------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------	|
    | *.reset()*           	| Resets the position of the text to default.                                                                                                   	|
    | *.stop(reset: bool)* 	| Stops the moving text to the current position. Set parameter `reset=True` to stop the movement and reset the position of the text to default. 	|
    | *.play(reset: bool)* 	| Plays the stopped text from the current position. Set parameter `reset=True` to play from the default position.                               	|

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
      <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/Marquee.gif">
   </p>

---

### Radiobutton Widget

Radiobutton of tkmacosx are fixed from multiple issues i.e. background color not showing properly when `indicator=0`, *activebackground*, *activeforeground* options not working, few other issues are fixed in tkmacosx Radiobutton. Radiobuttons are sets of related widgets that allow the user to select only one of a set of choices. Each radiobutton consists of two parts, the *indicator* and the *label*.

- Configurable options for a Colorscale widget. Syntax: `Radiobutton(root, options=value, ...)`

    | Options               	| Description                                                                                                                                                                                                                                                                                                                                                                                                                          	|
    |-----------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *activebackground*    	| The background color when the mouse is over the radiobutton.                                                                                                                                                                                                                                                                                                                                                                         	|
    | *activeforeground*    	| The foreground color when the mouse is over the radiobutton.                                                                                                                                                                                                                                                                                                                                                                         	|
    | *anchor*              	| If the widget inhabits a space larger than it needs, this option specifies where the radiobutton will sit in that space. The default is `anchor=tk.CENTER`. For other positioning options. For example, if you set `anchor=tk.NE`, the radiobutton will be placed in the top right corner of the available space.                                                                                                                    	|
    | *bg or background*    	| The normal background  color behind the indicator and label.                                                                                                                                                                                                                                                                                                                                                                         	|
    | *bitmap*              	| To display a monochrome image on a radiobutton, set this option to a bitmap.                                                                                                                                                                                                                                                                                                                                                         	|
    | *bd or borderwidth*   	| The size of the border around the indicator part itself. Default is two pixels.                                                                                                                                                                                                                                                                                                                                                      	|
    | *command*             	| A procedure to be called every time the user changes the state of this radiobutton.                                                                                                                                                                                                                                                                                                                                                  	|
    | *compound*            	| If you specify both text and a graphic (either a bitmap or an image), this option specifies where the graphic appears relative to the text. Possible values are *tk.NONE* (the default value), *tk.TOP*, *tk.BOTTOM*, *tk.LEFT*, *tk.RIGHT*, and *tk.CENTER*. For example, `compound=tk.BOTTOM` would position the graphic below the text. If you specify `compound=tk.NONE`, the graphic is displayed but the text (if any) is not. 	|
    | *cursor*              	| If you set this option to a cursor name, the mouse cursor will change to that pattern when it is over the radiobutton.                                                                                                                                                                                                                                                                                                               	|
    | *disabledforeground*  	| The foreground color used to render the text of a disabled radiobutton. The default is a stippled version of the default foreground color.                                                                                                                                                                                                                                                                                           	|
    | *font*                	| The font used for the text.                                                                                                                                                                                                                                                                                                                                                                                                          	|
    | *fg or foreground*    	| The color used to render the text.                                                                                                                                                                                                                                                                                                                                                                                                   	|
    | *height*              	| The number of lines (not pixels) of text on the radiobutton. Default is 1.                                                                                                                                                                                                                                                                                                                                                           	|
    | *highlightbackground* 	| The color of the focus highlight when the radiobutton does not have focus.                                                                                                                                                                                                                                                                                                                                                           	|
    | *highlightcolor*      	| The color of the focus highlight when the radiobutton has the focus.                                                                                                                                                                                                                                                                                                                                                                 	|
    | *highlightthickness*  	| The thickness of the focus highlight. Default is 1. Set `highlightthickness=0` to suppress the display of the focus highlight.                                                                                                                                                                                                                                                                                                       	|
    | *image*               	| To display a graphic image instead of text for this radiobutton, set this option to an image object. The image appears when the radiobutton is not selected; compare selectimage, below.                                                                                                                                                                                                                                             	|
    | *inidicatoron*        	| Normally a radiobutton displays its indicator. If you set this option to zero, the indicator disappears, and the entire widget becomes a “push-push” button that looks raised when it is cleared and sunken when it is set. You may want to increase the borderwidth value to make it easier to see the state of such a control.                                                                                                     	|
    | *justify*             	| If the text contains multiple lines, this option controls how the text is justified: *tk.CENTER* (the default), *tk.LEFT*, or *tk.RIGHT*.                                                                                                                                                                                                                                                                                            	|
    | *offrelief*           	| If you suppress the indicator by asserting `indicatoron=False`, the offrelief option specifies the relief style to be displayed when the radiobutton is not selected. The default values is *tk.RAISED*.                                                                                                                                                                                                                             	|
    | *overrelief*          	| Specifies the relief style to be displayed when the mouse is over the radiobutton.                                                                                                                                                                                                                                                                                                                                                   	|
    | *padx*                	| How much space to leave to the left and right of the radiobutton and text. Default is 1.                                                                                                                                                                                                                                                                                                                                             	|
    | *pady*                	| How much space to leave above and below the radiobutton and text. Default is 1.                                                                                                                                                                                                                                                                                                                                                      	|
    | *relief*              	| By default, a radiobutton will have *tk.FLAT* relief, so it doesn't stand out from its background. You can also use `relief=tk.SOLID`, which displays a solid black frame around the radiobutton.                                                                                                                                                                                                                                    	|
    | *selectcolor*         	| The color of the radiobutton when it is set. Default is red.                                                                                                                                                                                                                                                                                                                                                                         	|
    | *selectimage*         	| If you are using the image option to display a graphic instead of text when the radiobutton is cleared, you can set the selectimage option to a different image that will be displayed when the radiobutton is set.                                                                                                                                                                                                                  	|
    | *state*               	| The default is `state=tk.NORMAL`, but you can set `state=tk.DISABLED` to gray out the control and make it unresponsive. If the cursor is currently over the radiobutton, the state is *tk.ACTIVE*.                                                                                                                                                                                                                                   	|
    | *takefocus*           	| By default, the input focus will pass through a radiobutton. If you set `takefocus=0`, focus will not visit this radiobutton.                                                                                                                                                                                                                                                                                                        	|
    | *text*                	| The label displayed next to the radiobutton. Use newlines ('\n') to display multiple lines of text.                                                                                                                                                                                                                                                                                                                                  	|
    | *textvariable*        	| If you need to change the label on a radiobutton during execution, create a StringVar to manage the current value, and set this option to that control variable. Whenever the control variable's value changes, the radiobutton's annotation will automatically change to that text as well.                                                                                                                                         	|
    | *underline*           	| With the default value of -1, none of the characters of the text label are underlined. Set this option to the index of a character in the text (counting from zero) to underline that character.                                                                                                                                                                                                                                     	|
    | *value*               	| When a radiobutton is turned on by the user, its control variable is set to its current valueoption. If the control variable is an IntVar, give each radiobutton in the group a different integer value option. If the control variable is a StringVar, give each radiobutton a different string value option.                                                                                                                       	|
    | *variable*            	| The control variable that this radiobutton shares with the other radiobuttons in the group. This can be either an *IntVar* or a *StringVar*.                                                                                                                                                                                                                                                                                         	|
    | *width*               	| The default width of a radiobutton is determined by the size of the displayed image or text. You can set this option to a number of characters ( not pixels) and the radiobutton will always have room for that many characters.                                                                                                                                                                                                     	|
    | *wraplength*          	| Normally, lines are not wrapped. You can set this option to a number of characters and all lines will be broken into pieces no longer than that number.                                                                                                                                                                                                                                                                              	|

- Methods on `Radiobutton` widget objects:

    | Methods       	| Description                                                                                                                   	|
    |---------------	|-------------------------------------------------------------------------------------------------------------------------------	|
    | *.deselect()* 	| Clears (turns off) the radiobutton.                                                                                           	|
    | *.flash()*    	| Flashes the radiobutton a few times between its active and normal colors, but leaves it the way it started.                   	|
    | *.invoke()*   	| You can call this method to get the same actions that would occur if the user clicked on the radiobutton to change its state. 	|
    | *.select()*   	| Sets (turns on) the radiobutton.                                                                                              	|

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
      <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/Radiobutton.gif">
    </p>

---

### ColorVar Variable

ColorVar of tkmacosx set same color to each widget it is assigned to. As ColorVar is a tkinter variable wrapper so it will change the color of widgets whenever the change is made to ColorVar instances. ColorVar takes HEX values and all the color names which tkinter supports but the `get()` method returns only the HEX value. It will work with all of the following keyword arguments of different widgets *(eg:- `Canvas`, `Frame`, `Button`, `Label`, Canvas items, ...)*. ***'fg', 'foreground', 'bg', 'background', 'activebackground', 'activeforeground', 'disabledforeground', 'highlightbackground', 'highlightcolor', 'selectforeground', 'readonlybackground', 'selectbackground', 'insertbackground', 'disabledbackground', 'activefill', 'activeoutline', 'disabledfill','disabledoutline', 'fill', 'outline'*** *(might work with more but have not tested).*

- Configurable options for a ColorVar variable. Syntax: `ColorVar(root, options=value, ...)`

    | Options 	| Description                                                                                                                                                  	|
    |---------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *value* 	| The value is an optional value (defaults to "").                                                                                                             	|
    | *name*  	| The name is an optional Tcl name (defaults to PY_VARnum). If *name* matches an existing variable and *value* is omitted then the existing value is retained. 	|

- Methods on `ColorVar` variable objects:

    | Methods           	| Description                                                                                                                                                	|
    |-------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *.get()*          	| Returns the current value of the variable.                                                                                                                 	|
    | *.set(value: str)* 	| Changes the current value of the variable. If any widget options are slaved to this variable, those widgets will be updated when the main loop next idles. 	|

- **Example:**

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
      <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/assets/Colorvar.gif">
   </p>

---

### DictVar Variable

DictVar of tkmacosx stores python dictionary. It is very similar to tkinter `StringVar` with few modifications to it. `DictVar.get()` returns an instance of `dict` type whereas StringVar returns `str` type also DictVar method `get()` is a bit different `get(key=None, d=None)` get a key from `get()` method if `key=None` it will return the complete dictionary.

- Configurable options for a DictVar variable. Syntax: `DictVar(root, options=value, ...)`

    | Options 	| Description                                                                                                                                                  	|
    |---------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *value* 	| The value is an optional value (defaults to {}).                                                                                                             	|
    | *name*  	| The name is an optional Tcl name (defaults to PY_VARnum). If *name* matches an existing variable and *value* is omitted then the existing value is retained. 	|

- Methods on `DictVar` variable objects:

    | Methods                            	| Description                                                                                                                                                	|
    |------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *.get(key: any=None, d: any=None)* 	| Returns the current value of the variable. To get a specific value of dictionary use `key`, give a default value to `d` if the `key` is not available.     	|
    | *set(value: str)*                  	| Changes the current value of the variable. If any widget options are slaved to this variable, those widgets will be updated when the main loop next idles. 	|

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

    | Parameters 	| Description                                                                                                                            	|
    |------------	|----------------------------------------------------------------------------------------------------------------------------------------	|
    | *var*      	| Give the `tkinter.Variable` class like (`tk.StringVar`, `tk.IntVar`)                                                                   	|
    | *master*   	| Parent widget.                                                                                                                         	|
    | *value*    	| The value is an optional value (Given variable's default value).                                                                       	|
    | *name*     	| Set a name to group variables or to refer to assigned value when loaded.                                                               	|
    | *filename* 	| Set the name of the save file. (To make the file invisible in the directory start the name of the file with "." like ".cache-savevar") 	|

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

    | Parameters 	| Description                                                                                                                                                                                                                                                                               	|
    |------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
    | *color*    	| Give a color as either HEX or name of the color.                                                                                                                                                                                                                                          	|
    | *shade*    	| The amount of change required. Takes float between 0.0 to 1.0 eg: `shade=0.225`.                                                                                                                                                                                                          	|
    | *mode*     	| Use mode for more control over the shade of the color. Use `mode='-'` for darker shade, use `mode='+'` for lighter shade, use `mode='auto'` to automatically decide the shade *(the deafult)*. To change the intensity of shade checking use `mode='auto-110` where 110 is the intensity. 	|

---

### check_appearance

Checks DARK/LIGHT mode of macOS and returns boolean value. Other settings can also be checked with this function just by passing a different command line argument to check a particular setting to `cmd` parameter of `check_appearance`.

- Configurable options for a check_appearance function. Syntax: `check_appearance(cmd='defaults read -g AppleInterfaceStyle')`.

    | Parameters 	| Description                                                                                                    	|
    |------------	|----------------------------------------------------------------------------------------------------------------	|
    | *cmd*      	| Give commands. *For example: To check DARK/LIGHT mode the command is `'defaults read -g AppleInterfaceStyle'.`* 	|

---

### check_light_dark

Tells if the given RGB or HEX code is lighter or darker shade of color. Returns `"black"` for darker shade and `"white"` for lighter shade.

- Configurable options for a check_light_dark function. Syntax: `check_light_dark(value, intensity=110)`.

    | Parameters 	| Description                                                                                                    	|
    |------------	|----------------------------------------------------------------------------------------------------------------	|
    | *value*     | Give sequence of RBG values or hexcode.                                                                      	  |
    | *intensity* | The measurable amount of a brightness. By deafult it is 110.                                                    |

---

### gradient

This function returns sequences of rainbow colors hexcodes in order.

- Configurable options for a gradient function. Syntax: `gradient(iteration)`.

    | Parameters 	| Description                                                                                                    	|
    |------------	|----------------------------------------------------------------------------------------------------------------	|
    | *iteration* | Length of the sequences.                                                                                        |

## Changelog

- [**v0.1.6**](https://github.com/Saadmairaj/tkmacosx/releases/tag/v0.1.6)
  - Add new feature, *set image as background* in Button widget.
  - Add new functions (*hex_to_rgb, check_light_dark*).
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
  - Fix issues with __main__.py file.
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
  - Improve __init__.py file.

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
