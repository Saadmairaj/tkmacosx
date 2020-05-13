# tkmacosx

This module provides some modified widgets of Tkinter which works better on macOS and some more useful functions and classes as well. For example Button of tkmacosx which looks and feels exactly like a native tkinter button can change its *background* and *foreground* color on a mac and can do much more.

**Read more about all the classes and methods of tkmacosx on [tkmacosx documentation](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#documentation-of-tkmacosx).**

- [Button Widget](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx#button-widget)
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

<p align="center">
    <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/sampleimage.png" height="247" width="395">
</p>

## Demonstration

```bash
python -m tkmacosx
```

<p align="center">
    <img src="https://github.com/Saadmairaj/tkmacosx/blob/master/demonstration.gif" height="721" width="420">
</p>

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method of this repository before making a change.

Please make sure to update tests as appropriate.

## License

[Apache](https://github.com/Saadmairaj/tkmacosx/blob/master/LICENSE)
