import tkinter
import re
window = tkinter.Tk()
window.geometry("300x300")

def pwvalidate():
    pwd = txt.get()
    m1 = re.findall(r'[0-9]',pwd)
    m2 = re.findall(r'[a-z]',pwd)
    m3 = re.findall(r'[A-Z]',pwd)
    m4 = re.findall(r'[!@#$%^&*--=+]',pwd)
    if m1 and m2 and m3 and m4 and 6<=len(pwd)<=16:
        l1.configure(text='password is strong!')
    else:
        l1.configure(text='password is weaK!')

    


txt = tkinter.Entry()
txt.grid(column=0,row=0)

btn = tkinter.Button(window,text="validate",command=pwvalidate)
btn.grid(column=0,row=1)

l1 = tkinter.Label(window,text = "I will show result of validation!")
l1.grid(column=0,row=2)


window.mainloop()