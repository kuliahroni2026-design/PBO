
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)


p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))

pp = PersegiPanjang(p, l)

print("Luas:", pp.luas())
print("Keliling:", pp.keliling())