
# introduction to class and object in python

class employee:
    
    def __init__(self):   # < ---- special function - constructor  // This is called Parameterized Constructor
        self.id = 123
        self.name = "Prashant Takale"
        self.salary = 50000000
        self.designation = "SDE"
    
    # creating a function inside class
    def travel(sel , name):
        print(f"hi my name is {name}")


 #object creation 
sam = employee()  
# print(sam.designation) 



sam.travel("Prashant Takale")   # < --- obj to fun calling



"""

1 > What is __init__ in Python
-- >  __init__ is a special method that runs automatically when an object is created.
-- > if we not write (__init__) then Python creates a default constructor for you.

2 > Why is ( self )  used
-- > self means current object.
-- > Without self, Python won't know which object's data you are talking about

3 > self.id , self.name , ..... ?
-- > They are called instance variables
-- > Because each object will have its own copy

4 > Where do you use constructors in real projects?
-- >To initialize:
                    1. user details
                    2. database connections
                    3. model parameters
                    4. employee data
                    ok : -- >
"""