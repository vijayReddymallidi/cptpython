# n=int(input())*2
# for i in range(1,n,2):
#     print(" "*(n-i+1),end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in reversed(range(1,n,2)):
#     print(" "*(n-i+1),end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

#half diamond shape
# n=int(input())
# for i in range(1,n+1):
#     print("*"*i)
# for i in range(n,0,-1):
#     print("*"*i)

#binary triangle
# 1
# 01
# 101
# 0101
n=int(input())
for i in range(1,n+1):
    for j in reversed(range(1,i)):
        print(j%2,end="")
    print()
    