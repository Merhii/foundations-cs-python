def reverse_string(str):
    if len(str)==0:
        return str
    newstr=""
    for i in str:
        newstr=i+newstr
    return newstr

def main():
    string = str(input("Input :"))
    print (reverse_string(string))
main()
