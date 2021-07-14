# s=input(":")
# def split_join(line):
#     a=s.split(" ")
#     print(a)
#     a="-".join(a)
#     print(a)
#
# split_join(s)
def split_and_join(line):
    s=line.split(" ")
    s="-".join(s)
    return s


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)