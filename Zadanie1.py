# Zadanie 1

punkty = int(input("Podaj punkty: "))

if punkty > 80:
    print("zaliczono w termine 0")
elif punkty > 50 and punkty <= 80:
    print("można poprawić wynik")
else:
    print("należy poprawić wynik")
