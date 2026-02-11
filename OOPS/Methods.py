#methode are the fn's defined inside the body of the class that performs some operations, that may or may not use the attributes-

# class Dog():   
#    species = 'Mammal' #since all the dogs are mammals

#    def __init__(self,breed,name,spots):              
#       #user defined attributes
#       self.breed = breed
#       self.name = name       #Expecting string
#       self.spots = spots     #Expecting boolean

#     #user defined methods (operation/actions)-
#    def bark(self):   # this self is used to connect this method to the object
#       print('WOOF!! my name is {}'.format(self.name))
     

# #my_dog= Dog()     #o/p:- TypeError: Dog.__init__() missing 1 required positional argument: 'breed'
# my_dog= Dog(breed = 'Huskie', name='sammy', spots=False)
# print(type(my_dog))      #o/p:-     <class '__main__.Dog'>
# print(my_dog.breed)      #o/p:-     Huskie  
# print(my_dog.name)      #o/p:-     sammy  
# print(my_dog.spots)      #o/p:-     False 
# print(my_dog.species)      #o/p:-   Mammal

# my_dog.bark     #will not print anything, so there is a difference b/w calling attributes and methods, methods requires paranthesis
# my_dog.bark()             #o/p:- WOOF!! my name is sammy     


   #methods can take outside arguments-

# class Dog():   
   
#    species = 'Mammal' #since all the dogs are mammals

#    def __init__(self,breed,name,spots):              
#       #user defined attributes
#       self.breed = breed
#       self.name = name       #Expecting string
#       self.spots = spots     #Expecting boolean

#     #user defined methods (operation/actions)-
#    def bark(self, number):   # this self is used to connect this method to the object
#       print('WOOF!! my name is {} and my number is {}'.format(self.name,number))
     
# my_dog= Dog(breed = 'Huskie', name='sammy', spots=False)
# #my_dog.bark()             #o/p:- TypeError: Dog.bark() missing 1 required positional argument: 'number'
# my_dog.bark(10)             #o/p:-WOOF!! my name is sammy and my number is 10
 










class Circle():
    #class object attribute-
    pi = 3.14

    def __init__(self, radius=1):
        self.radius=radius
        self.area=self.pi*radius*radius

    # user defined method-
    def circumference(self):
        return 2*self.pi*self.radius
    
my_circle=Circle()
print(my_circle.pi)                 #o/p:- 3.14
print(my_circle.radius)             #o/p:- 1
print(my_circle.area)             #o/p:- 3.14
print(my_circle.circumference())    #o/p:- 6.28

my_circle=Circle(10)
print(my_circle.pi)                 #o/p:- 3.14
print(my_circle.radius)             #o/p:- 10
print(my_circle.area)             #o/p:- 314.0
print(my_circle.circumference())    #o/p:- 62.800000000000004




#Note:- we can call class object attribute like this also-

class Circle():
    #class object attribute-
    pi = 3.14

    def __init__(self, radius=1):
        self.radius=radius
        self.area=Circle.pi*radius*radius                   # we can use the name of class instead of self

    # user defined method-
    def circumference(self):
        return 2*Circle.pi*self.radius                       # we can use the name of class instead of self
    
my_circle=Circle()
print(my_circle.pi)                 #o/p:- 3.14
print(my_circle.radius)             #o/p:- 1
print(my_circle.area)             #o/p:- 3.14
print(my_circle.circumference())    #o/p:- 6.28

my_circle=Circle(10)
print(my_circle.pi)                 #o/p:- 3.14
print(my_circle.radius)             #o/p:- 10
print(my_circle.area)             #o/p:- 314.0
print(my_circle.circumference())    #o/p:- 62.800000000000004
