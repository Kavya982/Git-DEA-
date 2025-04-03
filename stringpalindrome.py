# st = input("Enter string = ")
# def isPalin(st):
#     flag=True
#     l=0
#     r=len(st)-1
#     while l<=r:
#         if(st[l]!=st[r]):
#             flag=False
#             break 
#         l+=1
#         r-=1
#     return flag
# if(isPalin(st)):
#     print(st," is a plaindrome")
# else:
#     print(st," is not a palindrome")

# second method 
st =input("Enter a string = ")
if(st==st[::-1]):
    print("palindrome")
else:
    print("Not a palindrome")