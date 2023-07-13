from tkinter import *

font = "Courier New"


def lbl_heading(parent, txt):
    lbl = Label(parent, text=str(txt), font=(
        font, 15, "bold"), padx=15, pady=10,bg = "powderblue")
    lbl.pack(anchor=W)

    return lbl


def lbl_text(parent, txt):
    lbl = Label(parent, text=str("• "+txt), font=(font, 15), padx=15,bg = "powderblue")
    lbl.pack(anchor=W)

    return lbl


def lbl_error(parent, error):
    lbl = Label(parent, text=str("• Error : "+error),font=(font, 15, "bold"), padx=15, foreground="#dd2c00",bg = "powderblue")
    lbl.pack(anchor=W)

    return lbl


def entry_text(parent, txt):
    lbl = Label(parent, text=str(txt), font=(font, 15), padx=15,bg = "powderblue")
    lbl.pack(fill=BOTH, side=LEFT)

    return lbl


def entry(parent, width):
    entry = Entry(parent, width=width)
    entry.pack(fill=BOTH, side=LEFT)

    return entry

def btn_in_frame(parent, text, command):
    btn = Button(parent, text=str(text), command=command,bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434')
    btn.pack(fill=BOTH, side=LEFT)

    return btn