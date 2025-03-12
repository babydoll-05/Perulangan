# Input jumlah hari
n = int(input("Masukkan jumlah hari pengamatan: "))

# Inisialisasi jumlah bakteri pada tiga hari pertama
a, b, c = 1, 1, 2  

# Cetak tiga hari pertama
print(f"Hari 1: {a} bakteri")
print(f"Hari 2: {b} bakteri")
print(f"Hari 3: {c} bakteri")

# Perulangan untuk menghitung jumlah bakteri pada hari-hari berikutnya
for day in range(4, n + 1):  
    next_bacteria = a + b + c  
    print(f"Hari {day}: {next_bacteria} bakteri")
    a, b, c = b, c, next_bacteria  # Geser nilai untuk iterasi berikutnya
