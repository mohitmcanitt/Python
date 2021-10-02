#When we declare a variable inside a class, but outside the method, it is called a static or class variable
class Employee:
    Course_name="MCA"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def print_details(self):
        print(self.name,self.roll_no,self.Course_name)




obj1=Employee("Mohit",56)
obj2=Employee("Rahul",72)
obj1.print_details()
obj2.print_details()

