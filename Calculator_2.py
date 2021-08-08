from tkinter import *

root = Tk()
root.wm_title("Calculator")
# root.maxsize((False , False))

# Display
display = Entry(root, font="arial 15 bold", bd=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


first_value = ""
temp = ""
D_fst_val = ""
second_value = ""
symbol = ""
Result = 0
text = ""


def Button_value(value):
    global D_fst_val

    display.delete(0, END)
    D_fst_val += value
    display.insert(0, D_fst_val)
    print("from button " + str(D_fst_val))


def clear_func():
    global D_fst_val, first_value, second_value, symbol, Result, temp
    first_value = D_fst_val = second_value = symbol = temp = ""
    Result = 0
    display.delete(0, END)


def ASMD(smbl):
    global symbol, D_fst_val, first_value, temp, text
    symbol = smbl
    text = smbl
    if not first_value:
        first_value = D_fst_val
    else:
        if temp:
            first_value = temp
        D_fst_val = ""
    display.delete(0, END)
    D_fst_val = ""


def Result_func():
    global symbol, Result, first_value, second_value, temp
    print(first_value, display.get())
    if symbol == "+":
        Result = float(first_value) + float(display.get())

    elif symbol == "-":
        Result = float(first_value) - float(display.get())

    elif symbol == "x":
        Result = float(first_value) * float(display.get())

    elif symbol == "%":
        Result = float(first_value) / float(display.get())

    display.delete(0, END)
    display.insert(0, Result)

    temp = Result
    # print(str(Result) + " from result")
    # smbl_lbl.grid(row=5, column=0)


# Buttons (0-9 , clear , +, - , * , %, =)
# smbl_lbl = Label(root, textvariable=text,
    #  font="Corbel 20 ", padx=12, pady=5)


btn_9 = Button(root, text="9", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("9"))
btn_8 = Button(root, text="8", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("8"))
btn_7 = Button(root, text="7", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("7"))

btn_6 = Button(root, text="6", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("6"))
btn_5 = Button(root, text="5", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("5"))
btn_4 = Button(root, text="4", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("4"))

btn_3 = Button(root, text="3", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("3"))
btn_2 = Button(root, text="2", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("2"))
btn_1 = Button(root, text="1", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("1"))


btn_0 = Button(root, text="0", font="arial 20 bold", padx=12,
               pady=5, command=lambda: Button_value("0"))
btn_dot = Button(root, text=".", font="arial 20 bold", padx=15,
                 pady=5, command=lambda: Button_value("."))

btn_equal = Button(root, text="=", font="arial 20 bold",
                   padx=12, pady=5, command=Result_func)

btn_clear = Button(root, text="Clear", font="arial 17 bold",
                   padx=10, pady=5, command=clear_func)


btn_div = Button(root, text="%", font="arial 20 bold",
                 padx=12, pady=5, command=lambda: ASMD("%"))

btn_mul = Button(root, text="x", font="arial 20 bold",
                 padx=16, pady=5, command=lambda: ASMD("x"))

btn_minus = Button(root, text="-", font="arial 20 bold",
                   padx=18, pady=5, command=lambda: ASMD("-"))

btn_add = Button(root, text="+", font="arial 20 bold",
                 padx=15, pady=5, command=lambda: ASMD("+"))


# Grid the buttons
btn_9.grid(row=1, column=2)
btn_8.grid(row=1, column=1)
btn_7.grid(row=1, column=0)

btn_6.grid(row=2, column=2)
btn_5.grid(row=2, column=1)
btn_4.grid(row=2, column=0)

btn_3.grid(row=3, column=2)
btn_2.grid(row=3, column=1)
btn_1.grid(row=3, column=0)

btn_0.grid(row=4, column=0)
btn_dot.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_clear.grid(row=0, column=4)

btn_div.grid(row=1, column=4)
btn_mul.grid(row=2, column=4)
btn_minus.grid(row=3, column=4)
btn_add.grid(row=4, column=4)

name = Label(root, text="Prepraid by Golam Mostafa Rabby.",font="arial 10 bold",bd=4, fg="blue")
name.grid(row=5, columnspan=5)

mainloop()
