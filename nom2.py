n=input()
if n[1]=='к' or n[1]=='и' or n[1]=='л':
    for i in range(1, len(n), 2):
        print(n[i], end=' ')
else:
    for i in range(0, len(n), 2):
        print(n[i], end=' ')


