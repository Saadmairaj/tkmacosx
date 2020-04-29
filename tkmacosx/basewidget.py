from tkinter import ttk
import tkinter as _TK
import re
import subprocess

try: 
    import colour as C
except Exception as e:
    import sys, os
    import tkinter.messagebox as ms
    Error_win = _TK.Tk()
    Error_win.withdraw()
    message = """
    Module "tkmacosx" is dependent on 
    "colour" Module. 

    Do you want to install it with pip now?
    Or install it manually later.
    
    Link to the colour github:
    https://github.com/vaab/colour"""
    if ms._show(e, message, 'warning', 'yesno')=='yes':
        Error_win.destroy()
        os.system('pip install colour')
        import colour as C
    else: 
        sys.exit(0)


def check_appearence(cmd='defaults read -g AppleInterfaceStyle'):
    """### Checks DARK/LIGHT mode of macos. Returns Boolean.
    #### Args:
    - `cmd`: Give commands. Like to check DARK/LIGHT mode the command is `'defaults read -g AppleInterfaceStyle'` .
    """
    out, err = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True, shell=True).communicate()
    if out: return True
    elif err: return False


def get_shade(color, shade: float, mode='auto'):
    """### Darken or Lghten a shade of A HEX color.
    #### Args:
    1. `color`: Give a color as either HEX or name of the color.
    2. `shade`: The amount of change required. Takes float. eg: shade=0.225.
    3. `mode`: 
        - `'-'` for darker shade.
        - `'+'` for lighter shade.
        - `'auto-110'` automatically decide lighter or darker. where 110 is the intensity.
    
    return hexcode"""
    if isinstance( color, str ):
        if color.startswith('#'):
            Hex = color.lstrip('#')
            color = tuple( int(Hex[i:i+2], 16) for i in (0, 2, 4) )
        else:  
            tmp = _TK.Frame()
            r,g,b = tmp.winfo_rgb(color)
            tmp.destroy()
            color = (r/257, g/257, b/257)
    if 'auto' in mode:
        intensity = 110.0 if len(mode)<=4 else float(mode.split('-')[1])
        mode = '-' if float(color[0]*0.299 + color[1]*0.587 \
                        + color[2]*0.114) > intensity else '+'
    if mode == '+':
        R = float(color[0]*(1-shade) + shade*255) \
                if float(color[0]*(1-shade) + shade*255) > 0 else 0.0
        G = float(color[1]*(1-shade) + shade*255) \
                if float(color[1]*(1-shade) + shade*255) > 0 else 0.0
        B = float(color[2]*(1-shade) + shade*255) \
                if float(color[2]*(1-shade) + shade*255) > 0 else 0.0
    elif mode == '-':
        R = float(color[0]*(1-shade) - shade*255) \
                if float(color[0]*(1-shade) - shade*255) > 0 else 0.0
        G = float(color[1]*(1-shade) - shade*255) \
                if float(color[1]*(1-shade) - shade*255) > 0 else 0.0
        B = float(color[2]*(1-shade) - shade*255) \
                if float(color[2]*(1-shade) - shade*255) > 0 else 0.0
    else: raise ValueError ('Invalid mode "{}"'. format(mode))
    return '#%02x%02x%02x' % (int(R),int(G),int(B))  


class _Frame(_TK.BaseWidget):
    """Don't use this Frame widget. The widget has no geometry manager.
    
    It is used in SFrame widget to support screen."""
    def __init__(self, master=None, cnf={}, **kw):
        cnf = _TK._cnfmerge((cnf, kw))
        _TK.BaseWidget.__init__(self, master, 'frame', cnf, {})


