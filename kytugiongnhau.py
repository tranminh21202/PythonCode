for i in range(int(input())):
    m = int(input())
    Z = [0] * (m + 1)
    x, y, z = map(int,input().split())
    Z[1] = x
    for j in range(2,  m + 1):
        if j % 2 == 0:
            Z[j] = min(Z[j - 1] + x, Z[j // 2] + z)
        else:
            Z[j] = min(Z[j - 1] + x, Z[j // 2 + 1] + y + z)

    print(Z[m])