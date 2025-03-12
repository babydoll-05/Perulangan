# Meminta input jumlah hari festival
N = int(input("Masukkan jumlah hari festival: "))

# Meminta input jumlah makanan per hari
M = int(input("Masukkan jumlah makanan yang dinilai per hari: "))

# Inisialisasi total nilai semua makanan
total_nilai_festival = 0
total_makanan_festival = 0

# Loop untuk setiap hari festival
for hari in range(1, N + 1):
    print(f"\nHari {hari}:")
    total_nilai_harian = 0

    # Loop untuk setiap makanan yang dinilai dalam sehari
    for makanan in range(1, M + 1):
        nilai = float(input(f"  Masukkan nilai untuk makanan ke-{makanan}: "))
        total_nilai_harian += nilai

    # Menghitung rata-rata nilai harian
    rata_rata_harian = total_nilai_harian / M
    print(f"  Rata-rata nilai hari {hari}: {rata_rata_harian:.2f}")

    # Menambahkan nilai ke total festival
    total_nilai_festival += total_nilai_harian
    total_makanan_festival += M

# Menghitung rata-rata nilai semua makanan selama festival
rata_rata_festival = total_nilai_festival / total_makanan_festival
print(f"\nRata-rata nilai keseluruhan festival: {rata_rata_festival:.2f}")
