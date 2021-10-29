from tkinter import *
import math as math


#root
root = Tk()

#size
root.minsize(width=210, height=300)

#title
root.title('Scientific Calculator App')

#entry widget
en = Entry(root, bg='gray', bd=4, font= 20, fg='white', justify = LEFT)


#click function
def click(to_print):
    prev = en.get() 
    en.delete(0, END)
    en.insert(0, prev + to_print)
    return
    

#evaluate operations function

def evaluate_expression():
    v = en.get()
    
    #percentage evaluation
    if '%' in str(v):
        #replace
        n = v.replace('%', '*')
        #concatenate
        result = n + '/100'
        e = eval(result)
        en.delete(0, END)
        en.insert(0, e)
    
    #normal evaluation
    else:
        ev = eval(v)           
        en.delete(0, END)
        en.insert(0, ev)
        
    return
    
    
#clear function    
def clear():
    en.delete(0, END)
    return 

#backspace function
def backspace():
    current_value = en.get()
    length = len(current_value) - 1
    en.delete(length, END)
    return

#scientific function
def scientific_notation(event):
    key = event.widget 
    text = key['text']
    number = en.get()
    result = ''
    
    #conditionals
    if text == 'log':
        result = str(math.log(float(number)))
    if text == 'sin':
        result = str(math.sin(float(number)))
    if text == 'cos':
        result = str(math.cos(float(number)))
    if text == 'tan':
        result = str(math.tan(float(number)))
    if text == 'fact':
        result = str(math.factorial(float(number)))         
    if text == 'sqrt':
        result = str(math.sqrt(float(number)))
        
           
   
    
    en.delete(0, END)
    en.insert(0, result)


#Parenthesis operation function
def parenthesis_func(event):
    key = event.widget
    number = en.get()
    text = key['text']
    
    a = []
    a.append(number)
    a.append(key)
    
    result = ''.join(a)
    
    en.delete(0, END)
    en.insert(0, result)
    return

#exponent function
def exponent_func(widget):
    key = event.widget
    number = en.get()

    text = '**'
    a = []
    a.append(number)
    a.append(text)
    a.append(number)

    result = ''.join(a)
    
    en.delete(0, END)
    en.insert(0, result)


def percent_func():
    a = []
    num = en.get()
    en.delete(0, END)
    prev = en.insert(0, num + '%')




#grid widget
en.grid(column = 0, row = 0, columnspan = 15, padx= 10, pady= 10)


#button widget that calls a function

#scientific buttons
log_button = Button(root, text='log', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = LEFT, width = 2, command = lambda: click('log'))

sin_button = Button(root, text='sin', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = RIGHT, width = 2, command = lambda: click('sin'))
cos_button = Button(root, text='cos', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = RIGHT, width = 2, command = lambda: click('cos'))


tan_button = Button(root, text='tan', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = RIGHT, width = 2, command = lambda: click('tan'))
exp_button = Button(root, text='exp', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = RIGHT, width = 2, command = lambda: click('**'))
factorial_button = Button(root, text='fact', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = RIGHT, width = 2, command = lambda: click('fact'))

open_parenthesis_button = Button(root, text='(', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = RIGHT, width = 2, command = lambda: click('('))
close_parenthesis_button = Button(root, text=')', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = RIGHT, width = 2, command = lambda: click(')'))





#number buttons
button_0 = Button(root, text='0', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('0'))
button_1 = Button(root, text='1', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('1'))
button_2 = Button(root, text='2', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('2'))
button_3 = Button(root, text='3', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('3'))
button_4 = Button(root, text='4', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('4'))
button_5 = Button(root, text='5', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('5'))
button_6 = Button(root, text='6', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('6'))
button_7 = Button(root, text='7', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('7'))
button_8 = Button(root, text='8', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('8'))
button_9 = Button(root, text='9', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('9'))
button_pi = Button(root, text='Pi', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = RIGHT, width = 2, command = lambda: click('3.141592653589793'))


#basic operation buttons

button_plus = Button(root, text='+', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, justify = LEFT, width = 5, command = lambda: click('+'))

button_minus = Button(root, text='-', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, justify = LEFT, width = 5, command = lambda: click('-'))
button_times = Button(root, text='*', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, justify = LEFT, width = 5, command = lambda: click('*'))
button_divide = Button(root, text='/', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, justify = LEFT, width = 5, command = lambda: click('/'))
button_sqrt = Button(root, text='sqrt', padx= 2, pady= 2, bg = 'gray', fg='white', font= 15, height = 1, justify = LEFT, width = 2, command = lambda: click('sqrt'))
button_point = Button(root, text='.', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: click('.'))
button_percent = Button(root, text='%', padx= 2, pady= 2, bg = 'black', fg='white', font= 15, height = 1, relief=RIDGE, justify = LEFT, width = 2, command = lambda: percent_func())


