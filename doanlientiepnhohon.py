t = int(input())
while t > 0:
    n = int(input())
    list1 = [int(x) for x in input().split()]
    st = []
    for i in range(len(list1)):
        while len(st) > 0 and list1[st[-1]] <= list1[i]:
            st.pop()
        if len(st) == 0:
            print(i+1,end=" ")
        else:
            print(i-st[-1],end=" ")
        st.append(i)
    print()
    t -= 1