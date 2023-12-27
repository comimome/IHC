
D=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for i in range(D)]
d=[0 for i in range(26)]
vs = 0
for i in range(D):
    t=int(input())
    d=[d[i]+1 for i in range(26)]
    d[t-1]=0
    v=s[i][t-1]-sum(list(d[j]*c[j] for j in range(26)))
    vs+=v
    print(vs)