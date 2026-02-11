# variable name is stored in namespace, and these variables have scope
# and scope determines the visibility of the variables into the other parts of code

# for this we have LEGB rule format which determines the scope of the varibale
#     L- local: Names assign in anyway within the function(def or lambda), and not declared global in that fn
#     E- Enclosing fn locals: Names in the local scope of any and all enclosed functions (def or lambda), from inner to outer
#     G- Global: Names assigned at the top level of a module file or declared global in a def within the file
#     B- Built in: names pre assigned in the built in names module like 'open', 'range' etc 




#Global
# x=1
# def printer():
#     #Enclosing fn local
#     x=2
#     def printx():
#         #local
#         x=3
#         print(f'value of x is {x}')
#     printx()  

# print(x)     #o/p:- 1
# printer()    #o/p:-value of x is 3        ----> since here local x is 3






#Global
# x=1
# def printer():
#     #Enclosing fn local
#     x=2
#     def printx():
#         #local
#         #x=3
#         print(f'value of x is {x}')
#     printx()    

# print(x)     #o/p:- 1
# printer()    #o/p:-value of x is 2        ----> since here local namespace is within the fn that is Enclosing fn local







#Global
# x=1
# def printer():
#     #Enclosing fn local
#     #x=2
#     def printx():
#         #local
#         #x=3
#         print(f'value of x is {x}')
#     printx()    

# print(x)     #o/p:- 1
# printer()    #o/p:-value of x is 1        



                 


                 #Changing the value of Global variable- using the 'global' keyword we can reach out to global namespace and can change the value of global variable




#Global
# x=100
# def printer():
#     global x
#     print(f'value of x is {x}')
#     #Local reassignment of global variable- 
#     x=200
#     print(f'new value of global variable is {x}')

# print(x)    #o/p:- 100
# printer()   #o/p:- new value of global variable is 200
# print(x)    #o/p:- 200
  

                    


                    #so due to this immense power of 'global' keyword we should restrain using it,instead we can change the value of global variable like this-
                    #this is much cleaner and safer way, so that we dont Accidentaly change the value of global variable
#Global
x=100
def printer(x):       #take global variable as a parameter here
    print(f'value of x is {x}')
    #Local reassignment of global variable- 
    x=200
    print(f'new value of global variable is {x}')
    return x  #here add this line

print(x)    #o/p:- 100
x=printer(x)   #o/p:- new value of global variable is 200    --> here we assigned the value into the global variable
print(x)    #o/p:- 200
                      
