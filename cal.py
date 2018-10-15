from tkinter import *

def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def Clear():
    global operator
    operator=''
    txt_input.set('')
    Display.insert(0,'vamsi calculator.......')

def Equal():
    global  operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator=''




vamsi=Tk()
vamsi.title("vamsi calculator")

operator =''
txt_input = StringVar(value="vamsi calculator.....")
#============================================screen====================================
Display = Entry(vamsi,font=('arial',30,'bold'),fg='white',bg='#ff0000',justify='center',bd=50,textvariable=txt_input)
Display.grid(columnspan=4)

#==========================================Buttons===========================================

#==========================================ROW1==============================================
btn7 = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=7,command=lambda:btn(7)).grid(row=1,column=0)

btn8 = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=8,command=lambda:btn(8)).grid(row=1,column=1)

btn9 = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=9,command=lambda:btn(9)).grid(row=1,column=2)

btnC = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='c',bg='green',command=Clear).grid(row=1,column=3)
#=========================================ROW2=====================================================
btn4 = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=4,command=lambda:btn(4)).grid(row=2,column=0)

btn5 = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=5,command=lambda:btn(5)).grid(row=2,column=1)

btn6 = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=6,command=lambda:btn(6)).grid(row=2,column=2)

btnplus = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='+',bg='orange',command=lambda:btn('+')).grid(row=2,column=3)
#=================================================ROW3 =================================================
btn1 = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=1,command=lambda:btn(1)).grid(row=3,column=0)

btn2 = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=2,command=lambda:btn(2)).grid(row=3,column=1)

btn3 = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=3,command=lambda:btn(3)).grid(row=3,column=2)


btnMINUS = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='-',bg='orange',command=lambda:btn('-')).grid(row=3,column=3)
#==============================================ROW4=========================================================
btnZERO = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=0,command=lambda:btn(0)).grid(row=4,column=0)

btnDOT = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='.',command=lambda:btn('.')).grid(row=4,column=1)

btn1DIV = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='/',command=lambda:btn('/')).grid(row=4,column=2)

btnMUL = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='*',bg='orange',command=lambda:btn('*')).grid(row=4,column=3)
#=============================================ROW5===============================================================
btnCOMA = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=',',command=lambda:btn(',')).grid(row=5,column=0)

btn1BRACKET = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='(',command=lambda:btn('(')).grid(row=5,column=1)

btn1ABRACKET = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text=')',command=lambda:btn(')')).grid(row=5,column=2)

btn1equal = Button(vamsi,padx=30,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='=',bg='orange',command=Equal).grid(row=5,column=3)


vamsi.mainloop()
