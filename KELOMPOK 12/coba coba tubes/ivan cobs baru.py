import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
from datetime import datetime

# Initialize root window
root = tk.Tk()
root.wm_title('SI JAGO PARKIR')
root.geometry('900x500+168+156')
root.configure(bg="#fff")
root.resizable(False, False)

#===================================================
# Fungsi utama login screen jadiiiiiiii UWOGHHHHH ^0^
#===================================================

def login_CMD():
    usernama = username.get()
    paswed = password.get()

    with open("users_akun.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if usernama == row[0] and paswed == row[1]:
                Main_menu()
                return True
    messagebox.showerror("Tidak Ditemukan", "Username dan/atau Password salah. Pastikan kapital dan spasi tepat.")
    return False 

#=======================================================
# MAIN REGISTER WINDOW
#=======================================================
def register():
    daftar_screen = Toplevel(root)
    daftar_screen.title("DAFTAR")
    daftar_screen.geometry('625x500')
    daftar_screen.config(bg='white')
    
    Frame(daftar_screen, width=280, height=2, bg='black').place(x=165, y=250)
    Frame(daftar_screen, width=280, height=2, bg='black').place(x=165, y=320)

    username_daftar = Entry(daftar_screen, width=25, fg='black', border=0, bg='#dee0df', font=('Microsoft YaHei UI light', 13))
    username_daftar.place(x=180, y=220)
    username_daftar.insert(0, '')
    
    password_daftar = Entry(daftar_screen, width=25, fg='black', border=0, bg='#dee0df', font=('Microsoft YaHei UI light', 13))
    password_daftar.place(x=180, y=290)
    password_daftar.insert(0, '')
   
    def daftar_fungsi():
        usernama_daftar = username_daftar.get()
        paswed_daftar = password_daftar.get()
        with open("users_akun.csv", mode="r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if usernama_daftar == row[0] and paswed_daftar == row[1]:
                    messagebox.showerror("Invalid", "Username dan Password sudah terdaftar", master=daftar_screen)
                    return
        if usernama_daftar == "" or paswed_daftar == "":
            messagebox.showerror("Invalid", "Masukan Username dan Password terlebih dahulu", master=daftar_screen)
        else:
            with open("users_akun.csv", mode="a", newline="") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([usernama_daftar, paswed_daftar])
            messagebox.showinfo('Sukses!', 'Akun username dan Password baru sudah terdaftar')
            daftar_screen.destroy()
          
    daftar = Button(daftar_screen, width=16, text='DAFTAR', border=0, bg='white', cursor='hand2', font=('Microsoft YaHei UI Light', 8, 'bold'), command=daftar_fungsi)
    daftar.place(x=244, y=370)

    tulis_username = Label(daftar_screen, text='Username :', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    tulis_username.place(x=172, y=195)
    tulis_password = Label(daftar_screen, text='Password :', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    tulis_password.place(x=172, y=265)

#===================================================================
# GUI login screen
#===================================================================
try:
    gambar_kiri = PhotoImage(file='KELOMPOK 12/LOGO LOGIN.png')
    tk.Label(root, image=gambar_kiri, bg='white').place(x=-5, y=-50)
except tk.TclError:
    print("Image file not found. Check the path to 'LOGO LOGIN.png'.")

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

masuk = Label(frame, text='Masuk', fg='red', bg='white', font=('century gothic', 23))
masuk.place(x=125, y=10)

def on_enter_username(e):
    if username.get() == 'Tulis Username Anda':
        username.delete(0, "end")
        username.config(fg='black')

def on_leave_username(e):
    if not username.get():
        username.insert(0, 'Tulis Username Anda')
        username.config(fg='grey')
        
username = Entry(frame, width=25, fg='grey', border=0, bg='white', font=('Microsoft YaHei UI Light', 13))
username.place(x=30, y=80)
username.insert(0, 'Tulis Username Anda')
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

password = Entry(frame, width=25, fg='grey', border=0, bg='white', font=('Microsoft YaHei UI Light', 13))
password.place(x=30, y=140)
password.insert(0, 'Tulis Password Anda')
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

Frame(frame, width=300, height=2, bg='black').place(x=25, y=110)
Frame(frame, width=300, height=2, bg='black').place(x=25, y=170)
Button(frame, width=39, pady=7, text='sign in', bg='#de2b28', cursor='hand2', fg='white', border=0, command=login_CMD).place(x=35, y=205)
akun = Label(frame, text='Tidak memiliki akun SI JAGO PARKIR?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
akun.place(x=62, y=250)
daftar = Button(frame, width=16, text='Daftar sekarang!', border=0, bg='white', cursor='hand2', font=('Microsoft YaHei UI Light', 8, 'bold'), command=register)
daftar.place(x=110, y=270)

copy = Label(root, text='Kelompok 12 Nexus Copyright @2024', fg='navy', border=0, bg='white', font=('Microsoft YaHei UI Light', 9, 'italic'))
copy.place(x=330, y=420)

#===============================================================
#-- MAIN MENU --
#===============================================================
def Main_menu():
    root.withdraw()
    screen1 = Toplevel(root)
    screen1.title("MAIN MENU")
    screen1.geometry("1280x720+0+0")
    screen1.config(bg='white')
    screen1.overrideredirect(True)

    about_btn = tk.Button(screen1, text="About", font=("century gothic", 25), fg="Red", bd=0, bg="White", command=ini_about)
    about_btn.place(x=20, y=165)

    menu_indicate = tk.Label(screen1, text="", bg="Red")
    menu_indicate.place(x=3, y=179, width=5, height=40)

    exit_btn = tk.Button(screen1, text="Keluar", font=("century gothic", 25), fg="Red", bd=0, bg="White", command=confirm_exit)
    exit_btn.place(x=20, y=228)

    menu_indicate = tk.Label(screen1, text="", bg="Red")
    menu_indicate.place(x=3, y=245, width=5, height=40)

    masuk_btn = tk.Button(screen1, text='Kendaraan masuk', fg='white', width=45, height=10, bd=0, bg="red", command=Kendaraan_baru)
    masuk_btn.place(x=1140, y=30)

    keluar_btn = tk.Button(screen1, text='Kendaraan keluar dan CEK', fg='white', width=45, height=10, bd=0, bg="red", command=parkir)
    keluar_btn.place(x=1140, y=280)

    cek_btn = tk.Button(screen1, text='Stok lahan parkir', fg='white', width=45, height=10, bd=0, bg="red", command=check_file)
    cek_btn.place(x=1140, y=530)

    # Implementing side panel functionality
    def hide_indicators():
        menu_indicate.config(bg="white")

    def ini_about():
        hide_indicators()
        menu_indicate.config(bg="Red")

    # Implementing exit confirmation
    def confirm_exit():
        exit_confirm = tk.messagebox.askyesno('Confirm Exit', 'Are you sure you want to exit?')
        if exit_confirm:
            root.destroy()

#===================================================================
# MAIN FUNCTIONALITIES
#===================================================================
def Kendaraan_baru():
    window = tk.Toplevel(root)
    window.title('Kendaraan Masuk')
    window.geometry('625x500')
    window.config(bg='white')

    Label(window, text="Silakan Masukkan Plat Kendaraan Anda:", font=('Microsoft YaHei UI Light', 12), bg='white').pack(pady=20)
    
    plat_input = Entry(window, width=20, fg='black', border=1, bg='#dee0df', font=('Microsoft YaHei UI Light', 13))
    plat_input.pack(pady=10)

    def simpan_plat():
        plat_nomor = plat_input.get().upper().strip()
        if not plat_nomor:
            messagebox.showerror("Input Error", "Plat nomor tidak boleh kosong.", master=window)
            return
        
        with open("kendaraan.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == plat_nomor:
                    messagebox.showerror("Error", "Kendaraan sudah masuk sebelumnya.", master=window)
                    return

        now = datetime.now()
        waktu_masuk = now.strftime("%Y-%m-%d %H:%M:%S")
        with open("kendaraan.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([plat_nomor, waktu_masuk])
        
        messagebox.showinfo("Success", f"Data kendaraan dengan plat {plat_nomor} berhasil disimpan.", master=window)
        window.destroy()

    Button(window, text="Simpan", font=('Microsoft YaHei UI Light', 10), bg='red', fg='white', command=simpan_plat).pack(pady=20)

def parkir():
    window = tk.Toplevel(root)
    window.title('Kendaraan Keluar')
    window.geometry('625x500')
    window.config(bg='white')

    Label(window, text="Silakan Masukkan Plat Kendaraan Anda:", font=('Microsoft YaHei UI Light', 12), bg='white').pack(pady=20)
    
    plat_input = Entry(window, width=20, fg='black', border=1, bg='#dee0df', font=('Microsoft YaHei UI Light', 13))
    plat_input.pack(pady=10)

    def cek_plat():
        plat_nomor = plat_input.get().upper().strip()
        if not plat_nomor:
            messagebox.showerror("Input Error", "Plat nomor tidak boleh kosong.", master=window)
            return

        found = False
        rows = []
        with open("kendaraan.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == plat_nomor:
                    found = True
                else:
                    rows.append(row)

        if found:
            with open("kendaraan.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            
            now = datetime.now()
            waktu_keluar = now.strftime("%Y-%m-%d %H:%M:%S")
            with open("history.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([plat_nomor, waktu_keluar])
            
            messagebox.showinfo("Success", f"Kendaraan dengan plat {plat_nomor} berhasil keluar.", master=window)
            window.destroy()
        else:
            messagebox.showerror("Error", "Plat nomor tidak ditemukan.", master=window)

    Button(window, text="Cek dan Keluar", font=('Microsoft YaHei UI Light', 10), bg='red', fg='white', command=cek_plat).pack(pady=20)

def check_file():
    try:
        with open('kendaraan.csv', 'r') as f:
            total_kendaraan = sum(1 for row in csv.reader(f))

        with open('stok_lahan_parkir.csv', 'r') as f:
            stok_lahan = sum(1 for row in csv.reader(f))

        messagebox.showinfo('Info Stok Lahan Parkir', f'Total kendaraan yang terparkir: {total_kendaraan}\nStok lahan parkir tersedia: {stok_lahan}')
    except FileNotFoundError:
        messagebox.showerror('Error', 'File tidak ditemukan.')

root.mainloop()
