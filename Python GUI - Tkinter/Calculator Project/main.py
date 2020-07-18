from tkinter import *
from tkinter.messagebox import *
import math as m
from audio_helper import PlayAudio
import threading

font = ('Verdana', 20, 'bold')
ob = PlayAudio()

def clear():
    ex = textField.get()
    ex = ex[0:len(ex)-1]
    textField.delete(0, END)
    textField.insert(0, ex)

def all_clear():
    textField.delete(0, END)

def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b['text']
    print(text)
    t = threading.Thread(target=ob.speak, args=(text))
    t.start()

    if text == 'x':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return

    textField.insert(END, text)

window=Tk()
window.title('My Calculators')
window.geometry('470x530')

pic = PhotoImage(file='img/cal2.png')
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP, pady=10)

heading = Label(window, text="My Calculator", font=font, underline=0)
heading.pack(side=TOP)

textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=10, fill=X, padx=10)

buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text='0', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
zeroBtn.grid(row=3, column=0)

dotBtn = Button(buttonFrame, text='.', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
dotBtn.grid(row=3, column=1)

equalBtn = Button(buttonFrame, text='=', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
equalBtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text='+', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
plusBtn.grid(row=0, column=3)

minusBtn = Button(buttonFrame, text='-', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
minusBtn.grid(row=1, column=3)

mulBtn = Button(buttonFrame, text='x', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
mulBtn.grid(row=2, column=3)

divBtn = Button(buttonFrame, text='/', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
divBtn.grid(row=3, column=3)

clearBtn = Button(buttonFrame, text='<--', font=font, width=11, relief='ridge', activebackground='pink', activeforeground='white', command=clear)
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text='AC', font=font, width=11, relief='ridge', activebackground='pink', activeforeground='white', command=all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2)

plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
mulBtn.bind('<Button-1>', click_btn_function)
divBtn.bind('<Button-1>', click_btn_function)
zeroBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)

def enterClick(event):
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)

textField.bind('<Return>', enterClick)

scFrame = Frame(window)

sqrtBtn = Button(scFrame, text='√', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
sqrtBtn.grid(row=0, column=0)

powBtn = Button(scFrame, text='^', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
powBtn.grid(row=0, column=1)

factBtn = Button(scFrame, text='x!', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
factBtn.grid(row=0, column=2)

radBtn = Button(scFrame, text='toRad', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
radBtn.grid(row=0, column=3)

degBtn = Button(scFrame, text='toDeg', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
degBtn.grid(row=1, column=0)

sinBtn = Button(scFrame, text='sinѲ', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
sinBtn.grid(row=1, column=1)

cosBtn = Button(scFrame, text='cosѲ', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
cosBtn.grid(row=1, column=2)

tanBtn = Button(scFrame, text='tanѲ', font=font, width=5, relief='ridge', activebackground='pink', activeforeground='white')
tanBtn.grid(row=1, column=3)

normalc = True

def calculate_sc(event):
    print("btn..")
    btn = event.widget
    text = btn['text']
    print(text)
    ex = textField.get()
    answer = ''
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))
    elif text == 'toRad':
        print("cal radian")
        answer = str(m.radians(float(ex)))
    elif text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sinѲ':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosѲ':
        print("cal cos")
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanѲ':
        print("cal tan")
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√':
        print("sqrt")
        answer = m.sqrt(int(ex))
    elif text == '^':
        print("pow")
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))

    textField.delete(0, END)
    textField.insert(0, answer)

def scal_click():
    global normalc
    if normalc:
        buttonFrame.pack_forget()
        scFrame.pack(side=TOP, pady=20)
        buttonFrame.pack(side=TOP)
        window.geometry('460x700')
        print("show sc")
        normalc = False
    else:
        print("show normal calculator")
        scFrame.pack_forget()
        window.geometry('510x550')
        normalc = True

sqrtBtn.bind("<Button-1>", calculate_sc)
powBtn.bind("<Button-1>", calculate_sc)
factBtn.bind("<Button-1>", calculate_sc)
radBtn.bind("<Button-1>", calculate_sc)
degBtn.bind("<Button-1>", calculate_sc)
sinBtn.bind("<Button-1>", calculate_sc)
cosBtn.bind("<Button-1>", calculate_sc)
tanBtn.bind("<Button-1>", calculate_sc)

fontMenu = ('', 13)
menubar = Menu(window)

mode = Menu(menubar, font=fontMenu, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=scal_click)

menubar.add_cascade(label="Mode", menu=mode)

window.config(menu=menubar)

window.mainloop()