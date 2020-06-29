from geometri.bangunruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import SegiTiga

print('Menggunakan OOP')

print('\nLuas Persegi Panjang')
p1 = PersegiPanjang(10, 3)
print(f'\n{p1.info()}')
print(f'Luas object persegi panjang ini adalah {p1.hitung_luas()}')

print('\nLuas Segitiga')
s1 = SegiTiga(10, 3)
print(f'\n{s1.info()}')
print(f'Luas object segitiga adalah {s1.hitung_luas()}')

print('\nMencoba membuat object dari class BangunRuang')
b1=BangunRuang()
print(b1.info())
print(b1.hitung_luas())

# Polymorphism: kemampuan object untuk merespon berbeda terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
    print(bangun_ruang.hitung_luas())
