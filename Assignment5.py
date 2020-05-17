#1. Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

def Syntaxhandling(x):
    try:
        return (eval(x))
    except SyntaxError:
        return ("Syntax Error in the Code")

print(Syntaxhandling('datetime(2020, 05, 10)'))

#2. Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
from sys import argv

def FileNameError():
    try:
        with open(argv[1], 'r') as my_file:
            return(my_file.read())
    except IOError:
        return("Wrong file name. Please provide correct file name.")
print(FileNameError())

#3. Write a program to handle an error if the user entered the number more than four digits it should return “Please length is too short/long !!! Please provide only four digits”
def UserNumber(num):
    valid = False
    while not valid:
        try:
            number = int(input(num))
            if len(str(number)) <= 4:
                return number
            else:
                print("Please length is too short/long !!! Please provide only four digits")
                continue
        except ValueError:
            print("Please only provide a number")
            continue


print(UserNumber('Please give me a 4 digit number> '))

#4. Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
def userPass(username, password):
    attemp = 1
    db = [{"User" :"admin","Pass": "consultadd1"},{"User" :"editor","Pass": "consultadd2"},{"User" :"client1","Pass": "consultadd3"}]
    while attemp <= 3:
        username = str(input(username))
        password = str(input(password))

        for i in range(len(db)):
            if (db[i]["User"] == username and db[i]["Pass"]==password):
                return "Welcome"
        else:
            if attemp == 3:
                return "No more login attempt left"
            username = "enter your User ID> "
            password = "enter your Password> "
            print("Please provide a correct username/ password")
            attemp += 1
            continue

print(userPass("enter your User ID> ", "enter your Password> "))

#6. Read any file using Python File handling concept and return only the even length string from the doc.txt file.

file = open('test.txt', 'r')
for each in file:
    if len(each)%2==0:
        print(each)