class _Canvas(_TK.Widget):
    """Internal Class especially for Button widget"""
    def __init__(self, master=None, cnf={}, **kw):
        super(_Canvas, self).__init__(master, 'canvas', cnf, kw)
    
    def find(self, *args):
        """Internal function."""
        return self._getints(
            self.tk.call((self._w, 'find') + args)) or ()
    def bbox(self, *args):
        """Return a tuple of X1,Y1,X2,Y2 coordinates for a rectangle
        which encloses all items with tags specified as arguments."""
        return self._getints(
            self.tk.call((self._w, 'bbox') + args)) or None
    def coords(self, *args):
        """Return a list of coordinates for the item given in ARGS."""
        return [self.tk.getdouble(x) for x in
                           self.tk.splitlist(
                   self.tk.call((self._w, 'coords') + args))]
    def _create(self, itemType, args, kw): # Args: (val, val, ..., cnf={})
        """Internal function."""
        args = _TK._flatten(args)
        cnf = args[-1]
        if isinstance(cnf, (dict, tuple)):
            args = args[:-1]
        else:
            cnf = {}
        return self.tk.getint(self.tk.call(
            self._w, 'create', itemType,
            *(args + self._options(cnf, kw))))
    def _arc(self, *args, **kw):
        """Create arc shaped region with coordinates x1,y1,x2,y2."""
        return self._create('arc', args, kw)
    def _bitmap(self, *args, **kw):
        """Create bitmap with coordinates x1,y1."""
        return self._create('bitmap', args, kw)
    def _image(self, *args, **kw):
        """Create image item with coordinates x1,y1."""
        return self._create('image', args, kw)
    def _line(self, *args, **kw):
        """Create line with coordinates x1,y1,...,xn,yn."""
        return self._create('line', args, kw)
    def _text(self, *args, **kw):
        """Create text with coordinates x1,y1."""
        return self._create('text', args, kw)
    def _rectangle(self, *args, **kw):
        """Create rectangle with coordinates x1,y1,x2,y2."""
        return self._create('rectangle', args, kw)
    def delete(self, *args):
        """Delete items identified by all tag or ids contained in ARGS."""
        self.tk.call((self._w, 'delete') + args)
    def itemcget(self, tagOrId, option):
        """Return the resource value for an OPTION for item TAGORID."""
        return self.tk.call(
            (self._w, 'itemcget') + (tagOrId, '-'+option))
    def itemconfigure(self, tagOrId, cnf=None, **kw):
        """Configure resources of an item TAGORID.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method without arguments.
        """
        return self._configure(('itemconfigure', tagOrId), cnf, kw)
    itemconfig = itemconfigure
    def tag_lower(self, *args):
        """Lower an item TAGORID given in ARGS
        (optional below another item)."""
        self.tk.call((self._w, 'lower') + args)
    lower = tag_lower
    def tag_raise(self, *args):
        """Raise an item TAGORID given in ARGS
        (optional above another item)."""
        self.tk.call((self._w, 'raise') + args)
    lift = tkraise = tag_raise
    def rounded_rect(self, x, y, w, h, c, tag1=None, tag2=None, **kw):
        'Internal function.'
        # Need fix to just have one tag to change the background color
        kw['extent'] = 90
        kw['style'] = 'arc'
        kw['outline'] = kw.pop('fill', 'black')
        if tag1: kw['tag'] = tag1
        self._arc(x,   y,   x+2*c,   y+2*c,   start= 90, **kw)
        self._arc(x+w-2*c, y+h-2*c, x+w, y+h, start=270, **kw)
        self._arc(x+w-2*c, y,   x+w, y+2*c,   start=  0, **kw)
        self._arc(x,   y+h-2*c, x+2*c,   y+h, start=180, **kw)
        kw.pop('extent', None)
        kw.pop('style', None)
        kw['fill'] = kw.pop('outline', None)
        if tag2: kw['tag'] = tag2
        self._line(x+c, y,   x+w-c, y    , **kw)
        self._line(x+c, y+h, x+w-c, y+h  , **kw)
        self._line(x,   y+c, x,     y+h-c, **kw)
        self._line(x+w, y+c, x+w,   y+h-c, **kw)
    def _rounded(self, x1, y1, x2, y2, r,**kw):
        self._arc(x1,  y1,  x1+r,   y1+r, start= 90, extent=90, style='pieslice', outline="", **kw)
        self._arc(x2-r-1, y1, x2-1, y1+r, start=  0, extent=90, style='pieslice', outline="", **kw)
        self._arc(x1, y2-r-1, x1+r, y2-1, start=180, extent=90, style='pieslice', outline="", **kw)
        self._arc(x2-r, y2-r, x2-1, y2-1, start=270, extent=90, style='pieslice', outline="", **kw)
        self._rectangle(x1+r/2, y1, x2-r/2, y2, width=0, **kw)
        self._rectangle(x1, y1+r/2, x2, y2-r/2, width=0, **kw)


