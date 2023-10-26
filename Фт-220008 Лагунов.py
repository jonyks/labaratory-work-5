try:
    a=input('Строка для шифрования ')
    b=int(input('Введите шаг '))%26
except:
    print('Пожалуйста введите верные данные')
    quit()
c='qwertyuiopasdfghjklzxcvbnm'
e=str(c.upper())
st=''
for i in a:
    if i in c:
        if ord(i)-96+b>26:
            d=ord(i)+b-26
            st=st+chr(d)
        else:st=st+chr(ord(i)+b)
    elif i in e:
        if ord(i)-64+b>26:
            d=ord(i)+b-26
            st=st+chr(d)
        else:st=st+chr(ord(i)+b)
    else:st=st+i
print(f'Зашифрованное слово {st}')
