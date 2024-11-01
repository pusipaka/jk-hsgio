import random
n=int(input())
y=int(input())
d=0
g=0
w=0
def ff():
    a = random.randint(-100, 100)
    return a
a1 = [[ff() for i2 in range(y)]for i in range(n)]
a2 = [[ff() for i3 in range(y)]for i1 in range(n)]
print(a1)
print(a2)
h=[[0 for i7 in range(y)]for i4 in range(n)]
try:
    for i in range(n*y+1):
        d=a1[w][g]+a2[w][g]
        h[w][g]=d
        g+=1
        if (i+1)%y==0:
            w+=1
            g=0
except:
    print(h)








