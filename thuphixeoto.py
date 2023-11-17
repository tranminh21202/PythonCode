class Oto:
    def __init__(self, xau):
        self.bien = xau[0]
        self.loai = xau[1]
        self.sl = xau[2]
        self.chieu = xau[3]
        self.tg = xau[4]
        if self.sl == "5" and self.chieu == "IN":
            self.thu = 10000
        if self.sl == "7" and self.chieu == "IN":
            self.thu = 15000
        if self.sl == "2" and self.chieu == "IN":
            self.thu = 20000
        if self.sl == "29" and self.chieu == "IN":
            self.thu = 50000
        if self.sl == "45" and self.chieu == "IN":
            self.thu = 70000

n = int(input())
ds = {}
for i in range(n):
    xau = input().split()
    a = Oto(xau)
    if a.chieu == "IN":
        if a.tg not in ds:
            ds[a.tg] = a.thu
        else:
            ds[a.tg] += a.thu
for x,y in ds.items():
    print(f"{x}: {y}")
