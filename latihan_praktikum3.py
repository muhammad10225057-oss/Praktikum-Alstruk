# 1. Buat variabel nilai dan kehadiran
nilai = 82
kehadiran = 90

# 2. Memeriksa masing-masing syarat
syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print("=== Pengujian Awal (Nilai = 82, Kehadiran = 90) ===")
print("Syarat Nilai (>= 75)       :", syarat_nilai)
print("Syarat Kehadiran (>= 80%)  :", syarat_kehadiran)

# 3. Menggunakan operator 'and'
lulus_and = syarat_nilai and syarat_kehadiran
print("Status Kelulusan (AND)     :", lulus_and)

# 4. Mengubah nilai menjadi 70
nilai = 70
syarat_nilai_baru = nilai >= 75
syarat_kehadiran_baru = kehadiran >= 80
lulus_and_baru = syarat_nilai_baru and syarat_kehadiran_baru

print("\n=== Pengujian Kedua (Nilai = 70, Kehadiran = 90) ===")
print("Syarat Nilai (>= 75)       :", syarat_nilai_baru)
print("Syarat Kehadiran (>= 80%)  :", syarat_kehadiran_baru)
print("Status Kelulusan (AND)     :", lulus_and_baru)

# 5. Menguji dengan operator 'or'
lulus_or_baru = syarat_nilai_baru or syarat_kehadiran_baru
print("Status Kelulusan (OR)      :", lulus_or_baru)