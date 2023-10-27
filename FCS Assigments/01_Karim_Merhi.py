# #Exercise I
# def fac(number):
#    if(number==1):
#         return number
#    else:
#         return number*fac(number-1)
    

# def main():
#     Number = int(input("Input: "))
#     Output=fac(Number)
#     print("Output: ")
#     print(Output)
# main()

# #Exercise II
# #--------------------------------------------

# def divs(n):
#     l1=[]
#     for i in range(1,n+1):
#         if( n % i == 0):
#             l1.append(i)
#     return l1
# def main():
#     number=int(input("Input: "))
#     print(divs(number))
# main()

# #Exercise III
# #--------------------------------------------

# def reverse_string(str):
#     if len(str)==0:
#         return str
#     newstr=""
#     for i in str:
#         newstr=i+newstr
#     return newstr

# def main():
#     string = str(input("Input :"))
#     print (reverse_string(string))
# main()

# #Exercise IV
# #--------------------------------------------

# def IsEven(l1):
#     l2=[]
#     for i in range(len(l1)):
#         if (l1[i]%2==0):
#             l2.append(l1[i])
#     return l2

# def main():
#     arr=eval(input("Input :"))
#     print(IsEven(arr))
# main()

# #Exercise V
# #--------------------------------------------

# def Strong_Password(password):
#     pwrc=0
#     pwrl=0
#     pwrs=0
#     for char in password:
#         if 65<= ord(char) <=90:
#             pwrc+=1
#         elif 97<= ord(char) <=122:
#             pwrl+=1
#         elif  ord(char) == 63 or ord(char) == 64 or ord(char) == 33 or ord(char) == 36:
#             pwrs+=1
#     if ((pwrc>0)and (pwrl>0)and (pwrs>0) and len(password)>8):
#         print("Strong Password")
#     else:
#         print("Weak Password")
          
# def main():
#     password=str(input("Input: "))
#     Strong_Password(password)
# main()