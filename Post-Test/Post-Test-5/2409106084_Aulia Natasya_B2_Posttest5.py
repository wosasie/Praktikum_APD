import os

username_benar = "Admin"
password_benar = "5555"
status_login = False
batas_login = 3

while batas_login > 0:
    os.system('cls || clear')
    print("=="*25)
    print("Login Admin".center(50))
    print("=="*25)
    username_admin = input("Masukkan username anda : ")
    password_admin = input("Masukkan password anda : ")

    if username_admin == username_benar and password_admin == password_benar:
        status_login = True
        print("==" *25)
        print("Berhasil login!".center(50))
        print("==" *25)
        input("Klik enter untuk melanjutkan...")
        break

    else:
        batas_login -= 1
        print("==" *25)
        print("Username atau password anda salah! ".center(50))
        print(f"Kesempatan login tersisa {batas_login} kali lagi!".center(50))
        print("==" *25)
        input("Klik enter untuk mencoba lagi...")


if status_login:
    jenis_merchandise = ["Topi", "Jaket", "Kaos Tim", "Miniatur Mobil", "Mug", "Poster" ]
    tim_merchandise = ["Ferrari", "McLaren", "Mercedes", "Red Bull", "Williams", "Ferrari"]
    harga_merchandise = ["560000", "892000", "749000", "540000", "377000", "120000"]
    stok_merchandise = ["20", "44", "12", "93", "55", "16"]
    edisi_merchandise = ["2023", "2022", "2024", "2021", "2020", "2023" ]

    while True:
        os.system('cls || clear')
        print("=="*25)
        print("List Katalog Merchandise F1".center(50))
        print("=="*25)

        print("[1] List Katalog Merchandise")
        print("[2] Merchandise Baru")
        print("[3] Update Stok Merchandise")
        print("[4] Hapus Merchandise")
        print("[5] Keluar")
        pilihan = input("Masukkan pilihan anda: ")

        if pilihan == "1":
            os.system('cls || clear')
            print("=="*25)
            print("List Katalog Merchandise".center(50))
            print("=="*25)

            for index, merchandise in enumerate(jenis_merchandise, 1):
                print(f"{index}. Jenis Merchandise : {merchandise}")
                print(f"   Tim Merchandise   : {tim_merchandise[index - 1]}")
                print(f"   Harga Merchandise : Rp{harga_merchandise[index - 1]}")
                print(f"   Stok Merchandise  : {stok_merchandise[index - 1]} pcs")
                print(f"   Edisi Tahun       : {edisi_merchandise[index - 1]}")

                print("==" * 25)
            input("Klik enter untuk kembali ke menu. . . ")

        elif pilihan == "2":
            os.system('cls || clear')
            print("==" *25)
            print("Merchandise Baru".center(50))
            print("==" *25)

            jenis_merchandise.append(input("Masukkan Jenis Merchandise : "))
            tim_merchandise.append(input("Masukkan Tim Merchandise : "))
            harga_merchandise.append(input("Masukkan Harga Merchandise : "))
            stok_merchandise.append(input("Masukkan Stock Merchandise : "))
            edisi_merchandise.append(input("Masukkan Tahun Edisi Merchandise : "))

            print("==" *25)
            print("Merchandise baru berhasil ditambahkan! ".center(50))
            print("==" *25)
            input("Klik enter untuk kembali ke menu. . . ")

        elif pilihan == "3":
            os.system('cls || clear')
            print("==" *25)
            print("Update Stock Merchandise".center(50))
            print("==" *25)

            for index, merchandise in enumerate(jenis_merchandise, 1):
                print(f"{index}. {merchandise}")
            index_update = int(input("Masukkan nomor merchandise yang ingin diupdate stoknya: ")) - 1
            stok_baru = input("Masukkan stok baru merchandise : ")
            stok_merchandise[index_update] = stok_baru

            print("==" *25)
            print(f"Stok merchandise {jenis_merchandise[index_update]} berhasil diupdate menjadi {stok_merchandise[index_update]} pcs!".center(50))
            print("==" *25)
            input("Klik enter untuk kembali ke menu. . . ")

        elif pilihan == "4":
            os.system('cls || clear')
            print("==" *25)
            print("Hapus Merchandise (Stok Habis)".center(50))
            print("==" *25)

            for index, merchandise in enumerate(jenis_merchandise, 1):
                print(f"{index}. {merchandise} - Stok : {stok_merchandise[index - 1]}")
            index = int(input("Masukkan nomor merchandise yang ingin dihapus (karena stok habis) : ")) - 1
            terjual_merch = jenis_merchandise.pop(index)
            tim_merchandise.pop(index)
            harga_merchandise.pop(index)
            stok_merchandise.pop(index)
            edisi_merchandise.pop(index)

            print("==" *30)
            print(f"Merchandise {terjual_merch} sudah terjual dan dihapus dari katalog. ".center(60))
            print("==" *30)
            input("Klik enter untuk kembali ke menu. . . ")
        
        elif pilihan == "5":
            print("==" *25)
            print("Anda memilih keluar. Terima Kasih! ".center(50))
            print("==" *25)
            break

        else:
            os.system('cls || clear')
            print("Menu {pilihan} tidak tersedia. ")
            input("Klik enter untuk kembali ke menu. . . ")
        
else:
        print("==" *25)
        print("Anda gagal login! ".center(50))
        print("==" *25)

