n = int(input())
a = [""] * n
b = [0] * n
c = [0] * n
kq = 0
for i in range(n):
    a[i] = input()
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            b[i] += 1
            c[j] += 1
for i in range(n):
    kq += (b[i] * (b[i]-1))/2
    kq += (c[i] * (c[i]-1))/2
print(int(kq))