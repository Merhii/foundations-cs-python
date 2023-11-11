class Tab:
    def __init__(self,URL,Title):
        self.URL=URL
        self.Title=Title
Tabs ={} #Title key URL value
Opened_Tabs=[]
def addTab():
    URL=str(input("Enter website url: "))
    Title=str(input("Enter website Title: "))
    _Tab = Tab(URL,Title) # created the object 
    Tabs[Title]=_Tab #assigned tittle key 
    Opened_Tabs.append(_Tab) #added _tab to my array

def closeTab(index):
    index=int(input("Enter Index you wish to close: "))
    for i in Opened_Tabs:
        if (index==i):
            Opened_Tabs.pop(i)

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
            addTab()
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