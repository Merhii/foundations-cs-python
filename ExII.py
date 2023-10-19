def divs(n):
    l1=[]
    for i in range(1,n+1):
        if( n % i == 0):
            l1.append(i)
    return l1
def main():
    number=int(input("Input: "))
    print(divs(number))
main()