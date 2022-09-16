# class Rectangle:
#     def __init__(self):
#         print(f"Został utworzony obiekt.")
#
#     def __del__(self):
#         print(f"Obiekt został usunięty.")
#
#     def load_data(self):
#         self.a = float(input(f"Podaj długość boku a:\n"))
#         self.b = float(input(f"Podaj długość boku b:\n"))
#         print(f"Bok ma teraz długości:\n"
#               f"a = {self.a}\n"
#               f"b = {self.b}\n")
#
#     def calculate_the_field(self):
#         self.field = self.a * self.b
#         return self.field
#
#     def display_the_fild(self):
#         print(f"Pole prostokąta wynosi {self.field}.")
#
#
# prostokat = Rectangle()
#
# prostokat.load_data()
# prostokat.calculate_the_field()
# prostokat.display_the_fild()

print("=" * 79)


# class QuadraticFunktion:
#     def __init__(self):
#         print(f"Został utworzony obiekt równania kwadratowego.")
#
#     def __del__(self):
#         print(f"Obiekt równania kwadratowego został usunięty.")
#
#     def load_data(self):
#         self.a = float(input(f"Podaj warstość parametru a:\n"))
#         self.b = float(input(f"Podaj warstość parametru b:\n"))
#         self.c = float(input(f"Podaj warstość parametru c:\n"))
#         print(f"Funkcja kwadratowa ma postać f(x) = {self.a}*x*x + {self.b}*x + {self.c}")
#
#     def roots_of_the_equation(self):
#         delta = self.b ** 2 - 4 * self.a * self.b
#         if delta < 0:
#             print(f"Równanie nie ma miejsc zerowych.")
#         elif delta == 0:
#             self.x0 = -self.b / (2 * self.b)
#             print(f"Jest jedno miejsce zerowe x0 = {round(self.x0, 2)}.")
#         else:
#             self.x1 = (-self.b - (delta ** 0.5)) / (self.a * 2)
#             self.x2 = (-self.b + (delta ** 0.5)) / (self.a * 2)
#             print(f"Są dwa miejsca zerowe funkcji x1 = {round(self.x1, 2)}, x2 = {round(self.x2, 2)}")
#
# funkcja = QuadraticFunktion()
# funkcja.load_data()
# funkcja.roots_of_the_equation()

print("=" * 79)


# import random
#
# class Tablical:
#     def __init__(self):
#         print(f"Obiekt klasy Tablical został utworzony.")
#
#     def __del__(self):
#         print(f"Obiekt klasy Tablical został usunięty.")
#
#     def create_the_table(self):
#         self.n = int(input(f"Podaj wymiar tablicy:\n"))
#         self.table = [[0 for i in range(self.n)] for j in range(self.n)]
#         for i in range(self.n):
#             for j in range(self.n):
#                 if i == j:
#                     self.table[i][j] = random.randint(1, 9)
#
#         for i in range(self.n):
#             for j in range(self.n):
#                 print(self.table[i][j], " ", end="")
#             print()
#
#     def diagonal_sum(self):
#         self.dsum = 0
#         for i in range(self.n):
#             self.dsum += self.table[i][i]
#         print(f"Suma liczb na przekątnej wynosi: {self.dsum}.")
#
# tablica = Tablical()
# tablica.create_the_table()
# tablica.diagonal_sum()

print("=" * 79)


