# Zadanie 1 (Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.)
print("Zadanie 3: Generuje liczby i wstawia je do pliku")
plik = open("liczby.txt", "w")
for liczba in range(1000):
    if liczba % 4 == 0:
        plik.write(f"{liczba} ")
plik.close()

# Zadanie 2 (Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.)
print("Zadanie 2: ")
plik = open("liczby.txt", "r")
wiersze = plik.readlines()
print(wiersze)
plik.close()

# Zadanie 3 (Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.)
print("Zadanie 3: ")
with open("tekst.txt", "w") as plik:
    for a in range(10):
        plik.write("Przykładowy tekst zapisywany do pliku\n")
with open("tekst.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")

# Zadanie 4 (Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
#   nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
#   konstruktor – który nadaje wartości
#   wyświetl_produkt() – drukuje informacje o produkcie na ekranie
#   ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
#   ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2)
print("Zadanie 4: ")


class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyświetl_produkt(self):
        return self.nazwa_produktu

    def ile_produktu(self):
        return self.ilosc, self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed


mleko = NaZakupy("mleko", 6, "l", 2.99)
chleb = NaZakupy("chleb", 1, "szt", 2.99)
cukier = NaZakupy("cukier", 3, "kg", 2.99)

print(mleko.wyświetl_produkt(), mleko.ile_produktu(), mleko.ile_kosztuje())

print(chleb.wyświetl_produkt(), chleb.ile_produktu(), chleb.ile_kosztuje())

print(cukier.wyświetl_produkt(), cukier.ile_produktu(), cukier.ile_kosztuje())


# Zadanie 5
# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
# wyświetl_dane – drukuje elementy na ekran
# pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# policz_sume – liczy sume elementow
# policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.
print("Zadanie 5: ")


class Ciągi:
    def __init__(self, pierwszy_wyraz, roznica, ilosc_wyrazow):
        self.pierwszy_wyraz = pierwszy_wyraz
        self.roznica = roznica
        self.ilosc_wyrazow = ilosc_wyrazow

    def wyświetl_dane(self):
        return f"Pierwszy wyraz: {self.pierwszy_wyraz} Różnica: {self.roznica} Ilość wyrazów: {self.ilosc_wyrazow}"

    def pobierz_elementy(self):
        pass

    def pobierz_parametry(self):
        # self.pierwszy_wyraz = int(input("Podaj pierwszy wyraz"))
        # self.roznica = int(input("Podaj roznice"))
        # self.ilosc_wyrazow = int(input("ilosc wyrazów"))
        # return 1
        pass

    def policz_sume(self):
        self.an = self.pierwszy_wyraz+(self.ilosc_wyrazow-1)*self.roznica
        return (self.pierwszy_wyraz+self.an)/2*self.ilosc_wyrazow

    def policz_elementy(self):
        self.ciag = []
        while len(self.ciag) != int(self.ilosc_wyrazow):
            self.ciag.append(self.pierwszy_wyraz)
            self.pierwszy_wyraz += self.roznica
        return self.ciag


pierwszy = Ciągi(1, 5, 20)
print(f"{pierwszy.wyświetl_dane()}\nSuma ciągu: {pierwszy.policz_sume()}\nCiąg: {pierwszy.policz_elementy()}")
# Zad. 6

# Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:

# sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
# sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
# sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
# wyświetl_wyrazy – wyświetla podane wyrazy
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.
print("Zadanie 6: ")


class Słowa:
    def __init__(self, słowo_1, słowo_2):
        self.słowo_1 = słowo_1
        self.słowo_2 = słowo_2

    def sprawdz_czy_palindrom(self):
        self.p1 = self.słowo_1 == self.słowo_1[::-1]
        self.p2 = self.słowo_2 == self.słowo_2[::-1]
        if (self.p1 and self.p2):
            return f"{self.słowo_1} i {self.słowo_2} to palindromy"
        elif (self.p1):
            return f"wyraz {self.słowo_1} to palindrom"
        elif (self.p2):
            return f"wyraz {self.słowo_2} to palindrom"
        else:
            return "brak palindromów"
    def sprawdz_czy_metagramy(self):
        pass
    def sprawdz_czy_anagramy(self):
        pass
        


slowo = Słowa("kajak", "ala")
print(f"{slowo.sprawdz_czy_palindrom()}")
