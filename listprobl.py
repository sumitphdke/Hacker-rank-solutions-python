# n=int(input("enter:"))
# print(n)
# for i in range(n):
#     print()
s=int(input("input"))
l = []#empty list
for i in range(s):#it will execute 4 times
    n = input("").split()#split method for eg(insert 0 5)means 5 at 0 index
    # print(n)#print the input
    if n[0] == "insert":#the if else part
        l.insert(int(n[1]), int((n[2])))
        # print(l)
    elif n[0]=="remove":#this is remove it will remove number at the specific index
        l.remove(int(n[1]))#int(n[1]) it will convert the string into integer
        # print(l)
    elif n[0]=="print":
        print(l)
    elif n[0]=="append":
        l.append(int(n[1]))
    elif n[0]=="sort":
        l.sort()
    elif n[0]=="reverse":
        l.reverse()
    elif n[0]=="pop":
        l.pop()

# print(l)
