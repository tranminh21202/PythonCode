class Hoa_Don():
    def __init__(self):
        self.mamh = input()
        self.tenmh = input()
        self.sl = int(input())
        self.dongia = int(input())
        self.ck = int(input())
        self.tong = (self.sl * self.dongia) - self.ck
    
    def __str__(self):
        return f"{self.mamh} {self.tenmh} {self.sl} {self.dongia} {self.ck} {self.tong}"
    
t = int(input())
ds = list()
while t > 0:
    a = Hoa_Don()
    ds.append(a)
    t -= 1
ds.sort(key=lambda x:x.tong,reverse=True)
for x in ds:
    print(x)