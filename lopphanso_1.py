import math
class PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def __str__(self):
        tmp = math.gcd(self.tu,self.mau)
        self.tur = int(self.tu/tmp)
        self.maur = int(self.mau/tmp)
        return str(self.tur) + "/" + str(self.maur)
    
tu,mau = (int(x) for x in input().split())
a = PS(tu,mau)
print(a)