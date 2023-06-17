# A. Suhu
suhu = int(input("Masukkan Suhu: "))
if suhu <= 0:
    print("Pada suhu", suhu, "air akan berwujud padat (es)")
elif suhu > 0 and suhu < 100:
    print("Pada suhu", suhu ,"air akan berwujud cair")
else:
    print("Pada suhu", suhu ,"air akan berwujud gas")

# B. Panggilan bedasarkan status
gender = input("Perempuan atau Laki-laki ? (L/P): ")
if gender == "L":
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if status == "Y":
        print("Hallo Bapak!")
    elif status == "N":
        print("Hallo Mas!")
    else:
        print("Pilihan tidak tersedia")
elif gender == "P":
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if status == "Y":
        print("Hallo Ibu!")
    if status == "Y":
        print("Hallo Mba!")
    else:
        print("Pilihan tidak tersedia")
else:
    print("Pilihan tidak tersedia")

# C. Data Diri
print("=============INPUT=============")
nama = input("Nama: ")
jk = input("Jenis Kelamin (L/P): ")
agama = int(input("Agama: "))
#1=Islam, 2=Prostetan, 3=Katolik, 4=Hindu, 5=Budha
if agama == 1:
    agama = "Islam"
elif agama==2:
    agama = "Prostetan"
elif agama==3:
    agama = "Katolik"
elif agama==4:
    agama = "Hindu"
elif agama==5:
    agama = "Budha"
else:
    print("Pilihan tidak tersedia")
print("=============OUTPUT=============")
print("Nama: ", nama)
print("Jenis Kelamin: ", jk)
print("Agama: ", agama)