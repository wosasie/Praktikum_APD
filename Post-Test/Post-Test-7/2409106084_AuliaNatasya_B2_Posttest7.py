
import os

# Global variables
data_login = {
    "username": "Admin",
    "password": "5555"
}
status_login = False
batas_login = 3
data_merchandise = {
    1: {"Jenis": "Topi", "Tim": "Ferrari", "Harga": "560000", "Stok": "20", "Edisi": "2023"},
    2: {"Jenis": "Jaket", "Tim": "McLaren", "Harga": "892000", "Stok": "44", "Edisi": "2022"},
    3: {"Jenis": "Kaos Tim", "Tim": "Mercedes", "Harga": "749000", "Stok": "12", "Edisi": "2024"},
    4: {"Jenis": "Miniatur Mobil", "Tim": "Red Bull", "Harga": "540000", "Stok": "93", "Edisi": "2021"},
    5: {"Jenis": "Mug", "Tim": "Williams", "Harga": "377000", "Stok": "55", "Edisi": "2020"}
}

# Fungsi tanpa parameter (menampilkan merchandise)
def show_merchandise():
    print("==" * 25)
    print("List Katalog Merchandise".center(50))
    print("==" * 25)
    
    # Variabel lokal untuk iterasi
    for key, data in data_merchandise.items():
        print(f"{key}. Jenis Merchandise : {data['Jenis']}")
        print(f"   Tim Merchandise : {data['Tim']}")
        print(f"   Harga Merchandise : Rp{data['Harga']}")
        print(f"   Stok Merchandise : {data['Stok']} pcs")
        print(f"   Edisi Tahun : {data['Edisi']}")
        print("==" * 25)

# Fungsi tanpa parameter (menambah merchandise baru)
def tambah_merchandise():
    print("==" * 25)
    print("Merchandise Baru".center(50))
    print("==" * 25)
    
    # Variabel lokal untuk input data baru
    jenis = input("Masukkan Jenis Merchandise : ")
    tim = input("Masukkan Tim Merchandise : ")
    harga = input("Masukkan Harga Merchandise : ")
    stok = input("Masukkan Stok Merchandise : ")
    edisi = input("Masukkan Tahun Edisi Merchandise : ")
    
    # Menyimpan input sebagai variabel lokal
    merchandise_baru = {
        "Jenis": jenis,
        "Tim": tim,
        "Harga": harga,
        "Stok": stok,
        "Edisi": edisi
    }

    data_merchandise[len(data_merchandise) + 1] = merchandise_baru
    print("==" * 25)
    print("Merchandise baru berhasil ditambahkan!".center(50))
    print("==" * 25)

# Fungsi dengan parameter (update stok)
# def update_stok(id_merchandise, stok_baru):
#     data_merchandise[id_merchandise]["Stok"] = stok_baru  # Mengubah stok berdasarkan parameter
#     print("==" * 25)
#     print(f"Stok merchandise {data_merchandise[id_merchandise]['Jenis']} berhasil diupdate menjadi {data_merchandise[id_merchandise]['Stok']} pcs!".center(50))
#     print("==" * 25)

def update_stok():
    print("==" * 25)
    print("Update Stock Merchandise".center(50))
    print("==" * 25)
    for key, data in data_merchandise.items():
        print(f"{key}. {data['Jenis']} - Stok saat ini: {data['Stok']} pcs")
    id_merchandise = int(input("Masukkan nomor merchandise yang ingin diupdate stoknya: "))
    
    stok_baru = input("Masukkan stok baru merchandise: ")

    data_merchandise[id_merchandise]["Stok"] = stok_baru
    print("==" * 25)
    print(f"Stok merchandise {data_merchandise[id_merchandise]['Jenis']} berhasil diupdate menjadi {data_merchandise[id_merchandise]['Stok']} pcs!".center(50))
    print("==" * 25)


# Prosedur hapus merchandise
def hapus_merchandise():
    print("==" * 25)
    print("Hapus Merchandise (Stok Habis)".center(50))
    print("==" * 25)

    # Variabel lokal untuk iterasi
    for key, data in data_merchandise.items():
        print(f"{key}. {data['Jenis']} - Stok : {data['Stok']} pcs")

    index = int(input("Masukkan nomor merchandise yang ingin dihapus (karena stok habis) : "))
    terjual_merch = data_merchandise.pop(index)  # Menghapus merchandise
    print("==" * 25)
    print(f"Merchandise {terjual_merch['Jenis']} sudah terjual dan dihapus dari katalog.".center(50))
    print("==" * 25)

# Prosedur login (menggunakan global variable untuk status_login)
def menu_login():
    global status_login, batas_login
    while batas_login > 0:
        os.system('cls || clear')
        print("==" * 25)
        print("Login Admin".center(50))
        print("==" * 25)
        
        # Variabel lokal untuk menyimpan input login
        username_admin = input("Masukkan username anda : ")
        password_admin = input("Masukkan password anda : ")

        if username_admin == data_login["username"] and password_admin == data_login["password"]:
            status_login = True
            print("==" * 25)
            print("Berhasil login!".center(50))
            print("==" * 25)
            input("Klik enter untuk melanjutkan...")
            break 
        else:
            batas_login -= 1
            print("==" * 25)
            print("Username atau password anda salah!".center(50))
            print(f"Kesempatan login tersisa {batas_login} kali lagi!".center(50))
            print("==" * 25)
            input("Klik enter untuk mencoba lagi...")

# Main program
menu_login()
if status_login:
    while True:
        os.system('cls || clear')
        print("==" * 25)
        print("List Katalog Merchandise F1".center(50))
        print("==" * 25)
        print("[1] List Katalog Merchandise")
        print("[2] Merchandise Baru")
        print("[3] Update Stok Merchandise")
        print("[4] Hapus Merchandise")
        print("[5] Keluar")
        pilihan = input("Masukkan pilihan anda : ")

        if pilihan == "1":
            os.system('cls || clear')
            show_merchandise()
            input("Klik enter untuk kembali ke menu. . . ")

        elif pilihan == "2":
            os.system('cls || clear')
            tambah_merchandise()
            input("Klik enter untuk kembali ke menu. . . ")

        elif pilihan == "3":
            os.system('cls || clear')
            # Mengambil input dari pengguna untuk di-pass sebagai parameter
            id_merchandise = int(input("Masukkan nomor merchandise yang ingin diupdate stoknya : "))
            stok_baru = input("Masukkan stok baru merchandise : ")
            update_stok(id_merchandise, stok_baru)
            input("Klik enter untuk kembali ke menu. . . ")

            


        elif pilihan == "4":
            os.system('cls || clear')
            hapus_merchandise()
            input("Klik enter untuk kembali ke menu. . . ")

        elif pilihan == "5":
            print("==" * 25)
            print("Anda memilih keluar. Terima Kasih!".center(50))
            print("==" * 25)
            break

        else:
            os.system('cls || clear')
            print(f"Menu {pilihan} tidak tersedia.")
            input("Klik enter untuk kembali ke menu. . . ")

else:
    print("==" * 25)
    print("Anda gagal login!".center(50))
    print("==" * 25)




