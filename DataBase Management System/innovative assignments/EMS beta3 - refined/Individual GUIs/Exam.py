import sys
import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


class Eaxm:
    def __init__(self, top=None):
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Eaxm ")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(insertbackground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="blue")
        self.Canvas1.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)
        self.Label1.configure(background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                              foreground="#ffffff", text='''Eaxm Table''')

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        self.tv = ScrolledTreeView(self.Canvas1)
        self.tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        self.tv['columns'] = ("Col1", "Col2", "Col3")
        self.tv.column("#0", width=50)
        self.tv.column("Col1", width=100)
        self.tv.column("Col2", width=100, anchor="center")
        self.tv.column("Col3", width=100)
        self.tv.heading("#0", text="Phantom", anchor="w")
        self.tv.heading("Col1", text="Column1", anchor="w")
        self.tv.heading("Col2", text="Column2", anchor="center")
        self.tv.heading("Col3", text="Column3", anchor="w")
        # count = 0
        # for i in range(20):
        #     self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                    values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
        #     count += 1

        self.add_button = tk.Button(self.Canvas1)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)
        self.add_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                  borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                      "-weight bold",
                                  foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                  pady="0", text='''Add''')

        self.delete_button = tk.Button(self.Canvas1)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)
        self.delete_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                         "-weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text="Delete")

        self.modify_button = tk.Button(self.Canvas1)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#3F454C",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     text='''Modify''')

        self.back_button = tk.Button(self.Canvas1)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)
        self.back_button.configure(activebackground="#ececec", activeforeground="#000000", background="#343a40",
                                   borderwidth="0", disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                   highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''')


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


root = tk.Tk()
top = Eaxm(root)
root.mainloop()
