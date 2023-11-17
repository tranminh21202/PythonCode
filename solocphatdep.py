a = []
xau = input()
for x in range(len(xau)):
    a.append(int(xau[x]))
st = []
for x in range(-1,-len(a)-1,-1):
    st.append(a[x])
    if len(st) == 1 and st[0] == 6:
        st.pop()
    elif len(st) == 2 and st[0] == 8 and st[1] == 6:
        st.pop()
        st.pop()
    elif len(st) ==3 and st[0] == 8 and st[1] == 8 and st[2] == 6:
        st.pop()
        st.pop()
        st.pop()
if len(st) != 0:
    print("NO")
else:
    print("YES")