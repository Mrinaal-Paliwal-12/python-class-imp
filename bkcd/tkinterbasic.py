import tkinter
window = tkinter.Tk()
window.title("GUI")



def clicked():
    name = "Hello "+txt.get()
    l1.configure(text = name)

l1 = tkinter.Label(window,text = "Hello world!", font=("Arial Bold",50))
l1.grid(column=0,row=0)

b1 = tkinter.Button(window,text = "enter" , bg='orange', fg='red', font=("Arial Bold",50), command=clicked)
b1.grid(column=1,row=0)

txt = tkinter.Entry(window,width=10)
txt.grid(column=2,row=0)



window.geometry('950x500')
window.mainloop()