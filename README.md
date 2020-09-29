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

Run the above command in the terminal or command line after installing tkmacosx to see working and almost all the configurable options of different widgets of tkmacosx. 

<p align='center'><img src="https://raw.githubusercontent.com/Saadmairaj/tkmacosx/master/assets/demonstration.gif" height="600"></p>

Also if you want to style your button to stand out, scroll down to bottom of the window opened from the above command and randomise or configure button to different styles.

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

## [Changelog](https://github.com/Saadmairaj/tkmacosx/blob/master/Information.md#changelog)

View the changes of the repository [here.](https://github.com/Saadmairaj/tkmacosx/blob/master/Information.md#changelog)

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method of this repository before making a change.

Please make sure to update tests as appropriate.

## License

[Apache](https://github.com/Saadmairaj/tkmacosx/blob/master/LICENSE)
