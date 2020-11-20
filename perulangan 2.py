import time

#Nama: Muhamad Rizky Nilzamyahya
#NIM: 2009106029 + 10 = 39
nim = int(input("Masukkan NIM kamu: "))

for i in range(nim + 10):
    if((i+1) % 9 == 0):
        print(9)
    else:
        print((i+1) % 9)
        time.sleep(2)