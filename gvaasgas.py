import random
def ff():
    a = random.randint(-100, 100)
    return a
n = int(input())
y = int(input())
a1 = [[ff() for i2 in range(y)]for i in range(n)]
a2 = [[ff() for i3 in range(y)]for i1 in range(n)]
h=[[0 for i7 in range(y)]for i4 in range(n)]

def gg(a1,a2,h):
    d = 0
    g = 0
    w = 0
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
gg(a1,a2,h)







