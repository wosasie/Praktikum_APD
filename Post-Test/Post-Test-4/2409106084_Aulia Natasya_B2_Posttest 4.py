batas_Login = 3
jumlah_Login = 0
username_Benar = "Sasa"
password_Benar = "84"

while jumlah_Login < 3:
    username_Input = input("Masukkan username anda: ")
    password_Input = input("Masukkan password anda: ")
    if username_Input == username_Benar and password_Input == password_Benar:
        print("Login berhasil ")

        berat_Badan_Dalam_Mg = float(input("Masukkan Berat badan dalam Mg: "))
        tinggi_Badan_Dalam_Km = float(input("Masukkan Tinggi badan dalam Km: "))

        berat_Badan_Dalam_Kg = berat_Badan_Dalam_Mg / 1000000
        tinggi_Badan_Dalam_M = tinggi_Badan_Dalam_Km * 1000
        bMI = berat_Badan_Dalam_Kg / (tinggi_Badan_Dalam_M ** 2)

        bMI = berat_Badan_Dalam_Kg / (tinggi_Badan_Dalam_M * tinggi_Badan_Dalam_M)
        print("BMI anda adalah " + str(bMI))

        if bMI < 18.5:
            print("Anda masuk dalam kategori underweight. ")
        elif bMI < 24.9:
            print("Anda masuk dalam kategori normal. ")
        elif bMI < 29.9:
            print("Anda masuk dalam kategori overweight. ")
        else:
            print("Anda masuk dalam kategori obesitas. ")

        print("Apakah anda ingin keluar? (Ya/Tidak): ")
        pilihan_Keluar = input()
        if pilihan_Keluar == "Ya":
            print("Terimakasih, program perhitungan BMI sudah selesai dijalankan ")
            break
        else:
            print("Silahkan kembali ke halaman login ")
    else:
        jumlah_Login = jumlah_Login + 1
        print("Login anda gagal " + str(jumlah_Login) + "kali. ")
        if jumlah_Login >= batas_Login:
            print("Login anda gagal 3 kali, program akan berhenti. ")





