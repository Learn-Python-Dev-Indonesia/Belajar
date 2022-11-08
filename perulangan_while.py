""""
Belajar perulangan dengan while
Ibu menyuruh anak membaca buku sebanyak 100 buku
"""
print('Ibu : "Nak, bacalah buku itu sebanyak 100 buku"')
print('Anak : "Oke, siap"')

jumlah_buku = 1000
jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_dibaca}')

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f'Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print(f'Jumlah buku yang sudah di baca{jumlah_buku_yang_sudah_dibaca}')
