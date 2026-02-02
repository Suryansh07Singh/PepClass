# class Student:         #Class method is defined inside the class with @classmethod decorator 
#   college='LPU'        # bound to the class and not the object of the class
#   @classmethod
#   def greet(cls):
#     print(cls)
#     return "Hello Students"
# s1=Student()
# print(s1.greet())
# #type(s1.greet())
print(dir(int))