def pirate(n,a):
    goldPlaces = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if a[j][1] >= a[i][1]:
                goldPlaces += 1
                break
    return goldPlaces

n = int(input())
a = []
for i in range(n):
    x,y = map(int, input().split())
    a.append([x,y])
print(pirate(n,a))












def numberOfAwards(R,G,B):
    number = 0
    G += B / 10
    R += G / 10

    number = R / 10
    return number

