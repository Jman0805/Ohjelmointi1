luku = int(input("Anna luku: "))

alkuluku = True

for i in range(2, luku):
    if luku % i == 0:
        alkuluku = False

if alkuluku:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")