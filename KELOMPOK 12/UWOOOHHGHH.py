import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
from datetime import datetime, timedelta
import random

root = tk.Tk()
root.wm_title('SI JAGO PARKIR')
root.geometry('900x500+168+156')
root.configure(bg="#fff")
root.resizable(False,False)

#===================================================
#fungsi utama login screen
#===================================================
def login_CMD():
    usernama=username.get()
    paswed=password.get()

    with open("users_akun.csv", mode="r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            if usernama == row[0] and paswed == row[1]:
                Main_menu()
                return True
    messagebox.showerror("Tidak Ditemukan","Username dan/atau Password salah. pastikan kapital dan spasi tepat")
    return False 


#=======================================================
# MAIN REGISTER WINDOW
#=======================================================
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
            with open("users_akun.csv", mode="r") as f:
                reader = csv.reader(f,delimiter=",")
                for row in reader:
                    if usernama_daftar == row[0] and paswed_daftar == row[1]:
                        messagebox.showerror("Invalid","Username dan Password sudah terdaftar",master=daftar_screen)
                        return True
                    else :
                        break
            #fungsi utama
            if usernama_daftar=="" and paswed_daftar=="":
                messagebox.showerror("Invalid","Masukan Username dan Password terlebih dahulu", master=daftar_screen)
            elif paswed_daftar=="":
                messagebox.showerror("Invalid","Masukan Username dan Password terlebih dahulu",master=daftar_screen)
            elif usernama_daftar=="":
                messagebox.showerror("Invalid","Masukan Username dan Password terlebih dahulu",master=daftar_screen)
            elif True :
                with open("users_akun.csv", mode="a", newline="") as f:
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
try:
    gambar_kiri = PhotoImage(file='KELOMPOK 12/LOGO LOGIN.png')
    tk.Label(root, image=gambar_kiri, bg='white').place(x=-5, y=-50)
except tk.TclError:
    print("Image file not found. Check the path to 'LOGO LOGIN.png'.")

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)
Label(root,image=gambar_kiri,bg='white').place(x=-5,y=-50)

masuk=Label(frame,text='Masuk',fg='red',bg='white',font=('century gothic',23))
masuk.place(x=125,y=10)

def on_enter_username(e):
    if username.get() == 'Tulis Username Anda':
        username.delete(0, "end")
        username.config(fg='black')

def on_leave_username(e):
    if not username.get():
        username.insert(0, 'Tulis Username Anda')
        username.config(fg='grey')
        

