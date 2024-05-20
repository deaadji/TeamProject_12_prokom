import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv

root = tk.Tk()
root.wm_title('SI JAGO PARKIR')
root.geometry('900x500')
root.configure(bg="#fff")
root.resizable(False,False)

#fungsi utama login screen
def daftar_CMD():
    usernama=username.get()
    paswed=password.get()

    if usernama=='admoon' and paswed=='halo dunia':
        print("ahayy")
        Main_menu()
    elif usernama!='admoon' and paswed!='halo dunia':
        messagebox.showerror("Tidak Ditemukan","Username dan/atau Password salah. pastikan kapital dan spasi tepat")
    elif usernama!='admoon':
        messagebox.showerror("Tidak Ditemukan","Username salah. pastikan kapital dan spasi tepat")
    elif paswed!='halo dunia':
        messagebox.showerror("Tidak Ditemukan","Password salah. pastikan kapital dan spasi tepat")

#main menu tapi blom jadi 
def Main_menu():
    screen1=Toplevel(root)
    screen1.title("woke")
    screen1.geometry('925x500')
    screen1.config(bg='white')

    Label(screen1,text='Awikwok',bg='white', font=('Calibri(body)',50,'bold')).pack(expand=True)

    screen1.mainloop()

#===================================================================
#GUI login screen
#===================================================================


#bug disini, janlup directory nya
gambar_kiri=PhotoImage(file='TeamProject_12_prokom/KELOMPOK 12/LOGO LOGIN.png')

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)
Label(root,image=gambar_kiri,bg='white').place(x=-5,y=-50)

heading=Label(frame,text='Masuk',fg='red',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=5)

def on_enter(e):
    username.delete(0, "end")

def on_leave(e):
    name=username.get()
    if name=='':
        username.insert(0,'Tulis Username Anda')
    
        
username = Entry(frame,width=25,fg='grey',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
username.place(x=30,y=80)
username.insert(0,'Tulis Username Anda')
username.bind('<FocusIn>', on_enter)
username.bind('<FocusOut>', on_leave)

def on_enter(e):
    password.delete(0, "end")

def on_leave(e):
    name=username.get()
    if name=='':
        password.insert(0,'Tulis Password Anda')
password = Entry(frame,width=25,fg='grey',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
password.place(x=30,y=140)
password.insert(0,'Tulis Password Anda')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame,width=300,height=2,bg='black').place(x=25,y=110)
Frame(frame,width=300,height=2,bg='black').place(x=25,y=170)
Button(frame,width=39,pady=7,text='sign in',bg='#de2b28',cursor='hand2',fg='white',border=0,command=daftar_CMD).place(x=35,y=205)
akun=Label(frame,text='Tidak memiliki akun SI JAGO PARKIR?',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
akun.place(x=62,y=250)
daftar=Button(frame,width=16,text='Daftar sekarang!',border=0,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'))
daftar.place(x=110,y=270)

copy=Label(root,text='Kelompok 12 Nexus Copyright @2024',fg='navy',border=0,bg='white',font=('Microsoft YaHei UI Light',9,'italic'))
copy.place(x=350,y=420)

root.mainloop() 

