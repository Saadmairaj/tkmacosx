# tkmacosx

Tkmacosx is a Python library extension to Tkinter module for masOS. Read more about tkmacos in detail in [tkmacosx](https://github.com/Saadmairaj/tkmacosx/tree/master/tkmacosx)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tkmacosx.

```bash
pip install tkmacosx
```

## Usage
```
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

    python -m tkmacosx
    
    
## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method of this repository before making a change.

Please make sure to update tests as appropriate.

## License
    
[Apache](https://github.com/Saadmairaj/tkmacosx/blob/master/LICENSE)
