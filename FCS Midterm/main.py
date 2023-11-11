class Tab:
    def __init__(self,URL,Title):
        self.URL=URL
        self.Title=Title

Tabs ={} #Title key URL value Dictionary
Opened_Tabs=[]
def addTab():
    URL=str(input("Enter website url: "))
    Title=str(input("Enter website Title: "))
    _Tab = Tab(URL,Title) # created the object 
    Tabs[Title]=_Tab #assigned tittle key 
    Opened_Tabs.append(_Tab) #added _tab to my array

def closeTab(index):
    if (len(Opened_Tabs)==0):
        print("List is empty")
        return
    if not(index):  # Found From StackOverflow https://stackoverflow.com/questions/47560026/how-to-get-python-3-to-use-enter-as-an-input
        Opened_Tabs.pop(-1) # Close last tab 
    else:
        Opened_Tabs.pop(int(index))     

def printTabs():
    if (len(Opened_Tabs)==0):
        print("List is empty")
        return
    for Tab in Opened_Tabs:
        print(Tab.Title)

def closeAllTabs():
    if (len(Opened_Tabs)==0):
        print("List is empty")
        return
    Opened_Tabs.clear()
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
    choice = int(input("Enter a choice 9 to exit: "))
    while(choice!=9):
        if (choice==1):
            addTab()
        elif (choice==2):
            index=input("Enter index you want to delete: ")
            closeTab(index)
        elif (choice==3):
            print("hi")
        elif (choice==4):
            printTabs()
        elif (choice==5):
            print("hi")
        elif (choice==6):
            closeAllTabs()
        elif (choice==7):
            print("hi")
        elif (choice==8):
            print("hi")
        elif (choice==9):
            print("hi")
        else:
            print("Invalid Choice!")
        choice = int(input("Enter a choice 9 to exit: "))
    print("Thank You For Using My Menu Program With <3 from SEF")

main()