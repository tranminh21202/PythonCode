tg = [0] * 11
def Data(n, a):
    if n == 0:
        return
    s = str(n)
    l = len(s)
    for i in range(10):
        a[i] += tg[l - 1]
    for i in range(l - 1):
        a[0] -= pow(10, i)
    for i in range(l):
        j ,p = 0,0
        if i == 0:
            p = 1
            j = 1
            a[0] += tg[l - 1 - i] * (ord(s[i]) - 48 - p)
        sum = tg[l - 1 - i]  * (ord(s[i]) - 48 - p)
        while j < ord(s[i]) - 48:
            a[j] += pow(10, l - i - 1) + sum;
            j += 1
        a[j] += n % (pow(10, l - i - 1)) + sum + 1
        for k in range (j + 1, 10):
            a[k] += sum
            
for i in range(10):
    tg[i] = int(i * pow(10, i - 1))
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [0] * 20
    b = [0] * 20
    Data(n - 1, a)
    Data(m, b)
    for i in range (10):
        print(b[i] - a[i], end = ' ')
    print()