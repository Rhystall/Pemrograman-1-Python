#Prosedur dasar operasi kalkulator
def penjumlahan(bil1, bil2):
    penjumlahan = bil1 + bil2
    print("Hasil Penjumlahan : ", penjumlahan)

def perkalian(bil1, bil2):
    perkalian = bil1 * bil2
    print("Hasil Perkalian : ", perkalian)

def pembagian(bil1, bil2):
    pembagian = bil1 / bil2
    print("Hasil Pembagian : ", pembagian)

def pengurangan(bil1, bil2):
    pengurangan = bil1 - bil2
    print("Hasil Pengurangan : ", pengurangan)

def pangkat(bil1, bil2):
    pangkat = bil1 ** bil2
    print("Hasil Pangkat : ", pangkat)

#Menu 
print("KALKULATOR")
print("1. Penjumlahan")
print("2. Perkalian")
print("3. Pembagian")
print("4. Pengurangan")
print("5. Pangkat")
pilihan = int(input("Masukkan pilihan : "))

#Kondisi menu spesial saat user memilih perpangkatan
if pilihan == 5:
    print("Bilangan 1 : Untuk bilangan yang akan di pangkatkan")
    print("Bilangan 2 : Untuk pangkat")
    bil1 = int(input("Bilangan pertama : "))
    bil2 = int(input("Bilangan kedua : "))
else:
    bil1 = int(input("Bilangan pertama : "))
    bil2 = int(input("Bilangan kedua : "))

#Kondisi function if else di saat user memilih pilihan
def hasil():    
    if pilihan == 1:
        penjumlahan(bil1, bil2)
    elif pilihan == 2:
        perkalian(bil1, bil2)
    elif pilihan == 3:
        pembagian(bil1, bil2)
    elif pilihan == 4:
        pengurangan(bil1, bil2)
    elif pilihan == 5:
        pangkat(bil1, bil2)
    else:
        print("Pilihan tidak tersedia")

hasil()

#Function yang akan ditampilam saat user kembali ke menu
def kalkulator():
    global pilihan, bil1, bil2
    print("KALKULATOR")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pembagian")
    print("4. Pengurangan")
    print("5. Pangkat")
    pilihan = int(input("Masukkan pilihan : "))
    bil1 = int(input("Bilangan pertama : "))
    bil2 = int(input("Bilangan kedua : "))


#Program untuk mengatur apakah akan kembali ke menu atau tidak
menu = "Y"
while menu != "N":
    menu = input("Apakah anda ingin kembali ke menu (Y/N) ? : ")
    
    if menu == "Y":
        kalkulator()
        hasil()
    elif menu == "N":
        print("Terima kasih telah menggunakan kalkulator ini")
    else:
        print("Tidak ada pilihan")