# Bentuk dasar for range di phyton
for i in range (10):
    print("Hello World!")

# Bentuk dasar for range dengan minimal maksimal 
for i  in range (1, 10):
    print(f"Perulangan ke- {i}")

# Bentuk dasar for range dengan minimal maksimal dan step
for i in range (0, 20, 2):
    print(f"Perulangan ke- {i}")

#Perulangan menurun
for i in range (10, 0, -1):
    print(f"Perulangan ke- {i}")

#Fungsi Break
for i in range (1, 20):
    print(f"Perulangan ke- {i}")
    if i == 9:
        break

#Fungsi Continue
for i in range (1, 5):
    print(f"Perulangan ke- {i}")
    if i == 4:
        continue

