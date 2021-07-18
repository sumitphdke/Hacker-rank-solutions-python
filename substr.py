
def count_substring(string, sub_string):
    k=sub_string
    l=len(k)
    c=0
    for i in range(0,len(string)):
        s=string[i:i+l]
        if k==s:
            c=c+1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
# string="I am an Indian, by birth"
# k="birth"
# c=0
# l=len(k)
# for i in range(0,len(string)+1):
#     s=string[i:i+l]
#     if s==k:
#         c=c+1
# print(c)