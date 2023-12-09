def tabela(dane_BMI):
    try:
        with open(dane_BMI, 'r') as plik:
            for line in plik:
                kolumna = line.strip().split(',')
                masa = float(kolumna[0])
                wzrost = float(kolumna[1])
                BMI = masa / pow(wzrost / 100, 2)
                BMI = round(BMI, 2)

                if BMI < 16.0:
                    okr = "Wygłodzenie"
                elif 16.0 <= BMI <= 16.99:
                    okr = "Wychudzenie"
                elif 17.0 <= BMI <= 18.49:
                    okr = "Niedowaga"
                elif 18.5 <= BMI <= 24.99:
                    okr = "Porządana masa ciała"
                elif 25.0 <= BMI <= 29.99:
                    okr = "Nadwaga"
                elif 30.0 <= BMI <= 34.99:
                    okr = "Otyłość I stopnia"
                elif 35.0 <= BMI <= 39.99:
                    okr = "Otyłość II stopnia (duża)"
                elif 40.0 <= BMI:
                    okr = "Otyłość III stopnia (chorobliwa)"
                print(f"Waga: {masa} kg, Wzrost: {wzrost} cm, BMI: {BMI}, Kategoria BMI: {okr}")
    except FileNotFoundError:
        print("Nie mogę znależć pliku")


def main():
    f = input("Podaj ścieżkę do tabeli danych: ")
    tabela(f)


main()
