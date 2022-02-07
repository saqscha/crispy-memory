

import tkinter as tk
import tkinter.font as tkFont
from tkinter import END 



result = ""


root = tk.Tk()
root.title("Bino-Taschenrechner")
root.geometry("220x300")
root.configure(bg="lightgrey")

buttonfont = tkFont.Font(family='Arial', size=12, weight='bold')

label = tk.Label(root, text="", bg='lightgrey')
label.pack(side='top', padx=2, pady=2)

inputw = tk.Entry(root)
inputw.configure(borderwidth=0, bg='white')
inputw.pack(side='top')


def left_bracket():
    inputw.insert(END, "(")

def right_bracket():
    inputw.insert(END, ")")

def zero():
    inputw.insert(END, "0")

def one():
    inputw.insert(END, "1")

def two():
    inputw.insert(END, "2")

def three():
    inputw.insert(END, "3")

def four():
    inputw.insert(END, "4")

def five():
    inputw.insert(END, "5")

def six():
    inputw.insert(END, "6")

def seven():
    inputw.insert(END, "7")

def eight():
    inputw.insert(END, "8")

def nine():
    inputw.insert(END, "9")

def plus():
    inputw.insert(END, "+")

def minus():
    inputw.insert(END, "-")

def multiply():
    inputw.insert(END, "*")


def result():
    result = inputw.get()
    inputw.delete(0, tk.END)
    inputw.insert(0, eval(result))





def hoch2():
    inputw.insert(END, "**2")
    
def AC():
    inputw.delete(0, tk.END)


rahmenka = tk.Frame(master=root, bg='white')
rahmenka.pack(side='bottom',)

rahmen5 = tk.Frame(master=rahmenka, bg='white')
rahmen5.pack(side='left',)

rahmen36_ = tk.Frame(master=rahmenka, bg='white')
rahmen36_.pack(side='bottom',)

rahmen10 = tk.Frame(master=root, bg='white')
rahmen10.pack(side='bottom',)


rahmen_lr = tk.Frame(master=rahmen5, bg='white')
rahmen_lr.pack(side='top',)
rahmen_12 = tk.Frame(master=rahmen5, bg='white')
rahmen_12.pack(side='bottom',)
rahmen_45 = tk.Frame(master=rahmen5, bg='white')
rahmen_45.pack(side='bottom',)
rahmen_78 = tk.Frame(master=rahmen5, bg='white')
rahmen_78.pack(side='bottom',)
rahmen_3result = tk.Frame(master=rahmen36_, bg='white')
rahmen_3result.pack(side='bottom')
rahmen_space2 = tk.Frame(master=rahmen36_, bg='white')
rahmen_space2.pack(side='top')
rahmen_9minus = tk.Frame(master=rahmen36_, bg='white')
rahmen_9minus.pack(side='top')
rahmen_6plus =tk.Frame(master=rahmen36_, bg='white')
rahmen_6plus.pack(side='bottom')



class rahmen_lr():
    left_bracket_button = tk.Button(master=rahmen_lr, text="(", bg="grey", \
                                    command=left_bracket, height=2, width=2,)
    left_bracket_button.pack(side='left', padx=5, pady=5)

    right_bracket_button = tk.Button(master=rahmen_lr, text=")", \
                                     command=right_bracket, height=2, width=2,)
    right_bracket_button.pack(side='right', padx=5, pady=5, anchor=tk.NW)

class rahmen_12():
    button_one = tk.Button(master=rahmen_12, text="1", \
                           command=one, height=2, width=2,)
    button_one.pack(side='left', padx=5, pady=5)

    button_two = tk.Button(master=rahmen_12, text="2", \
                           command=two, height=2, width=2,)
    button_two.pack(side='right', padx=5, pady=5)

class rahmen_45():
    button_four = tk.Button(master=rahmen_45, text="4", \
                            command=four, height=2, width=2,)
    button_four.pack(side='left', padx=5, pady=5)

    button_five = tk.Button(master=rahmen_45, text="5", \
                            command=five, height=2, width=2,)
    button_five.pack(side='right', padx=5, pady=5)

class rahmen_78():
    button_seven = tk.Button(master=rahmen_78, text="7", \
                             command=seven, height=2, width=2,)
    button_seven.pack(side='left', padx=5, pady=5)

    button_eight = tk.Button(master=rahmen_78, text="8", \
                             command=eight, height=2, width=2,)
    button_eight.pack(side='right', padx=5, pady=5)

class rahmen_3result():
    button_three = tk.Button(master=rahmen_3result, text="3", \
                             command=three, height=2, width=2,)
    button_three.pack(side='left', padx=5, pady=5)

    button_result = tk.Button(master=rahmen_3result, text="=", \
                           command=result, height=2, width=2,)
    button_result.pack(side='right', padx=5, pady=5)

class rahmen_9minus():
    button_nine = tk.Button(master=rahmen_9minus, text="9", \
                            command=nine, height = 2, width = 2,)
    button_nine.pack(side='left', padx=5, pady=5)

    button_space1 = tk.Button(master=rahmen_9minus, text="-", \
                            command=minus,)
    button_space1.pack(side='right', padx=5, pady=5)

class rahmen_6plus():
    button_six = tk.Button(master=rahmen_6plus, text="6",
                            command=six, height=2, width=2,)
    button_six.pack(side='left', padx=5, pady=5)

    button_plus = tk.Button(master=rahmen_6plus, text="+", \
                            command=plus,)
    button_plus.pack(side='right', padx=5, pady=5)

class rahmen_space2():
    button_twoo = tk.Button(master=rahmen_space2, text="^2",
                            command=hoch2, height=2, width=2,)
    button_twoo.pack(side='left', padx=5, pady=5)

    button_clear = tk.Button(master=rahmen_space2, text="AC", \
                            command=AC,)
    button_clear.pack(side='right', padx=5, pady=5)




if __name__ == '__main__':
    root.mainloop()


