#one time usable fn to which we do not have to give the name, and never reference them again

# first see built in map and filter fn in python

                                     

                                #map function-    map(fn, iterable)
# def square(num):
#     return num**2

# my_nums=[1,2,3,4,5]
# map(square,my_nums)     #o/p:- 
# for item in map(square,my_nums):
#     print(item)                     #o/p:- 1 4 9 16 25


#Note:- map applies square fn to the every element of my_nums
# list(map(square, my_nums))          #o/p:- 1 4 9 16 25         ---> Note:  list(map(square(), my_nums))     will give error, so no need to add parantheses after the name of fn





# def splicer(mystring):
#     if len(mystring)%2==0:
#         return 'EVEN'
#     else:
#         return mystring[0]
    
# names=['Aditya', 'nandy', 'joshi', 'ansh']
# print(list(map(splicer, names)))            #o/p:-     ['EVEN', 'n', 'j', 'EVEN']

      


                                          # filter fn-     filter(fn, iterable)

# def check_even(num):
#     return num%2==0

# mynums=[1,2,3,4,5,6]

# #Note: filter, filters the list based on the condition defined in fn
# print(list(filter(check_even, mynums)))      #o/p:- [2, 4, 6]



                               

                            #lambda expression,    lambda fn is also called anonymous fn

#let say we have this fn, that we want to convert into lambda expression-
# def square(num):
#     return num**2

# # step 1-
# def square(num): return num**2

# # step 2-
# lambda num): return num**2

# # step 3-
# lambda num: num**2



# here is how lambda expresson is used with map fn-
# mynums=[1,2,3,4,5]
# print(list(map(lambda num: num**2, mynums)))    #o/p: [1, 4, 9, 16, 25]

# here is how lambda expresson is used with filter fn-

#lambda expression of check_even fn-
#   lambda num: num%2==0

# mynums=[1,2,3,4,5]
# print(list(filter(lambda num: num%2==0, mynums)))    #o/p: [2, 4]



                #let say you want to return the first character of names
# names=['Aditya','nandan','joshi','sachin']
# print(list(map(lambda name:name[0],names)))         #o/p:- ['A', 'n', 'j', 's']


#                 #let say you want to return the reverse of the names
# names=['Aditya','nandan','joshi','sachin']
# print(list(map(lambda x:x[::-1],names)))         #o/p:- ['aytidA', 'nadnan', 'ihsoj', 'nihcas']




#Note:  not every complex fn can be transformed into the lambda expression













# Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.

# Remember, don't run the function, simply provide the definition.

# To give an idea what the function would look like when tested:

# myfunc(5,6,7,8)
# # Output: [6, 8]
# Added note: this exercise requires that the function return a list. Print statements will not work here.



#Approach 1-

def myfunc(*args):
    mylist=[]
    for item in args:
        if(item%2==0):
            mylist.append(item)
    return mylist 

#Approach 2-

def myfunc(*args):
    return list(filter(lambda num: num % 2 == 0, args))
