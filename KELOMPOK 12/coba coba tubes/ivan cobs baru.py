import tkinter as tk
from tkinter import messagebox
import csv

# Create the main application window
root = tk.Tk()
root.wm_title('SI JAGO PARKIR')
root.geometry('900x500')
root.configure(bg="#fff")
root.resizable(False, False)

#===================================================
# Function for the login command
#===================================================

def login_CMD():
    username_input = username.get()
    password_input = password.get()

    try:
        with open("users.csv", mode="r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if username_input == row[0] and password_input == row[1]:
                    Main_menu()
                    return
        messagebox.showerror("Tidak Ditemukan", "Username dan/atau Password salah. Pastikan kapital dan spasi tepat.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File users.csv tidak ditemukan.")

#====================================================
# Function to display the main menu
#====================================================

def Main_menu():
    screen1 = tk.Toplevel(root)
    screen1.title("Main Menu")
    screen1.geometry('900x500')
    screen1.config(bg='white')

    tk.Label(screen1, text='Main Menu', bg='white', font=('Calibri', 30, 'bold')).pack(pady=20)

    parkir_button = tk.Button(screen1, text="Parkir", font=('Calibri', 15), width=20, command=parkir)
    parkir_button.pack(pady=10)

    laporan_button = tk.Button(screen1, text="Laporan", font=('Calibri', 15), width=20, command=laporan)
    laporan_button.pack(pady=10)

    logout_button = tk.Button(screen1, text="Logout", font=('Calibri', 15), width=20, command=screen1.destroy)
    logout_button.pack(pady=10)

def parkir():
    parkir_screen = tk.Toplevel(root)
    parkir_screen.title("Parkir")
    parkir_screen.geometry('900x500')
    parkir_screen.config(bg='white')

    tk.Label(parkir_screen, text='kendaraan keluar', bg='white', font=('Calibri', 20)).pack(pady=20)

def laporan():
    laporan_screen = tk.Toplevel(root)
    laporan_screen.title("Laporan")
    laporan_screen.geometry('600x400')
    laporan_screen.config(bg='white')

    tk.Label(laporan_screen, text='cek kapasitas', bg='white', font=('Calibri', 20)).pack(pady=20)

#=======================================================
# Function for the registration window
#=======================================================

def register():
    register_screen = tk.Toplevel(root)
    register_screen.title("DAFTAR")
    register_screen.geometry('625x500')
    register_screen.config(bg='white')
    
    tk.Frame(register_screen, width=280, height=2, bg='black').place(x=165, y=270)
    tk.Frame(register_screen, width=280, height=2, bg='black').place(x=165, y=340)

    username_register = tk.Entry(register_screen, width=25, fg='white', border=0, bg='grey', font=('Microsoft YaHei UI Light', 13))
    username_register.place(x=180, y=240)
    
    password_register = tk.Entry(register_screen, width=25, fg='white', border=0, bg='grey', font=('Microsoft YaHei UI Light', 13))
    password_register.place(x=180, y=310)
   
    def daftar_fungsi():
        username_new = username_register.get()
        password_new = password_register.get()
        if not username_new or not password_new:
            messagebox.showerror("Invalid", "Masukan Username dan Password terlebih dahulu", master=register_screen)
        else:
            with open("users.csv", mode="a", newline="") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([username_new, password_new])
            messagebox.showinfo('Sukses!', 'Akun username dan Password baru sudah terdaftar')
            register_screen.destroy()
          
    daftar_button = tk.Button(register_screen, width=16, text='DAFTAR', border=0, bg='white', cursor='hand2', font=('Microsoft YaHei UI Light', 8, 'bold'), command=daftar_fungsi)
    daftar_button.place(x=244, y=370)

#===================================================
# GUI login screen
#===================================================

# Ensure the path to your image is correct
try:
    gambar_kiri = tk.PhotoImage(file='TeamProject_12_prokom/KELOMPOK 12/LOGO LOGIN.png')
    tk.Label(root, image=gambar_kiri, bg='white').place(x=-5, y=-50)
except tk.TclError:
    print("Image file not found. Check the path to 'LOGO LOGIN.png'.")

frame = tk.Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = tk.Label(frame, text='Masuk', fg='red', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=120, y=5)

def on_enter_username(e):
    if username.get() == 'Tulis Username Anda':
        username.delete(0, "end")
        username.config(fg='black')

def on_leave_username(e):
    if not username.get():
        username.insert(0, 'Tulis Username Anda')
        username.config(fg='grey')
        
username = tk.Entry(frame, width=25, fg='grey', border=0, bg='white', font=('Microsoft YaHei UI Light', 13))
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

password = tk.Entry(frame, width=25, fg='grey', border=0, bg='white', font=('Microsoft YaHei UI Light', 13))
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

show_password_check = tk.Checkbutton(frame, text="Show Password", variable=show_password_var, onvalue=1, offvalue=0, command=toggle_password, bg='white', fg='grey', font=('Microsoft YaHei UI Light', 9))
show_password_check.place(x=30, y=170)

tk.Frame(frame, width=300, height=2, bg='black').place(x=25, y=110)
tk.Frame(frame, width=300, height=2, bg='black').place(x=25, y=190)
tk.Button(frame, width=39, pady=7, text='sign in', bg='#de2b28', cursor='hand2', fg='white', border=0, command=login_CMD).place(x=35, y=215)

akun_label = tk.Label(frame, text='Tidak memiliki akun SI JAGO PARKIR?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
akun_label.place(x=62, y=260)
daftar_button = tk.Button(frame, width=16, text='Daftar sekarang!', border=0, bg='white', cursor='hand2', font=('Microsoft YaHei UI Light', 8, 'bold'), command=register)
daftar_button.place(x=110, y=280)

copy_label = tk.Label(root, text='Kelompok 12 Nexus Copyright @2024', fg='navy', border=0, bg='white', font=('Microsoft YaHei UI Light', 9, 'italic'))
copy_label.place(x=350, y=420)

# Start the main loop of the application
root.mainloop()
