n1=int(input())
k1=list(map(int,input().split()))
s1=[1]*n1
for i1 in range(n1):
    if i1==0:
        if k1[i1]>k1[i1+1]:
            s1[i1]=s1[i1]+s1[i1+1]
    elif i1>0:
        if k1[i1]>k1[i1-1]:
            s1[i1]=s1[i1]+s1[i1-1]
print(sum(s1))
