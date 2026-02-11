# inheritance is a way to define new classes based on the already existed classes
# it increases reusability of the code and reduces the complexity of the program in terms of readability



# class Animal():                            #Base class
#     def __init__(self):
#       print('Animal created')
#     def who_am_i(self):
#        print('i am an animal')
#     def eat(self):
#        print('i am eating')    


# class Dog(Animal):                        #Derived class
#    def __init__(self):
#       Animal.__init__(self)                # it means create an instance of animal class when we create an instance of dog class
#       print('Dog created')


# my_dog = Dog()      # when we run here, o/p:  Animal created   Dog created
# my_dog.who_am_i()   #o/p:- i am an animal      ---->  since we derived the animal class, that is why we can use this fn
# my_dog.eat()        #o/p:- i am eating         ---->since we derived the animal class, that is why we can use this fn




    #here is how we can overide the fn of Base class and also we can add more methods in derived class-

class Animal():                            #Base class
    def __init__(self):
      print('Animal created')
    def who_am_i(self):
       print('i am an animal')
    def eat(self):
       print('i am eating')    


class Dog(Animal):           #Derived class
   def __init__(self):
      #Animal.__init__(self)  # it means create an instance of animal class when we create an instance of dog class
      print('Dog created')

   def who_am_i(self):
      print('i am a dog') 

   def bark(self):
      print('WOOF!!')    


my_dog = Dog()      # when we run here,           o/p:  Dog created
my_dog.who_am_i()   #no/p:- i am a dog      --->  since we override this fn in dog class 
my_dog.eat()        #o/p:- i am eating 
my_dog.bark()        #o/p:- WOOF!!
