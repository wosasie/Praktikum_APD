# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])


# daftar_buku = {}

# daftar_buku["novel 1"] = "Senyum pertama di pagi hari airin"
# daftar_buku[1] = "matahari"
# print(daftar_buku)


# daftar_buku = dict(Buku1 = "Harry Potter", Buku2 = "Percy Jackson", Buku3 = "Twilight")
# print (daftar_buku)

# print(daftar_buku.get("Buku2"))
# print(daftar_buku["Buku2"])

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# for i in Nilai:
#     print(i)

# for i, j in Nilai.items():
#     print(f" Nilai dari {i} itu valuenya adalah : {j} ")

# for i, j in Nilai.items(): 
#      print(j)

# Nilai["Struktur Data"] = 99

# Nilai.update({"Struktur Data" : 99})
# Nilai.update({"Matematika" : 77})

# print(Nilai)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# print(Nilai)
# print()

# trashbin = Nilai.pop("Matematika")

# print(Nilai)
# print()
# print(type(trashbin))

# del Nilai["Fisika"]
# print()
# print(Nilai)

# Nilai.clear()
# print(Nilai)

# print(f"jumlah elemen dari variable dict nNilai adalah {len(Nilai)}")

# daftar_nilai  = Nilai.copy()
# print(daftar_nilai)


# key = "carlos sainz", "carles leclerc", "daniel riccardo"
# value = 1
# daftar_kemenangan = dict.fromkeys(key, value)

# # print(daftar_kemenangan)


# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# #mengakses key dan value dari dictionary
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     #mengambil nilai dari list
#     for song in j:
#         print(song)
#         print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }

# for key, value in mahasiswa.items():
#     print("ID mahasiswa : ", key)
#     # for key_a, value_a in value.items():
#     # print (key_a, " : ", value_a)
#     # print("")

# print (mahasiswa[111]["Nama"])
# print (mahasiswa[111]["Hobi"][-1])






