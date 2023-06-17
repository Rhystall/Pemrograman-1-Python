print("====PROGRAM SEDERJANA MENGHITUNG JUMLAH TOTAL BILANGAN====")
bilangan = int(input("Masukkan bilangan: "))
total = 0

while(bilangan > 0):
    total += bilangan
    bilangan -= 1

print("Total nilai: ", total)
