# 1. Membuat variabel harga dan jumlah
harga = 12500
jumlah = 4

# 2. Menghitung total harga
total_harga = harga * jumlah

# 3. Menghitung sisa pembagian (modulo) total harga dengan 2000
sisa_pembagian = total_harga % 2000

# 4. Menghitung harga setelah diskon Rp5.000
diskon = 5000
harga_setelah_diskon = total_harga - diskon

# 5. Menampilkan hasil perhitungan dengan label yang jelas
print("=== RINCIAN PEMBELIAN BUKU ===")
print(f"Harga per Buku       : Rp{harga:,}")
print(f"Jumlah Buku          : {jumlah} buah")
print("-" * 35)
print(f"Total Harga          : Rp{total_harga:,}")
print(f"Sisa Pembagian %2000 : {sisa_pembagian}")
print(f"Harga Setelah Diskon : Rp{harga_setelah_diskon:,}")