#evaluator button
button_equal = Button(root, text='=', padx=2, bg = 'black', fg='white', font= 15, height = 1, justify = RIGHT, width = 10, command = lambda: evaluate_expression())


#clear button
button_clear = Button(root, text='Clear', padx= 2, pady= 2, bg = 'red', fg='white', font= 5, height =1, justify = LEFT, width = 5, command = lambda: clear())

#backspace button 
button_backspace = Button(root, text='Back', padx= 2, pady= 2, bg = 'red', fg='white', font= 5, height = 1, justify = LEFT, width = 5, command = lambda: backspace())


#bind
log_button.bind('<Button - 1>', scientific_notation)
sin_button.bind('<Button - 1>', scientific_notation)
cos_button.bind('<Button - 1>', scientific_notation)
tan_button.bind('<Button - 1>', scientific_notation)
factorial_button.bind('<Button - 1>', scientific_notation)
button_sqrt.bind('<Button - 1>', scientific_notation)
open_parenthesis_button.bind('<Button - 1>', parenthesis_func)
close_parenthesis_button.bind('<Button - 1>', parenthesis_func)
exp_button.bind('<Button - 1>', exponent_func)
button_percent.bind('<Button - 1>', percent_func)

#grid
log_button.grid(row=1, column=1, columnspan=1, rowspan=1,ipadx=7)
sin_button.grid(row=1, column=2, columnspan=1, rowspan=1, padx=1, pady=3, ipadx=7)
cos_button.grid(row=1, column=3, columnspan=1, rowspan=1, pady = 3, ipadx=7)
tan_button.grid(row=1, column=4, columnspan=1, rowspan=1, padx=1, pady=3, ipadx=13)
exp_button.grid(row=1, column=5, columnspan=1, rowspan=1, pady = 3, ipadx=13)
factorial_button.grid(row=2, column=1, columnspan=1, rowspan=1, pady = 3, ipadx=7)
button_sqrt.grid(row=2, column=2, columnspan=1, rowspan=1, pady = 3, ipadx=7)
open_parenthesis_button.grid(row=2, column=3, columnspan=1, rowspan=1, pady = 3,ipadx=7)
close_parenthesis_button.grid(row=2, column=4, columnspan=1, rowspan=1, pady = 3, ipadx=13)
button_pi.grid(row=2, column=5, columnspan=1, rowspan=1, pady = 3, ipadx=13)

button_7.grid(row=3, column=1, columnspan=1, rowspan=1, pady= 3)
button_8.grid(row=3, column=2, columnspan=1, rowspan=1, padx = 1, pady= 3)
button_9.grid(row=3, column=3, columnspan=1, rowspan=1, padx= 1, pady= 3)
button_backspace.grid(row=3, column=4, columnspan=1, rowspan=1, padx= 1, pady= 3)
button_clear.grid(row=3, column=5, columnspan=1, rowspan=1, padx= 1, pady= 3)
button_4.grid(row=4, column=1, columnspan=1, rowspan=1, pady= 3)
button_5.grid(row=4, column=2, columnspan=1, rowspan=1, pady= 3)
button_6.grid(row=4, column=3, columnspan=1, rowspan=1, pady= 3)
button_times.grid(row=4, column=4, columnspan=1, rowspan=1, pady= 3)
button_divide.grid(row=4, column=5, columnspan=1, rowspan=1, pady= 3)
button_1.grid(row=5, column=1, columnspan=1, rowspan=1, pady= 3)
button_2.grid(row=5, column=2, columnspan=1, rowspan=1, pady= 3)
button_3.grid(row=5, column=3, columnspan=1, rowspan=1, pady= 3)
button_plus.grid(row=5, column=4, columnspan=1, rowspan=1, pady= 3)
button_minus.grid(row=5, column=5, columnspan=1, rowspan=1, pady= 3)
button_0.grid(row=6, column=1, columnspan=1, rowspan=1, pady= 3)
button_point.grid(row=6, column=2, columnspan=1, rowspan=1, pady= 3)
button_equal.grid(row=6, column=4, columnspan=4, rowspan=4, ipadx=15, ipady= 2)
button_percent.grid(row=6, column=3, columnspan=1, rowspan=1, pady=3)


#loop
root.mainloop()