string='''
1. Open Tab
2. Close Tab
3. Switch Tab
4. Display All Tabs
5. Open Nested Tab
6. Clear All Tabs
7. Save Tabs
8. Import Tabs
9. Exit'''
def main():
    print(string)
    choice = int(input("Enter a choice 9 to exit"))
    while(choice!=9):
        if (choice==1):
            print("hi")
        elif (choice==2):
            print("hi")
        elif (choice==3):
            print("hi")
        elif (choice==4):
            print("hi")
        elif (choice==5):
            print("hi")
        elif (choice==6):
            print("hi")
        elif (choice==7):
            print("hi")
        elif (choice==8):
            print("hi")
        elif (choice==9):
            print("hi")
        else:
            print("Invalid Choice!")
        choice = int(input("Enter a choice 9 to exit"))
        
main()