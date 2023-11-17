class ThiSinh:
    def __init__(self, ten, ns, diem1, diem2, diem3):
        self.ten = ten
        self.ns = ns
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tong = diem1 + diem2 + diem3
    def __str__(self):
        return self.ten + " " + self.ns + " " + "{:.1f}".format(self.tong)
ten = input()
ns = input()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())
a = ThiSinh(ten,ns,diem1,diem2,diem3)
print(a)