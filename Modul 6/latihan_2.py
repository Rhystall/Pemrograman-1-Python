#Hitung keliling luas dengan prosedur
def keliling_luas_persegi(sisi):
    keliling = 4 * sisi
    print("Keliling persegi: ", keliling)
    luas = sisi * sisi
    print("Luas persegi: ", luas)

sisi = int(input("Masukkan sisi persegi: "))
keliling_luas_persegi(sisi)
