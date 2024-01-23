print("Výtejte v aplikaci pro výpočet obvodu obdelníku")

a = input("Zadejte proměnu a:")
b = input("Zadejte proměnu b:")

a = int(a)
b = int(b)

if a>0 and b>0:
    výsledek = 2*a+2*b
    print("Výsledej je:", výsledek)
else:
    print("Ne.")