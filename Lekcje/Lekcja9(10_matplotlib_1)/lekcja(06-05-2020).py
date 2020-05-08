import matplotlib.pyplot as plt
import numpy as np
import os
# Zadanie 1
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20].
# Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

a = []
for i in range(1, 22):
    a.append(1/i)
plt.plot(a)
plt.xlabel('funkcja 1/x dla x ϵ [1, 20]')
plt.xticks(np.arange(0, 22, step=1))
plt.show()

# Zadanie 2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.

a = []
for i in range(1, 22):
    a.append(1/i)
plt.plot(a, 'g:')
plt.plot(a, 'g>')
plt.title('Funkcja 1/x dla x ϵ [1, 20]')
plt.xticks(np.arange(0, 22, step=1))
plt.show()

# Zadanie 3
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety i legendę do wykresu.

x = np.arange(0, 30, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.title('Funkcje sin(x) i cos(x)  dla x ϵ [0, 30]')
plt.legend(loc=4)
plt.show()

# Zadanie 4
# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji,
# tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.

x = np.arange(0, 30, 0.1)
s = np.sin(x)*-1
s2 = np.sin(x)+2
plt.plot(x, s, label='sin(x)')
plt.plot(x, s2, label='sin(x)')
plt.title('Wykres sin(x),sin(x)')
plt.ylabel('sin(x)')
plt.xlabel('x')
plt.legend(loc=6)
plt.show()