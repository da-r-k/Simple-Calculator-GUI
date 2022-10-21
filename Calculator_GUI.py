from tkinter import *
import math
import time

s=""
s1=""
x=""
boo=0

#Clear All
def AC():
    global s
    global s1
    global x
    s=""
    s1=""
    x=s
    l0.configure(text="0")
    l1.configure(text="")

#Sign Change
def sc():
    global s
    global s1
    global x
    if s=="":
        s=0
    s=str(float(s)*-1)
    l0.configure(text=s)
    l1.configure(text=s1)

#Percentage
def p():
    global s
    global s1
    global x
    if s=="":
        s=0
    s=str((float(s))/100)
    l0.configure(text=s)
    l1.configure(text=s1)

#Division
def d():
    global s
    global s1
    global x
    global boo
    if boo==1:
        s1=s1[:-1]+"÷"
        x=x[:-1]+"/"
    elif s=="":
        x="0/"
        s1="0÷"
    else:
        s1=str(eval(x+s))
        x=s1+"/"
        s1=s1+"÷"
    l0.configure(text=s)
    s=""
    l1.configure(text=s1)
    boo=1

#Multiply
def m():
    global s
    global s1
    global x
    global boo
    if boo==1:
        s1=s1[:-1]+"×"
        x=x[:-1]+"*"
    elif s=="":
        x="0*"
        s1="0×"
    else:
        s1=str(eval(x+s))
        x=s1+"*"
        s1=s1+"×"
    l0.configure(text=s)
    s=""
    l1.configure(text=s1)
    boo=1
    
#Addition
def a():
    global s
    global s1
    global x
    global boo
    if boo==1:
        s1=s1[:-1]+"+"
        x=x[:-1]+"+"
    elif s=="":
        x="0+"
        s1="0+"
    else:
        s1=str(eval(x+s))
        x=s1+"+"
        s1=s1+"+"
    l0.configure(text=s)
    s=""
    l1.configure(text=s1)
    boo=1

#Subtraction
def sb():
    global s
    global s1
    global x
    global boo
    if boo==1:
        s1=s1[:-1]+"−"
        x=x[:-1]+"-"
    elif s=="":
        x="0-"
        s1="0−"
    else:
        s1=str(eval(x+s))
        x=s1+"-"
        s1=s1+"−"
    l0.configure(text=s)
    s=""
    l1.configure(text=s1)
    boo=1

#Decimal point
def xd():
    global s
    global s1
    global x
    global boo
    if s.count(".")==0:
        s=s+"."
        l0.configure(text=s)
        l1.configure(text=s1)


#Functions for number buttons
def b1():
    global s
    global s1
    global x
    global boo
    if s=="0":
        s=""
    s=s+"1"
    l0.configure(text=s)
    l1.configure(text=s1)
    boo=0
    
def b2():
    global s
    global s1
    global x
    global boo
    if s=="0":
        s=""
    boo=0
    s=s+"2"
    l0.configure(text=s)
    l1.configure(text=s1)
    
def b3():
    global s
    global s1
    global x
    if s=="0":
        s=""
    s=s+"3"
    l0.configure(text=s)
    l1.configure(text=s1)    
    global boo
    boo=0

def b4():
    global s
    global s1
    global x
    if s=="0":
        s=""
    s=s+"4"
    l0.configure(text=s)
    l1.configure(text=s1)
    global boo
    boo=0
    
def b5():
    global s
    global s1
    global x
    if s=="0":
        s=""    
    s=s+"5"
    l0.configure(text=s)
    l1.configure(text=s1)
    global boo
    boo=0

def b6():
    global s
    global s1
    global x
    if s=="0":
        s=""
    s=s+"6"
    l0.configure(text=s)
    l1.configure(text=s1)
    global boo
    boo=0
    
def b7():
    global s
    global s1
    global x
    if s=="0":
        s=""
    s=s+"7"
    l0.configure(text=s)
    l1.configure(text=s1)
    global boo
    boo=0
    
def b8():
    global s
    global s1
    global x
    if s=="0":
        s=""
    s=s+"8"
    l0.configure(text=s)
    l1.configure(text=s1)
    global boo
    boo=0

def b9():
    global s
    global s1
    global x
    if s=="0":
        s=""
    s=s+"9"
    l0.configure(text=s)
    l1.configure(text=s1)
    global boo
    boo=0

def b0():
    global s
    global s1
    global x
    if s=="0":
        s=""
    s=s+"0"
    l0.configure(text=s)
    l1.configure(text=s1)
    global boo
    boo=0
    
