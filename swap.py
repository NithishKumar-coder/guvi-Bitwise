n = int(input())
L = [int(x) for x in input().split()][:n]
for i in range(0,n-1,2) :
    L[i],L[i+1] = L[i+1], L[i]
print(*L)
