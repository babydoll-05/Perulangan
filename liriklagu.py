# Meminta input jumlah putaran lagu
N = int(input("Masukkan jumlah putaran lagu: "))

# Inisialisasi total baris lirik
total_baris = 0  

# Perulangan untuk menyanyikan lagu dengan jumlah pengulangan yang bertambah
for putaran in range(1, N + 1):
    print(f"\nPutaran {putaran}:")
    for _ in range(putaran):
        print("Happy Birthday to You")
        total_baris += 1  # Menambahkan total baris lirik yang dinyanyikan

# Menampilkan total baris lirik yang dinyanyikan
print(f"\nTotal baris lirik yang dinyanyikan: {total_baris}")
