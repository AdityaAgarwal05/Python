# fns are object that can be passed into other objects/variables
# we can define a fn inside a fn                  
# a fn can return a fn



  #assigning fn to another variable-
# def hello():
#     return "Hello there!!"

# print(hello)                  #o/p:- <function hello at 0x0000025051DDC0F0>
# print(hello())                #o/p:- Hello there!!


# greet = hello                 #o/p:- fns are object that can be passed into other object
# print(greet())                #o/p:- Hello there!!



    # del keyword-
# del hello
# #print(hello())               #o/p:-  NameError: name 'hello' is not defined

# print(greet())                #o/p:- Hello there!!   -> pass by value.











                          #pasing a fn in another fn and calling a fn into another fn

# def hello(NAME='jose'):
#     print('Hi!! this is from hello fn')      

#     def greet():
#         return '\t Hi!! this is greet fn inside hello fn'
    
#     def welcome():
#         return '\t Hi!! this is welcome fn inside hello fn'
    
#     print(greet())
#     print(welcome())
#     print('THIS IS THE END OF THE HELLO FUNCTION')



# hello()         # o/p:- Hi!! this is from hello fn
#                 #                 Hi!! this is greet fn inside hello fn
#                 #                 Hi!! this is welcome fn inside hello fn
#                 #       THIS IS THE END OF THE HELLO FUNCTION

# greet()         #o/p:- NameError: name 'greet' is not defined 
# welcome()       #o/p:- NameError: name 'welcome' is not defined       
    
    









              # As we can see that the scope of greet and welcome is limited to hello only and we can not access them outside of the scope of hello
              # here is how to acheive this- we should make hello fn, returning a fn

# def hello(NAME):
#     print('Hi!! this is from hello fn')      

#     def greet():
#         return '\t Hi!! this is greet fn inside hello fn'
    
#     def welcome():
#         return '\t Hi!! this is welcome fn inside hello fn'
    
#     print('THIS IS THE END OF THE HELLO FUNCTION')
#     if NAME=='jose':
#         return greet
#     else:
#         return welcome
    


# my_func=hello('jose')
# print(my_func)             #o/p:- <function hello.<locals>.greet at 0x000001C1AB4D7B60>
# print(my_func())             #o/p:-   Hi!! this is greet fn inside hello fn

        




# def aditya():
    
#     def kannu():
#         print('i am kannu')

#     return kannu    


# some_func = aditya()
# some_func()           #o/p:- i am kannu






                                  #Passing a fn as an argument-

# def hello():
#     return 'Hello Aditya'

# def greet(some_func):             #some_func is a fn, and we are taking this fn as an argument
#     print(some_func())            #here we are printing this fn
#     print("greetings of the day!!")   

# greet(hello)            #passing a fn as an argument, dont do like this--> greet(hello()) 
#                         #o/p:- Hello Aditya
#                         #      greetings of the day!!
            




                          #Decorators-

#this is our decorator fn-
# def new_decorators(original_func):       --> here we are taking a fn as an argument
#     def wrap_fn():                       --> here we are defining a fn inside a fn
#         print('here we can write some extra code before the original fn')

#         original_func()                  --> here we are calling a fn inside a fn

#         print('here we can write some extra code after the actual fn')

#     return wrap_fn                       --> here we are returning a fn in a fn


# #this is the fn that need to be decorated
# def func_needs_decorator():
#     print('i want to be decorated')

# #func_needs_decorator()      #o/p:- i want to be decorated

# #here we have decorated the fn- 
# decorated_func =  new_decorators(func_needs_decorator)

# decorated_func()         #o/p:- 
                           #      here we can write some extra code before the original fn
                           #      i want to be decorated
                           #      here we can write some extra code after the actual fn

  


     # we can make this method easy to use by using @ operator-

#this is our decorator fn-
def new_decorators(original_func):
    def wrap_fn():
        print('here we can write some extra code before the original fn')

        original_func()

        print('here we can write some extra code after the actual fn')

    return wrap_fn   

#this is the fn that need to be decorated
@new_decorators
def func_needs_decorator():
    print('i want to be decorated')

func_needs_decorator()     #o/p:- 
                           #      here we can write some extra code before the original fn
                           #      i want to be decorated
                           #      here we can write some extra code after the actual fn


# now if you want again you original fn, just comment out the @ operator line-
#@new_decorators
def func_needs_decorator():
    print('i want to be decorated')

func_needs_decorator()                 #o/p:-i want to be decorated       




#Note:we can give any custom names to both our decorator function and the wrapper function 

