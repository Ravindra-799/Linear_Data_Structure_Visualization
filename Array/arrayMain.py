from tkinter import *
from Array.staticArray import initStatArray
from Array.dynamicArray import initDynamicArray

fontName = "Courier New"

def initArrayWindow():
    window = Tk()
    window.title("Array")
    w, h = 1280, 720
    window.geometry("%dx%d" % (w, h))
    window.config(bg = "powderblue")

    # Label: Array
    Label(
        window,
        text="Array : ",
        font=(fontName, 20, "bold"),
        padx=15,
        pady=10,
        bg = "powderblue"
    ).pack(anchor=W)

    # Label: Array Definition Text
    Label(
        window,
        padx=15,
        text="• Array is a data structure used to store homogeneous elements at contiguous locations.",
        font=(fontName, 15),
        bg = "powderblue"
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• Arrays are used to store multiple values in a single variable, instead of declaring\n  separate variables for each value.",
        justify=LEFT,
        font=(fontName, 15),
        bg = "powderblue"
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• An array is a container object that holds a fixed number of values of a single type.",
        font=(fontName, 15),
        bg = "powderblue"
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• Array elements are numbered, starting with zero.",
        font=(fontName, 15),
        bg = "powderblue"
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• Types of Array : ",
        font=(fontName, 15, "bold"),
        bg = "powderblue"
    ).pack(anchor=W, pady=10)

    frame1 = Frame(window)

    Button(
        frame1,
        text="Static Array",
        font=(fontName, 15, "bold"),
        width=15,
        command=initStatArray,
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(side=LEFT)

    Button(
        frame1,
        text="Dynamic Array",
        font=(fontName, 15, "bold"),
        width=15,
        command=initDynamicArray,
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(side=LEFT)


    frame1.pack(anchor=W, padx=15)
    

    window.mainloop()