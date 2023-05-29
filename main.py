def prendeles():
    pizza_fajtak = {
        "sonkás": 1000,
        "kukoricás": 900,
        "hagymás": 800
    }

    extrak = {
        "extra sajt": 200,
        "gomba": 150,
        "ananász":170,
        "olívabogyó": 100
    }

    innivalok = {
        "Coca-Cola": 300,
        "Víz": 200,
        "Baracklé": 280,
        "Fanta": 280
    }

    rendelesossz = []

    print("Üdvözöllek a pizzarendelő chatbotban! Miben segíthetek?")
    print("Elérhető pizzák: sonkás, kukoricás, hagymás")
    print("Elérhető plusz feltétek: extra sajt, gomba, olívabogyó,ananász")
    print("Elérhető italok: Coca-Cola,Fanta,Víz,Baracklé")

    while True:
        user_input = input("Mit szeretnél rendelni? (vagy 'kész' a rendeléshez): ")

        if user_input == "kész":
            break

        if user_input in pizza_fajtak:
            rendelesossz.append(("pizza", user_input, pizza_fajtak[user_input]))
            print(f"{user_input} pizzát hozzáadtuk a rendeléshez.")
        elif user_input in extrak:
            rendelesossz.append(("plusz feltét", user_input, extrak[user_input]))
            print(f"{user_input} plusz feltétet hozzáadtuk a rendeléshez.")
        elif user_input in innivalok:
            rendelesossz.append(("ital", user_input, innivalok[user_input]))
            print(f"{user_input} italt hozzáadtuk a rendeléshez.")
        else:
            print("Sajnálom, nem értettem. Kérlek, válassz a rendelhető opciók közül.")

    total_ar = sum(item[2] for item in rendelesossz)
    print("Rendelési állomány:")
    for item in rendelesossz:
        print(f"{item[0]}: {item[1]} - {item[2]} Ft")
    print(f"Végösszeg: {total_ar} Ft")

if __name__ == "__main__":
    prendeles()
