# B. Validasi Nilai
bilangan = int(input("Masukan bilangan yang akan dibagi: "))
pembagi = int(input("Masukan bilangan pembagi: "))
if (pembagi == 0):
    print("Pembagi tidak boleh 0")
else:
    print("Hasil bagi" ,bilangan / pembagi)
