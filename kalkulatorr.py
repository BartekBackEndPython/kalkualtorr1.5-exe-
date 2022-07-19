#https://www.geeksforgeeks.org/get-your-system-information-using-python-script/

try:
    import os
    os.system(f"title kalkulatorr1.5 - uruchamianie")


    from colorama import init


    init()


    from colorama import Fore

    from math import factorial as f

    from math import sqrt as sq

    from math import isqrt



    def mnozenie(a, b):
        return a * b


    def dzielenie(a, b):
        return a / b


    def dzielenie_(a, b):
        return a % b


    def dodawanie(a, b):
        return a + b


    def odejmowanie(a, b):
        return a - b


    def potęgowanie(a, b):
        return a ** b


    def bmi(waga, wzrost):
        return waga / (wzrost / 100) ** 2


    def przelicznik_predkosci(tryb, predkosc):
        if tryb == 0:
            return predkosc * 3.6
        if tryb == 1:
            return predkosc / 3.6



    if __name__ == "__main__":
        powiadomienie_ = "ValueError,mozliwe powody: w przypadku silni podana liczba minusowa lub podana wartosc nie jest liczba lub jest liczba zmiennoprzecinkowa, lub wykladnik potegi jest inny niż integer."

        print(Fore.MAGENTA + "")

        werjsa = "1.6"

        print("kalkulatorr1.6")

        print(Fore.GREEN + "")

        print("CO NOWEGO:\n")

        print(Fore.YELLOW + "")

        print(
            "COś tam dodano.\n\n\nTIP:W liczbch float musisz napisac kropke zamiast przecinku "
            "np.3.14 - poprawnie, 3,14 -zle(jest tak ponieważ nie chciało mi sie napisać replace'a)")

        print("\n")


        while True:
            try:
                print(Fore.RED + "")
                try:
                    os.system(f"title kalkulator1.5 - menu wyboru działania - wymiary okna - {os.get_terminal_size()}")
                    wybór = int(input(
                        "Wybierz dzialanie? wpisz liczbę od 1 do 9 \n1.mnozenie\n2.dzielenie\n3.dodawanie\n4.odejmowanie\n5.potegowanie\n6.silnie\n7.pierwiastek kwadratowy\n8.BMI\n9.przelicznik predkosci: "))
                    if wybór < 1 or wybór > 9:
                        print(Fore.LIGHTWHITE_EX + "")
                        print("Wartosc musi być integer'em od 1 do 9.")
                    if wybór == 1:
                        os.system(f"title kalkulatorr1.5 - mnożenie - wymiary okna - {os.get_terminal_size()}")
                        print(Fore.WHITE + "")
                        c = float(input("podaj czynnik: "))
                        d = float(input("podaj czynnik: "))
                        wynik = round(mnozenie(c, d), 6)
                        wynik_ = Fore.CYAN + str(wynik)

                        print(wynik_)
                    if wybór == 2:
                        os.system(f"title kalkulatorr1.5 - dzielenie - wymiary okna - {os.get_terminal_size()}")
                        print(Fore.WHITE + "")
                        c = float(input("podaj dzielna:  "))
                        d = float(input("podaj dzielnik: "))
                        if c and d != 0:
                            if dzielenie_(c, d) == 0:
                                wynik = round(dzielenie(c, d))
                                wynik_ = Fore.CYAN + str(wynik)

                                print(wynik_)

                            else:
                                wynik = dzielenie(c, d)
                                wynik_ = Fore.CYAN + str(wynik)

                                print(wynik_)

                        else:
                            print(Fore.YELLOW + "")
                            print("Nie mozna dzielic przez zero.")

                    if wybór == 3:
                        os.system(f"title kalkulatorr1.5 - dodawanie - wymiary okna - {os.get_terminal_size()}")
                        print(Fore.WHITE + "")
                        c = float(input("podaj składnik: "))
                        d = float(input("podaj składnik: "))
                        wynik = round(dodawanie(c, d), 6)
                        wynik_ = Fore.CYAN + str(wynik)

                        print(wynik_)
                    if wybór == 4:
                        os.system(f"title kalkulatorr1.5 - odejmowanie - wymiary okna - {os.get_terminal_size()}")
                        print(Fore.WHITE + "")
                        c = float(input("podaj odjemna:  "))
                        d = float(input("podaj odjemnik: "))
                        wynik = round(odejmowanie(c, d), 6)
                        wynik_ = Fore.CYAN + str(wynik)

                        print(wynik_)
                    if wybór == 5:
                        os.system(f"title kalkulatorr1.5 - potęgowanie - wymiary okna - {os.get_terminal_size()}")
                        print(Fore.WHITE + "")
                        c = float(input("podaj podstawe potegi:  "))
                        d = int(input("podaj wykładnik potegi: "))
                        wynik = round(potęgowanie(c, d), 6)
                        wynik_ = Fore.CYAN + str(wynik)

                        print(wynik_)
                    if wybór == 6:
                        os.system(f"title kalkulatorr1.5 - silnie - wymiary okna - {os.get_terminal_size()}")
                        print(Fore.WHITE + "")
                        c = int(input("podaj liczbe z której chcesz uzyskac silnię: "))
                        wynik = f(c)
                        wynik_ = Fore.CYAN + str(wynik)

                        print(wynik_)
                    if wybór == 7:
                        os.system(f"title kalkulatorr1.5 - pierwiastek kwadratowy - wymiary okna - {os.get_terminal_size()}")
                        print(Fore.WHITE + "")
                        c = float(input("podaj liczbe z ktorej chcesz uzyskac pierwiastek kwadratowy: "))
                        wynik = sq(c)
                        wynik_ = Fore.CYAN + str(wynik)

                        print(wynik_)
                    if wybór == 8:
                        os.system(f"title kalkulatorr1.5 - licznik BMI - wymiary okna - {os.get_terminal_size()}")
                        print(Fore.WHITE + "")
                        c = int(input("podaj swoja wagę(kg): "))
                        d = int(input("podaj swoj wzrost(cm): "))
                        wynik = round(bmi(c, d), 6)
                        wynik_ = Fore.CYAN + str(wynik)

                        print(wynik_)
                    if wybór == 9:
                        os.system(f"title kalkulatorr1.5 - przelicznik m/s - km/h i km/h - m/s - wymiary okna - {os.get_terminal_size()}")
                        c = None
                        d = None
                        print(Fore.WHITE + "")
                        while c != 1 and c != 2:
                            c = int(input("podaj tryb przeliczania(1.m/s na km/h, 2.km/h na m/s: "))
                        if c == 1:
                            c = 0
                        else:
                            c = 1
                        d = int(input("podaj prędkość: "))
                        wynik = round(przelicznik_predkosci(c, d), 6)
                        wynik_ = Fore.CYAN + str(wynik)


                        print(wynik_)




                except ValueError:
                    print(
                        "ValueError,mozliwe powody: w przypadku silni podana liczba minusowa lub podana wartosc nie jest liczba lub jest liczbą zmiennoprzecinkowa, lub wykladnik potegi jest inny niz integer.")

            except KeyboardInterrupt:
                print("\n")
                print("KeyboardInterrupt(Error) został obsłużony.")
                print("\n")




except KeyboardInterrupt:
    print("\n")
    print("KeyboardInterrupt(Error) został obsłużony")
    print("\n")


