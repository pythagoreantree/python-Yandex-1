def format_number(nomer):
    if (nomer.startswith('8')):
        nomer = nomer[1:]
    if (nomer.startswith('+7')):
        nomer = nomer[2:]
    nomer = nomer.replace("-", "").replace("(", "").replace(")", "")
    if (len(nomer) == 7):
        nomer = '495' + nomer
    return nomer

def compare_numbers(nomer1, nomer2):
    if nomer1 == nomer2:
        return print('YES')
    else:
        return print('NO')


new_number = format_number(str(input()))
compare_numbers(new_number, format_number(str(input())))
compare_numbers(new_number, format_number(str(input())))
compare_numbers(new_number, format_number(str(input())))