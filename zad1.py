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


# ===== TESTY =====
if __name__ == "__main__":
    # 1. Przemienność dodawania
    a = Vector3(1, 2, 3)
    b = Vector3(4, 5, 6)
    print("a + b =", a + b)
    print("b + a =", b + a)
    print("Czy a+b == b+a?")
    if (a + b) == (b + a):
        print("Tak")
    else:
        print("Nie")

    # 2. Kąt między wektorami
    v1 = Vector3(0, 3, 0)
    v2 = Vector3(5, 5, 0)
    dot = v1.dot(v2)
    cos_theta = dot / (v1.length() * v2.length()) # cos 0
    angle = math.degrees(math.acos(cos_theta)) # 0 w stopniach
    #print("Kąt między [0,3,0] i [5,5,0] =", angle, "stopni")
    print(f"Kąt między [0,3,0] i [5,5,0] = {round(angle, 2)} stopni")

    # 3. Wektor prostopadły
    v3 = Vector3(4, 5, 1)
    v4 = Vector3(4, 1, 3)
    perp = v3.cross(v4)
    print("Wektor prostopadły =", perp)

    # 4. Normalizacja wektora
    norm_perp = perp.normalize()
    print("Znormalizowany wektor =", norm_perp)

