# def aku_fungsi():
#     print("hello world ")

# aku_fungsi()

# def tambah(a,b):
#     hasil = a+b
#     print(hasil)

# tambah(10,3)

# def tambah(a,b):
#     hasil = a+b
#     return hasil
# tambah(2,4)
       
# tambahan = tambah(2,5) + tambah (4,6)
# tambahan = 6 + 18
# print(tambahan)


# def pilihan(opsi):
#     match opsi:
#         case 1:
#             print(1)
#             return
#         case 2:
#             print(2)
#             return
#     print(3)

# # pilihan(2)

# def cetak (nama, nim, matkul):
#     print(nama, nim, matkul)

# cetak("Fathir", 41, "Kalkulus ")

# def cetak (nama, nim, *matkul): #dilakukan agar dapat membuat tuple, syarat membuat ini parameter paling akhir
#     print(nama, nim, matkul)

# cetak("Fathir", 41, "Kalkulus", "Fisika Dasar")


# #rumus: sisi x sisi
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# # rumus: sisi x sisi x sisi
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)
# # pemanggilan Fungsi
# luas_persegi(4)
# volume_persegi(6)

# var = 2,4,5

# var1, var2, var3, = var
# print(var1)
# print(var2)
# print(var3)

# print(type(var))

#jika ingin buat gungsi taruh di atas


# membuat variabel global
Nama = "Informatika"
Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# membuat variabel lokal
def info():
    Nama = "Teknik Elektro"
    Mata_Kuliah = "Pengantar Teknik ELektro"
    # mengakses variabel lokal
    print("Prodi:", Nama)
    print("Mata Kuliah:", Mata_Kuliah)
# mengakses variabel global
print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)
# memanggil fungsi info
info()



