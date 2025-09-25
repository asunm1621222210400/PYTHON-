#### OVERRIDING
##
##class Student:
##    def function(self):
##        print("python")
##class College(Student):
##    def function(self):
##        print("framework")
##obj=College()
##obj.function()
##
#### OVERRIDING USING SUPER KEYWORD
##
##class Student:
##    def function(self):
##        print("python")
##class College(Student):
##    def function(self):
##        super().function()
##        print("framework")
##obj=College()
##obj.function()
##
#### OVERRIDING USING HIERARCHICAL INHERTANCE
##
##class Student:
##    def function(self):
##        print("python")
##class College(Student):
##    def function(self):
##        print("framework")
##class Teacher(Student):
##    def function(self):
##        print("website")
##obj=Student()
##obj1=College()
##obj2=Teacher()
##
##obj.function()
##obj1.function()
##obj2.function()
##
## IF CONDITION IN OVERRIDING
##
##class Student:
##    def function(self,marks):
##        self.marks=marks
##        marks=0
##        if marks<35:
##            print("python")
##class College(Student):
##    def function(self,marks):
##        if marks>75:
##           super().function(marks)
##           print("framework")
##obj=College()
##obj.function(20)
##obj.function(90)
##
##
##
## OPERATOR OVERLOADING
##
##class Student:
##    def __init__(self, marks):
##        self.marks=marks
##    def __add__(self,other):
##        return Student(self.marks+other.marks)
##    def __str__(self):
##        return f"{self.marks}"
##obj=Student(10)
##obj1=Student(20)
##print(obj+obj1)
##
#### SINGLE DISPATCH
##
##from functools import singledispatch
##
##@singledispatch
##
##def process(data):
##    print("data")
##@process.register(int)
##def _(data):
##    print(data*data)
##@process.register(str)
##def _(data):
##    print(data.upper())
##process(10)
##process("python")
##process(2.4)
##
##
##
##
####TASK
##
##a=int(input("Enter the number1:"))
##b=int(input("Enter the number2:"))
##c=int(input("Enter the number3:"))
##if a>=c and a>=b:
##    print("The largest number is:",a)
##elif b>=a and b>=c:
##    print("The largest number is:",b)
##else:
##    print("The largest number is:",c)
##
####2
##
##a=input("Enter the string:")
##b="aeiouAEIOU"
##count=0
##
##for i in a:
##    if i in b:
##        count+=1
##print("Number of vowels is:",count)
##
####3
##
##a=321
##b=0
##while a>0:
##    digit=a%10
##    b=b*10+digit
##    a=a//10
##print(b)
##
####4
##
##n=int(input("enter the integers:"))
##a,b=0,1
##for i in range(n):
##    a,b=b,a+b
##    print(a, end=" ")
##    
####5
##
##a=input("Enter the string:")
##rev=" "
##for i in a:
##    rev = i + rev
##print("Reversed string:",rev)
##
##    
##    
##
##

##from Multipledispatch import dispatch
##
##@dispatch(int,int)
##def add(x,y):
##    print(x+y)
##@dispatch(str,str)
##def add(x,y):
##    print(x+y)
##add(20,30)
##add("python","css")
