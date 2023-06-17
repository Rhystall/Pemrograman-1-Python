# C. Identifikasi biaya operasi penyakit
print("<-- Menu Hitung Biaya Operasi -->")
print("1. Hitung Biaya Operasi Mata")
print("2. Hitung Biaya Operasi Jantung")
inputan_operasi = int(input("Masukkan pilihan : "))
if inputan_operasi == 1:
    print("JENIS PENYAKIT MATA :")
    print("1. Katarak")
    print("2. Plus/Minus")
    print("3. Silinder")
    jp = int(input("Masukkan Nomor Penyakit Mata : "))
    if(jp == 1):
        print("Biaya Operasi Katarak = Rp. 7.500.00")
    elif(jp == 2):
        print("Biaya Operasi Plus/Minus = Rp. 5.000.000")
    elif(jp == 3):
        print("Biaya Operasi Silinder = Rp. 4.000.000")
    else:
        print("Operasi tidak tersedia")
elif inputan_operasi == 2:
    print("JENIS PENYAKIT JANTUNG :")
    print("1. Jantung Koroner")
    print("2. Katup Jantung")
    print("3. Otot Jantung")
    jp = int(input("Masukkan Nomor Penyakit Mata : "))
    if(jp == 1):
        print("Biaya Operasi Jantung Kororer = Rp. 500.000.000")
    elif(jp == 2):
        print("Biaya Operasi Katup Jantung = Rp. 350.000.000")
    elif(jp == 3):
        print("Biaya Operasi Otot Jantung = Rp. 450.000.000")
else:
    print("Pilihan tidak tersedia")