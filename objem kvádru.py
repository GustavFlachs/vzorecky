print("Výtejte v aplikaci pro výpočet objemu kvádru")

a = input("Zadejte proměnu a:")
b = input("Zadejte proměnu b:")
c = input("Zadejte proměnu c:")

a = int(a)
b = int(b)
c = int(c)

if a>0 and b>0:
    výsledek = a*b*c
    print("Výsledej je:", výsledek)
else:
    print("Ne.")