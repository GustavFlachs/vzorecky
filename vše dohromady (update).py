while true:
##"break" to stop app##
print("Vítejte v aplikaci pro výpočet vzorečků pro obdelník")

print("Pro výpočet objemu zadejte 1.")
print("Pro výpočet obvodu zadejte 2.")
print("Pro výpočet obsahu zadejte 3.")
print("Pro ukončení zadejte 4")

volba = input("Zadejte vaší volbu: ")

if volba == "1":
    a = int(input("Zadejte stranu a: "))
    b = int(input("Zadejte stranu b: "))
    c = int(input("Zadejte stranu c: "))

    if a>0 and b>0 and c>0:
        výsledek = a*b*c

        print("objem kvádru je :, výsledek")
    else:
        print("co to robíš chuligáne?")

if volba == "2":
    a = int(input("Zadejte stranu a: "))
    b = int(input("Zadejte stranu b: "))
    if a>0 and b>0:
        print("Výsledek je: ", 2*a+2*b)
    else:
        print("NEEEE!")

if volba == "3:":
    a = int(input("Zadejte stranu a: "))
    b = int(input("Zadejte stranu b: "))
    if a>0 and b>0:
        print("Výsledek je: ", a*b)
    else:
        print("NEEEEEEEEEEE!")
