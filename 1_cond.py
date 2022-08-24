troom, tcond = map(int, input().split())
reg = input()
if reg == 'auto':
    print(tcond)
if reg == 'fan':
    print(troom)
if reg == 'freeze':
    if tcond < troom:
        print(tcond)
    else:
        print(troom)
if reg == 'heat':
    if tcond > troom:
        print(tcond)
    else:
        print(troom)