def eq():
    global s1
    global s
    global x
    global boo
    try:
        if s=="":
            s="0"
        if boo==1:
            x=x[:-1]
            s="+0"
        x=str(eval(x+s))
        s=x
        s1=""
        l0.configure(text=s)
        l1.configure(text=s1)
        x=""
        boo=0
        if s=="0":
            s=""
    except:
        s1=""
        s="Error"
        l0.configure(text=s)
        l1.configure(text=s1)
        x=""
        s=""
        boo=0
        
    
  
#Configuring colors of buttons on hover, click and release
def bx1(e):
    bb1.configure(bg="#d1d1d1")
    b1()
def byy1(e):
    bb1.configure(bg="#d1d1d1")
def bxx1(e):
    bb1.configure(bg="#f4f4f4")


def bx2(e):
    bb2.configure(bg="#d1d1d1")
    b2()
def byy2(e):
    bb2.configure(bg="#d1d1d1")
def bxx2(e):
    bb2.configure(bg="#f4f4f4")


def bx3(e):
    bb3.configure(bg="#d1d1d1")
    b3()
def byy3(e):
    bb3.configure(bg="#d1d1d1")
def bxx3(e):
    bb3.configure(bg="#f4f4f4")

    
def bx4(e):
    bb4.configure(bg="#d1d1d1")
    b4()
def byy4(e):
    bb4.configure(bg="#d1d1d1")
def bxx4(e):
    bb4.configure(bg="#f4f4f4")


def bx5(e):
    bb5.configure(bg="#d1d1d1")
    b5()
def byy5(e):
    bb5.configure(bg="#d1d1d1")
def bxx5(e):
    bb5.configure(bg="#f4f4f4")    

    
def bx6(e):
    bb6.configure(bg="#d1d1d1")
    b6()
def byy6(e):
    bb6.configure(bg="#d1d1d1")
def bxx6(e):
    bb6.configure(bg="#f4f4f4")

    
def bx7(e):
    bb7.configure(bg="#d1d1d1")
    b7()
def byy7(e):
    bb7.configure(bg="#d1d1d1")
def bxx7(e):
    bb7.configure(bg="#f4f4f4")

    
def bx8(e):
    bb8.configure(bg="#d1d1d1")
    b8()
def byy8(e):
    bb8.configure(bg="#d1d1d1")
def bxx8(e):
    bb8.configure(bg="#f4f4f4")

    
def bx9(e):
    bb9.configure(bg="#d1d1d1") 
    b9()
def byy9(e):
    bb9.configure(bg="#d1d1d1")
def bxx9(e):
    bb9.configure(bg="#f4f4f4")


def bx0(e):
    bb0.configure(bg="#d1d1d1")
    b0()
def byy0(e):
    bb0.configure(bg="#d1d1d1")
def bxx0(e):
    bb0.configure(bg="#f4f4f4")

    
def dx(e):
    bbd.configure(bg="#d0d0d0")
    d()
def byyd(e):
    bbd.configure(bg="#d1d1d1")
def bxxdx(e):
    bbd.configure(bg="#eaeaea")

    
def mx(e):
    bbm.configure(bg="#d0d0d0")
    m()
def byym(e):
    bbm.configure(bg="#d1d1d1")
def bxxmx(e):
    bbm.configure(bg="#eaeaea")  


def eqx(e):
    bbe.configure(bg="#c05050")
    eq()
def byye(e):
    bbe.configure(bg="#d06060")
def bxxeqx(e):
    bbe.configure(bg="#e86f6f")

    
def ax(e):
    bba.configure(bg="#d0d0d0") 
    a()
def byya(e):
    bba.configure(bg="#d1d1d1")
def bxxax(e):
    bba.configure(bg="#eaeaea")


def sbx(e):
    bbs.configure(bg="#d0d0d0")
    sb()
def byys(e):
    bbs.configure(bg="#d1d1d1")
def bxxsbx(e):
    bbs.configure(bg="#eaeaea")

    
def acx(e):
    bbAC.configure(bg="#d05050",fg="white") 
    AC()
def byyAC(e):
    bbAC.configure(bg="#d1d1d1")

    
def bcx(e):
    global s
    bbAC.configure(bg="#d1d1d1",fg="#e56477")
    s=s[:-1]
    if s=="":
        s="0"
    l0.configure(text=s)


def xdx(e):
    bbx.configure(bg="#d0d0d0") 
    xd()
def byyxdx(e):
    bbx.configure(bg="#d1d1d1")
