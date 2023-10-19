def Strong_Password(password):
    pwrc=0
    pwrl=0
    pwrs=0
    for char in password:
        if 65<= ord(char) <=90:
            pwrc+=1
        elif 97<= ord(char) <=122:
            pwrl+=1
        elif  ord(char) == 63 or ord(char) == 64 or ord(char) == 33 or ord(char) == 36:
            pwrs+=1
    if ((pwrc>0)and (pwrl>0)and (pwrs>0) and len(password)>8):
        print("Strong Password")
    else:
        print("Weak Password")
          

          

def main():
    password=str(input("Input: "))
    Strong_Password(password)
main()