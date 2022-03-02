class Student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    def __del__(self):
        print("Object has been destroyed")

obj_1=Student("lakshay",21104067)
print(obj_1.name)
print(obj_1.rollnumber)