class Widget(_Canvas):
    """Internal class used for tkinter macos Buttton"""

    _buttons = []  # list of all buttons
    _features =  [  'activebackground', 'activeforeground', 'activeimage', 'activebitmap', 'anchor', 'bitmap', 
                    'borderwidth', 'bd', 'bordercolor', 'borderless', 'command', 'compound', 'disabledforeground', 
                    'disabledbackground', 'fg', 'font', 'foreground', 'height', 'image', 'overrelief', 'padx', 
                    'pady', 'repeatdelay', 'repeatinterval', 'text', 'textvariable', 'underline', 'width' ]

    def __init__(self, master=None, cnf={}, **kw):
        kw = _TK._cnfmerge( (cnf, kw) )
        kw = { k:v for k,v in kw.items() if v is not None }
        self.stopped = None
        self.cnf = {}
        for i in kw.copy().keys():
            if i in self._features: self.cnf[i] = kw.pop(i, None)

        self.cnf['fg'] = self.cnf.get('fg') if self.cnf.get('fg', None) else self.cnf.get('foreground','black')
        self.cnf['bd'] = self.cnf.get('bd') if self.cnf.get('bd', None) else self.cnf.get('borderwidth',6)
        self.cnf['borderless'] = self.cnf.get('borderless', False)
        self.cnf['disabledforeground'] = self.cnf.get('disabledforeground', 'grey')
        if self.cnf.get('textvariable') is not None: self.cnf['text'] = self.cnf['textvariable'].get()
        self.cnf['anchor'] = self.cnf.get('anchor', 'center')

        kw['takefocus'] = kw.get('takefocus', 1)
        kw['highlightthickness'] = kw.get('highlightthickness', 0)
        kw['width'] = kw.get('width', 87)
        kw['height'] = kw.get('height', 24)

        super(Widget, self).__init__(master=master, **kw)
        self._buttons.append(self)
        self._size = (self.winfo_width(), self.winfo_height())
        if self.cnf.get('text'): self._text(0,0,text=None, tag='_txt')
        if self.cnf.get('image'): self._image(0,0,image=None, tag='_img')
        elif self.cnf.get('bitmap'): self._bitmap(0,0,image=None, tag='_bit')
        self.bind_class('button_release', '<ButtonRelease-1>', self.on_release, '+')
        self.bind_class('button_press', '<Button-1>', self.on_press, '+' )
        self.bind_class('set_size', '<Configure>', self._set_size, '+')
        self.original_bg = self['bg']

        #  Focus in and out effect 
        main_win =  self.winfo_toplevel()
        def _chngIn(evt):
            if self.focus_get() is None:
                color = get_shade(self['bg'], 0.04, 'auto-120')
                self.itemconfig('_border1', outline=color)
                self.itemconfig('_border2', fill=color)
            if self.focus_get() and get_shade(self['bg'], 0.04, 'auto-120') == self.itemcget('_border2','fill'):
                color = get_shade(self['bg'], 0.1, 'auto-120')
                self.itemconfig('_border1', outline=color)
                self.itemconfig('_border2', fill=color)
        main_win.bind_class(main_win,'<FocusIn>', _chngIn, '+')
        main_win.bind_class(main_win,'<FocusOut>', _chngIn, '+')
        self._getconfigure2(self.cnf)

    def _set_size(self, *ags):
        """Internal function. This will resize everything that is in the button"""
        if ags[0].width == self._size[0] and ags[0].height == self._size[1]: return
        self._size = (ags[0].width, ags[0].height)
        self.delete('_bd_color1')
        self.delete('_bd_color2')
        self.delete('_border1')
        self.delete('_border2')
        self.delete('_tf')
        # Need fix (laggy on resizing) ----> workaround: cancel if still resizing 
        if self.stopped: self.after_cancel(self.stopped)
        self.stopped = self.after(50, lambda: self.on_press_color(tag='_activebg', 
            width=ags[0].width, height=ags[0].height,color=self.cnf.get('activebackground'))  )
        self.rounded_rect(0, -1, ags[0].width, ags[0].height+3, 6, width=self.cnf.get('bd',6), fill=self.cnf.get('bordercolor', 
                get_shade(self['bg'], 0.04, 'auto-120')), tag1='_bd_color1', tag2='_bd_color2')
        self.rounded_rect(2, 2, ags[0].width-5, ags[0].height-4, 3, width=1, fill=get_shade(self['bg'], 0.1, 'auto-120'), 
                tag1='_border1', tag2='_border2')
        self.rounded_rect(2, 2, ags[0].width-4, ags[0].height-3, 4, width=2, fill='#81b3f4', tag='_tf', state='hidden')
        self.coords('_txt', ags[0].width/2, ags[0].height/2)
        self.coords('_img', ags[0].width/2, ags[0].height/2)
        self.coords('_bit', ags[0].width/2, ags[0].height/2)
        self._compound(self.cnf.get('compound'), width=ags[0].width, height=ags[0].height)
        self.tag_raise('_txt')
        self.tag_raise('_img')
        self.tag_raise('_bit')
        self.tag_raise('_tf')
        self.after(50, self._getconfigure2)
        self.master.focus()

    def on_press(self, *ags):
        ''' Internal function. When button is pressed <Button-1>'''
        self._rpin = None
        self._rpinloop = True

        def cmd(*a):
            self.cnf['command']() if self.cnf.get('command') else None
            self.unbind_class('button_command', '<ButtonRelease-1>')
            if self.cnf.get('repeatdelay', 0) and self.cnf.get('repeatinterval', 0) and self._rpinloop:
                self._rpin = self.after( self.cnf.get('repeatinterval', 0), cmd )
        def on_enter(*a):
            self.itemconfig('_activebg', state='normal')
            self.itemconfig('_border1', state='hidden')
            self.itemconfig('_border2', state='hidden')
            if self.cnf.get('repeatdelay',0) and self.cnf.get('repeatinterval', 0):
                self._rpinloop = True
                cmd()
            self.bind_class('button_command', '<ButtonRelease-1>', 
                lambda *a: self.after(0, cmd), '+')
        def on_leave(*a):
            self.itemconfig('_activebg', state='hidden')
            self.itemconfig('_border1', state='normal')
            self.itemconfig('_border2', state='normal')
            if self.cnf.get('repeatdelay',0) and self.cnf.get('repeatinterval', 1):
                self._rpinloop = False
                self.after_cancel(self._rpin)
            self.unbind_class('button_command', '<ButtonRelease-1>')

        if self['state'] == 'normal':
            self.focus_set()
            self.itemconfig('_activebg', state='normal')
            self.itemconfig('_border1', state='hidden')
            self.itemconfig('_border2', state='hidden')
            self.bind_class('on_press_enter', '<Enter>', on_enter, '+')
            self.bind_class('on_press_leave', '<Leave>', on_leave, '+')
            if self.cnf.get('repeatdelay',0) and self.cnf.get('repeatinterval', 1):
                self._rpin = self.after(self.cnf.get('repeatdelay',0), cmd)
            self.bind_class('button_command', '<ButtonRelease-1>', cmd, '+')
            
    def on_release(self, *ags):
        '''Internal function. When button is released <ButtonRelease-1>'''
        if self['state'] == 'normal':
            self.itemconfig('_activebg', state='hidden')
            self.itemconfig('_border1', state='normal')
            self.itemconfig('_border2', state='normal')
            self.unbind_class('on_press_enter', '<Enter>')
            self.unbind_class('on_press_leave', '<Leave>')
            self.unbind_class('button_command', '<ButtonRelease-1>')
            self._rpinloop = False
            if self._rpin: self.after_cancel(self._rpin) 

    def _configure(self, cmd, cnf=None, kw=None):
        'Internal function to configure the inherited class'
        return super()._configure(cmd, cnf, kw)

    def configure(self, cnf=None, **kw):
        """Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.

        Returns tuple of 2 configuration settings info, if any
        """
        kw = _TK._cnfmerge( (cnf, kw) )
        cnf = {}
        for i in list(kw):
            if i in self._features: 
                cnf[i] = kw.pop(i,None)
        r1 = super().configure(**kw)
        if kw.get('bg') or kw.get('background'):
            self.original_bg = self['bg']
        self.after(10, self._getconfigure2, cnf)
        if r1 is not None:
            r1.update(self.cnf)
        return r1
    config = configure

    def cget(self, key):
        """Return the resource value for a KEY given as string."""
        if key in self._features: return self.cnf[key]
        else: return super().cget(key)
    __getitem__ = cget

    def _getconfigure2(self, cnf={}, **kw):
        """Internal Function.
        This function configure all the resouces of the Widget and save it to the class dict."""
        kw = _TK._cnfmerge( (cnf, kw) )
        kw = { k:v for k,v in kw.items() if v is not None }        
        self.cnf.update(kw)
        self.cnf = { k:v for k, v in self.cnf.items() if v is not None }
        self.cnf['fg'] = self.cnf.get('fg') if self.cnf.get('fg', None) else self.cnf.get('foreground','black')
        self.cnf['bd'] = self.cnf.get('bd') if self.cnf.get('bd', None) else self.cnf.get('borderwidth',6)
        if self.cnf.get('textvariable') is not None: self.cnf['text'] = self.cnf['textvariable'].get()

        if self['state'] == 'disabled':
            super().configure(bg=self.cnf.get('disabledbackground'))
        elif self['state'] == 'normal':
            super().configure(bg=self.original_bg)

        self._rel = self['relief']
        if self.cnf.get('overrelief') is not None:
            self._rel = self['relief']
            self.bind_class("overrelief", "<Enter>", lambda _: self.config(relief=kw['overrelief']), '+')
            self.bind_class("overrelief", "<Leave>", lambda _: self.config(relief=self._rel), '+')
        else:
            self.unbind_class('overrelief', '<Enter>')
            self.unbind_class('overrelief', '<Leave>')
            self._configure('configure', { 'relief': self._rel }, kw=None)
        
        if kw.get('activebackground') is not None:
            self.on_press_color(tag='_activebg', width=self.winfo_reqwidth(), 
                height=self.winfo_reqheight(), color=self.cnf.get('activebackground'))
            self.tag_lower('_activebg')
        elif kw.get('activebackground') is '': 
            self.cnf.pop('activebackground', None)
            self.on_press_color(tag='_activebg', width=self.winfo_reqwidth(), 
                height=self.winfo_reqheight(), color=None)
        
        if kw.get('activeforeground') is not None:
            self.bind_class('active_fg','<Enter>', lambda _:self.itemconfig('_txt',fill=kw['activeforeground'] ))
            self.bind_class('active_fg','<Leave>', lambda _:self.itemconfig('_txt',fill=self.cnf.get('fg','black')) )
        elif kw.get('activeforeground') is '':
            self.unbind_class('active_fg','<Enter>')
            self.unbind_class('active_fg','<Leave>')
            self.itemconfig('_txt',fill=self.cnf.get('fg','black'))
        
        for set_size_if in ('text', 'font', 'textvariable', 'image', 'bitmap', 
                            'compound', 'padx', 'pady', 'width', 'height'):
            if kw.get(set_size_if) is not None:
                W, H = self._info_button(
                        text = self.cnf.get('text'), 
                        font = self.cnf.get('font'), 
                        image = self.cnf.get('image'),
                        bitmap = self.cnf.get('bitmap'),
                        padding = ( self.cnf.get('padx',0), self.cnf.get('pady',0) ), 
                        compound = self.cnf.get('compound'),
                        textvariable = self.cnf.get('textvariable') )
                W = kw.get('width', W)
                H = kw.get('height', H)
                self._configure('configure', { 'width': W, 'height': H })
                break

        if self.cnf.get('image'):
            if kw.get('activeimage') is not None:
                self.bind_class('active_img','<Enter>', lambda _:self.itemconfig('_img',image=kw['activeimage'])   )
                self.bind_class('active_img','<Leave>', lambda _:self.itemconfig('_img',image=self.cnf.get('image'))   )
            elif kw.get('activeimage') is '':
                self.unbind_class('active_img','<Enter>')
                self.unbind_class('active_img','<Leave>')
                self.itemconfig('_img',image=self.cnf.get('image'))
            # For Image config
            config_cnf_img = {}
            for i in ('anchor', 'image'):
                config_cnf_img.update( {i : kw.get(i, self.cnf.get(i))} )
            self.itemconfig('_img', config_cnf_img, state=self['state'])
        elif self.cnf.get('bitmap'):
            if kw.get('activebitmap') is not None:
                self.bind_class('active_bit','<Enter>', lambda _:self.itemconfig('_bit',image=kw['activebitmap'])   )
                self.bind_class('active_bit','<Leave>', lambda _:self.itemconfig('_bit',image=self.cnf.get('bitmap'))   )
            elif kw.get('activebitmap') is '':
                self.unbind_class('active_bit','<Enter>')
                self.unbind_class('active_bit','<Leave>')
                self.itemconfig('_bit',image=self.cnf.get('bitmap'))
            # For bitmap config
            config_cnf_bit = {}
            for i in ('anchor', 'bitmap'):
                config_cnf_bit.update( {i : kw.get(i, self.cnf.get(i))} )
            self.itemconfig('_bit', config_cnf_bit, state=self['state'])

        if kw.get('compound'):
            self._compound(kw.get('compound'), self.winfo_reqheight(), self.winfo_reqwidth())
        
        if self.cnf.get('textvariable') is not None:
            self.cnf['text'] = self.cnf['textvariable'].get()
            self.cnf['textvariable'].trace_add( 'write', lambda *ag: 
                    self.itemconfig('_txt', text = self.cnf['textvariable'].get() ))

        # For Text config
        config_cnf_txt = {}
        for i in ('text','anchor','font','justify'):
            config_cnf_txt.update( {    i : kw.get(i, self.cnf.get(i))  } )
        self.itemconfig( '_txt', config_cnf_txt, state=self['state'], 
                        fill=kw.get('fg', self.cnf.get('fg')), 
                        disabledfill=kw.get('disabledforeground', 
                        self.cnf.get('disabledforeground')))  
        # if commented and state='disabled then doesnt disable completely. (NEED FIX)
        self.after(10, lambda: self.itemconfig( '_txt', state=self['state']))   
             
        if int(self['takefocus']) and self['state'] == 'normal':
            self.bind_class('takefocus', '<FocusIn>' , lambda _: self.itemconfig('_tf', state='normal'))
            self.bind_class('takefocus', '<FocusOut>', lambda _: self.itemconfig('_tf', state='hidden'))
        elif not int(self['takefocus']) or self['state'] == 'disabled':
            self.unbind_class('takefocus', '<FocusIn>' )
            self.unbind_class('takefocus', '<FocusOut>')
            self.itemconfig('_tf', state='hidden')
    
        Edge_color = get_shade(self['bg'], 0.1, 'auto-120')    # This will darken the border around the button
        self.itemconfig('_border1', outline=Edge_color)
        self.itemconfig('_border2', fill=Edge_color)

        if kw.get('bd'):
            self.itemconfig('_bd_color1', width=kw.get('bd', 6))
            self.itemconfig('_bd_color2', width=kw.get('bd', 6))

        if bool(kw.get('borderless')): 
            # Modify configurations of master widget to support `borderless=1`.
            def configure(cnf=None, **kw):
                """Configure resources of a widget.

                The values for resources are specified as keyword
                arguments. To get an overview about
                the allowed keyword arguments call the method keys.
                """
                #  Need a better fix ..
                kw = _TK._cnfmerge((cnf, kw))
                r = self.master._configure('configure', None, kw)
                if kw.get('bg') or kw.get('background'):
                    for i in self._buttons:
                        if i['borderless']:
                            i.cnf.update( {'bordercolor': i.master['bg']} )
                            i.itemconfig('_bd_color1', outline=i.master['bg'])
                            i.itemconfig('_bd_color2', fill=i.master['bg'])
                return r

            self.master.configure = configure
            self.master.config = configure
            self.cnf.update( {'bordercolor': self.master['bg']} )
            self.itemconfig('_bd_color1', outline=self.master['bg'])
            self.itemconfig('_bd_color2', fill=self.master['bg'])
        elif not bool(kw.get('borderless', True)) or not self.cnf.get('borderless'):
            if self.cnf.get('bordercolor') == self.master['bg']:
                self.cnf.pop('bordercolor', None)
            bd_color = self.cnf.get('bordercolor', get_shade(self['bg'], 0.04, 'auto-120'))
            self.cnf.update( {'bordercolor': bd_color} )
            self.itemconfig('_bd_color1', outline=kw.get('bordercolor', bd_color) )
            self.itemconfig('_bd_color2', fill=kw.get('bordercolor', bd_color) )
    
    def bind_class(self, className, sequence=None, func=None, add='+'):
        className = className+str(self)
        bindtags = list( self.bindtags() )
        if className in bindtags: bindtags.remove(className)
        bindtags.insert(bindtags.index('Canvas'), className)
        self.bindtags(bindtags)
        return super().bind_class(className, sequence=sequence, func=func, add=add)
    
    def unbind_class(self, className, sequence):
        className = className+str(self)
        bindtags = list(self.bindtags())
        if className in bindtags: bindtags.remove(className)
        self.bindtags(bindtags)
        return super().unbind_class(className, sequence)

    def on_press_color(self, **kw):
        '''### Give gradient color effect
        Internal funtion. return tag
        #### Arguments:
        1. `color`: ("#4b91fe", "#055be5")
        2. `tag`
        3. `height`
        4. `width`'''
        self.cnf['activebackground'] = self.cnf.get('activebackground', ("#4b91fe", "#055be5"))
        width = self.coords('_activebg')
        if len(width) > 3:
            width = width[2]
        if self.winfo_height() == len(self.find('withtag', '_activebg')) \
            and self.winfo_width() == width and not kw.get('color'): return
        self.delete('_activebg')
        tag = kw.get('tag', 'press')
        if kw.get('color') is None: kw.pop('color', None)
        cr = kw.get( 'color', ("#4b91fe", "#055be5") )  # This is the default color for mac 
        if isinstance(cr, tuple):
            if None in cr: 
                cr = list(cr)
                cr.remove(None)
                cr = cr[0]
        w, h = self.winfo_width(), self.winfo_height()
        if not isinstance(cr, tuple): cr = ( C.Color(cr),C.Color(cr) )
        else: cr = ( C.Color(cr[0]),C.Color(cr[1]) )
        for i, j in enumerate(list( cr[0].range_to( cr[1],  kw.get('heigh', h)) )):
            self._line(0, i, kw.get('width',w), i, fill=j, tag=tag, state='hidden')
        self.tag_lower(tag)     # keep the tag last 
        return tag 

    def _info_button(self, **kw):
        """Internal Funtion.\n
        This function takes essentials parameters to give
        the approximate width and height accordingly. \n
        It creates a ttk button and use all the resouces given 
        and returns width and height of the ttk button, after taking 
        width and height the button gets destroyed also the custom style."""
        _style_tmp = ttk.Style()
        _style_tmp.configure('%s.TButton'%self, font=kw.get('font') ) 
        _style_tmp.configure('%s.TButton'%self, padding=kw.get('padding') )
        tmp = ttk.Button(self, text=kw.get('text'), image=kw.get('image'), 
            bitmap=kw.get('bitmap'), textvariable=kw.get('textvariable'),
            compound=kw.get('compound'), style='%s.TButton'%self )
        geo = tmp.winfo_reqwidth(), tmp.winfo_reqheight()
        del _style_tmp   # Need fix --- doesn't really delete the custom style
        tmp.destroy()
        return geo

    def _compound(self, flag, height, width):
        "Internal function. Use `compound = 'left'/'right'/'top'/'bottom'` to configure."
        _PiTag = '_img' if self.cnf.get('image') else '_bit'
        _im_size = self.bbox(_PiTag)
        _txt_size = self.bbox('_txt')
        if _im_size and _txt_size:
            W_im = _im_size[2] - _im_size[0]
            H_im = _im_size[3] - _im_size[1]
            W_txt = _txt_size[2] - _txt_size[0]
            H_txt = _txt_size[3] - _txt_size[1]
            if flag is 'bottom':
                width = (width/2, width/2)
                height = (height/2-H_im/2, height/2+H_txt/2)
            elif flag is 'top' :
                width = (width/2, width/2)
                height = (height/2+H_im/2, height/2-H_txt/2)
            elif flag is 'right' :
                width = (width/2-W_im/2, width/2+W_txt/2)
                height = (height/2, height/2)
            elif flag is'left':
                width = (width/2+W_im/2, width/2-W_txt/2)
                height = (height/2, height/2)
            elif flag is not None:
                raise _TK.TclError('bad compound "{}": must be \
                    none, text, image, center, top, bottom, left, or right'.format(flag))
            if isinstance(height, tuple):
                self.coords('_txt', width[0], height[0])
                self.coords(_PiTag, width[1], height[1])
                return { 'width':width, 'height':height }
        return None
    
    def keys(self):
        """Return a list of all resource names of this widget."""
        K_all = ['background', 'bd', 'bg', 'borderwidth', 'cursor', 'height', 'highlightbackground', 'highlightcolor', 
            'highlightthickness','relief', 'state', 'takefocus', 'width', 'activebackground', 'activeforeground', 
            'activeimage', 'activebitmap', 'anchor', 'bitmap', 'command', 'compound', 'disabledforeground', 'fg', 
            'font', 'foreground', 'image', 'overrelief', 'padx', 'pady', 'repeatdelay', 'repeatinterval', 'text', 
            'textvariable', 'underline', 'bordercolor', 'borderless', 'disabledbackground']
        K_all.sort()
        return K_all
