class Phong:
    def __init__(self,ma,ten):
        self.ma = ma
        self.ten = ten

    def getMaphong(self):
        return self.ma
    
    def getTenphong(self):
        return self.ten

class Nhan_Vien:
    def __init__(self,ma,ten,lcb,snc,dsphong):
        self.ma = ma
        self.ten = ten
        self.lcb = lcb
        self.snc = snc
        self.dsphong = dsphong

    def get_heso(self):
        t = self.ma[0]
        n = int(self.ma[1:3])
        if t == "A":
            if n >= 1 and n<=3:
                return 10
            elif n>=4 and n<=8:
                return 12
            elif n>=9 and n<=15:
                return 14
            elif n>=16:
                return 20
        elif t == "B":
            if n >= 1 and n<=3:
                return 10
            elif n>=4 and n<=8:
                return 11
            elif n>=9 and n<=15:
                return 13
            elif n>=16:
                return 16
        elif t == "C":
            if n >= 1 and n<=3:
                return 9
            elif n>=4 and n<=8:
                return 10
            elif n>=9 and n<=15:
                return 12
            elif n>=16:
                return 14
        elif t == "D":
            if n >= 1 and n<=3:
                return 8
            elif n>=4 and n<=8:
                return 9
            elif n>=9 and n<=15:
                return 11
            elif n>=16:
                return 13
            
    def get_luong(self):
        return self.lcb * self.snc * self.get_heso() * 1000


    def get_phong(self):
        tm = self.ma[3:]
        for x in self.dsphong:
            if x.getMaphong() == tm:
                return x.getTenphong()
            
    def __str__(self):
        return self.ma + " " + self.ten + " " + self.get_phong() + " " + str(self.get_luong())

k = int(input())
dsp = []
while k > 0:
    tmp = input()
    ma = tmp[0:2]
    ten = tmp[3:]
    p = Phong(ma,ten)
    dsp.append(p)
    k -= 1   
t = int(input())
ds = []
while t > 0:
    ma = input()
    ten = input()
    lcb = int(input())
    snc = int(input())
    a = Nhan_Vien(ma,ten,lcb,snc,dsp)
    ds.append(a)
    t -= 1
for x in ds:
    print(x)