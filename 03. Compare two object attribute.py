class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def compare(self,other):
        if(self.age==other.age):
            return True    
        else:
            return False    

obj1=person("Mohit",24)
obj2=person("Rohit",24)

if obj1.compare(obj2):
    print("Equal Age")
else:
    print("Age is not equal")

