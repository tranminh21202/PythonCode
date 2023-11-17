class Rectangle:
    def __init__(self, dai, rong, mau):
        self.dai = dai
        self.rong = rong
        self.mau = mau
    def color(self):
        return self.mau[:1].upper() + self.mau[1:].lower()

    def perimeter(self):
        tmp = self.dai + self.rong
        return tmp*2
    
    def area(self):
        return self.dai*self.rong
    
arr = input().split()
if int(arr[0]) <= 0 or int(arr[1]) <= 1:
    print("INVALID")
else:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
