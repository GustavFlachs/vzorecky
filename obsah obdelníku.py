print("Výtejte v aplikaci pro výpočet obsahu obdelníku")

a = input("Zadejte proměnu a:")
b = input("Zadejte proměnu b:")

a = int(a)
b = int(b)

if a>0 and b>0:
    výsledek = a*b
    print("Výsledej je:", výsledek)
else:
    print("Ne.")