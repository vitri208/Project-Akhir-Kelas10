import tkinter as tk
from tkinter import ttk as tema
from tkinter.messagebox import showinfo
root = tk.Tk()
# saya tidak pakai ttkbootstrap karena tidak kedetect.
# import ttkbootstrap as tb

email = tk.StringVar()
passw = tk.StringVar()
agree = tk.BooleanVar()
errorinfocount = 0

def confirm():
  if agree.get() == True :
    h = f'Congratulations! The account is made.'
    showinfo(title='Accepted', message= h)
  else :
    if errorinfocount < 2 :
      h = f'Error, Try again. Tries left = {2 - errorinfocount}'
    else :
      h = 'Error, Try again. No tries left'
    errorcount()
    showinfo(title='Rejected', message= h)

def errorcount():
  global errorinfocount
  errorinfocount += 1
  if errorinfocount == 3 :
    root.destroy()

root.title('Create An Account')
root.geometry('400x400')
root.resizable(False, False)
root.config(bg='gray')

frame = tema.Frame(root)
frame.pack(padx= 10, pady=10, fill='x', expand=True)

label = tk.Label(frame, text='Create An Account', font=('arial', 16, 'bold'))
label.pack(padx= 10, pady=20, fill='x', expand=True)

labelEmail = tema.Label(frame, text='Email :')
labelEmail.pack(padx=10, pady=0, fill='x', expand=True)
formEmail = tema.Entry(frame, textvariable= email)
formEmail.pack(padx=10, pady=5, fill='x', expand=True)

labelPass = tema.Label(frame, text='Password :')
labelPass.pack(padx=10, pady=0, fill='x', expand=True)
formPass = tema.Entry(frame,show='*', textvariable= passw)
formPass.pack(padx=10, pady=5, fill='x', expand=True)

stj = tema.Checkbutton(frame, variable= agree, text='I have read and agree with the terms of service', onvalue=1,offvalue=0)
stj.pack(padx=10, fill='x', expand=True)

Btn = tema.Button(frame, text='Confirm', command=confirm)
Btn.pack(padx=10, pady=5, fill='x',expand=True)

DTY = tema.Button(frame, text='EXIT', command=root.destroy)
DTY.pack(padx=80, pady=5, fill='x', expand=True)

root.mainloop()