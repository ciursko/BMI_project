def main():
    while True:
        jednostka = input("Możesz obliczyć BMI w jednostach metrycznych lub imperialnych. Czy chcesz używać jednostki metrycznej? ")

        BMI = 0
        if jednostka.lower() == "tak":
            masa = float(input("Podaj masę ciała w kilogramach: "))
            wzrost = float(input("Podaj wzrost w centymetrach: "))
            BMI = masa / pow(wzrost / 100, 2)
            jednostki_opis = "metryczne"
        elif jednostka.lower() == "nie":
            masa = float(input("Podaj masę ciała w funtach: "))
            wzrost = float(input("Podaj wzrost w calach: "))
            BMI = masa * 703 / pow(wzrost, 2)
            jednostki_opis = "imperialne"
        else:
            print("Nieprawidłowa odpowiedź. Spróbuj jeszcze raz.")
            continue

        BMIo = round(BMI, 2)  # zaokrąglone
        klasyfikacja = kategoria(BMIo)

        with open("dane_BMI_po.txt", "a") as file:
            file.write(f"Jednostki: {jednostki_opis}\n")
            file.write(f"Twoja waga {masa}\n")
            file.write(f"Twój wzrost {wzrost}\n")
            file.write(f"Twoje BMI wynosi: {BMIo}\n")
            file.write(f"Kategoria: {klasyfikacja}\n")
            file.write("\n")

        print(f"Twoje BMI wynosi: {BMIo}")
        print(f"Kategoria: {klasyfikacja}")
def kategoria(BMIo):
    if BMIo < 16.0:
        return "Wygłodzenie"
    elif 16.0 <= BMIo <= 16.99:
        return "Wychudzenie"
    elif 17.0 <= BMIo <= 18.49:
        return "Niedowaga"
    elif 18.5 <= BMIo <= 24.99:
        return "Porządana masa ciała"
    elif 25.0 <= BMIo <= 29.99:
        return "Nadwaga"
    elif 30.0 <= BMIo <= 34.99:
        return "Otyłość I stopnia"
    elif 35.0 <= BMIo <= 39.99:
        return "Otyłość II stopnia (duża)"
    elif BMIo >= 40.0:
        return "Otyłość III stopnia (chorobliwa)"


main()