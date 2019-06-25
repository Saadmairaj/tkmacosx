import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk
from tkmacosx.widget import *
from tkmacosx.variables import *
from tkmacosx.colorscale import Colorscale
from tkmacosx.colors import Hex as C_dict

def grid(root,row,column):
    "Defines rows and columns if grid method is used"
    if column:
        for y in range(column): tk.Grid.columnconfigure(root, y, weight=1)
    if row:
        for x in range(row): tk.Grid.rowconfigure(root, x, weight=1)
    return

class sample(tk.Tk):
    def __init__(self):
        super(sample, self).__init__()
        self.resizable(0,0)
        self.geometry('420x700+300+100')
        self.title('Mac OSX Button Testing')
        self.wm_attributes('-modified',1)
        self.main_color = ColorVar(value='#FFA69A')
        self['bg'] = self.main_color
        grid(self, 20, 5)
        self.L1 = tk.Label(self, text='Comparison', bg=self.main_color, font=('',18,'bold'))
        self.L1.grid(row=0, column=0, columnspan=5, sticky='nsew')
        Button(self, text='Hello').grid(row=1, column=1, sticky='s')
        ttk.Button(self, text='Hello').grid(row=1, column=3, sticky='s')
        tk.Button(self, text='Hello').grid(row=1, column=2, sticky='s')
        tk.Label(self, bg=self.main_color, font=('', 10),text='(Mac OSX)').grid(row=2, column=1, sticky='n',)
        tk.Label(self, bg=self.main_color, font=('', 10),text='(ttk themed)').grid(row=2, column=3, sticky='n')
        tk.Label(self, bg=self.main_color, font=('', 10),text='(Default)').grid(row=2, column=2, sticky='n')
        ttk.Separator(self, orient='vertical').grid(row=3, column=0, columnspan=5, sticky='ew')

        # ------------ Seperator -------------

        # ------------ Demonstration ------------

        self.sfr = SFrame(self, bg=self.main_color)
        self.sfr.grid(rowspan=16, columnspan=5, sticky='nsew')
        for i in range(5):
            self.sfr.grid_columnconfigure(i, weight=1)
        self.L2 = tk.Label(self.sfr, text='Demonstration', bg=self.main_color, font=('',20,'bold'))
        self.L2.grid(row=1, column=0, columnspan=5, sticky='new', pady=(20,10))

        # ------------ Active Color ------------
        
        self.L3 = tk.Label(self.sfr, text='1. Change Active color', bg=self.main_color, 
            font=('',15,'bold'))
        self.L3.grid(row=2, column=0, columnspan=5, sticky='nsew', pady=10)
        self.L4  =tk.Label(self.sfr, text='The active color can be changed to any gradient color.', 
            bg=self.main_color, font=('',10))
        self.L4.grid(row=3, column=0, columnspan=5, sticky='new')
        self.B1 = Button(self.sfr, text='Press Me', pady=20)
        self.B1.grid(row=4, column=0, columnspan=5, pady=20)
        self.C1 = tk.StringVar(value='Select')
        self.L5 = tk.Label(self.sfr, text='From', bg=self.main_color, font=('',12))
        self.L5.grid(row=5, column=1, sticky='nwe')
        self.Om1 = tk.OptionMenu(self.sfr, self.C1, *C_dict.keys(), 
            command=self.change_active_color)
        self.Om1.config(bg=self.main_color, width=15)
        self.Om1.grid(row=6, column=1,sticky='s', pady=(0,10))
        for i in range(self.Om1['menu'].index('end')+1):
            self.Om1['menu'].entryconfig(i, foreground=list(C_dict)[i])
        self.C2 = tk.StringVar(value='Select')
        self.L6 = tk.Label(self.sfr, text='To', bg=self.main_color, font=('',12))
        self.L6.grid(row=5, column=3, sticky='nwe')
        self.Om2 = tk.OptionMenu(self.sfr, self.C2, *C_dict.keys(), 
            command=self.change_active_color)
        self.Om2.config(bg=self.main_color, width=15)
        self.Om2.grid(row=6, column=3, sticky='s', pady=(0,10))
        for i in range(self.Om2['menu'].index('end')+1):
            self.Om2['menu'].entryconfig(i, foreground=list(C_dict)[i])
        

        # ------------ Backgroung Color ------------

        # ttk.Separator(self.sfr, orient='vertical').grid(row=6, column=2, columnspan=1, sticky='ew')
        self.L7 = tk.Label(self.sfr, text='2. Change Background color', bg=self.main_color, 
            font=('',15,'bold'))
        self.L7.grid(row=7, column=0, columnspan=5, sticky='nsew', pady=(50,0))
        self.L8  =tk.Label(self.sfr, text='Click on the button to choose the color.', 
            bg=self.main_color, font=('',10))
        self.L8.grid(row=8, column=0, columnspan=5, sticky='new', pady=10)

        self.B2 = Button(self.sfr, text='Color me', font=('',30,), pady=10, padx=10)
        self.B2.grid(row=9, column=0, columnspan=5, sticky='', pady=20)

        self.B3 = Button(self.sfr, text='Change Background Color', bg='#d0c0ea', borderless=1)
        self.B3['command'] = lambda: self.B2.config(bg=askcolor()[1])
        self.B3.grid(row=10, column=0, columnspan=5, sticky='w', pady=10)
        self.B4 = Button(self.sfr, text='Change Foreground Color', bg="#d0c0ea", borderless=1)
        self.B4['command'] = lambda: self.B2.config(fg=askcolor()[1])
        self.B4.grid(row=10, column=0, columnspan=5, sticky='e', pady=10)

        # ------------ Borderless ------------

        self.L9 = tk.Label(self.sfr, text='3. Switch Between Borderless', bg=self.main_color, 
            font=('',15,'bold'))
        self.L9.grid(row=11, column=0, columnspan=5, sticky='sew', pady=(50,0))
        self.L10 = tk.Label(self.sfr, text="""
    In borderless it will blend with its parent widget background color.
    Give parameter `borderless = True / False` to use it.""", bg=self.main_color, font=('',10))
        self.L10.grid(row=12, column=0, columnspan=5, sticky='new')

        self.B5 = Button(self.sfr, text='No Borders', borderless=1, height=40,
            bg='#212F3D', fg='white', activebackground=("#EAECEE", "#212F3D"))
        self.B5.grid(row=13, columnspan=5, pady=(20,5))

        self.B6 = Button(self.sfr, text='No Borders', borderless=1, height=40,
            bg='#F7DC6F', fg='#21618C', activebackground=('#B3B6B7','#58D68D'))
        self.B6.grid(row=14, columnspan=5, pady=(0,20))
        self.var1 = tk.BooleanVar(value=True)
        self.CB1 = tk.Checkbutton(self.sfr, text='Toggle Borderless',variable=self.var1, 
            bg=self.main_color, command=self.change_borderless_state)
        self.CB1.grid(row=15, columnspan=5, pady=(0,10))


        # ------------ Bordercolor ------------

        self.L11 = tk.Label(self.sfr, text='4. Change Bordercolor', bg=self.main_color, 
            font=('',15,'bold'))
        self.L11.grid(row=16, column=0, columnspan=5, sticky='sew', pady=(50,0))
        self.L12 = tk.Label(self.sfr, text="Change Bordercolor of the button\nNote: if borderless=True, then the bordercolor won't work.",
            bg=self.main_color, font=('',10))
        self.L12.grid(row=17, column=0, columnspan=5, sticky='new')

        self.B7 = Button(self.sfr, text='Border', pady=10, padx=5)
        self.B7.grid(row=18, columnspan=5, pady=30)

        self.B8 = Button(self.sfr, text='Change Bordercolor', borderless=1, bg="#d0c0ea") 
        self.B8['command']=lambda: self.B7.config(bordercolor=askcolor()[1])
        # self.B8.grid(row=19, columnspan=5)

        self.CS1 = Colorscale(self.sfr, value='hex', mousewheel=0,
            command=lambda e: self.B7.config(bordercolor=e))
        self.CS1.grid(row=19, columnspan=5, sticky='ew', padx=10)


        # ------------ Active Image and transparent Image ------------

        self.L11 = tk.Label(self.sfr, text='5. Active and Transparent Image', bg=self.main_color, 
            font=('',15,'bold'))
        self.L11.grid(row=20, column=0, columnspan=5, sticky='sew', pady=(50,0))
        self.L12 = tk.Label(self.sfr, text="Can pass activeimage to the button. Also it supports transparent images.",
            bg=self.main_color, font=('',10))
        self.L12.grid(row=21, column=0, columnspan=5, sticky='new')

        # from PIL import Image
        self.Img1 = Image.open(os.path.abspath(os.path.dirname(os.path.abspath(__file__))+'/images/B1.png'))
        self.Img_1 = ImageTk.PhotoImage(self.Img1.resize((200, 200), Image.ANTIALIAS))
        self.Img2 = Image.open(os.path.abspath(os.path.dirname(os.path.abspath(__file__))+'/images/B2.png'))
        self.Img_2 = ImageTk.PhotoImage(self.Img2.resize((200, 200), Image.ANTIALIAS))

        self.B10 = Button(self.sfr, image=self.Img_1, activeimage=self.Img_2, bg='#D7BDE2', 
            activebackground=('lightyellow','lightblue'), borderless=1)
        self.B10.grid(row=22, columnspan=5, pady=20)

        self.Scale1 = tk.Scale(self.sfr, orient='vertical', from_=100, to=300, bg=self.main_color, bd=0,
            command=lambda v: self.on_size_scale('vertical', v), troughcolor='#505452', font=('',10,'bold'),
            length=400, showvalue=0, width=10, sliderlength=60, resolution=50 )
        self.Scale1.bind('<Enter>', lambda _: self.Scale1.config(showvalue=1))
        self.Scale1.bind('<Leave>', lambda _: self.Scale1.config(showvalue=0))
        self.Scale1.grid(row=22, columnspan=5, sticky='w')
        self.Scale1.set(200)

    def change_active_color(self, *ags):
        c1 = self.C1.get() if not self.C1.get() == 'Select' else None
        c2 = self.C2.get() if not self.C2.get() == 'Select' else None
        self.Om1.config(bg=c1)
        self.Om2.config(bg=c2)
        self.B1['activebackground'] = (c1, c2)
    
    def change_borderless_state(self):
        if self.var1.get(): 
            self.B5['borderless'] = 1
            self.B6['borderless'] = 1
        else: 
            self.B5['borderless'] = 0
            self.B6['borderless'] = 0

    def on_size_scale(self, scale, value):
        value = int(float(value))
        if scale == 'vertical':
            self.Img_1 = ImageTk.PhotoImage(self.Img1.resize((value, value), Image.ANTIALIAS))
            self.Img_2 = ImageTk.PhotoImage(self.Img2.resize((value, value), Image.ANTIALIAS))
            self.B10['image'] = self.Img_1
            self.B10['activeimage'] = self.Img_2
        
        
#  Testing Demo 
if __name__ == "__main__":
    sample().mainloop()
