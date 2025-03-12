# Meminta input jumlah minggu
N = int(input("Masukkan jumlah minggu menabung: "))

# Inisialisasi nilai awal
total_tabungan = 0

# Perulangan untuk menambahkan kelipatan 3 setiap minggu
for minggu in range(1, N + 1):
    tabungan_minggu_ini = 3 * minggu * 1000  # Kelipatan 3 dari minggu
    total_tabungan += tabungan_minggu_ini
    print(f"Minggu {minggu}: Menabung Rp{tabungan_minggu_ini}, Total: Rp{total_tabungan}")

# Menampilkan total tabungan akhir
print(f"\nTotal tabungan setelah {N} minggu: Rp{total_tabungan}")
