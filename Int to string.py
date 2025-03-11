def int_to_string(angka):
    num_dict = {
        '0': 'nol', '1': 'satu', '2': 'dua', '3': 'tiga', '4': 'empat',
        '5': 'lima', '6': 'enam', '7': 'tujuh', '8': 'delapan', '9': 'sembilan'
    }
    return " ".join(num_dict[digit] for digit in angka)
print(int_to_string('3124'))
