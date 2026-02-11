# A sample class-

# class Sample():
#    pass

# my_sample = Sample()
# print(type(my_sample))   #o/p:- <class '__main__.Sample'>         --> __main_ is telling that this particular instance of Sample is connected with our main script here


 
                 #Creating attributes in class 

#attributes are characterstics of an object

# class Dog():                              #    self keyword connects this method with to the instance of the class
#    def __init__(self,breed):              #   this method will always call upon whenever we will create an instance of the class, it is constructor, it should be the very first method of the class
#       #it is an attribute, we take an argument from user and assign it to attribute using self.attribute_name
#       self.breed = breed
     

# #my_dog= Dog()     #o/p:- TypeError: Dog.__init__() missing 1 required positional argument: 'breed'
# my_dog= Dog(breed = 'Huskie')
# print(type(my_dog))      #o/p:-     <class '__main__.Dog'>
# print(my_dog.breed)      #o/p:-     Huskie


# We can have the name of our argument and attribute different-    howeever by convention we have their name same
# class Dog():                                #   self keyword connects this method with to the instance of the class
#    def __init__(self,mybreed):              #   this method will always call upon whenever we will create an instance of the class, it is constructor
#       #it is an attribute, we take an argument from user and assign it to attribute using self.attribute_name
#       self.breed = mybreed
     

# #my_dog= Dog()     #o/p:- TypeError: Dog.__init__() missing 1 required positional argument: 'breed'
# my_dog= Dog(mybreed = 'Huskie')
# print(type(my_dog))      #o/p:-     <class '__main__.Dog'>
# print(my_dog.breed)      #o/p:-     Huskie



     # lets add some more attributes to this class-

# class Dog():                              
#    def __init__(self,breed,name,spots):              
#       #it is an attribute, we take an argument from user and assign it to attribute using self.attribute_name
#       self.breed = breed
#       self.name = name       #Expecting string
#       self.spots = spots     #Expecting boolean
     

# #my_dog= Dog()     #o/p:- TypeError: Dog.__init__() missing 1 required positional argument: 'breed'
# my_dog= Dog(breed = 'Huskie', name='sammy', spots=False)
# print(type(my_dog))      #o/p:-     <class '__main__.Dog'>
# print(my_dog.breed)      #o/p:-     Huskie  
# print(my_dog.name)      #o/p:-     sammy  
# print(my_dog.spots)      #o/p:-     False 



       




      # class object attributes- we can have attributes such that it remains same for any instance of the claas


class Dog():   
   
   # class object attribute- same for any instance of the class, so no need to use "self" keyword
   species = 'Mammal' #since all the dogs are mammals


   def __init__(self,breed,name,spots):              
      #user defined attributes
      self.breed = breed
      self.name = name       #Expecting string
      self.spots = spots     #Expecting boolean
     

#my_dog= Dog()     #o/p:- TypeError: Dog.__init__() missing 1 required positional argument: 'breed'
my_dog= Dog(breed = 'Huskie', name='sammy', spots=False)
print(type(my_dog))      #o/p:-     <class '__main__.Dog'>
print(my_dog.breed)      #o/p:-     Huskie  
print(my_dog.name)      #o/p:-     sammy  
print(my_dog.spots)      #o/p:-     False 
print(my_dog.species)      #o/p:-   Mammal




                     
