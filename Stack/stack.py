from tkinter import *
from tkinter import messagebox

# initial Values
x, x1, y1 = 160, 121, 540
y, x2, y2 = 565, 200, 590

count = 0
txtTop = []
arrow = []
box = []
box_txt = []
lst = []

lbl_error = None
peek_ele = None
canvas = None
txtCapacity = None
capacity = None
inpIntEntry = None
window = None
res = None

def initStackWindow():
    global lbl_error,canvas,inpIntEntry,window,res,peek_ele,txtCapacity,capacity

    window = Tk()
    window.title("Stack")
    #w, h = window.winfo_screenwidth(), window.winfo_screenheight() - 20
    window.geometry("1280x720")
    window.config(bg = "powderblue")

    try:
        window.state("zoomed")
    except TclError:
        print("Linux Error")

    # Label: Stack
    Label(
        window,
        text="Stack : ",
        font=("Courier New", 20, "bold"),
        padx=15,
        pady=10,bg = "powderblue"
    ).pack(anchor=W)

    # Label: Stack Definition Text
    Label(
        window,
        padx=15,
        text="• Stack is a linear data structure which follows a particular order in which the operations are performed.",
        font=("Courier New", 15),
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• Stack is an abstract data type with a bounded(predefined) capacity.",
        font=("Courier New", 15),
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    Label(
        window,
        padx=15,
        text="• It is a simple data structure that allows adding and removing elements in a particular order.",
        font=("Courier New", 15),
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    # Label: Stack Definition Text
    Label(
        window,
        padx=15,
        text="• The order may be LIFO(Last In First Out) or FILO(First In Last Out).",
        font=("Courier New", 15),
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    left_frame1 = Frame(window)

    inpIntEntry = Entry(
        left_frame1,
    )
    inpIntEntry.pack(fill=BOTH, side=LEFT)

    # Button PUSH
    Button(
        left_frame1,
        text="PUSH",
        command=push_box,
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(side=LEFT)


    # Button POP
    Button(
        left_frame1,
        text="POP",
        command=pop_box,
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(side=LEFT)
    entry_text(left_frame1,"Size : ")
    res = Entry(left_frame1,)
    res.pack(fill=BOTH, side=LEFT)

    # End of buttons frame 1.
    left_frame1.pack(padx=10, pady=10, anchor=W)

    # Label: Stack Definition Text
    lbl_error = Label(
        window,
        padx=15,
        font=("Courier New", 15, "bold"),
        text="• Error : ",
        foreground="#dd2c00",
        bg = "powderblue"
    )
    lbl_error.pack(anchor=W)

    peek_ele = Label(
        window,
        padx=15,
        font=("Courier New", 15, "bold"),
        text="• Peek Element : ",
        foreground="#dd2c00",
        bg = "powderblue"
    )
    peek_ele.pack(anchor=W)

    
    txtCapacity = Label(window, padx=15, font=("Courier New", 15, "bold"), text="• Current Queue Capacity : ",justify=LEFT, foreground="#dd2c00",bg = "powderblue")
    txtCapacity.pack(anchor=W)

    # Canvas: To draw Stack
    canvas = Canvas(
        window,
        bg="#FFF",
        height="700",
        width="700"
    )

    canvas.create_line(110, 50, 110, 600)
    canvas.create_line(210, 50, 210, 600)
    canvas.create_line(110, 600, 211, 600)
    canvas.create_text(155, 620, text="Stack")

    canvas.pack(padx=10, pady=10, anchor=W, expand=True, fill=BOTH)
    scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=X)
    canvas.configure(yscrollcommand=scrollbar.set)

    window.mainloop()
def entry_text(parent, txt):
    lbl = Label(parent, text=str(txt), font = ("Courier New",15) ,padx=15,bg = "powderblue")
    lbl.pack(fill=BOTH, side=LEFT)

    return lbl

def getInput():
    try:
        inp = str(int(inpIntEntry.get()))
        if len(inp) > 4:
            inp = inp[0:4]
            inp += ".."
            return inp
        else:
            return inp
    except ValueError:
        return False

def push_box():
    global lbl_error,canvas

    if getInput():
        if count != int(res.get()):
            box.append(canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="#ffd28c", width=2))
            box_txt.append(canvas.create_text((x, y), text=str(getInput())))
            arrow.append(canvas.create_line(x + 60, y, x + 100, y, arrow=FIRST))
            txtTop.append(canvas.create_text((x + 140, y), text="TOP (Index = {0})".format(count)))
            update_value()
            lst.append(str(getInput()))

            if count > 1:
                canvas.delete(txtTop[0])
                canvas.delete(arrow[0])
                txtTop.pop(0)
                arrow.pop(0)
                    
            lbl_error.config(text="• Error : ")
            peek_ele.config(text = "• Peek Element : " + str(getInput()))
            txtCapacity.config(text="• Current Stack Capacity : " + str(int(res.get()) - count),bg="powderblue")

        else:
            lbl_error.config(text="• Error : STACK OVERFLOW")
            

            
    else:
        lbl_error.config(text="• Error : Only integer value is accepted.")
    canvas.configure(scrollregion=canvas.bbox("all"))


def pop_box():
    global lbl_error,canvas
    try:
        canvas.delete(txtTop[0])
        canvas.delete(arrow[0])
        canvas.delete(box[len(box) - 1])
        canvas.delete(box_txt[len(box_txt) - 1])

        txtTop.pop(0)
        arrow.pop(0)
        box.pop(len(box) - 1)
        box_txt.pop(len(box_txt) - 1)
        downgrade_values()
        lst.pop()

        if count != 0:
            arrow.append(canvas.create_line(
                x + 60, y + 60, x + 100, y + 60, arrow=FIRST))
            txtTop.append(canvas.create_text((x + 115, y + 60), text="TOP"))

        lbl_error.config(text="• Error : ")
        peek_ele.config(text = "• Peek Element : " + str(lst[count - 1]))
        txtCapacity.config(text="• Current Stack Capacity : " + str(int(res.get()) - count),bg="powderblue")

    except IndexError:
        lbl_error.config(text="• Error : STACK UNDERFLOW")
        txtCapacity.config(text="• Current Stack Capacity : " + str(int(res.get())),bg="powderblue")
        peek_ele.config(text = "• Peek Element : " + str(capacity))


def update_value():
    global x, x1, y1
    global y, x2, y2
    global count

    y -= 60
    y1 -= 60
    y2 -= 60
    count += 1


def downgrade_values():
    global x, x1, y1
    global y, x2, y2
    global count

    y += 60
    y1 += 60
    y2 += 60
    count -= 1
