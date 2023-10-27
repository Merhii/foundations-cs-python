def choiceOne(number):
    if(number<10):
        return 1 # Base Case
    else:
        return 1+choiceOne(number//10) # recursion case
def choiceTwo(array):
    if(len(array)==0):
        return 0 # Base Case
    elif (len(array)==1):
        return array[0]

    #using divide an concour
    mid = len(array)//2
    midLeft = choiceTwo(array[:mid])
    midRight = choiceTwo(array[mid:])
    
    if (midRight>midLeft):
        return midRight
    else:
        return midLeft
    
def choiceThree(html,tag):
    count =0
    openTag=f"<{tag}>" #put the string in tag format
    closeTag=f"</{tag}>"
    start= html.find(openTag)
    if start == -1: 
        return 0
    end=html.find(closeTag,start)
    if end == -1:
        return 0
    # if it didnt find the starting or ending tag then return 0
    count+=1
    count+=choiceThree(html[end+len(closeTag):],tag)
    # html[end+len(closeTag): searches after the first tag is found
    return count

def main():
    print("1. Count Digits\n2. Find Max\n3.1. Count Tags\n3.2. Count Normalized Columns\n4. Exit\n- - - - - - - - - - - - - - -")
    choice=float(input("Enter a choice:"))
    if(choice==1):
        number = int(input("Input:"))
        if (number<0):
            number = abs(number)
        n=choiceOne(number)
        print (f"Output:{n}")
    elif(choice==2):
        array = eval(input("Input:"))
        maximuim=choiceTwo(array)
        print(f'Output: {maximuim}')
    elif(choice==3.1):
        html ="""
        <html>
        <head>
        <title>My Website</title>
        </head>
        <body>
        <h1>Welcome to my website!</h1>
        <p>Here you'll find information about me and my hobbies.</p>
        <h2>Hobbies</h2>
        <ul>
        <li>Playing guitar</li>
        <li>Reading books</li>
        <li>Traveling</li>
        <li>Writing cool h1 tags</li>
        </ul>
        </body>
        </html>
        """
        tag=str(input("Input:"))
        count=choiceThree(html,tag)
        print(f"count is : {count}")
    elif(choice==4):
        print("Thanks for using my menu")
    else:
        print ("Invalid Opperation")

main()
