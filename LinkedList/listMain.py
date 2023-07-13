from tkinter import *
from LinkedList.singlyList import initSinglyList
from LinkedList.doublyList import initDoublyList
from LinkedList.circularList import initCircularList

fontName = "Courier New"

def initList():
    window = Tk()
    window.title("Linked List")
    window.geometry("1280x720")
    window.config(bg = "powderblue")

    Label(
        window,
        text="Linked List : ",
        font=(fontName, 20, "bold"),
        padx=15,
        pady=10,
        bg = "powderblue"
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        font=(fontName, 15),
        text="• A linked list is a linear collection of data elements, whose order is not given by their\n  physical "
             "placement in memory. ",
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        font=(fontName, 15),
        text="• Instead, each element points to the next. It is a data structure consisting\n  of a collection of "
             "nodes which together represent a sequence. ",
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        pady=20,
        font=(fontName, 15, "bold"),
        text="Types of Linked List : ",
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    # Frame Containing buttons
    left_frame1 = Frame(window)

    # Button Singly Linked List
    Button(
        left_frame1,
        font=(fontName, 15),
        text="Singly Linked List",
        command=initSinglyList,
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(side=LEFT)

    # Button Doubly Linked List
    Button(
        left_frame1,
        font=(fontName, 15),
        text="Doubly Linked List",
        command=initDoublyList,
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(side=LEFT)

    # Button Circular Linked List
    Button(
        left_frame1,
        font=(fontName, 15),
        text="Circular Linked List",
        command=initCircularList,
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(side=LEFT)

    # End of buttons frame 1.
    left_frame1.pack(padx=10, anchor=W)

    window.mainloop()
