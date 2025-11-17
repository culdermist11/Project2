# Zadanie 5 A

with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("ALR,113")
    plik.close()

plik = open("notowania_gieldowe.txt","r")
print(plik.read())
plik.close()
