from tkinter import *

def calPercentage():
    res=int(e1.get()) / int(e2.get()) * 100
    myText.set(res)
 
master = Tk()
myText=StringVar();
Label(master, text="Scored Marks").grid(row=0, sticky=W)
Label(master, text="Out of Marks").grid(row=1, sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)
e2 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(master, text='Quit', command=master.destroy)
b1.grid(row=4,column=3, sticky=W)

b2 = Button(master, text="Calculate", command=calPercentage)
b2.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)


        
