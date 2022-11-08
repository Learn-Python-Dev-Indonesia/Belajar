"""
Latian percabangan :
Ibuk : Menyuruh anak beli kopi, jika ada rokok surya rolong belikan satu bungkus
"""
print('Ibu : "Nak, Belikan Bapakmu Kopi, jika di toko ada Rokok Surya belikan satu bungkus?"')
print('Anak : "ooo Iya Buk, mana uang nya"')
print('Anak : Oke Buk, Budi tak berangkat Sekarang ya."')
print('Ibuk: "Iya nak hati-hati"')

kopi_hitam = 10
rokok_surya = 9

print('Budi :')
if kopi_hitam > 0 :
    if rokok_surya == 0 :
        print('Beli Kopi')
    else:
        print('Beli Kopi dan Roko surya satu bungkus')
else:
    print('tidak jadi beli')
print('Budi: "pulang dan menyerahkan apa yang di perintakan ibunya')
