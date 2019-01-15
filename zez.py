arr='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
n=input()
for i in range(len(n)):
    k=n[i]
    m=k
    for j in range(len(arr)-1 ):
        if k==arr[j]:
            m=arr[j+1]
        if k=='Я':
            m=arr[33]
        if k == 'я':
            m =arr[0]
    print(m,end='')
