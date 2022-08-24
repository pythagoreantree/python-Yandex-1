a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

if e == 0 and f == 0:
    if a == 0 and b == 0 and c != 0 and d != 0:
        print(1, round((-c/d), 5), 0)
    elif a != 0 and b != 0 and c == 0 and d == 0:
        print(1, round((-a/b), 5), 0)
    elif a == 0 and b != 0 and c == 0 and d != 0:
        print(4, 0)
    elif a != 0 and b == 0 and c != 0 and d == 0:
        print(3, 0)
    elif a == 0 and b != 0 and c != 0 and d == 0:
        print(2, 0, 0)
    elif a != 0 and b == 0 and c == 0 and d != 0:
        print(2, 0, 0)
    elif a == 0 and b == 0 and c == 0 and d == 0:
        print(5)
    elif a != 0 and b != 0 and c != 0 and d != 0:
        if a/c != b/d:
            print(2, 0, 0)
        else:
            print(1, round((-a/b), 5), 0)
    elif a == 0 and b != 0 and c != 0 and d != 0:
        print(2, 0, 0)
    elif a != 0 and b == 0 and c != 0 and d != 0:
        print(2, 0, 0)
    elif a != 0 and b != 0 and c == 0 and d != 0:
        print(2, 0, 0)
    elif a != 0 and b != 0 and c != 0 and d == 0:
        print(2, 0, 0)
elif e != 0 and f == 0:
    if a == 0 and b == 0:
        print(0)
    elif c == 0 and d == 0 and (a != 0 or b != 0):
        if a == 0 and b != 0:
            print(4, round(e / b, 5))
        elif a != 0 and b == 0:
            print(3, round(e / a, 5))
        else:
            print(1, round((-a) / b, 5), round(e / b, 5))
    elif a == 0 and b != 0 and c == 0 and d != 0:
        print(0)
    elif a != 0 and b == 0 and c != 0 and d == 0:
        print(0)
    elif a == 0 and b != 0 and c != 0 and d == 0:
        print(2, 0, round((e / b), 5))
    elif a != 0 and b == 0 and c == 0 and d != 0:
        print(2, round((e / a), 5), 0)
    elif a != 0 and b != 0 and c != 0 and d != 0:
        if a/c != b/d:
            x = (e*d)/(a*d - b*c)
            y = (-c/d)*x
            print(2, round(x, 5), round(y, 5))
        else:
            print(0)
    elif a == 0 and b != 0 and c != 0 and d != 0:
        x = (-e*d)/(b*c)
        y = e/b
        print(2, round(x, 5), round(y, 5))
    elif a != 0 and b == 0 and c != 0 and d != 0:
        x = e / a
        y = (-c*e) / a*d
        print(2, round(x, 5), round(y, 5))
    elif a != 0 and b != 0 and c == 0 and d != 0:
        print(2, round((e/a), 5), 0)
    elif a != 0 and b != 0 and c != 0 and d == 0:
        print(2, 0, round((e/b), 5))
elif e == 0 and f != 0:
    if c == 0 and d == 0:
        print(0)
    elif a == 0 and b == 0 and (c != 0 or d != 0):
        if c == 0 and d != 0:
            print(4, round(f/d, 5))
        elif c != 0 and d == 0:
            print(3, round(f/c, 5))
        else:
            print(1, round((-c)/d, 5), round(f/d, 5))
    elif a == 0 and b != 0 and c == 0 and d != 0:
        print(0)
    elif a != 0 and b == 0 and c != 0 and d == 0:
        print(0)
    elif a == 0 and b != 0 and c != 0 and d == 0:
        print(2, round(f/c, 5), 0)
    elif a != 0 and b == 0 and c == 0 and d != 0:
        print(2, 0, round(f/d, 5))
    elif a != 0 and b != 0 and c != 0 and d != 0:
        if a*d != b*c:
            x = (f*b)/(b*c - a*d)
            y = (-a/b)*x
            print(2, round(x, 5), round(y, 5))
        else:
            print(0)
    elif a == 0 and b != 0 and c != 0 and d != 0:
        print(2, round((f/c), 5), 0)
    elif a != 0 and b == 0 and c != 0 and d != 0:
        print(2, 0, round((f/d), 5))
    elif a != 0 and b != 0 and c == 0 and d != 0:
        print(2, round(((-b*f)/(a*d)), 5), round((f/d), 5))
    elif a != 0 and b != 0 and c != 0 and d == 0:
        print(2, round((f/c), 5), round(((-a*f)/(b*c)), 5))
else:
    if (a == 0 and b == 0) or (c == 0 and d == 0):
        print(0)
    elif a == 0 and c == 0 and b != 0 and d != 0:
        if b/d == e/f:
            print(4, round(e/b, 5))
        else:
            print(0)
    elif a != 0 and c != 0 and b == 0 and d == 0:
        if a/c == e/f:
            print(3, round(e/a, 5))
        else:
            print(0)
    elif a == 0 and c != 0 and b != 0 and d == 0:
        print(2, round(f / c, 5), round(e / b, 5))
    elif a != 0 and c == 0 and b == 0 and d != 0:
        print(2, round(e / a, 5), round(f / d, 5))
    elif a == 0 and c == 0 and b == 0 and d == 0:
        print(0)
    elif a != 0 and b != 0 and c != 0 and d != 0:
        if a*d != b*c:
            x = (f*b - d*e)/(b*c - a*d)
            y = (e - a*x)/b
            print(2, round(x, 5), round(y, 5))
        elif a*d == b*c and b*f != e*d:
            print(0)
        else:
            print(1, round(-a/b, 5), round(e/b, 5))
    elif a == 0 and b != 0 and c != 0 and d != 0:
        x = (f*b - d*e)/(b*c)
        y = e/b
        print(2, round(x, 5), round(y, 5))
    elif a != 0 and b == 0 and c != 0 and d != 0:
        x = e/a
        y = (a*f - c*e)/(a*d)
        print(2, round(x, 5), round(y, 5))
    elif a != 0 and b != 0 and c == 0 and d != 0:
        x = (d*e - f*b)/(a*d)
        y = f/d
        print(2, round(x, 5), round(y, 5))
    elif a != 0 and b != 0 and c != 0 and d == 0:
        x = f/c
        y = (c*e - a*f)/(b*c)
        print(2, round(x, 5), round(y, 5))
