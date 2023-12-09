def main():
    masa = float(input("Podaj mase ciała w kilogramach: ")) # Wprowadzanie masy ciała i wzrostu od użytkownika
    wzrost = float(input("Podaj wzrost w centymetrach: "))
    BMI: float = masa / pow(wzrost / 100, 2) # Obliczanie BMI
    BMI = float(round(BMI, 2)) # Zaokrąglanie do dwóch miejsc po przecinku
    print(BMI) # Wyświetlanie obliczonego BMI
    if BMI < 16.0: # Określanie kategorii BMI i wyświetlanie odpowiedniego komunikatu
        print("Wygłodzenie")
    elif 16.0 <= BMI <= 16.99:
        print("Wychudzenie")
    elif 17.0 <= BMI <= 18.49:
        print("Niedowaga")
    elif 18.5 <= BMI <= 24.99:
        print("Porządana masa ciała")
    elif 25.0 <= BMI <= 29.99:
        print("Nadwaga")
    elif 30.0 <= BMI <= 34.99:
        print("Otyłość I stopnia")
    elif 35.0 <= BMI <= 39.99:
        print("Otyłość II stopnia (duża)")
    elif 40.0 <= BMI:
        print("Otyłość III stopnia (chorobliwa)")


main()
