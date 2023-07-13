from tkinter import *
from Array.widget import *

window = None
error = None
canvas = None
inpElement = None
inpInsIndex = None
inpDelIndex = None
program = None
res = None

x2 = [110]
y1 = 90
rect_data = [None] * 10
rect_text = [None] * 10
index = -1

def initStatArray():
    global error, canvas, inpElement, inpDelIndex, inpInsIndex, program, window,res
    x1 = []
    window = Tk()
    window.title("Visual Static Array")
    #w, h = window.winfo_screenwidth(), window.winfo_screenheight() - 20
    window.geometry("1280x720")
    window.config(bg = "powderblue")

    try:
        window.state("zoomed")
    except TclError:
        print("Linux Error")

    lbl_heading(window, "Static Array : ")
    lbl_text(window, "A static array has memory allocated at compile time.")
    lbl_text(window, "Compile time is when your code is converted by the compiler into machine instructions.")
    lbl_text(window, "There is no way to change the amount of memory allocated when the program is running.")
    lbl_text(window, "Length of following array is 10. (Given at time of programming)")

    frame1 = Frame(window)

    entry_text(frame1, "• Index :")
    inpInsIndex = entry(frame1, 15)
    entry_text(frame1, "Element :")
    inpElement = entry(frame1, 15)
    btn_in_frame(frame1, "Insert", insertElement)

    entry_text(frame1, " | ")

    entry_text(frame1, "Index :")
    inpDelIndex = entry(frame1, 15)
    btn_in_frame(frame1, "Delete", deleteElement)

    entry_text(frame1, " | ")

    entry_text(frame1, "Size : ")
    res = entry(frame1,15)
    btn_in_frame(frame1,"Create",emptyArray)
    entry_text(frame1," | ")
    btn_in_frame(frame1, "Reset", reset)

    frame1.pack(anchor=W, pady=15)

    error = lbl_error(window, "")

    program = Label(window, text="• Program : ",font=("Courier New", 15, 'bold'), bg = "powderblue")
    program.pack(anchor=W, padx=15, pady=10)

    canvas = Canvas(window, width=500, height=800, bg="#FFF")
    canvas.pack(fill=BOTH, expand=True, anchor=W, padx=15, pady=15)
    scrollbar = Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    scrollbar.pack(side=BOTTOM, fill=X)
    canvas.configure(xscrollcommand=scrollbar.set)

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def emptyArray():
    x1 = 100
    y1 = 80
    temp = 110
    for i in range(int(res.get()) - 1):
    
        temp = temp + 90
        x2.append(temp)
    for i in range(int(res.get())):
        canvas.create_rectangle(x1, y1, x1+90, y1+80, width=2)
        canvas.create_text(x1+40, y1+100, text=str(i))
        x1 += 90
    canvas.configure(scrollregion=canvas.bbox("all"))

def element(text, index):
    id_rect_data = canvas.create_rectangle(
        x2[index], y1, x2[index] + 70, y1 + 60, fill="#ffd28c")
    id_txt_data = canvas.create_text(x2[index]+32, y1+30, text=str(text))

    return id_rect_data, id_txt_data

def getElementText():
    try:
        inp = str(int(inpElement.get()))
        if len(inp) > 4:
            inp = inp[0:4]
            inp += ".."
            return inp
        else:
            return inp
    except ValueError:
        return False

def getDelIndex():
    try:
        inp = int(inpDelIndex.get())
        if inp <= int(res.get()) - 1 and inp >= 0:
            return str(inp)
        else:
            return False
    except ValueError:
        return False

def getInpIndex():
    try:
        inp = int(inpInsIndex.get())
        if inp <= int(res.get()) - 1 and inp >= 0:
            return str(inp)
        else:
            return False
    except ValueError:
        return False

def setError(err):
    global error
    error.config(text=str("• Error : "+err))

def insertElement():
    global index

    if getInpIndex():
        i = int(getInpIndex())

        if getElementText():

            if not isEmpty(i):
                canvas.delete(rect_data[i])
                canvas.delete(rect_text[i])
                rect_data[i] = None
                rect_text[i] = None

            setError("")
            upProg(0,i,getElementText())
            ele = element(getElementText(), i)
            rect_data[i] = ele[0]
            rect_text[i] = ele[1]
        else:
            setError("Only integer value is accepted.")
    else:
        setError("Index Out of Bounds .")
        upProg(1,0,"Java Exception : IndexOutOfBoundsException | Python Exception : IndexError")

def isEmpty(index):

    if rect_data[index] != None and rect_text[index] != None:
        return False
    else:
        return True

def deleteElement():

    if getDelIndex():
        i = int(getDelIndex())

        if not isEmpty(i):
            setError("")
            canvas.delete(rect_data[i])
            canvas.delete(rect_text[i])
            rect_data[i] = None
            rect_text[i] = None
            upProg(0,i,"Null")
        else:
            upProg(0,i,"Null")
    else:
        setError("Enter value between 0 to 9.")
        upProg(1,0,"Java Exception : IndexOutOfBoundsException | Python Exception : IndexError")

def upProg(type,index,data):
    if type == 0:
        program.config(text=str("• Program : Array["+str(index)+"] = "+str(data)+";"))
    
    if type == 1:
        program.config(text="• Program : "+str(data))

def reset():
    window.destroy()
    resetValues()
    initStatArray()

def resetValues():
    g = globals()
    g['error'] = None
    g['canvas'] = None
    g['inpElement'] = None
    g['inpInsIndex'] = None
    g['inpDelIndex'] = None
    g['program'] = None
    g['x1'] = []
    g['y1'] = 90
    g['rect_data'] = [None] * 10
    g['rect_text'] = [None] * 10
    g['index'] = -1

def on_closing():
    resetValues()
    window.destroy()