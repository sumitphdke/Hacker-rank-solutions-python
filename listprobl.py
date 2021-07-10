# n=int(input("enter:"))
# print(n)
# for i in range(n):
#     print()
l=[]
n=input("").split()
print(n)
if n[0]=="insert":
    l.insert(int(n[1]),int((n[2])))
print(l)
s=input("").split()
print(s)
if s[0]=="remove":
    l.remove(int(s[1]))
print(l)
