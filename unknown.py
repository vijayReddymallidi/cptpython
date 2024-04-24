#employee rating hackearth
def employee_rating(w):
    cons=0
    max_c=0
    for i in range(len(w)):
        if w[i]>6:
            cons+=1
            max_c=max(max_c,cons)
        else:
            cons=0
    return max_c
n=int(input())
work=list(map(int, input().split()))
result=employee_rating(work)
print(result)

# l=[(1,2),(1,2,3)]
# print(len(max(l,key=len)))


#Ali and Helping innocent people
# def valid(st):
#     s=list(st)
#     print(s)
#     for i in range(len(s)):
#         if s[i].isdigit():
#             s[i]=int(s[i])
#     for i in range(len(s)):
#         if s[i] not in list("AEIOUY"):
#             if (s[0]+s[1])%2==0 and (s[3]+s[4])%2==0 and (s[4]+s[5])%2==0 and (s[-1]+s[-2])%2==0:
#                 return "valid"
#             else:
#                 return "invalid"
#         else:
#             return "invalid"
# s= input().upper()
# result=valid(s)
# print(result)

#Zoos hackerearth
# from collections import Counter
# def zoo(s):
#     d=Counter(s)
#     if d["z"]*2==d["o"]:
#         return True
#     else:
#         return False

# s=input()
# print(zoo(s))