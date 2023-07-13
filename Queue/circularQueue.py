from tkinter import *

window = None
txtCapacity = None 
inpIntEntry = None 
canvas = None
lbl_Error = None

#defaults 
fontName = "Courier New"
capacity = None
front = -1
rear = -1
c = 0

x1 = 100
y1 = 100

arr_data = []
arr_x1 = [100]

arr_front = []
arr_rear = []

def initCircularQueue():
    global window, txtCapacity, inpIntEntry, canvas, lbl_Error,capacity

    window = Tk()
    window.title("Visual Simple Queue")
    #w, h = window.winfo_screenwidth(), window.winfo_screenheight() - 20
    window.geometry("1280x720")
    window.config(bg = "powderblue")

    try:
        window.state("zoomed")
    except TclError:
        print("Linux Error")

    Label(
        window,
        text="Circular Queue : ",
        font=("Courier New", 20, "bold"),
        padx=15,
        pady=10,
        bg = "powderblue"
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        font=("Courier New", 15),
        text="• Circular Queue is also a linear data structure, which follows the principle of FIFO(First In First "
             "Out),",
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        font=("Courier New", 15),
        text="  but instead of ending the queue at the last position, it again starts from the first position after the "
             "last,",
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    # Label: Queue Definition Text
    Label(
        window,
        padx=15,
        font=("Courier New", 15),
        text="  hence making the queue behave like a circular data structure.",
        justify=LEFT,
        bg = "powderblue"
    ).pack(anchor=W)

    # Frame Containing Integer Input, Button Enqueue, Button Dequeue
    frame1 = Frame(window)

    inpIntEntry = Entry(frame1)
    inpIntEntry.pack(fill=BOTH,side=LEFT)

    Button(
        frame1,
        text="Enqueue (Insert)",
        command=insert,
        font=(fontName, 15, "bold"),
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(fill=BOTH,side=LEFT)

    Button(
        frame1,
        text="Dequeue (Delete)",
        font=(fontName, 15, "bold"),
        command=delete,
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(fill=BOTH,side=LEFT)

    capacity = Entry(frame1)
    capacity.pack(fill=BOTH,side=LEFT)

    Button(
        frame1,
        text="Create  ",
        font=(fontName, 15, "bold"),
        command=emptyQueue,
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(fill=BOTH,side=LEFT)

    Button(
        frame1,
        text="Reset Queue",
        command=reset,
        font=(fontName, 15, "bold"),
        bg="#ff523b", fg="#fff", activebackground='#ff523b',activeforeground='#563434'
    ).pack(fill=BOTH,side=LEFT)

    frame1.pack(anchor=W, padx=15, pady=15)

    txtCapacity = Label(window, padx=15, font=(fontName, 10, "bold"), text="• Current Queue Capacity : " + str(capacity),justify=LEFT,bg="powderblue")
    txtCapacity.pack(anchor=W)

    lbl_Error = Label(
        window,
        padx=15,
        font=(fontName, 15, "bold"),
        text="• Error : ",
        justify=LEFT,
        foreground="#dd2c00",
        bg = "powderblue"
    )
    lbl_Error.pack(anchor=W)

    #----- Canvas Start ------#
    canvas = Canvas(window, width=500, height=800, bg="#FFF")
    canvas.pack(fill=BOTH, expand=True, anchor=W, padx=15, pady=15)

    

    scrollbar = Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    canvas.configure(xscrollcommand=scrollbar.set)
    #----- Canvas End -------#

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def dataBox(inp):
    global arr_data

    data = []
    data.append(canvas.create_rectangle(x1 + 10, y1 + 10, x1 + 80, y1 + 70, fill="#ffd28c"))
    data.append(canvas.create_text(x1 + 45, y1 + 40, text=str(inp)))
    
    return data

def deleteBox(box):
    canvas.delete(box[0])
    canvas.delete(box[1])

def emptyQueue():
    x = x1
    global c,arr_x1,arr_data
    arr_data = [[None,None]] * int(capacity.get())
    a = 100
    for i in range(int(capacity.get()) - 1):
        arr_x1.append(a + 90)
        a = a + 90
    c = int(capacity.get())
    for i in range(int(capacity.get())):
        canvas.create_rectangle(x, y1, x + 90, y1 + 80, width=2)
        x += 90
    canvas.create_line(x1 - 60, y1 + 45, x1, y1 + 45, arrow=LAST, width=2)
    canvas.create_line(x1 - 60, y1 + 45, x1 - 60, y1 + 160, width=2)
    canvas.create_line(x1 - 60, y1 + 160, x + 50, y1 + 160, width=2)
    canvas.create_line(x + 50, y1 + 45, x + 50, y1 + 160, width=2)
    canvas.create_line(x, y1 + 45, x + 50, y1 + 45, width=2)

def txtFront(loc):
    try:
        f = arr_front[0]
        canvas.delete(f)
        arr_front.pop(0)
    except IndexError:
        print(end="")

    arr_front.append(canvas.create_text(arr_x1[loc] + 45, y1 + 120, text="Front ( Head )"))

def txtRear(loc):
    try:
        r = arr_rear[0]
        canvas.delete(r)
        arr_rear.pop(0)
    except IndexError:
        print(end="")

    arr_rear.append(canvas.create_text(arr_x1[loc] + 45, y1 + 100, text="Rear ( Tail )"))

def incX1():
    global x1
    x1 += 90

def decX1():
    global x1
    x1 -= 90

def incCapacity():
    global txtCapacity, c
    c += 1
    txtCapacity.config(text="• Current Queue Capacity : " + str(c),bg="powderblue")

def decCapacity():
    global txtCapacity, c
    c -= 1
    txtCapacity.config(text="• Current Queue Capacity : " + str(c),bg="powderblue")

def setError(err):
    lbl_Error.config(text="• Error : "+str(err))

def isEmpty():
    if front == -1 and rear == -1:
        return True
    else:
        return False

def getInpData():
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

def insert():
    global front, rear, x1

    setError("")

    if getInpData():

        if front == 0 and rear == int(capacity.get()) - 1 or rear == 0 and front == int(capacity.get()) - 1:

            setError("Queue is Full.")

        elif front == -1 and rear == -1:
            front = 0
            rear = 0

            txtFront(0)
            txtRear(0)

            arr_data[rear] = dataBox(str(getInpData()))
            decCapacity()

        elif rear > -1 and rear < int(capacity.get()):

            if front > 0 and rear == int(capacity.get()) - 1:

                rear = 0
                x1 = arr_x1[rear]

                arr_data[rear] = dataBox(str(getInpData()))

                txtRear(rear)
                txtFront(front)

                decCapacity()

            else:

                isFull = True

                for data in arr_data:
                    if data[0] == None:
                        isFull = False

                if not isFull :
                    rear += 1
                    x1 = arr_x1[rear]

                    arr_data[rear] = dataBox(str(getInpData()))

                    txtRear(rear)
                    txtFront(front)

                    decCapacity()

                else:

                    setError("Queue is Full.")
    else:
        setError("Only integer value is accepted.")

def delete():
    global front, rear, x1

    setError("")

    if not isEmpty():
        if front < int(capacity.get()) and front > -1:
            if front == rear:
                deleteBox(arr_data[front])
                arr_data[front] = [None,None]
                front += 1
                incCapacity()
            else:
                empty = True

                for data in arr_data:
                    if data[0] != None:
                        empty = False
                        
                if not empty:
                    try:
                        deleteBox(arr_data[front])
                        arr_data[front] = [None,None]

                        front += 1
                        x1 = arr_x1[front]
                    except IndexError:
                        front = 0
                        x1 = arr_x1[front]
                    txtFront(front)
                    incCapacity()
                else:
                    setError("Queue is Empty.")
    else:
        setError("Queue is empty.")

def resetValues():
    g = globals()

    g['window'] = None
    g['txtCapacity'] = None 
    g['inpIntEntry'] = None 
    g['canvas'] = None
    g['lbl_Error'] = None

    g['capacity'] = None
    g['c'] = 0
    g['front'] = -1
    g['rear'] = -1

    g['x1'] = 100
    g['y1'] = 100

    g['arr_data'] = []
    g['arr_x1'] = [100]

    g['arr_front'] = []
    g['arr_rear'] = []

def reset():
    window.destroy()
    resetValues()
    initCircularQueue()
    
def on_closing():
    window.destroy()
    resetValues()
