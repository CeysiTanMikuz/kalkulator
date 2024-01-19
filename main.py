print("""
============================
PROGRAM KALKULATOR BY : ALEX
============================

""")

angka1 = float(input('Masukan Angka Pertama : '))
operator = input('Pilih Operator (x, +, -, /, %, //) : ')
angka2 = float(input('Masukan Angka Kedua : '))

if operator == '+':
    hasil = angka1 + angka2
    print(f'Hasil Dari Penjumlahan Tersebut Adalah : {hasil}')
    print(f'Terima Kasih Telah Memakai Kalkulatornya :) ')
elif operator == 'x':
    hasil1 = angka1 * angka2
    print(f'Hasil Dari Pengurangan Tersebut Adalah : {hasil1}')
    print(f'Terima Kasih Telah Memakai Kalkulatornya :) ')
elif operator =='%':
    hasil2 = angka1 % angka2
    print(f'Hasil Dari Modulus Tersebut Adalah : {hasil2}')
    print(f'Terima Kasih Telah Memakai Kalkulatornya :) ')
elif operator == '/':
    hasil3 = angka1 / angka2
    print(f'Hasil Dari Pembagian Tersebut Adalah : {hasil3}')
    print(f'Terima Kasih Telah Memakai Kalkulatornya :) ')
elif operator == '//':
    hasil4 = angka1 // angka2
    print(f'Hasil Dari Floor Division Tersebut Adalah : {hasil4}')
    print(f'Terima Kasih Telah Memakai Kalkulatornya :) ')
elif operator =='-':
    hasil5 = angka1 - angka2
    print(f'Hasil Dari Perkalian Tersebut Adalah : {hasil5}')
    print(f'Terima Kasih Telah Memakai Kalkulatornya :) ')



else:
    print('Input Tidak Valid Silakan Masukan Sesuai Operator')

    print(f'Terima Kasih Telah Memakai Kalkulatornya :) ')
