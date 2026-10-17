t=5
for _ in range(t):
    n=int(input())
    a=[1,3,4,5,6,15,16]
    b=[2,7,8,9,10,17,18]
    c=[]
    for i in range(n):
        c.append(a[i])
        c.append(b[i])
    c.sort()
    print(*c)
