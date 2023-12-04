from tkinter import*
import tkinter.messagebox as tmsg
import data
import math
import time
from math import*

def click(value):
    ex =entryField.get()
    answer=''
    
    try:
        if value == 'C':
            ex=entryField.get()
            ex=ex[0:len(ex)-1]
            entryField.delete(0,END)
            entryField.insert(0,ex)
            
        elif value == 'clr':
            entryField.delete(0,END)
            
        elif value == '√':
            answer = math.sqrt(eval(ex))
        
        elif value == 'pi':
            answer= math.pi
            
        elif value == 'cos θ':
            answer=math.cos(math.radians(eval(ex)))
            
        elif value == 'sin θ':
            answer=math.sin(math.radians(eval(ex)))
            
        elif value == 'tan θ':
            answer=math.tan(math.radians(eval(ex)))
            
        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            
        elif value == 'x\u00B2':
            answer = eval(ex) ** 2
        
        elif value == 'x\u00B3':
            answer = eval(ex) ** 3
            
        elif value == 'log':
            answer = math.log2(eval(ex))
            
        elif value == 'log 10':
            answer = math.log10(eval(ex))
            
        elif value == 'cosh':
            answer = math.cosh(eval(ex))
            
        elif value == 'sinh':
            answer = math.cosh(eval(ex))
            
        elif value == 'tanh':
            answer = math.cosh(eval(ex))
            
        elif value == chr(8731):
            answer = eval(ex)**(1/3)
            
        elif value == 'x!':
            answer = math.factorial(ex)
            
        elif value == '=':
            answer = eval(ex)
            
        else:
            entryField.insert(END,value)
            return
        
    except SyntaxError :
        pass
       
    entryField.delete(0,END)
    entryField.insert(0,answer)
        
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
button_text_list = [ "7", '8', "9", "*", "cos", "(",
                    "4", '5', "6", "-", "sin", ")",
                    "1", '2', "3", "+", "tan", "%",
                    ".", '0', "/", "√", "log", "pi",
                    "x\u00B3", 'x\u00B2', chr(8731), "x\u02b8", "log10", "x!",
                    "sinh", 'cosh', "tanh", "C", "clr", "="]

for i in button_text_list :
    button= Button(root, font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='light blue', width=3, activebackground='blue',text=i, command=lambda button=i: click(button) )
    button.grid(row=rowvalue,column=columnvalue)
    columnvalue+=1
    if columnvalue>5:
        rowvalue+=1
        columnvalue=0


root.mainloop()