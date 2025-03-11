n = int(input("Masukkan angka: "))
faktorial = 1
for i in range(1, n+1):
    faktorial *= i
print(f"Faktorial dari {n} adalah {faktorial}")
