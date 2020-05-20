#1. Write a program that calculates and prints the value according to the given formula: Q= Square root of [(2*C*D)/H]
D = 1,4,9,16,25
C, H = 50,30
val = map(lambda x:(2*C*x/H)**1/2,D)
print(list(val))

#2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.
class Shape:
    length = 0
    def Area(self):
        return (self.length ** 2)

class Square(Shape):
    def __init__(self,length):
        self.length = length

print(Shape().Area())
print(Square(2).Area())

#3. Create a class to find the three elements that sum to zero from a set of n real numbers.

class SumOfThree:
    def Sum0(self, InputList):
        OutputList = []
        for i in range(0,len(InputList)-3):
            for j in range(i+1,len(InputList)):
                for k in range(j+1, len(InputList)):
                    if InputList[i]+InputList[j]+InputList[k] == 0:
                        OutputList.append([InputList[i],InputList[j],InputList[k]])
        return OutputList
InputList = [-25,-10,-7,-3,2,4,8,10]
SumOfThree().Sum0(InputList)

#4. What is the output of the following code? Explain your answer as well.
class A:
    def __init__(self, x=1):
        self.x = x

class der(A):
    def __init__(self, y=2):
        super().__init__()
        self.y = y

def main():
    obj = der()
    print(obj.x, obj.y)


main()

#Ans:  the result will be 1 2. The Class der is inheriting the class A and when we are calling the main function, it is getting the value of x from Class A and y from the child class der.
# Super is calling the function in parent class, it is easy to maintain the code with super, so you can just change the parent class name and you don't have to update the code to call the function, auper will call that.


class A:
    def __init__(self, x):
        self.x = x

    def count(self, x):
        self.x = self.x + 1


class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y

    def count(self):
        self.y += 1


def main():
    obj = B()
    obj.count()

    print(obj.x, obj.y)


main()

# Ans will be 3 1. Main function is calling class B, which is inheriting class A. In class B y's default value is 0 but in count function it is incrementing by 1, so y will be 1. A.__init__(self, 3) is initializing x with 3. so x will be 3.

class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)

    def multiply(self, i):
        self.i = 4 * i;



class B(A):
    def __init__(self):
        super().__init__()

    def multiply(self, i):
        self.i = 2 * i;

obj = B()

#Ans: Above code will print 30.
# Reason: we are creating an object of class B which is a child class of A. using super inside init function of B we are inheriting init of A and getting the value of i as 15. But the multiply function of B is overriding the multiply function of A, hence i = 15*2 = 30.


