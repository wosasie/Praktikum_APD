nama_Barang = input("Nama Barang : ")
harga_Barang = float(input("Harga Barang : "))
jumlah_Barang = int(input("Jumlah Barang : "))
persen_Diskon = float(input("Persen Diskon : "))

total_Sebelum_Diskon = jumlah_Barang * harga_Barang
total_Diskon = persen_Diskon / 100 * total_Sebelum_Diskon
harga_Setelah_Diskon = total_Sebelum_Diskon - total_Diskon
total_Bayar = harga_Setelah_Diskon
sisa_Bagi_Diskon = persen_Diskon % 3

print("anda membeli ", jumlah_Barang, nama_Barang, "dengan harga satuan ", harga_Barang, ", total diskon adalah", total_Diskon, ", dan total yang harus dibayar adalah ", total_Bayar, ". ")
print (persen_Diskon, "dibagi dengan 3 sisanya ", sisa_Bagi_Diskon)