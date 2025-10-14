import math

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar: float):
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)

    def dot(self, other): # iloczyn skalarny
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other): # iloczyn wektorowy (wektor prostopadly)
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        l = self.length()
        if l == 0:
            return Vector3(0,0,0) # wyjatek dla 0
        return self / l # normalizacja do dlugosci 1

    def __repr__(self):
        #return f"Vector3({self.x}, {self.y}, {self.z})"
        return f"Vector3({round(self.x, 3)}, {round(self.y, 3)}, {round(self.z, 3)})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

def read_vector(name):
    print(f"\nPodaj współrzędne wektora {name}:")
    x = float(input("x = "))
    y = float(input("y = "))
    z = float(input("z = "))
    return Vector3(x, y, z)

def menu():
    while True:
        print("\n====== MENU ======")
        print("1. Oblicz kąt między dwoma wektorami")
        print("2. Oblicz wektor prostopadły (iloczyn wektorowy)")
        print("3. Znormalizuj wektor")
        print("4. Zakończ program\n")

        choice = input("Wybierz opcję (1–4): ")

        if choice == "1":
            v1 = read_vector("v1")
            v2 = read_vector("v2")
            dot = v1.dot(v2)
            cos_theta = dot / (v1.length() * v2.length())
            cos_theta = max(min(cos_theta, 1), -1)
            angle = math.degrees(math.acos(cos_theta))
            print(f"\nKąt między {v1} i {v2} = {round(angle, 2)}°")

        elif choice == "2":
            v1 = read_vector("v1")
            v2 = read_vector("v2")
            perp = v1.cross(v2)
            print(f"\nWektor prostopadły do {v1} i {v2} = {perp}")

        elif choice == "3":
            v = read_vector("v")
            norm = v.normalize()
            print(f"\nZnormalizowany wektor {v} = {norm}")

        elif choice == "4":
            print("Zamykanie programu. Do zobaczenia!")
            break

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")


if __name__ == "__main__":
    menu()