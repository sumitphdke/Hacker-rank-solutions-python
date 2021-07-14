def mutate_string(string, position, character):
    s=string
    r=character
    u=position
    s= s[:u] + r + s[u + 1:]
    return s

if __name__ == '__main__':
    s = input("")
    i, c = input("").split()
    result=mutate_string(s, int(i), c)
    print(result)
#
# s="sumit"
# u=int(input(":"))#2
# r=input(":")#k
# s= s[:u] + r + s[u+1:]
# print(s)
