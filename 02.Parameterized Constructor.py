class person:

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def message(self):
        print(self.name,self.roll_no)

obj=person("Mohit","56")
person.message(obj)
