#If dengan satu kondisi
nilai = int(input("Masukkan bilangan bulat: "))
if (nilai > 0):
    print("Bilangan", nilai, "merupakan bilangan positif")

#If dengan dua kondisi
nilai = int(input("Masukkan bilangan bulat: "))
if (nilai > 0):
    print("Bilangan", nilai, "merupakan bilangan positif")
else:
    print("Bilangan", nilai, "merupakan bilangan negatif")

#If dengan tiga kondisi atau lebih
nilai = int(input("Masukkan bilangan bulat: "))
if (nilai > 0):
    print("Bilangan", nilai, "merupakan bilangan positif")
elif (nilai < 0):
    print("Bilangan", nilai, "merupakan bilangan negatif")
else:
    print(nilai, "Merupakan bilangan nol")