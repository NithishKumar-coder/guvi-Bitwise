n=int(input())
arr = list(map(int, input().split()))
a=arr[0]
for i in range(1,n):
	a=a^arr[i]
print(a)
