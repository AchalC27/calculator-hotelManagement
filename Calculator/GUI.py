from tkinter import*
import tkinter.messagebox as tmsg
from data import*
from math import*

def click(value):
    current_expression =entryField.get()
    result=''
    
    if value == 'C':
        current_expression = current_expression[:-1]
            
    elif value == 'clr':
        entryField.delete(0,END)
            
    elif value == '√':
        result = square_root(float(current_expression))
        
    elif value == 'pi':
        result= pi()
            
    elif value == 'cos θ':
        result = cos(float(current_expression))
            
    elif value == 'sin θ':
        result = sin(float(current_expression))
            
    elif value == 'tan θ':
        result = tan(float(current_expression))
            
    elif value == 'x\u02b8':
        result = power(eval(current_expression), value)
            
    elif value == 'x\u00B2':
        result = power(eval(current_expression), 2)
        
    elif value == 'x\u00B3':
        result = power(eval(current_expression), 3)
            
    elif value == 'log':
        result = log(float(current_expression))
            
    elif value == 'log 10':
        result = log10(float(current_expression))
            
    elif value == 'cosh':
        result = cosh(float(current_expression))
            
    elif value == 'sinh':
        result = sinh(float(current_expression))
            
    elif value == 'tanh':
        result = tanh(float(current_expression))
            
    elif value == chr(8731):
        result = power(eval(current_expression), 1/3)
            
    elif value == 'x!':
        result = factorial(current_expression)
            
    elif value == '=':
        result = calculate(current_expression)
            
    else:
        entryField.insert(END,value)
        return
       
    entryField.delete(0,END)
    entryField.insert(0,result)
        
root = Tk()
canvas_width = 555
canvas_height = 600
root.geometry(f'{canvas_width}x{canvas_height}')
root.config(bg='light blue')
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)
root.title('CalCulator')
sc_variable = StringVar()
entryField = Entry(root, textvariable=sc_variable, font='lucida 35 bold', fg='black', bg='white', borderwidth=10, )
entryField.grid(row=0,column=0,columnspan=6)

rowvalue=1
columnvalue=0
list = [ "7", '8', "9", "*", "cos", "(",
                    "4", '5', "6", "-", "sin", ")",
                    "1", '2', "3", "+", "tan", "%",
                    ".", '0', "/", "√", "log", "pi",
                    "x\u00B3", 'x\u00B2', chr(8731), "x\u02b8", "log10", "x!",
                    "sinh", 'cosh', "tanh", "C", "clr", "="]

for i in list :
    button= Button(root, font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='light blue', width=3, activebackground='blue',text=i, command=lambda button=i: click(button) )
    button.grid(row=rowvalue,column=columnvalue)
    columnvalue+=1
    if columnvalue>5:
        rowvalue+=1
        columnvalue=0


root.mainloop()