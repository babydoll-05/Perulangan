def hitung_ips():
    bobot_nilai = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    jumlah_mk = int(input("Berapa jumlah mata kuliah? "))
    total_sks = jumlah_mk * 3
    total_bobot = 0
    for i in range(1, jumlah_mk + 1):
        nilai = input(f"Nilai MK {i}: ").strip().upper()
        if nilai in bobot_nilai:
            total_bobot += bobot_nilai[nilai] * 3
        else:
            print("Nilai tidak valid! Masukkan A, B, C, atau D.")
            return
    ips = total_bobot / total_sks
    print(f"Nilai IPS anda semester ini {ips:.2f}")
hitung_ips()
