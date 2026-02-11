#        functional parameters-  *args, **kwargs
# *args    - arguments
# **kwargs - keyword arguments

# these are a way to accept an arbitary number of arguments and keyword arguments without having to define the bunch of parameters in our fn call

#return 5% of the sum of a and b
# def myfunc(a,b):
#     return sum((a,b)) * 0.05          #Note- sum fn takes arguments in tuple

# print(myfunc(50,50)) #o/p:- 5.0

# def myfunc(a,b,c=0,d=0,e=0):
#     return sum((a,b,c,d,e)) * 0.05

# print(myfunc(50,50,100)) #o/p:- 10.0
# print(myfunc(50,50,100,50,50)) #o/p:- 15.0
# print(myfunc(50,50,100,50,50,100)) #o/p:- TypeError: myfunc() takes from 2 to 5 positional arguments but 6 were given


# so to solve this problem we can use *args-
# def myfunc(*args):
#    return sum(args) * 0.05

# print(myfunc(50,50,100,50,50,100)) #o/p:-20
# print(myfunc(50,50,100)) #o/p:- 10.0

# def myfunc(*hereCanBeAnyVariable):
#    return sum(hereCanBeAnyVariable) * 0.05

# print(myfunc(50,50)) #o/p:-5.0


# def myfunc(*args):
#    for item in args:
#       print(item)

# myfunc(1,32,23,87,56,96)
#o/p:-
# 1
# 32
# 23
# 87
# 56
# 96






         #kwargs keyword- as *args returns a tupple, similarly *kwargs returns a dictionary

# def myfunc(**kwargs):
#    print(kwargs)         # returns dictionary, eg.)- {'fruit': 'pomegranate', 'vaggie': 'raddish'}
#    if 'fruit' in kwargs:
#       print('i would like to eat {}'.format(kwargs['fruit']))
#    else:
#       print('sorry!!')
      
      
# myfunc(fruit='apple')      #O/p:-i would like to eat apple
# myfunc(veggie='raddish')      #O/p:-sorry!!
# myfunc(fruit='pomegranate')      #O/p:-i would like to eat pomegranate
# myfunc(fruit='pomegranate', vaggie='raddish')      #O/p:-i would like to eat pomegranate


              # we can use them in combination-


# def myfunc(*args,**kwargs):
#    print('i would like to have {} {}'.format(args[0],kwargs['food']))         

# myfunc(10,20,30,fruit='orange', food='sandwich', animal='dog')  #o/p:-  i would like to have 10 sandwich


# def myfunc(*args,**kwargs):
#    print('i would like to have {} {}'.format(args[0],kwargs['food']))         

# myfunc(10,20,30,fruit='orange', food='sandwich', animal='dog', 50)  #o/p:-  SyntaxError: positional argument follows keyword argument
