def fac(number):
   if(number==1):
        return number
   else:
        return number*fac(number-1)
    

def main():
    Number = int(input("Input: "))
    Output=fac(Number)
    print("Output: ")
    print(Output)
main()