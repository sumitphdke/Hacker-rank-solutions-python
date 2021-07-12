def swapcase(s):
    k=""
    for i in s:
        if i == i.lower():
            k = k + i.upper()
        elif i == i.upper():
            k = k + i.lower()
    return k
s= input()
result = swapcase(s)
print(result)