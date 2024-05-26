from tkinter import * 
root=Tk() 
root.title("Simple Calculator")
# root.geometry('400x400')
e=Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add(number): 
    # e.delete(0, END) 
    current=e.get()
    e.delete(0, END)  
    e.insert(0, str(current)+ str(number))
    
def button_clear(): 
    e.delete(0, END) 

def button_res():
    first_number=e.get() 
    global f_num 
    global math
    math="Addition"
    f_num=int(first_number)
    e.delete(0, END) 
    
def button_sub():
    first_number=e.get() 
    global f_num 
    global math
    math="Subtraction"
    f_num=int(first_number)
    e.delete(0, END) 

def button_mul():
    first_number=e.get() 
    global f_num 
    global math
    math="Multiplication"
    f_num=int(first_number)
    e.delete(0, END)  

def button_div():
    first_number=e.get() 
    global f_num 
    global math
    math="Division"
    f_num=int(first_number)
    e.delete(0, END) 
    
def button_equal():
    second_number=e.get() 
    e.delete(0, END)
    
    if math=="Addition":
        e.insert(0, f_num + int(second_number))
    if math=="Subtraction":
        e.insert(0, f_num - int(second_number))
    if math=="Multiplication":
        e.insert(0, f_num * int(second_number))
    if math=="Division":
        e.insert(0, f_num / int(second_number))
    
#we need some buttons here 0-9, add, clear and = 
b0=Button(root, text='0', bg='black',fg='white', command=lambda:button_add(0), padx=40, pady=20)
b1=Button(root, text='1', bg='black',fg='white', command=lambda:button_add(1), padx=40, pady=20)
b2=Button(root, text='2', bg='black',fg='white', command=lambda:button_add(2), padx=40, pady=20)
b3=Button(root, text='3', bg='black',fg='white', command=lambda:button_add(3), padx=40, pady=20)
b4=Button(root, text='4', bg='black',fg='white', command=lambda:button_add(4), padx=40, pady=20)
b5=Button(root, text='5', bg='black',fg='white', command=lambda:button_add(5), padx=40, pady=20)
b6=Button(root, text='6', bg='black',fg='white', command=lambda:button_add(6), padx=40, pady=20)
b7=Button(root, text='7', bg='black',fg='white', command=lambda:button_add(7), padx=40, pady=20)
b8=Button(root, text='8', bg='black',fg='white', command=lambda:button_add(8), padx=40, pady=20)
b9=Button(root, text='9', bg='black',fg='white', command=lambda:button_add(9), padx=40, pady=20)
bp=Button(root, text='+', bg='black',fg='white', command=button_res, padx=39, pady=20)
bC=Button(root, text='Clear', bg='black',fg='white', command=button_clear, padx=79, pady=20)
br=Button(root, text='=', bg='black',fg='white', command=button_equal, padx=91, pady=20)

bs=Button(root, text='-', bg='black',fg='white', command=button_sub, padx=41, pady=20)
bm=Button(root, text='*', bg='black',fg='white', command=button_mul, padx=40, pady=20)
bd=Button(root, text='/', bg='black',fg='white', command=button_div, padx=41, pady=20)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)

bC.grid(row=4, column=1, columnspan=2)
bp.grid(row=5, column=0)
br.grid(row=5, column=1, columnspan=2)

bs.grid(row=6, column=0)
bm.grid(row=6, column=1)
bd.grid(row=6, column=2)

root.mainloop()
