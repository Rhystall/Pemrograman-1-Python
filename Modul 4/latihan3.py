#Mencari bilangan fpb
def hitung_fpb(x, y):
    if x > y:
        terkecil = x
    else:
        terkecil = y
    for i in range(1, terkecil+1):
        if (x % i == 0) and (y % i == 0):
            fpb = i
    return fpb

x = int(input("Masukan bilangan x: "))
y = int(input("Masukan bilangan y: "))
hasil = hitung_fpb(x, y)
print(hasil)