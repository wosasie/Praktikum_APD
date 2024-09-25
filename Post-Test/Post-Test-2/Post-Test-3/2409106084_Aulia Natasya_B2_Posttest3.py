berat_Badan_Dalam_Mg = float(input("Masukkan Berat badan dalam Mg: "))
tinggi_Badan_Dalam_Km = float(input("Masukkan Tinggi badan dalam Km: "))

berat_Badan_Dalam_Kg = berat_Badan_Dalam_Mg / 1000000
tinggi_Badan_Dalam_M = tinggi_Badan_Dalam_Km * 1000
bMI = berat_Badan_Dalam_Kg / (tinggi_Badan_Dalam_M ** 2)

if bMI < 18.5:
    print("Anda masuk dalam kategori underweight. ")
elif bMI < 24.9:
    print("Anda masuk dalam kategori normal. ")
elif bMI < 29.9:
    print("Anda masuk dalam kategori overweight. ")
else:
    print("Anda masuk dalam kategori obesitas. ")

