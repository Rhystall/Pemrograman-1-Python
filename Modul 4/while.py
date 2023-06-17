#Hello World
i = 0
while i <= 7:
    print("Hello, world!")
    i += 1

#Perulangan increment
a = 1
b = 10
while a < b:
    print("Step ke- ", a)
    a += 1

#Perulangan decrement
a = 10
b = 0
while a > b:
    print("Anda memiliki sisa ", a, "detik")
    a -= 1

#Fungsi Break
a = 0
b = 10
while a < b:
    print("Step ke- ", a)
    a += 1
    if a == 5: 
        print("Step ke- ", a, "Dihentikan!")
        break

#Fungsi Continue
a = 2
b = 8
while a < b:
    print("Step ke- ", a)
    a += 1
    if a == 5:
        print("Skip") 
        continue
    