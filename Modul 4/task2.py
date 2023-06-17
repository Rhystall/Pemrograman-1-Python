print("====Program Sederhana Menghitung Pangkat====")
bilangan = int(input("Masukkan bilangan: "))
pangkat = int(input("Masukkan bilangan pencacah: "))
hasil = 1
for i in range(pangkat):
    hasil *= bilangan
print(hasil)
