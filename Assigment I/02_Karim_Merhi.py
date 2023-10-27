# Exercise I:

def choiceOne(number):
    if(number<10):
        return 1 # Base Case
    else:
        return 1+choiceOne(number//10) # recursion case
def main():
    print("1. Count Digits\n2. Find Max\n3.1. Count Tags\n3.2. Count Normalized Columns\n4. Exit\n- - - - - - - - - - - - - - -")
    choice=float(input("Enter a choice:"))
    if(choice==1):
        number = int(input("Input:"))
        if (number<0):
            number = abs(number)
        n=choiceOne(number)
        print (f"Output:{n}")
main()