def bxxxdx(e):
    bbx.configure(bg="#eaeaea")


def bxxxx(e):
    bbAC.configure(bg="#eaeaea",fg="#e56477")

    
def bxp(e):
    bbp.configure(bg="#d0d0d0")
    p()
def bxxp(e):
    bbp.configure(bg="#eaeaea")
def byyp(e):
    bbp.configure(bg="#d1d1d1")


def bxxsc(e):
    bbsc.configure(bg="#eaeaea")
def byysc(e):
    bbsc.configure(bg="#d1d1d1")
    
    


#UI

w=Tk()
w.configure(bg="#e86f6e")
w.title("CALCULATOR")


l0=Label(text="0",fg="#eaeaea",bg="#e86f6e",font=('AvenirNext LT Pro Regular',30),anchor="e",padx="15")
l1=Label(text=s1,fg="#f6c2b5",bg="#e86f6e",font=('AvenirNext LT Pro Regular',14),anchor="e",padx="15",pady="10")


bbAC=Button(w, text="AC",font=('AvenirNext LT Pro Regular',16),pady="15",padx="15",bd=0,bg="#eaeaea",fg="#e56477",activebackground="brown3",activeforeground="#eaeaea",command=AC)
bbsc=Button(w, text="±",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#eaeaea",fg="#3f4653",activebackground="#c1c1c1",command=sc)
bbp=Button(w, text="%",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#eaeaea",fg="#3f4653",activebackground="#c1c1c1",command=p)
bbd=Button(w, text="÷",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#eaeaea",fg="#3f4653",activebackground="#c1c1c1",command=d)
bb7=Button(w, text="7",font=('AvenirNext LT Pro Regular',16),pady="15",padx="15",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b7)
bb8=Button(w, text="8",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b8)
bb9=Button(w, text="9",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b9)
bbm=Button(w, text="✕",font=('AvenirNext LT Pro Regular',13),pady="15",padx="18",bd=0,bg="#eaeaea",fg="#3f4653",activebackground="#c1c1c1",command=m)
bb4=Button(w, text="4",font=('AvenirNext LT Pro Regular',16),pady="15",padx="15",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b4)
bb5=Button(w, text="5",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b5)
bb6=Button(w, text="6",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b6)
bbs=Button(w, text="−",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#eaeaea",fg="#3f4653",activebackground="#c1c1c1",command=sb)
bb1=Button(w, text="1",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b1)
bb2=Button(w, text="2",font=('AvenirNext LT Pro Regular',16),pady="15",padx="15",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b2)
bb3=Button(w, text="3",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b3)
bba=Button(w, text="+",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#eaeaea",fg="#3f4653",activebackground="#c1c1c1",command=a)
bb0=Button(w, text="0",font=('AvenirNext LT Pro Regular',16),pady="15",padx="18",bd=0,bg="#f4f4f4",fg="#3f4653",activebackground="#c1c1c1",command=b0)
bbx=Button(w, text=".",font=('AvenirNext LT Pro Regular',16),pady="15",padx="15",bd=0,bg="#eaeaea",fg="#3f4653",activebackground="#c1c1c1",command=xd)
bbe=Button(w, text="=",font=('Cambria',20),pady="10",padx="18",bd=0,bg="#e86f6e",fg="#eaeaea",activebackground="brown3",activeforeground="white",command=eq)




l0.grid(column=0,row=0,columnspan=4,rowspan=2,sticky="news",pady=(12,0))
l1.grid(column=0,row=3,columnspan=4,sticky="news")
bbAC.grid(column=0,row=4,sticky="news")
bbsc.grid(column=1,row=4,sticky="news")
bbp.grid(column=2,row=4,sticky="news")
bbd.grid(column=3,row=4,sticky="news")
bb7.grid(column=0,row=5,sticky="news")
bb8.grid(column=1,row=5,sticky="news")
bb9.grid(column=2,row=5,sticky="news")
bbm.grid(column=3,row=5,sticky="news")
bb4.grid(column=0,row=6,sticky="news")
bb5.grid(column=1,row=6,sticky="news")
bb6.grid(column=2,row=6,sticky="news")
bbs.grid(column=3,row=6,sticky="news")
bb1.grid(column=0,row=7,sticky="news")
bb2.grid(column=1,row=7,sticky="news")
bb3.grid(column=2,row=7,sticky="news")
bba.grid(column=3,row=7,sticky="news")
bb0.grid(column=0,row=8,columnspan=2,sticky="news")
bbx.grid(column=2,row=8,sticky="news")
bbe.grid(column=3,row=8,sticky="news")

#Keybindings
w.bind('1', bx1)
w.bind('<KeyRelease-1>',bxx1)
bb1.bind('<Leave>',bxx1)
bb1.bind('<Enter>',byy1)


w.bind('%',bxp)
w.bind('<KeyRelease-%>',bxxp)
bbp.bind('<Enter>',byyp)
bbp.bind('<Leave>',bxxp)


w.bind('2', bx2)
w.bind('<KeyRelease-2>',bxx2)
bb2.bind('<Leave>',bxx2)
bb2.bind('<Enter>',byy2)


w.bind('3', bx3)
w.bind('<KeyRelease-3>',bxx3)
bb3.bind('<Leave>',bxx3)
bb3.bind('<Enter>',byy3)


bbsc.bind('<Enter>',byysc)
bbsc.bind('<Leave>',bxxsc)


w.bind('4', bx4)
w.bind('<KeyRelease-4>',bxx4)
bb4.bind('<Leave>',bxx4)
bb4.bind('<Enter>',byy4)


w.bind('5', bx5)
w.bind('<KeyRelease-5>',bxx5)
bb5.bind('<Leave>',bxx5)
bb5.bind('<Enter>',byy5)


w.bind('6', bx6)
w.bind('<KeyRelease-6>',bxx6)
bb6.bind('<Leave>',bxx6)
bb6.bind('<Enter>',byy6)


w.bind('7', bx7)
w.bind('<KeyRelease-7>',bxx7)
bb7.bind('<Leave>',bxx7)
bb7.bind('<Enter>',byy7)


w.bind('8', bx8)
w.bind('<KeyRelease-8>',bxx8)
bb8.bind('<Leave>',bxx8)
bb8.bind('<Enter>',byy8)


w.bind('9', bx9)
w.bind('<KeyRelease-9>',bxx9)
bb9.bind('<Leave>',bxx9)
bb9.bind('<Enter>',byy9)


w.bind('0', bx0)
w.bind('<KeyRelease-0>',bxx0)
bb0.bind('<Leave>',bxx0)
bb0.bind('<Enter>',byy0)


w.bind('/', dx)
w.bind('<KeyRelease-/>',bxxdx)
bbd.bind('<Leave>',bxxdx)
bbd.bind('<Enter>',byyd)


w.bind('*', mx)
w.bind('<KeyRelease-*>',bxxmx)
bbm.bind('<Leave>',bxxmx)
bbm.bind('<Enter>',byym)


w.bind('-',sbx)
w.bind('<KeyRelease-->',bxxsbx)
bbs.bind('<Leave>',bxxsbx)
bbs.bind('<Enter>',byys)


w.bind('+',ax)
w.bind('<KeyRelease-+>',bxxax)
bba.bind('<Leave>',bxxax)
bba.bind('<Enter>',byya)


w.bind('=', eqx)
w.bind('<KeyRelease-=>',bxxeqx)
bbe.bind('<Leave>',bxxeqx)
bbe.bind('<Enter>',byye)


w.bind('.', xdx)
w.bind('<KeyRelease-.>',bxxxdx)
bbx.bind('<Leave>',bxxxdx)
bbx.bind('<Enter>',byyxdx)


w.bind('<Return>', eqx)
w.bind('<KeyRelease-Return>',bxxeqx)
bbe.bind('<Leave>',bxxeqx)
bbe.bind('<Enter>',byye)


w.bind('<BackSpace>', bcx)
w.bind('<KeyRelease-BackSpace>',bxxxx)
w.bind('<Delete>', acx)
w.bind('<KeyRelease-Delete>',bxxxx)
bbAC.bind('<Enter>',byyAC)
bbAC.bind('<Leave>',bxxxx)

#Uniform scaling of buttons accross the app
w.resizable(False, False)
w.grid_rowconfigure(0,weight=1)
w.grid_rowconfigure(1,weight=1)
w.grid_rowconfigure(2,weight=1)
w.grid_rowconfigure(3,weight=1)
w.grid_rowconfigure(4,weight=1)
w.grid_rowconfigure(5,weight=1)
w.grid_rowconfigure(6,weight=1)
w.grid_rowconfigure(7,weight=1)
w.grid_rowconfigure(8,weight=1)
w.grid_columnconfigure(0,weight=1)
w.grid_columnconfigure(1,weight=1)
w.grid_columnconfigure(2,weight=1)
w.grid_columnconfigure(3,weight=1)

w.mainloop()

# Coded by Soumyadwip