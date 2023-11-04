student_data = [
 {
 "ID": 1,"Name": "Ahmad","Age": 20,"Major": "Finnance","GPA": 3.4
 },
 {
"ID": 2,"Name": "Merhi","Age": 20,"Major": "Computer Engineering","GPA": 3.7
 },
{
"ID": 3,"Name": "Mohamad","Age": 25,"Major": "BITM","GPA": 1.7
 },
 {
"ID": 4,"Name": "Bakri","Age": 23,"Major": "BITM","GPA": 1.6
 },
{
"ID": 5,"Name": "Lotfi","Age": 18,"Major": "HCIS","GPA": 2.7
 },
]
def main():
    print('''
 1. Get Student by ID
 2. Get All Students
 3. Get Students by Major
 4. Add Student
 5. Find Common Majors
 6. Delete Student
 7. Calculate Average GPA
 8. Get Top Performers
 9. Exit
 - - - - - - - ''')
    choice=int(input("Enter Choice:"))
    if (choice==1):
        hashmapId=int(input("Enter ID:"))
        for item in student_data:
            if(item["ID"]== hashmapId):
                print(item)
    elif(choice==2):
        print(student_data)
    elif (choice==3):
        hashmapMajor=str(input("Enter Major:"))
        for item in student_data:
            if(item["Major"]== hashmapMajor):
                print(item)
    elif (choice==4):
        newId=int(input("Enter ID:"))
        name=str(input("Enter Name:"))
        age=int(input("Enter Age:"))
        major=str(input("Enter Major:"))
        gpa=float(input("Enter Gpa:"))
        newStudent={
            "ID": newId,"Name": name,"Age": age,"Major": major,"GPA": gpa},
        student_data.append(newStudent)
        print(student_data)
    elif (choice==5):
        commonMap={}
        for item in student_data:
            major = item["Major"]
            if major in commonMap:
                commonMap[major]+=1
            else:
                commonMap[major]=1
        print(commonMap)
    elif (choice==6):
        hashmapId=int(input("Enter ID:"))
        for item in student_data:
            if(item["ID"]== hashmapId):
                student_data.remove(item)
            print(student_data)
    elif (choice==7):
        sum=0
        count=0
        for item in student_data:
            sum+=item["GPA"]
            count+=1
        print(sum/count)
    elif (choice==8):
        max=3.0
        for item in student_data:
            if(item["GPA"]>=max):
                print(item)
    elif (choice==9):
        print("Thanks for using my Menu Program!!!")
    else:
        print("Invalid Input")

main()