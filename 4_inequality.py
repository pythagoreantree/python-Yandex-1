a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print('NO SOLUTION')
else:
    if a != 0:
        x = ((c ** 2) - b) / a
        d = (((c ** 2) - b) % a == 0)
        if ((a*x + b) >= 0) & d:
            print(int(x))
        else:
            print('NO SOLUTION')
    else:
        if (b == 0) & (c == 0):
            print('MANY SOLUTIONS')
        elif (b != 0) & (c != 0) & (b == (c ** 2)):
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')