username = Entry(frame,width=25,fg='grey',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
username.place(x=30,y=80)
username.insert(0,'Tulis Username Anda')
username.bind('<FocusIn>', on_enter_username)
username.bind('<FocusOut>', on_leave_username)

def on_enter_password(e):
    if password.get() == 'Tulis Password Anda':
        password.delete(0, "end")
        password.config(fg='black', show='*')

def on_leave_password(e):
    if not password.get():
        password.insert(0, 'Tulis Password Anda')
        password.config(fg='grey', show='')

password = Entry(frame,width=25,fg='grey',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
password.place(x=30,y=140)
password.insert(0,'Tulis Password Anda')
password.bind('<FocusIn>', on_enter_password)
password.bind('<FocusOut>', on_leave_password)

# Checkbox to toggle password visibility
show_password_var = tk.IntVar()

def toggle_password():
    if show_password_var.get():
        password.config(show='')
    else:
        password.config(show='*')

show_password_check = tk.Checkbutton(frame, text="Show Password", variable=show_password_var, onvalue=1, offvalue=0, command=toggle_password, bg='white', fg='black', font=('Microsoft YaHei UI Light', 10))
show_password_check.place(x=30, y=170)

Frame(frame,width=300,height=2,bg='black').place(x=25,y=110)
Frame(frame,width=300,height=2,bg='black').place(x=25,y=170)
Button(frame,width=39,pady=7,text='sign in',bg='#de2b28',cursor='hand2',fg='white',border=0,command=login_CMD).place(x=35,y=205)
akun=Label(frame,text='Tidak memiliki akun SI JAGO PARKIR?',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
akun.place(x=62,y=250)
daftar=Button(frame,width=16,text='Daftar sekarang!',border=0,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=register)
daftar.place(x=110,y=270)

copy=Label(root,text='Kelompok 12 Nexus Copyright @2024',fg='navy',border=0,bg='white',font=('Microsoft YaHei UI Light',9,'italic'))
copy.place(x=330,y=420)



#===============================================================
#-- MAIN MENU --
#===============================================================
def Main_menu():
    #untuk hide login screen
    root.withdraw()

    screen1=Toplevel(root)
    screen1.title("MAIN MENU")
    m = screen1.maxsize()
    screen1.geometry('{}x{}+0+0'.format(*m))
    screen1.config(bg='white')
    screen1.overrideredirect(True)

    #label waktu
    def jam_time():
        current_time = datetime.now().strftime('%H:%M:%S')  
        time_label.config(text=current_time) 
        screen1.after(1000, jam_time)

    def hari_time():
        current_time = datetime.now().strftime('%A, %B %d 20%y')  
        hari_label.config(text=current_time) 
        screen1.after(1000, jam_time)

    time_label = tk.Label(screen1, bg='white', text="", font=("century gothic", 30))
    time_label.place(x=890,y=120)
    hari_label = tk.Label(screen1, bg='white', text="", font=("century gothic", 20))
    hari_label.place(x=530,y=133)
    jam_time()
    hari_time()

    #===============================
    about_btn = tk.Button(screen1, text="about", font=("century gothic", 25), fg="Red", bd=0, bg="White", command=ini_about)
    about_btn.place(x=20, y=165)

    menu_indicate = tk.Label(screen1, text="", bg="Red")
    menu_indicate.place(x=3, y=179, width=5, height=40)

    exit_btn = tk.Button(screen1, text="Keluar", font=("century gothic", 25), fg="Red", bd=0, bg="White", command=confirm_exit)
    exit_btn.place(x=20, y=228)

    menu_indicate = tk.Label(screen1, text="", bg="Red")
    menu_indicate.place(x=3, y=245, width=5, height=40)

    masuk_btn = tk.Button(screen1, text='Kendaraan masuk', fg='white', width=45, height=10, bd=0, bg="red", command=Kendaraan_baru)
    masuk_btn.place(x=1140, y=30)

    keluar_btn = tk.Button(screen1, text='Kendaraan keluar dan CEK', fg='white', width=45, height=10, bd=0, bg="red", command=parkir_keluar)
    keluar_btn.place(x=1140, y=280)

    cek_btn = tk.Button(screen1,text='cek kapasitas', fg='white', width=45, height=10, bd=0, bg="red",command=laporan)
    cek_btn.place(x=1140, y=550)

    layar_gede = tk.Frame(screen1, highlightbackground= "black", highlightthickness=5,bg="white")

    layar_gede.place(x=150,y=178)
    layar_gede.pack_propagate(False)
    layar_gede.configure(height=500, width=900)

    try:
        gambar_judul = PhotoImage(file='KELOMPOK 12/MENU_LABEL.png')
        tk.Label(screen1, image=gambar_judul, bg='white').place(x=15, y=10)
    except tk.TclError:
        print("Image file not found. Check the path to 'MENU_LABEL.png'.")
    screen1.mainloop()


#==========================================================
#fungsi waktu, demi masa, wal-ashr
#==========================================================
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

filename = 'MAIN_data_waktu.csv'
def nulis_waktu_tanggal():
    write_current_datetime(filename)

def ngasi_waktu_tanggal():
    elapsed_hours, elapsed_minutes, elapsed_seconds = calculate_elapsed_time(filename)
    print(f"\nElapsed time since data was stored:")
    print(f"{elapsed_hours} hours, {elapsed_minutes} minutes, {elapsed_seconds} seconds")


#======================================================
#
#fungsi-fungsi main menu
#
#======================================================
def Kendaraan_baru():
    nambah_screen=Toplevel(root)
    nambah_screen.title("KENDARAAN BARU")
    nambah_screen.geometry('880x480+158+190')
    nambah_screen.configure(bg="white")
    nambah_screen.resizable(False,False)
    nambah_screen.overrideredirect(True)

    kota_nopol = Entry(nambah_screen,width=5,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',30))
    kota_nopol.place(x=130,y=110)

    inp_nopol = Entry(nambah_screen,width=15,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',30))
    inp_nopol.place(x=270,y=110)

    kode_unik_entry = Entry(nambah_screen,width=15,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',30))
    kode_unik_entry.place(x=130,y=220)
    
    tk.Label(nambah_screen, text='kode kota', bg='white', font=('Calibri', 14)).place(x=130,y=80)
    tk.Label(nambah_screen, text='kode plat', bg='white', font=('Calibri', 14)).place(x=270,y=80)
    tk.Label(nambah_screen, text='kode unik', bg='white', font=('Calibri', 14)).place(x=130,y=190)
    tk.Label(nambah_screen, text='DISINI KENDARAAN MASUK', bg='white', font=('Calibri', 20)).pack(pady=20)

    def save_data():
        plate_kode = (kota_nopol.get()+ ' ' +inp_nopol.get())
        code = random.randint(100000, 999999)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if kota_nopol.get()=='' or inp_nopol.get()=='':
            messagebox.showerror(title='gagal!', message='Nopol tidak boeh kocong ')
        elif plate_kode:
            with open("parking_data2.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([plate_kode, code, current_time])
            kota_nopol.delete(0, tk.END) 
            inp_nopol.delete(0, tk.END)  
            messagebox.showinfo(title='Sukses!', message='Berhasil menyimpan!')
        else:
            messagebox.showerror(title='gagal!', message='gagal menyimpan!\npastikan nopol benar')

    Simpan=Button(nambah_screen,width=16,text='Simpan',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=save_data)
    Simpan.place(x=134,y=300)


    def read_data():
        data = []
        try:
            with open("parking_data2.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist

        # Display data in a new window
        display_window = tk.Tk()
        display_window.title("KENDARAAN PARKIR SAAT INI")

        data_text = "Plat Nomor\tkode Unik\t\tWaktu Masuk\n"
        for row in data:
            data_text += f"{row[0]}\t\t{row[1]}\t\t{row[2]}\n"

        data_label = tk.Label(display_window, text=data_text, font=("Microsoft YaHei UI Light", 12))
        data_label.pack()

        display_window.mainloop()
    
    liat_data=Button(nambah_screen,width=16,text='liat',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=read_data)
    liat_data.place(x=134,y=350)
    
        
def parkir_keluar():
    parkir_screen=Toplevel(root)
    parkir_screen.title("KENDARAAN KELUAR DAN CEK")
    parkir_screen.geometry('880x480+158+190')
    parkir_screen.configure(bg="white")
    parkir_screen.resizable(False,False)
    parkir_screen.overrideredirect(True)
    tk.Label(parkir_screen, text='DISINI KENDARAAN KELUAR', bg='white', font=('Calibri', 20)).pack(pady=20)

    cek_box = Entry(parkir_screen,width=12,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',30))
    cek_box.place(x=90,y=90)

    tk.Label(parkir_screen, text='Nopol atau Kode Unik', bg='white', font=('Calibri', 14)).place(x=90,y=56)


    def search_data():
        search_value = cek_box.get()  # Get search value

        found_data = None
        try:
            with open("parking_data2.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    if (row[0] == search_value) or \
                    (row[1] == search_value):
                        found_data = row
                        break  # Stop after finding the first match
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist

        if found_data:
            search_result_text = (f"Ditemukan!\nPlat Nomor  : {found_data[0]}\nKode Unik    : {found_data[1]}\nWaktu Masuk   : {found_data[2]}")
        else:
            search_result_text = f"Tidak ada nopol {search_value} di parkiran"

        # Display search result
        search_result_window=Toplevel(root)
        search_result_window.geometry('880x310+158+340')
        search_result_window.configure(bg="light grey")
        search_result_window.resizable(False,False)
        search_result_window.overrideredirect(True)

        search_result_label = tk.Label(search_result_window, text=search_result_text,bg='white',font=("Century Gothic", 17),justify="left")
        search_result_label.place(x=40,y=40)

        search_result_window.mainloop()
    
    cek_data=Button(parkir_screen,width=16,text='CEK',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'),command=search_data)
    cek_data.place(x=430,y=100)


def laporan():
    laporan_screen=Toplevel(root)
    laporan_screen.title("CEK KAPASITAS")
    laporan_screen.geometry('880x480+158+190')
    laporan_screen.configure(bg="white")
    laporan_screen.resizable(False,False)
    laporan_screen.overrideredirect(True)

    tk.Label(laporan_screen, text='DISINI KAPASITASNYA SEGINI', bg='white', font=('Calibri', 20)).pack(pady=20)

def confirm_exit():
    response = messagebox.askyesno("Konfirmasi Keluar", "Apakah Anda yakin ingin keluar?")
    if response:
        root.destroy()

def ini_about():
    abot_bosku=Toplevel(root)
    abot_bosku.geometry('880x480+158+190')
    abot_bosku.configure(bg="#fff")
    abot_bosku.resizable(False,False)
    abot_bosku.overrideredirect(True)

    about_label = Label(abot_bosku, text=info_about, font=("Microsoft YaHei UI Light", 16), bg="white")
    about_label.pack()

info_about = (
    "Si Jago Parkir\n"
    "Developer: Kelompok 12 Nexus 2023\n"
    " \n"
    "MAINFRAME DEVELOPER\n"
    "Adji Kusuma\n"
    " \n"
    "CODE SUPERVISOR \n"
    "Ivan vadilah\n"
    " \n"
    "BACKEND FRAME BUILDER\n"
    "Irma Arisa\n"
    " \n"
    "Copyright @2024 Kelompok 12 Nexus\n"
    )


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

