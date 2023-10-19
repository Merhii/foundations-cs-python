def IsEven(l1):
    l2=[]
    for i in range(len(l1)):
        if (l1[i]%2==0):
            l2.append(l1[i])
    return l2

def main():
    arr=eval(input("Input :"))
    print(IsEven(arr))
main()