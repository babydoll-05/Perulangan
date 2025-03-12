# Meminta input ukuran tabel perkalian
N = int(input("Masukkan ukuran tabel perkalian: "))

# Perulangan untuk baris
for i in range(1, N + 1):
    # Perulangan untuk kolom
    for j in range(1, N + 1):
        print(f"{i * j:4}", end=" ")  # Format agar rapi
    print()  # Pindah ke baris baru
