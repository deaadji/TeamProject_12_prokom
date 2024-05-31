import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
from datetime import datetime
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

    #try:
    #    gambar_dafatar = PhotoImage(file='KELOMPOK 12/DAFTAR.png')
    #    tk.Label(daftar_screen, image=gambar_dafatar, bg='white').place(x=100,y=200)
    #except:
    #    print("Image file not found. Check the path to 'DAFTAR.png'.")


#===================================================================
#GUI login screen
#===================================================================
#bug disini, janlup directory nya
try:
    gambar_kiri = PhotoImage(file='KELOMPOK 12/LOGO LOGIN.png')
    tk.Label(root, image=gambar_kiri, bg='white').place(x=-5, y=-50)
    Label(root,image=gambar_kiri,bg='white').place(x=-5,y=-50)
except tk.TclError:
    print("Image file not found. Check the path to 'LOGO LOGIN.png'.")

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)


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

show_password_check = tk.Checkbutton(frame, text="Lihat Password", variable=show_password_var, onvalue=1, offvalue=0, command=toggle_password, bg='white', fg='black', font=('Microsoft YaHei UI Light', 10))
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

    try:
        gambar_jar = PhotoImage(file='KELOMPOK 12/MAIN MENU JAR.png')
        tk.Label(screen1, image=gambar_jar, bg='white').place(x=130,y=570)
    except:
        print("Image file not found. Check the path to 'DAFTAR.png'.")
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

    exit_btn = tk.Button(screen1, text="Logout", font=("century gothic", 25), fg="Red", bd=0, bg="White", command=confirm_Logout)
    exit_btn.place(x=20, y=228)

    menu_indicate = tk.Label(screen1, text="", bg="Red")
    menu_indicate.place(x=3, y=245, width=5, height=40)

    logout_btn = tk.Button(screen1, text="Keluar", font=("century gothic", 25), fg="Red", bd=0, bg="White", command=confirm_exit)
    logout_btn.place(x=18, y=293)

    menu_indicate = tk.Label(screen1, text="", bg="Red")
    menu_indicate.place(x=3, y=309, width=5, height=40)

    try:
        gambar_masuk = PhotoImage(file='KELOMPOK 12/MASHOK.png')
        masuk_btn = tk.Button(screen1, image=gambar_masuk, bd=0, bg="white", command=Kendaraan_baru)
        masuk_btn.place(x=1130, y=30)
    except tk.TclError:
        print("Image file not found. Check the path to 'LOGO LOGIN.png'.")

    try:
        gambar_keluar = PhotoImage(file='KELOMPOK 12/KELVAR.png')
        keluar_btn = tk.Button(screen1, image=gambar_keluar ,bd=0,bg="white", command=parkir_keluar)
        keluar_btn.place(x=1130, y=280)
    except tk.TclError:
        print("Image file not found. Check the path to 'LOGO LOGIN.png'.")

    try:
        gambar_cek = PhotoImage(file='KELOMPOK 12/CAPASITY.png')
        cek_btn = tk.Button(screen1, image=gambar_cek, bd=0, bg="white",command=laporan)
        cek_btn.place(x=1130, y=550)
    except tk.TclError:
        print("Image file not found. Check the path to 'LOGO LOGIN.png'.")

    layar_gede = tk.Frame(screen1, highlightbackground= "black", highlightthickness=5,bg="white")

    layar_gede.place(x=150,y=178)
    layar_gede.pack_propagate(False)
    layar_gede.configure(height=500, width=900)

    try:
        gambar_judul = PhotoImage(file='KELOMPOK 12/MENU_LABEL.png')
        tk.Label(screen1, image=gambar_judul, bg='white').place(x=35, y=30)
    except tk.TclError:
        print("Image file not found. Check the path to 'MENU_LABEL.png'.")
    screen1.mainloop()


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
    code = random.randint(100000, 999999)

    kota_nopol = Entry(nambah_screen,width=5,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',30))
    kota_nopol.place(x=130,y=110)

    inp_nopol = Entry(nambah_screen,width=15,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',30))
    inp_nopol.place(x=270,y=110)

    kode_unik_entry = Entry(nambah_screen,width=12,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',30))
    kode_unik_entry.place(x=130,y=220)
    kode_unik_entry.insert(0,code)

    jenis_kendaraan_entry = Entry(nambah_screen,width=12,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',30))
    jenis_kendaraan_entry.place(x=430,y=220)
    jenis_kendaraan_entry.insert(0,'sepeda motor')

    def ganti_funct():
        if jenis_kendaraan_entry.get()=='sepeda motor':
            jenis_kendaraan_entry.delete(0,'end')
            jenis_kendaraan_entry.insert(0,'mobil')
        elif jenis_kendaraan_entry.get()=='mobil':
            jenis_kendaraan_entry.delete(0,'end')
            jenis_kendaraan_entry.insert(0,'sepeda motor')
        
    def on_enter(e):
        kota_nopol.delete(0, "end")
    kota_nopol.insert(0,'AD')
    kota_nopol.bind('<FocusIn>', on_enter)
    
    tk.Label(nambah_screen, text='kode kota', bg='white', font=('century gothic', 14)).place(x=130,y=80)
    tk.Label(nambah_screen, text='kode plat', bg='white', font=('century gothic', 14)).place(x=270,y=80)
    tk.Label(nambah_screen, text='kode unik', bg='white', font=('century gothic', 14)).place(x=130,y=190)
    tk.Label(nambah_screen, text='Jenis Kendaraan', bg='white', font=('century gothic', 14)).place(x=430,y=190)
    tk.Label(nambah_screen, text='INPUT KENDARAAN MASUK', fg='white', bg='red', font=('century gothic', 20, 'bold')).pack(pady=8)

    def save_data():
        plate_kode = (kota_nopol.get()+ ' ' +inp_nopol.get())
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if kota_nopol.get()=='' or inp_nopol.get()=='':
            messagebox.showerror(title='gagal!', message='Nopol tidak boeh kocong ')
        elif kota_nopol.get()=='AD' and inp_nopol.get()=='':
            messagebox.showerror(title='gagal!', message='Kode Plat tidak boeh kocong ')
        elif plate_kode:
            with open("parking_data2.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([plate_kode, kode_unik_entry.get(), current_time, jenis_kendaraan_entry.get()])
            kota_nopol.delete(0, tk.END) 
            inp_nopol.delete(0, tk.END)  
            kota_nopol.insert(0,'AD')
            kode_unik_entry.delete(0,'end')
            code = random.randint(100000, 999999)
            kode_unik_entry.insert(0, code)
            messagebox.showinfo(title='Sukses!', message='Berhasil Masuk, Berhasil menyimpan!')
        else:
            messagebox.showerror(title='gagal!', message='gagal menyimpan!\npastikan nopol benar')  

    def reset_code_numb():
        kode_unik_entry.delete(0,'end')
        code = random.randint(100000, 999999)
        kode_unik_entry.insert(0, code)


    Simpan=Button(nambah_screen,width=16,text='Simpan',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=save_data)
    Simpan.place(x=134,y=300)

    new_code_bt=Button(nambah_screen,width=16,text='kode baru',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=reset_code_numb)
    new_code_bt.place(x=264,y=300)

    def read_data():
        data = []
        try:
            with open("parking_data2.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist

        # Display data in a new window
        display_window = tk.Tk()
        display_window.title("KENDARAAN PARKIR SAAT INI")

        data_text = "Plat Nomor\tkode Unik\t\tWaktu Masuk\t\tJenis Kendaraan\n"
        for row in data:
            data_text += f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t{row[3]}\n" 

        data_label = tk.Label(display_window, text=data_text, font=("Microsoft YaHei UI Light", 12))
        data_label.pack()

        display_window.mainloop()

    def DELETE_ALL():
        modified_data = []
        response = messagebox.askyesno("Konfirmasi hapus", "Apakah Anda yakin ingin hapus semua kendaraan di data?")
        if response:
            try:
                with open("parking_data2.csv", "w", newline="") as outfile:
                    writer = csv.writer(outfile)
                    writer.writerows(modified_data)

                messagebox.showinfo(title="Sukses!", message="Semua Data berhasil dihapus!")
            except FileNotFoundError:
                messagebox.showerror(title="Gagal!", message="File 'parking_data2.csv' tidak ditemukan!")
            except Exception as e:
                messagebox.showerror(title="Gagal!", message="Terjadi kesalahan: " + str(e))

    liat_data=Button(nambah_screen,width=16,text='lihat Parkiran',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=read_data)
    liat_data.place(x=134,y=350)

    delete_alll=Button(nambah_screen,width=16,text='Delete all',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=DELETE_ALL)
    delete_alll.place(x=714,y=120)

    ganti_button=Button(nambah_screen,width=16,text='Ganti Kendaraan',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'), command=ganti_funct)
    ganti_button.place(x=714,y=235)
    
    
                                          #====================================================================
                                          # KELUAR 
                                          #====================================================================
def parkir_keluar():
    parkir_screen=Toplevel(root)
    parkir_screen.title("KENDARAAN KELUAR DAN CEK")
    parkir_screen.geometry('880x480+158+190')
    parkir_screen.configure(bg="white")
    parkir_screen.resizable(False,False)
    parkir_screen.overrideredirect(True)
    tk.Label(parkir_screen, text='CEK DAN KENDARAAN KELUAR', fg='white', bg='red', font=('century gothic', 20,'bold')).pack(pady=8)

    cek_box = Entry(parkir_screen,width=12,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',30))
    cek_box.place(x=90,y=90)

    tk.Label(parkir_screen, text='Nopol atau Kode Unik', bg='white', font=('century gothic', 14, )).place(x=90,y=56)

        #=======================
        #PENCARIAN DATA UTAMA
    def search_data():
        search_value = cek_box.get()
        found_data = None
        try:
            with open("parking_data2.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if (row[0] == search_value) or \
                    (row[1] == search_value):
                        found_data = row
                        break 
        except FileNotFoundError:
            pass 

        if found_data:
            search_result_text = (f"Ditemukan!\nPlat Nomor  : {found_data[0]}\nKode Unik    : {found_data[1]}\nWaktu Masuk   : {found_data[2]}")
            date_str = (f'{found_data[2]}')  
            datetime_stored = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            now = datetime.now()
            elapsed = now - datetime_stored
            hours = elapsed.seconds // 3600
            minutes = (elapsed.seconds % 3600) // 60
            seconds = elapsed.seconds % 60
            waktu_berlalu=(f"durasi parkir: {hours} jam, {minutes} menit, {seconds} detik")
        else:
            search_result_text = f"Tidak ada Data {search_value} di parkiran"
        
        def hitung_biaya_parkir():
            try:
                jenis_kendaraan = str(f'{found_data[3]}')
                durasi_jam = int(f'{hours}')
            except:
                print('error   : ambil jenis stopped')

            try:
                if durasi_jam == 0:
                    durasi_jam = 1
                else :
                    durasi_jam = int(f'{hours}')
            except:
                print("durasi stopped")
                return

                # Hitung biaya parkir
            try :
                if jenis_kendaraan == "sepeda motor":
                    if durasi_jam < 1:
                        biaya = 2000
                    else:
                        biaya_awal = 2000
                        durasi_sisa_jam = int(durasi_jam // 60)

                    biaya_tambahan = durasi_sisa_jam * 1000
                    if durasi_jam >= 1 and durasi_jam <= 5:
                            biaya_tambahan += 1000
                    elif durasi_jam >= 6 and durasi_jam <= 12:
                            biaya_tambahan += 3000
                    elif durasi_jam >= 13 and durasi_jam <= 24:
                            biaya_tambahan += 5000
                    else:
                            biaya_tambahan += 8000

                    biaya = biaya_awal + biaya_tambahan
                elif jenis_kendaraan == "mobil":
                    if durasi_jam >= 0 and durasi_jam <= 1 :
                            biaya = 5000
                    elif durasi_jam >=2 and durasi_jam <=9 :
                            biaya_awal = 5000
                            durasi_sisa_jam = int(durasi_jam - 1)

                            biaya_tambahan = durasi_sisa_jam * 2000
                            biaya = biaya_awal + biaya_tambahan
                    elif durasi_jam >=10 and durasi_jam <=24 :
                            biaya_awal = 5000
                            durasi_sisa_jam = int(durasi_jam - 1)

                            biaya_tambahan = durasi_sisa_jam * 1000
                            biaya = biaya_awal + biaya_tambahan
                    else:
                            biaya_awal = 5000
                            durasi_sisa_jam = int(durasi_jam - 1)

                            biaya_tambahan = durasi_sisa_jam * 500
                            biaya = biaya_awal + biaya_tambahan
                else:
                    print("Jenis kendaraan tidak valid.")
                    return
            except :
                print('menghitung stopped')
            
            # Tampilkan hasil
            try :
                biaya_print = (f"Biaya parkir untuk {jenis_kendaraan}\nSelama {durasi_jam:.2f} jam adalah")
                biaya_rupiah = (f'Rp{biaya:,}')
                biaya_Final = tk.Label(parkir_screen, text=biaya_print, width= 50,bg='white',font=("Century Gothic", 14))
                biaya_Final.place(x=356,y=160)
                biaya_tunjuk = tk.Label(parkir_screen, text=biaya_rupiah,bg='white',font=("Century Gothic", 30, 'bold'),justify="left")
                biaya_tunjuk.place(x=565,y=210)
            except:
                None
        hitung_biaya_parkir()

        search_result_window=Toplevel(root)
        search_result_window.geometry('440x310+158+340')
        search_result_window.configure(bg="white")
        search_result_window.resizable(False,False)
        search_result_window.overrideredirect(True)

        search_result_label = tk.Label(search_result_window, text=search_result_text,bg='white',font=("Century Gothic", 14),justify="left")
        search_result_label.place(x=35,y=20)

        try:
            durasi_label = tk.Label(search_result_window, text=waktu_berlalu,bg='white',font=("Century Gothic", 14),justify="left")
            durasi_label.place(x=35,y=120)
        except:
            None
        search_result_window.mainloop()

    def delete_line_from_csv():
        plate_kode_to_delete = cek_box.get() 
        updated_data = []

        # Read the entire CSV file into memory
        with open("parking_data2.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != plate_kode_to_delete:  # Check if plate code matches
                    updated_data.append(row)

        # Overwrite the original file with the updated data (excluding the deleted line)
        with open("parking_data2.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)

        # Confirmation message (optional)
        messagebox.showinfo(title="Sukses!", message="plat nomor " + plate_kode_to_delete + "Keluar dari Parkiran!")


    def read_data():
        data = []
        try:
            with open("parking_data2.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist

        # Display data in a new window
        display_window = tk.Tk()
        display_window.title("KENDARAAN PARKIR SAAT INI")

        data_text = "Plat Nomor\tkode Unik\t\tWaktu Masuk\t\tJenis Kendaraan\n"
        try:
            for row in data:
                data_text += f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\n" 
        except:
            None

        data_label = tk.Label(display_window, text=data_text, font=("Microsoft YaHei UI Light", 12))
        data_label.pack()

        display_window.mainloop()

    keluar_data=Button(parkir_screen,width=16,text='Kendaraan Keluar',fg='white',border=2,bg='red',cursor='hand2',font=('Microsoft YaHei UI',8,'bold'), command=delete_line_from_csv)
    keluar_data.place(x=560,y=100)

    Read_data_keluar=Button(parkir_screen,width=16,text='Lihat Parkiran',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'),command=read_data)
    Read_data_keluar.place(x=720,y=100)

    cek_data=Button(parkir_screen,width=16,text='CEK',fg='black',border=2,bg='white',cursor='hand2',font=('Microsoft YaHei UI Light',8,'bold'),command=search_data)
    cek_data.place(x=400,y=100)


def laporan():
    laporan_screen=Toplevel(root)
    laporan_screen.title("CEK KAPASITAS")
    laporan_screen.geometry('880x480+158+190')
    laporan_screen.configure(bg="white")
    laporan_screen.resizable(False,False)
    laporan_screen.overrideredirect(True)

    tk.Label(laporan_screen, text='KAPASITAS TEMPAT PARKIR', fg='white', bg='red', font=('Century Gothic', 20 ,'bold')).pack(pady=8)

    Kaps_maks_entry = Entry(laporan_screen,width=10,fg='black',border=0,bg='light grey',font=('Microsoft YaHei UI Light',20))
    Kaps_maks_entry.place(x=100,y=90)
    Kaps_maks_entry.insert(0,'100')

    kapasitas_lab = Label(laporan_screen,text='Kapasitas Maks:',fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',13))
    kapasitas_lab.place(x=100,y=62)

    def cek_utama():
        try:
            if Kaps_maks_entry.get() == "":
                print('error')
            elif int(Kaps_maks_entry.get()) ==0:
                print('error')
            elif int(Kaps_maks_entry.get()) >= 1:
                kapasitas_maks= int(Kaps_maks_entry.get())
                jumlah_kendaraan = sum(1 for _ in open('parking_data2.csv'))
                slot_kosong = kapasitas_maks - jumlah_kendaraan

                angka_terisi = Label(laporan_screen,text=jumlah_kendaraan,fg='red',border=0,bg='white',font=('Microsoft YaHei UI',93, 'bold'))
                angka_terisi.place(x=130,y=202)

                angka_terisi = Label(laporan_screen,text=slot_kosong,fg='black',border=0,bg='white',font=('Microsoft YaHei UI',93, 'bold'))
                angka_terisi.place(x=430,y=202)

                text_maks = Label(laporan_screen,text='Kendaraan diparkiran:',fg='black',border=0,bg='white',font=('Microsoft YaHei UI',14))
                text_maks.place(x=90,y=195)

                text_total = Label(laporan_screen,text='Tempat Kosong:',fg='black',border=0,bg='white',font=('Microsoft YaHei UI',14))
                text_total.place(x=410,y=195)
            else:
                print('error')
        except:
            None


    kapasitas_button = Button(laporan_screen,text='update',fg='black',bg='white',font=('Microsoft YaHei UI',10), command=cek_utama)
    kapasitas_button.place(x=280,y=92)
        
def confirm_exit():
    response = messagebox.askyesno("Konfirmasi Keluar", "Apakah Anda yakin ingin keluar?")
    if response:
        root.destroy()

def destroy_top_level_windows(root):
  for widget in root.winfo_children():
    if isinstance(widget, tk.Toplevel) and widget != root:
      widget.destroy()

def confirm_Logout():
    response = messagebox.askyesno("Konfirmasi Logout kembali ke Layar Login?", "Apakah Anda yakin ingin keluar?")
    if response:
        destroy_top_level_windows(root)
    root.deiconify()

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
    " \n"
    "See our code on :\n"
    "https://github.com/deaadji/TeamProject_12_prokom\n"
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

