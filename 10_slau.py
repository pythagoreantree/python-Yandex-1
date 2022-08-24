a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if (a == 0 and b == 0 and e != 0) or (c == 0 and d == 0 and f != 0):
    print(0)
elif a == 0 and b == 0 and e == 0:
    if c != 0 and d == 0:
        x = f / c
        print(3, x)
    elif c == 0 and d != 0:
        y = f / d
        print(4, y)
    else:
        print(5)
elif c == 0 and d == 0 and f == 0:
    if a != 0 and b == 0:
        x = e / a
        print(3, x)
    elif a == 0 and b != 0:
        y = e / b
        print(4, y)
    else:
        print(5)
elif a == 0 and c == 0 and b != 0 and d != 0 and e != 0 and f != 0:
    if (b / d) == (e / f):
        y = e / b
        print(4, y)
elif a == 0 and c == 0 and b != 0 and d != 0 and e == 0 and f != 0:
    print(0)
elif a == 0 and c == 0 and b != 0 and d != 0 and e != 0 and f == 0:
    print(0)
elif a != 0 and c != 0 and b == 0 and d == 0 and e != 0 and f != 0:
    if (a / c) == (e / f):
        x = e / a
        print(3, x)
elif a != 0 and c != 0 and b == 0 and d == 0 and e == 0 and f != 0:
    print(0)
elif a != 0 and c != 0 and b == 0 and d == 0 and e != 0 and f == 0:
    print(0)
elif a != 0 and b != 0 and c != 0 and d != 0:
    # first case one decision
        if (a / c) != (b / d):
            y = (a*f - c*e)/(a*d - c*b)
            x = (e - b*y)/a
            print(2, round(x, 5), round(y, 5))
        elif (a / c) == (b / d) and e != 0 and f != 0 and (b / d) != (e / f):
            print(0)
        elif (a / c) == (b / d) and e == 0 and f == 0:
            print(1, round(-a/b, 5), 0)
        else:
            if a < c:
                print(1, round((-a/b), 5), round((e/b), 5))
            else:
                print(1, round((-c/d), 5), round((f/d), 5))
elif a == 0 and b != 0 and c != 0 and d == 0:
    x = f / c
    y = e / b
    print(2, round(x, 5), round(y, 5))
elif a != 0 and b == 0 and c == 0 and d != 0:
    x = e / a
    y = f / d
    print(2, round(x, 5), round(y, 5))
elif a == 0 and b != 0 and c != 0 and d != 0:
    y = e / b
    x = (f - d*y)/ c
    print(2, round(x, 5), round(y, 5))
elif a != 0 and b == 0 and c != 0 and d != 0:
    x = e / a
    y = (f - c*x) / d
    print(2, round(x, 5), round(y, 5))
elif a != 0 and b != 0 and c == 0 and d != 0:
    y = f / d
    x = (e - b*y) / a
    print(2, round(x, 5), round(y, 5))
elif a != 0 and b != 0 and c != 0 and d == 0:
    x = f / c
    y = (e - a*x) / b
    print(2, round(x, 5), round(y, 5))
