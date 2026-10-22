# Inisialisasi struktur data awal
nilai = [78, 85, 90, 85]
mahasiswa = {"nama": "Nadia", "kelas": "IF-A"}
koordinat = (5, 8)
angka = {2, 4, 4, 6, 8}

# 1. Tampilkan nilai pertama dari list
print("1. Nilai pertama list       :", nilai[0])

# 2. Tambahkan nilai 95 ke list dan tampilkan list terbaru
nilai.append(95)
print("2. List setelah append(95)  :", nilai)

# 3. Tampilkan nama mahasiswa dari dictionary
print("3. Nama mahasiswa (dict)    :", mahasiswa["nama"])

# 4. Tampilkan koordinat pertama dari tuple
print("4. Koordinat pertama tuple  :", koordinat[0])

# 5. Tampilkan angka unik dengan sorted(angka)
print("5. Angka unik (sorted set)  :", sorted(angka))