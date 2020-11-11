#Tema: Balok
print("")
print("Tentukan Nilai dari: \na.Luas permukaan balok \nb.Keliling balok \nc.Volume Balok")
print("Beserta nilai biner dari setiap hasil")
print("")

#MENCARI NILAI LUAS PERMUKAAN DAN NILAI BINERNYA
print("a.Luas Permukaan \nDiketahui:")
p1 = int(input("p = "))
l1 = int(input("l = "))
t1 = float(input("t = "))
print("")

print("Rumus:")
print("L = 2 * ((p * l) + (p * t) + (l * t))")
L = 2 * ((p1 * l1) + (p1 * t1) + (l1 * t1))
print("Luas Permukaan Balok =", L)
desimal = int(L)
binerL = bin(desimal) .replace("b","")
print("Nilai biner =", binerL)
print("")

#MENCARI NILAI KELILING DAN NILAI BINERNYA
print("b.Keliling \nDiketahui:")
p2 = int(input("p = "))
l2 = int(input("l = "))
t2 = float(input("t = "))
print("")

print("Rumus:")
print("K = 4 * (p + l + t)")
K = 4 * (p2 + l2 + t2)
print("Keliling Balok =", K)
desimal = int(K)
binerK = bin(desimal) .replace("b","")
print("Nilai biner =", binerK)
print("")

#MENCARI NILAI VOLUME SAMA NILAI BINERNYA
print("c.Volume \nDiketahui:")
p3 = int(input("p = "))
l3 = int(input("l = "))
t3 = float(input("t = "))
print("")

print("Rumus:")
print("V = p * l * t")
V = p3 * l3 * t3
print("Volume Balok =", V)
desimal = int(V)
binerV = bin(desimal) .replace("b","")
print("Nilai biner =", binerV)
print("")

#MASUKKAN LIST SATU-SATU
listLP = []
listLP.append(p1)
listLP.append(l1)
listLP.append(t1)
listLP.append(L)

listK = []
listK.append(p2)
listK.append(l2)
listK.append(t2)
listK.append(K)

listV = []
listV.append(p3)
listV.append(l3)
listV.append(t3)
listV.append(V)

Jawaban = []
Jawaban.append(L)
Jawaban.append(K)
Jawaban.append(V)

binerLKV = []
binerLKV.append(binerL)
binerLKV.append(binerK)
binerLKV.append(binerV)

#PRINT ISI LIST
print("List Luas Permukaan:")
print("p =", listLP[0])
print("l =", listLP[1])
print("t =", listLP[2])
print("Luas Permukaan =", listLP[3])
print("")

print("List Keliling:")
print("p =", listK[0])
print("l =", listK[1])
print("t =", listK[2])
print("Keliling =", listK[3])
print("")

print("List Volume:")
print("p =", listV[0])
print("l =", listV[1])
print("t =", listV[2])
print("Volume =", listV[3])
print("")

print("List Hasil Jawaban:")
print("L =", Jawaban[0])
print("K =", Jawaban[1])
print("V =", Jawaban[2])
print("")

print("List dalam bentuk biner:")
print("Biner L =", binerLKV[0])
print("Biner K =", binerLKV[1])
print("Biner V =", binerLKV[2])
print("")