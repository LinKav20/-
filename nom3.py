n=input()
if n[0]=='а' or n[1]=='э' or n[1]=='е' or n[1]=='я':
    for i in range(len(n)):
        print(n[i], end=' ')
else:
    for i in range(len(n)-1,-1,-1):
        print(n[i], end=' ')

