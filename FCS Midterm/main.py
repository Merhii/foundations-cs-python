import json # Json in Python https://www.youtube.com/watch?v=ttQidKChD4c
import requests
from bs4 import BeautifulSoup # Web scraping https://www.youtube.com/watch?v=0uiPOxUcLgg


def openTab(parentIndex=None):   #From StackOverflow https://stackoverflow.com/questions/36418542/what-does-def-method-parameter-none-mean
    URL=str(input("Enter website url: "))
    Title=str(input("Enter website Title: "))
    if (parentIndex is None):
        _Tab = Tab(URL,Title) # created the object 
        Tabs[Title]=_Tab #assigned tittle key 
        Opened_Tabs.append(_Tab) #added _tab to my array
    else:
        parentTab = Opened_Tabs[parentIndex]
        childTab = Tab(URL,Title)
        parentTab.nestedTabs[Title]=childTab

def closeTab(index):
    if (len(Opened_Tabs)==0):
        print("List is empty")
        return
    if not(index):  # Found From StackOverflow https://stackoverflow.com/questions/47560026/how-to-get-python-3-to-use-enter-as-an-input
        Opened_Tabs.pop(-1) # Close last tab 
    else:
        Opened_Tabs.pop(int(index))     

def switchTab(index):
    if (len(Opened_Tabs)==0):
        print("List is empty")
        return
    if not(index):  # Found From StackOverflow https://stackoverflow.com/questions/47560026/how-to-get-python-3-to-use-enter-as-an-input
        req = requests.get(Opened_Tabs[0].URL)
        soup = BeautifulSoup(req.text) 
    else:
        req = requests.get(Opened_Tabs[int(index)].URL)
        soup = BeautifulSoup(req.text) 
    print(soup)    

def openNestedTab():
    parentIndex= int(input("Enter Parent Index: "))
    parentTab = Opened_Tabs[parentIndex]
    openTab(parentIndex)

def printTabs(tabs, padding=0):
    if (len(tabs)==0):
        print("List is empty")
        return
    for Tab in tabs:
        print(" "*padding + Tab.Title) # added padding to check on the nested ones
        if (Tab.nestedTabs):
            printTabs(Tab.nestedTabs.values(),padding+1)
        

def closeAllTabs():
    if (len(Opened_Tabs)==0):
        print("List already empty")
        return
    Opened_Tabs.clear()

def tab_to_dict(tab): # W3Schools https://www.w3schools.com/python/ref_func_isinstance.asp
    if isinstance(tab, Tab):    # bool function to check if tab is a Tab object
        return {'URL': tab.URL,'Title':tab.Title, 'nestedTabs': tab.nestedTabs}
    return tab

def saveTabs():
    with open("Test.json","w") as json_file:
        json.dump(Tabs, json_file, default=tab_to_dict)
        print("Dictonary saved in json file")

def importTabs():
    File=str(input("Enter File Name: "))
    with open(File,"r") as json_file:
        jsonTabs =json_file.read()
        print("Dictonary loaded from json file successfully")
        # print(type(jsonTabs))
        print(jsonTabs)        # Test Cases 
        jsonDict= json.loads(jsonTabs)
        # print(type(jsonDict)) Geeks for Geeks https://www.geeksforgeeks.org/python-convert-string-dictionary-to-dictionary/
        # print(jsonDict)
        Opened_Tabs.append(Tabs)
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
            openTab()
        elif (choice==2):
            index=input("Enter index you want to delete: ")
            closeTab(index)
        elif (choice==3):
            index=input("Enter index you want to view it's HTML's Code: ")
            switchTab(index)
        elif (choice==4):
            printTabs(Opened_Tabs)
        elif (choice==5):
            openNestedTab()
        elif (choice==6):
            closeAllTabs()
        elif (choice==7):
            saveTabs()
        elif (choice==8):
            importTabs()
        elif (choice==9):
            exit()
        else:
            print("Invalid Choice!")
        choice = int(input("Enter a choice 9 to exit: "))
    print("Thank You For Using My Menu Program With <3 from SEF")

main()