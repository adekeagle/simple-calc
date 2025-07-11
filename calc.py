#!/usr/bin python3

import tkinter as tk
from tkinter import *
from tkinter import messagebox

def fn_calc():
    try:
        number1 = float(num1.get())
        number2 = float(num2.get())
        operation = operator.get()

        if operation == '+':
            result = number1 + number2
        elif operation == '-':
            result = number1 - number2
        elif operation == '*':
            result = number1 * number2
        elif operation == '/':
            if number2 == 0:
                raise Exception('You can not devide by 0')
            else:
                result = number1 / number2
        else:
            result = 'No operator find'
        messagebox.showinfo('Result', f'Result: {result}')
    except Exception as ex:
        messagebox.showerror('ERROR', str(ex))

window = tk.Tk()
operator = tk.StringVar()
window.geometry('500x150')
window.title('Calculator')

frame1 = tk.Frame(window)
frame1.grid(column=0, row=0, padx=10)

frame2 = tk.Frame(window)
frame2.grid(column=1, row=0)

frame3 = tk.Frame(window)
frame3.grid(column=2, row=0)

frame4 = tk.Frame(window)
frame4.grid(column=0, row=1)

num1 = tk.Entry(frame1)
num1.grid(row=0, column=0)

radio1 = tk.Radiobutton(frame2, text='+', variable=operator, value='+')
radio2 = tk.Radiobutton(frame2, text='-', variable=operator, value='-')
radio3 = tk.Radiobutton(frame2, text='*', variable=operator, value='*')
radio4 = tk.Radiobutton(frame2, text='/', variable=operator, value='/')
radio1.grid(column=0, row=0)
radio2.grid(column=0, row=1)
radio3.grid(column=0, row=2)
radio4.grid(column=0, row=3)

num2 = tk.Entry(frame3)
num2.grid(column=3, row=0)

btn1 = tk.Button(window, text='Evaluate', command=fn_calc)
btn1.grid(column=1, row=1)

window.mainloop()
