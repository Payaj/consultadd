#1. Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.
y = filter(lambda x:(x%3!=0 and x%7==0),list(range(50)))
#print(list(y))

#2. Write a program in Python to  multiple the element of list by itself using traditional function and pass the function to map to complete the operation.

def Mult(num):
    multiply = num*num
    return multiply

finalList = map(Mult,list(range(1,5)))
#print(list(finalList))

#3. Write a program to Python find out the character in a string which is uppercase using list comprehension.
String = "Hi, my name is Payaj. I'm writing a program to find UPPER case characters"
List = [i for i in String if i.isupper()]
#print(List)

#4. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
Student = ['Smit', 'Jaya', 'Rayyan']
capital = ['CSE', 'Networking', 'Operating System']

newDict = {s:c for (s,c) in zip(Student,capital)}
#print(newDict)

#6. Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

def revStr_gen(String):
    for i in range(len(String)-1,-1,-1):
        yield (String[i])

givenString = "Consultadd Training"
reverse_String = "".join([i for i in revStr_gen(givenString)])
#print(reverse_String)

#7. Write any example on decorators.
def sq(num):
    numsq = num**2
    return numsq

num1 = sq
num2 = num1(2)
#print(num2)
