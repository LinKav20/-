n=int(input())
for i in range(n):
    k = 2**(i+1)
    if k < n:
        print(k, end=' ')
    else:
        break

