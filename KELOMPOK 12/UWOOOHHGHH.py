import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
from datetime import datetime, timedelta

root = tk.Tk()
root.wm_title('SI JAGO PARKIR')
root.geometry('900x500')
root.configure(bg="#fff")
root.resizable(False,False)

#===================================================
#fungsi utama login screen jadiiiiiiii UWOGHHHHH ^0^
#===================================================

def login_CMD():
    usernama=username.get()
    paswed=password.get()

    with open("users.csv", mode="r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            if usernama == row[0] and paswed == row[1]:
                Main_menu()
                return True
    messagebox.showerror("Tidak Ditemukan","Username dan/atau Password salah. pastikan kapital dan spasi tepat")
    return False 

#=======================================================
# MAIN REGISTER WINDOW

def register():
    daftar_screen=Toplevel(root)
    daftar_screen.title("DAFTAR")
    daftar_screen.geometry('625x500')
    daftar_screen.config(bg='white')
    
    Frame(daftar_screen,width=280,height=2,bg='black').place(x=165,y=250)
    Frame(daftar_screen,width=280,height=2,bg='black').place(x=165,y=320)

    username_daftar = Entry(daftar_screen,width=25,fg='black',border=0,bg='#dee0df',font=('Microsoft YaHei UI light',13))
    username_daftar.place(x=180,y=220)
    username_daftar.insert(0,'')
    
    password_daftar = Entry(daftar_screen,width=25,fg='black',border=0,bg='#dee0df',font=('Microsoft YaHei UI light',13))
    password_daftar.place(x=180,y=290)
    password_daftar.insert(0,'')
   
    def daftar_fungsi():
            usernama_daftar=username_daftar.get()
            paswed_daftar=password_daftar.get()
            #kalo paswed dan user ada di data
            with open("users.csv", mode="r") as f:
                reader = csv.reader(f,delimiter=",")
                for row in reader:
                    if usernama_daftar == row[0] and paswed_daftar == row[1]:
                        messagebox.showerror("Invalid","Username dan Password sudah terdaftar",master=daftar_screen)
                        return True
            #fungsi utama
            if usernama_daftar=="":
                messagebox.showerror("Invalid","Masukan Username dan Password terlebih dahulu", master=daftar_screen)
            elif paswed_daftar=="":
                messagebox.showerror("Invalid","Masukan Username dan Password terlebih dahulu",master=daftar_screen)
            else:
                with open("users.csv", mode="a", newline="") as f:
                    writer = csv.writer(f,delimiter=",")
                    writer.writerow([usernama_daftar, paswed_daftar])
            messagebox.showinfo('Sukses!','Akun username dan Password baru sudah terdaftar')
            daftar_screen.destroy()
          
    daftar=Button(daftar_screen,width=16,text='DAFTAR',border=0,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=daftar_fungsi)
    daftar.place(x=244,y=370)

    tulis_username=Label(daftar_screen,text='Username :',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    tulis_username.place(x=172,y=195)
    tulis_password=Label(daftar_screen,text='Password :',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    tulis_password.place(x=172,y=265)

#===================================================================
#GUI login screen
#===================================================================


#bug disini, janlup directory nya
gambar_kiri=PhotoImage(file='TeamProject_12_prokom/KELOMPOK 12/LOGO LOGIN.png')

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)
Label(root,image=gambar_kiri,bg='white').place(x=-5,y=-50)

masuk=Label(frame,text='Masuk',fg='red',bg='white',font=('century gothic',23))
masuk.place(x=125,y=10)

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
    name=password.get()
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
copy.place(x=330,y=420)

#====================================================================
#main menu ////// tapi blom jadi 


def Main_menu():
    screen1=Toplevel(root)
    screen1.title("woke")
    m = screen1.maxsize()
    screen1.geometry('{}x{}+0+0'.format(*m))
    screen1.config(bg='white')


    home_btn = tk.Button(screen1, text="Home", font=("Microsoft YaHei UI Light", 25), fg="Red", bd=0, bg="White")
    home_btn.place(x=20, y=95)

    home_indicate = tk.Label(screen1, text="", bg="Red")
    home_indicate.place(x=3, y=105, width=5, height=40)

    menu_btn = tk.Button(screen1, text="Menu", font=("Microsoft YaHei UI Light", 25), fg="Red", bd=0, bg="White")
    menu_btn.place(x=20, y=165)

    menu_indicate = tk.Label(screen1, text="", bg="Red")
    menu_indicate.place(x=3, y=155, width=5, height=40)

    about_btn = tk.Button(screen1, text="About", font=("Microsoft YaHei UI Light", 25), fg="Red", bd=0, bg="White")
    about_btn.place(x=20, y=225)

    menu_indicate = tk.Label(screen1, text="", bg="Red")
    menu_indicate.place(x=3, y=205, width=5, height=40)

    pil1_btn = tk.Button(screen1, width=45, height=10, bd=0, bg="red")
    pil1_btn.place(x=1140, y=30)

    pil2_btn = tk.Button(screen1, width=45, height=10, bd=0, bg="red")
    pil2_btn.place(x=1140, y=280)

    pil3_btn = tk.Button(screen1, width=45, height=10, bd=0, bg="red")
    pil3_btn.place(x=1140, y=550)

    main_frame = tk.Frame(screen1, highlightbackground= "black", highlightthickness=5)

    main_frame.place(x=150,y=120)
    main_frame.pack_propagate(False)
    main_frame.configure(height=500, width=900)

    screen1.mainloop()


#==========================================================
#fungsi waktu, demi waktu, wal-ashr

def write_current_datetime(filename):
  with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Time'])

    current_datetime = datetime.now()
    writer.writerow([current_datetime.strftime("%Y-%m-%d"), current_datetime.strftime("%H:%M:%S")])

def calculate_elapsed_time(filename):
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row

    for row in reader:
      date_str, time_str = row
      datetime_stored = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
      break  # Assuming only one row of data

  now = datetime.now()
  elapsed = now - datetime_stored
  hours = elapsed.seconds // 3600
  minutes = (elapsed.seconds % 3600) // 60
  seconds = elapsed.seconds % 60
  return hours, minutes, seconds

filename = 'baru_data_waktu.csv'
def nulis_waktu_tanggal():
    write_current_datetime(filename)
    print(f"Current date and time written to {filename}")

def ngasi_waktu_tanggal():
    elapsed_hours, elapsed_minutes, elapsed_seconds = calculate_elapsed_time(filename)
    print(f"\nElapsed time since data was stored:")
    print(f"{elapsed_hours} hours, {elapsed_minutes} minutes, {elapsed_seconds} seconds")

root.mainloop() 

#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⠀⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀ amogus
#⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀ 
#⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣿⣷⠀ 
#⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⡇⠀ 
#⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀ 
#⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⠀ 
#⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀ 
#⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
#⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ 
#⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀ 
#⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀ 
#⠀⠀⠛⢿⣿⣿⣿⣿ ⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿ ⠀⠈⠻⣿⣿⣿⣿⡿⠀⠀⠀⠀ 
#⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

