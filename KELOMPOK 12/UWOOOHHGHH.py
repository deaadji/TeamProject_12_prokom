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
def login_CMD():
    usernama=username.get()
    paswed=password.get()

    with open("users.csv", mode="r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            if row == [usernama,paswed]:
                Main_menu()
            elif row!= [usernama,paswed]:
                messagebox.showerror("Tidak Ditemukan","Username dan/atau Password salah. pastikan kapital dan spasi tepat")


    if usernama=='admoon' and paswed=='halo dunia':
        Main_menu()
    elif usernama!='admoon' and paswed!='halo dunia':
        messagebox.showerror("Tidak Ditemukan","Username dan/atau Password salah. pastikan kapital dan spasi tepat")
    elif usernama!='admoon':
        messagebox.showerror("Tidak Ditemukan","Username salah. pastikan kapital dan spasi tepat")
    elif paswed!='halo dunia':
        messagebox.showerror("Tidak Ditemukan","Password salah. pastikan kapital dan spasi tepat")


#=====================================================================================
#main menu tapi blom jadi 


def Main_menu():
    screen1=Toplevel(root)
    screen1.title("woke")
    m = screen1.maxsize()
    screen1.geometry('{}x{}+0+0'.format(*m))
    screen1.config(bg='white')

    Label(screen1,text='Awikwok',bg='white', font=('Calibri(body)',50,'bold')).pack(expand=True)

    screen1.mainloop()






#=======================================================
# MAIN REGISTER WINDOW

def register():
    daftar_screen=Toplevel(root)
    daftar_screen.title("DAFTAR")
    daftar_screen.geometry('625x500')
    daftar_screen.config(bg='white')

    def on_enter(e):
        username_daftar.delete(0, "end")

    def on_leave(e):
        name=username_daftar.get()
        if name=='':
            username_daftar.insert(0,'Tulis Username Anda')
    
    Frame(daftar_screen,width=300,height=2,bg='black').place(x=165,y=270)
    Frame(daftar_screen,width=300,height=2,bg='black').place(x=165,y=340)

    username_daftar = Entry(daftar_screen,width=25,fg='grey',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    username_daftar.place(x=180,y=240)
    username_daftar.insert(0,'Tulis Username Anda')
    username_daftar.bind('<FocusIn>', on_enter)
    username_daftar.bind('<FocusOut>', on_leave)

    def on_enter(e):
        password_daftar.delete(0, "end")

    def on_leave(e):
        name=password_daftar_daftar.get()
        if name=='':
            password_daftar.insert(0,'Tulis Password Anda')
    password_daftar = Entry(daftar_screen,width=25,fg='grey',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    password_daftar.place(x=180,y=310)
    password_daftar.insert(0,'Tulis Password Anda')
    password_daftar.bind('<FocusIn>', on_enter)
    password_daftar.bind('<FocusOut>', on_leave)

    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f,delimiter=",")
        email= "admoon"
        passuword = "halo dunia"
        def daftar_fungsi():
            if username=="":
                messagebox.showerror("Invalid","Masukan Username dan Password terlebih dahulu")
            elif password=="":
                messagebox.showerror("Invalid","Masukan Username dan Password terlebih dahulu")
            else:
                writer.writerow(email,passuword)
        daftar=Button(daftar_screen,width=16,text='DAFTAR',border=0,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=daftar_fungsi)
        daftar.place(x=244,y=370)
        #print("Registration is succesful!")
        ##   print("Please try again!")
    



#===================================================================
#GUI login screen
#===================================================================


#bug disini, janlup directory nya
gambar_kiri=PhotoImage(file='KELOMPOK 12/LOGO LOGIN.png')

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
Button(frame,width=39,pady=7,text='sign in',bg='#de2b28',cursor='hand2',fg='white',border=0,command=login_CMD).place(x=35,y=205)
akun=Label(frame,text='Tidak memiliki akun SI JAGO PARKIR?',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
akun.place(x=62,y=250)
daftar=Button(frame,width=16,text='Daftar sekarang!',border=0,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=register)
daftar.place(x=110,y=270)

copy=Label(root,text='Kelompok 12 Nexus Copyright @2024',fg='navy',border=0,bg='white',font=('Microsoft YaHei UI Light',9,'italic'))
copy.place(x=350,y=420)

root.mainloop() 

