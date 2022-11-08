""""
Latian dasar perulangan : dengan For
Ibu menyuruh anak membaca buku sebanyak 100 buku
"""

print('Ibu : "Nak, bacalah buku itu sebanyak 100 buku"')
print('Anak : "Oke, siap"')

jumlah_buku = 100

jumlah_buku_yang_sudah_dibaca = 0
print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f'Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print(f'jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_dibaca}')