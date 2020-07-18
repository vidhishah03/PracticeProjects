from tkinter import *

def btnclick(num):
    global operator
    operator+=str(num)
    text_input.set(operator)

def btnclear():
    global operator
    operator=""
    text_input.set("")

def btnequals():
    global operator
    res=str(eval(operator))
    text_input.set(res)
    operator=res

def backsp():
    global operator
    operator=operator[:-1]
    text_input.set(operator)



calc = Tk()
calc.title("Calculator")
operator = ""
text_input = StringVar()

screen = Entry(calc, font=("Arial", 30, "bold"), bg="#08C6AB", justify="right", bd=30, insertwidth=4,textvariable=text_input).grid(columnspan=4)

btn7 = Button(calc,command=lambda:btnclick(7), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="7", fg="white").grid(row=1, column=0)

btn8 = Button(calc,command=lambda:btnclick(8), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="8", fg="white").grid(row=1, column=1)

btn9 = Button(calc,command=lambda:btnclick(9), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="9", fg="white").grid(row=1, column=2)

addition = Button(calc,command=lambda:btnclick("+"), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="+", fg="white").grid(row=1,
                                                                                                           column=3)

btn4 = Button(calc,command=lambda:btnclick(4), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="4", fg="white").grid(row=2, column=0)

btn5 = Button(calc,command=lambda:btnclick(5), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="5", fg="white").grid(row=2, column=1)

btn6 = Button(calc,command=lambda:btnclick(6), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="6", fg="white").grid(row=2, column=2)

subt = Button(calc,command=lambda:btnclick("-"), padx=30, font=("Arial", 30, "bold"), bd=10, bg="black", text="-", fg="white").grid(row=2, column=3)

btn1 = Button(calc,command=lambda:btnclick(1), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="1", fg="white").grid(row=3, column=0)

btn2 = Button(calc,command=lambda:btnclick(2), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="2", fg="white").grid(row=3, column=1)

btn3 = Button(calc,command=lambda:btnclick(3), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="3", fg="white").grid(row=3, column=2)

mult = Button(calc,command=lambda:btnclick("*"), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="x", fg="white").grid(row=3, column=3)

btn0 = Button(calc,command=lambda:btnclick(0), padx=26, font=("Arial", 30, "bold"), bd=10, bg="black", text="0", fg="white").grid(row=4, column=0)

clear = Button(calc,command=btnclear, padx=23, font=("Arial", 30, "bold"), bd=10, bg="black", text="C", fg="white").grid(row=5, column=1)

eq = Button(calc, padx=25, command=btnequals, font=("Arial", 30, "bold"), bd=10, bg="black", text="=", fg="white").grid(row=5, column=3)

div = Button(calc,command=lambda:btnclick("/"), padx=30, font=("Arial", 30, "bold"), bd=10, bg="black", text="/", fg="white").grid(row=4, column=3)


btnopen = Button(calc,command=lambda:btnclick("("), padx=30, font=("Arial", 30, "bold"), bd=10, bg="black", text="(", fg="white").grid(row=4, column=1)

btnclose = Button(calc,command=lambda:btnclick(")"), padx=30, font=("Arial", 30, "bold"), bd=10, bg="black", text=")", fg="white").grid(row=4, column=2)

btndec = Button(calc,command=lambda:btnclick("."), padx=33, font=("Arial", 30, "bold"), bd=10, bg="black", text=".", fg="white").grid(row=5, column=0)

btnback = Button(calc,command=backsp, padx=8, font=("Arial", 30, "bold"), bd=10, bg="black", text="del", fg="white").grid(row=5, column=2)



calc.mainloop()
