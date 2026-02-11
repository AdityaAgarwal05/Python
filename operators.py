                              
# range(x)  --> starts from 0 till x-1
# range(x,y)--> y not included
# enumerate(word)
# zip(a,b) 
# in  
# min max 
# random 
# input


                         # range()  operator

# for num in range(10):
#     print(num)     #o/p:- 0 1 2 3 4 5 6  7 8 9



# for num in range(3,10):
#     print(num)     #o/p:- 3 4 5 6  7 8 9



# for num in range(2,20,2):
#     print(num)     #o/p:- 2 4 6 8 10 12 14 16 18   


# print(list(range(2,20,2)))    #o/p:- [2, 4, 6, 8, 10, 12, 14, 16, 18]



                               #enumerate ---------> returns tupple



# word = 'abcde'

# for item in enumerate (word):
#     print (item)                 #o/p:- (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')      --> returns tupple


# for item,value in enumerate (word):
#     print (item) 
#     print (value) 
#     print('\n')                            #o/p:- 0 a  1 b   2 c   3 d  4 e

            






                             #zip  ---------> returns tupple


# a = [1,2,3]
# b= ['a','b','c']
# for item in zip(a,b):
#     print(item)           #o/p:- (1, 'a') (2, 'b')  (3, 'c')
             

# a = [1,2,3]
# b= ['a','b','c']
# c= [100,200,300]
# for item in zip(a,b,c):
#     print(item)           #o/p:- (1, 'a', 100) (2, 'b', 200) (3, 'c', 300)



# a = [1,2,3,4,5,6]
# b= ['a','b','c']
# c= [100,200,300]
# for item in zip(a,b,c):
#     print(item)           #o/p:- (1, 'a', 100) (2, 'b', 200) (3, 'c', 300)





# a = [1,2,3]
# b= ['a','b','c']
# c= [100,200,300]
# print(list(zip(a,b,c)))    #o/p:- [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]





                          # in operator
                       

# print('x' in ['x','y','z'] )                    #o/p:-True
# print('x' in [1,2,3] )                          #o/p:-False
# print('a' in 'i am an engineer' )               #o/p:-True
# print('k1' in {'k1':1, 'k2':2} )                #o/p:-True

# d = {'k1':1, 'k2':2}
# print(1 in d.values())                           #o/p:-True

# d = {'k1':1, 'k2':2}
# print('k3' in d.keys())                           #o/p:-False


                           



                           # min max fn



# mylist = [1,2,3,4,5]
# print(min(mylist))
# print(max(mylist))






                            #random library

# mylist = [1,2,3,4,5]
# from random import shuffle  
# shuffle(mylist)      # it does not return anything that is why print(shuffle(mylist)) will not return anything
# print(mylist)                      #o/p:- [5, 2, 3, 4, 1]   



# from random import randint
# print(randint(0,100))           #o/p:- random number between 0 to 100










                                #input fn


# a = input('Enter a number here: ')            #o/p:- Enter a number here: 5   --> input always takes as a string
# print(type(a))  # <class 'str'>



a = int(input('Enter a number here: ')) 
print(type(a))  # <class 'int'>
