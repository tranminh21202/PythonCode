import math
class PSO:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def cong(self,p):
        tu = (self.tu * p.mau) + (self.mau * p.tu)
        mau = self.mau * p.mau
        return PSO(tu,mau)
    
    def __str__(self):
        tmp = math.gcd(self.tu,self.mau)
        self.tur = int(self.tu/tmp)
        self.maur = int(self.mau/tmp)
        return str(self.tur) + "/" + str(self.maur)
    
x1,x2,x3,x4 = (int(x) for x in input().split())
p1 = PSO(x1,x2)
p2 = PSO(x3,x4)
kq = p1.cong(p2)
print(kq)