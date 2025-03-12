# Meminta input jarak total menuju gerbang keluar
N = int(input("Masukkan jarak menuju gerbang keluar (dalam km): "))

# Inisialisasi hari dan total jarak yang sudah ditempuh
hari = 0
jarak_tempuh = 0
langkah_harian = 1  # Jarak yang ditempuh Budi di hari pertama

# Perulangan untuk menghitung jarak yang ditempuh setiap hari
while jarak_tempuh < N:
    hari += 1
    jarak_tempuh += langkah_harian
    print(f"Hari {hari}: Budi berjalan {langkah_harian} km, total: {jarak_tempuh} km")
    langkah_harian += 1  # Setiap hari Budi bisa berjalan lebih jauh

# Menampilkan hasil akhir
print(f"\nBudi berhasil keluar dari hutan dalam {hari} hari!")
