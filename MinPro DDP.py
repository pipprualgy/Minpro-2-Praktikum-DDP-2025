# Registrasi username dan password
def login (nama,password):
    benar = False
    file = open("password.txt", "r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==nama and b==password):
            benar = True
            break
    file.close
    if(benar):
        print("login berhasil, silakan masuk")
    else:
        print("belum terdaftar, silakan registrasi")

def registrasi(nama,password):
    file = open("password.txt", "a")
    file.write("\n"+nama+","+password)

def access(option):
    global nama
    if(option == "login"):
        nama = input("masukkan ID: ")
        password = input("Masukkan Password: ")
        login(nama,password)
    else:
        print("Masukkan ID dan password baru")
        nama = input("Masukkan ID: ")
        password = input("Masukkan password: ")
        registrasi(nama,password)
        print("registrasi anda berhasil, silakan masuk")

def begin():
    global option
    print("Selamat datang di program pendataan KTA")
    print("Ketik (login) jika sudah punya username")
    print("Ketik (regis) jika belum punya username")
    option = input("Silakan ketik (login/regis) : ")
    print("=" * 50)
    if (option!="login" and option!="regis"):
        begin()

begin()
access(option)


# Program Pendataan Kartu Tanda Anggota (KTA) Pramuka
print("-" * 50) 
print("Nama: Ahmad Afif Al Ghifary")
print("NIM: 2509116002")
print("Tugas: Mini Project 2 DDP")
print("Kelas: Sistem Informasi A 2025")
print("-" * 50)


data_siswa = []

def Menu_input():
    print("-" * 50)
    print("Mekanisme Pengisian Data Kartu Tanda Anggota (KTA) Pramuka")
    print("-" * 50)
    print("Pilihan menu:")
    print("1. Masukkan data siswa ")
    print("2. Revisi data siswa ")
    print("3. Lihat data siswa ")
    print("4. Hapus data siswa ")
    print("5. Selesai")
    print("-" * 40)


#Penerapan konsep create
def buat_data():
    print("\nTambah Data Siswa")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan alamat: ")
    sekolah = input("Masukkan asal sekolah: ")
    golongan = input("Masukkan golongan kepramukaan: ")
    domisili = input("Masukkan domisili: ")
    
    data_siswa.append((nama, alamat, sekolah, golongan, domisili))
    print("\nData siswa berhasil ditambahkan")
    print("\nData siap dicetak menjadi kartu")


#Penerapan konsep update (ubah/revisi datasiswa)
def mengubah_data():
    print("\nRevisi Data Siswa ")
    lihat_data()
    if data_siswa:
        try:
            indeks = int(input("Masukkan nomor siswa yang ingin direvisi: ")) - 1
            if 0 <= indeks < len(data_siswa):
                siswa = list(data_siswa[indeks]) #tuple dijadikan  list agar data bisa diubah
            
                print(f"\nData saat ini untuk siswa ke-{indeks+1}:")
                print(f"  Nama: {siswa[0]}")
                print(f"  Alamat: {siswa[1]}")
                print(f"  Asal Sekolah: {siswa[2]}")
                print(f"  Golongan: {siswa[3]}")
                print(f"  Domisili: {siswa[4]}")

                print("\nMasukkan data baru (kosongkan jika tidak ingin diubah):")
                nama_baru = input(f"Nama baru ({siswa[0]}): ") or siswa[0]
                alamat_baru = input(f"Alamat baru ({siswa[1]}): ") or siswa[1]
                sekolah_baru = input(f"Asal Sekolah baru ({siswa[2]}): ") or siswa[2]
                golongan_baru = input(f"Golongan baru ({siswa[3]}): ") or siswa[3]
                domisili_baru = input(f"Domisili baru ({siswa[4]}): ") or siswa[4]

                #data siswa yang sudha terupdate
                data_siswa[indeks] = (nama_baru, alamat_baru, sekolah_baru, golongan_baru, domisili_baru)

                print("\nData siswa berhasil diubah!")
            else:
                print("Nomor siswa tidak valid.")
        except ValueError:
            print("Input tidak valid. tolong masukkan angka.")


#Penerapan konsep Read
def lihat_data():
    print("\nDaftar Data Siswa: ")
    if not data_siswa:
        print("Belum ada siswa yang terdata.")
    else:
        for i, siswa in enumerate(data_siswa):
            nama, alamat, sekolah, golongan, domisili = siswa
            print(f"[{i+1}]")
            print(f"  Nama: {nama}")
            print(f"  Alamat: {alamat}")
            print(f"  Asal Sekolah: {sekolah}")
            print(f"  Golongan: {golongan}")
            print(f"  Domisili: {domisili}")



#Penerapan konsep delete
def hapus_data():
    print("\nHapus Data Siswa ")
    lihat_data()
    if data_siswa:
        try:
            indeks = int(input("Masukkan nomor siswa yang mau dihapus: ")) - 1
            if 0 <= indeks < len(data_siswa):
                nama_siswa = data_siswa[indeks][0] # Ambil nama siswa dari tuple
                data_siswa.pop(indeks)
                print(f"\nData dengan nama siswa '{nama_siswa}' telah dihapus ")
            else:
                print("Nomor siswa tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")


#cara menjalankan program
def mulai():
    while True:
        Menu_input()
        menu_ke  = input("Masukkan nomor menu: ")
        
        if menu_ke == "1":
            buat_data()
        elif menu_ke  == "2":
            mengubah_data()
        elif menu_ke == "3":
            lihat_data()
        elif menu_ke == "4":
            hapus_data()
        elif menu_ke == "5":
            print("\ntengkyu, program kelar.")
            break
        else:
            print("\npilihan tidak valid, masukkan angka 1-5.")
        
        input("\ntekan enter untuk kembali ke menu ")
        print("\n")

#Menjalankan program
if __name__ == "__main__":
    mulai()
