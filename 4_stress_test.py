a = int(input())
b = int(input())
c = int(input())

def delitsa(a, b):
    return a%b == 0


if c < 0:
    print('NO SOLUTION')
else:
    if (a == 0) & (b == 0) & (c == 0):
        print('MANY SOLUTIONS')
    elif (a == 0) & (b != 0) & (c != 0):
        if b == (c ** 2):
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    elif (a == 0) & (b == 0) & (c != 0):
        print('NO SOLUTION')
    elif (a == 0) & (b != 0) & (c == 0):
        print('NO SOLUTION')
    elif (a != 0) & (b == 0) & (c != 0):
        x = (c ** 2) / a
        d = delitsa((c ** 2), a)
        if (((a > 0) & (x > 0)) | ((a < 0) & (x < 0))) & d:
            print(int(x))
        else:
            print('NO SOLUTION')
    elif (a != 0) & (b == 0) & (c == 0):
        x = 0
        print(int(x))
    elif (a != 0) & (b != 0) & (c != 0):
        x = ((c ** 2) - b) / a
        d = delitsa(((c ** 2) - b), a)
        edge = -b / a
        if (((a < 0) & (x < edge)) | ((a > 0) & (x > edge))) & d:
            print(int(x))
        else:
            print('NO SOLUTION')
    elif (a != 0) & (b != 0) & (c == 0):
        x = (-b / a)
        d = delitsa((- b), a)
        if d:
            print(int(x))
        else:
            print('NO SOLUTION')
