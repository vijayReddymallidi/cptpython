# t=eval(input())
# n=int(input())
# def find_tulple(t,n):
#     return n in t
# print(find_tulple(t,n))
# print("",end="")
# if __name__ == '__main__':
#     s = input()
#     c1,c2,c3,c4,c5=False,False,False,False,False
#     for i in s:
#         if i.isalnum():
#             c1=True
#         elif i.isalpha():
#             c2=True
#         elif i.isdigit():
#             c3=True
#         elif i.islower():
#             c4=True
#         elif i.isupper():
#             c5=True
#     print(c1,c2,c3,c4,c5,sep="\n")
def print_formatted(number):
    for i in range(1,n+1):
        print(i  , oct(i).lstrip('0o') , hex(i).lstrip('0x').upper() , bin(i).lstrip('0b') )
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)