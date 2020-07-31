from tkinter import *
import parser

root = Tk()

root.title('CALCULATOR')
root.geometry('310x298')


#get the user input and place it in the textfield
i = 0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1

def fact():
	entire = int(display.get())
	fact = entire
	for x in range (1,entire):
		fact = fact*x
	clear_all()
	display.insert(0,fact)






def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length

def clear_all():
    display.delete(0,END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

#adding the input field
display = Entry(root,font=("Times New Roman",20))
display.grid(row=1,ipady=20,columnspan=6,sticky=W+E,  )
#adding buttons to the calculator
Button(root,font=("Times New Roman", 10), text="1", bg = 'SpringGreen2' , fg = 'black',height=3,width=6,command=lambda: get_variables ( 1 ) ).grid ( row=3 ,
                                                                                                               column=0 )
Button(root,font=("Times New Roman", 10),text="2", bg = 'SpringGreen2' , fg = 'black'  ,height=3,width=6,command = lambda :get_variables(2)).grid(row=3,column=1)
Button(root,font=("Times New Roman", 10),text="3", bg = 'SpringGreen2' , fg = 'black'  ,height=3,width=6,command = lambda :get_variables(3)).grid(row=3,column=2)
Button(root,font=("Times New Roman", 10), text="4" , bg='SpringGreen2' , fg='black' , height=3,width=6 , command=lambda: get_variables(4)).grid(row=4 ,
                                                                                                           column=0)
Button(root,font=("Times New Roman", 10), text="5", bg='SpringGreen2', fg='black', height=3,width=6, command = lambda: get_variables(5)).grid(row=4, column=1)
Button(root,font=("Times New Roman", 10),text="6",bg='SpringGreen2',fg='black',height=3,width=6,command = lambda :get_variables(6)).grid(row=4,column=2)
Button(root,font=("Times New Roman", 10),text="7",bg='SpringGreen2',fg='black',height=3,width=6,command = lambda :get_variables(7)).grid(row=5,column=0)
Button(root,font=("Times New Roman", 10),text="8",bg='SpringGreen2',fg='black',height=3,width=6,command = lambda :get_variables(8)).grid(row=5,column=1)
Button(root,font=("Times New Roman", 10),text="9",bg='SpringGreen2',fg='black',height=3,width=6,command = lambda :get_variables(9)).grid(row=5,column=2)
#adding other buttons to the calculator
Button(root,font=("Times New Roman", 10),text="AC",bg='LightGoldenrod2',fg='black',height=3,width=6,command=lambda :clear_all()).grid(row=6,column=0)
Button(root,font=("Times New Roman", 10),text="0",bg='SpringGreen2',fg='black',height=3,width=6,command = lambda :get_variables(0)).grid(row=6,column=1)
Button(root,font=("Times New Roman", 10),text="=",bg='LightGoldenrod2',fg='black',height=3,width=6,command=lambda :calculate()).grid(row=6,column=2)

Button(root,font=("Times New Roman", 10),text="+",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation("+")).grid(row=3,column=3)
Button(root,font=("Times New Roman", 10),text="-",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation("-")).grid(row=4,column=3)
Button(root,font=("Times New Roman", 10),text="*",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation("*")).grid(row=5,column=3)
Button(root,font=("Times New Roman", 10),text="/",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation("/")).grid(row=6,column=3)

# adding new operations
Button(root,font=("Times New Roman", 10),text="pi",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation("*3.14")).grid(row=3,column=4)
Button(root,font=("Times New Roman", 10),text="%",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation("%")).grid(row=4,column=4)
Button(root,font=("Times New Roman", 10),text="(",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation("(")).grid(row=5,column=4)
Button(root,font=("Times New Roman", 10),text="exp",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation("**")).grid(row=6,column=4)

Button(root,font=("Times New Roman", 10),text="del",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :undo()).grid(row=3,column=5)
Button(root,font=("Times New Roman", 10),text="x!",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :fact()).grid(row=4,column=5)
Button(root,font=("Times New Roman", 10),text=")",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation(")")).grid(row=5,column=5)
Button(root,font=("Times New Roman", 10),text="^2",bg='LightGoldenrod2',fg='black',height=3,width=6,command= lambda :get_operation("**2")).grid(row=6,column=5)
root.mainloop()
