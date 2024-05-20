import tkinter as tk
from tkinter import *

root = tk.Tk()
root.wm_title('SI JAGO PARKIR')
root.geometry('900x500')
root.configure(bg="#fff")

gambar_kiri=PhotoImage(file='KELOMPOK 12/LOGO LOGIN.png')

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)
Label(root,image=gambar_kiri,bg='white').place(x=-5,y=-50)

heading=Label(frame,text='Masuk',fg='red',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=5)

username = Entry(frame,width=25,fg='grey',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
username.place(x=30,y=80)
username.insert(0,'Tulis Username Anda')

username = Entry(frame,width=25,fg='grey',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
username.place(x=30,y=140)
username.insert(0,'Tulis Password Anda')

Frame(frame,width=300,height=2,bg='black').place(x=25,y=110)
Frame(frame,width=300,height=2,bg='black').place(x=25,y=170)
Button(frame,width=39,pady=7,text='sign in',bg='#de2b28',cursor='hand2',fg='white',border=0).place(x=35,y=205)
akun=Label(frame,text='Tidak memiliki akun SI JAGO PARKIR?',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
akun.place(x=62,y=250)
daftar=Button(frame,width=16,text='Daftar sekarang!',border=0,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'))
daftar.place(x=110,y=270)

copy=Label(root,text='Kelompok 12 Nexus Copyright @2024',fg='navy',border=0,bg='white',font=('Microsoft YaHei UI Light',9,'italic'))
copy.place(x=350,y=420)

root.mainloop()
