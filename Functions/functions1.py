
    # fn without arguments- 
# def say_hello():
#     print('hello')

# say_hello()       #o/p:- hello
# say_hello         #o/p:-



     # fn with arguments- 
# def say_hello(name):
#     print(f'hello {name}')

#say_hello('aditya')  #o/p:-hello aditya
# say_hello()  #o/p:- TypeError: say_hello() missing 1 required positional argument: 'name'




     # default arguments-
# def say_hello(name='This is default name'):
#     print(f'hello {name}')

# say_hello('aditya')  #o/p:-hello aditya
# say_hello()  #o/p:- hello This is default name





        # fn returning a value-
# def add(num1,num2):
#     return num1+num2

# print(add(1,2))   #o/p:- 3
# result= add(5,4)
# print(result)      #o/p:- 9
# print(add('1','2'))   #o/p:- 12     ---> this is the problem with dynamically typed language








     # Q.) check whether given number is even or odd
# def even_check(num):
#     if(num%2==0):
#         return True
#     else:
#         return False
    
# def even_check(num):
#         return num%2==0  
    

# print(even_check(5))    #o/p:- False
# print(even_check(4))    #o/p:- True


     # Q.) Return true if any number in the list is even

# def check(mylist):
#      for item in mylist:
#           if(item%2==0):
#                return True
               
#      return False    

# mylist = [1,3,5,7,9]    
# print(check(mylist))     #o/p:- False

# mylist = [1,2,3,5,7,9]    
# print(check(mylist))     #o/p:- True


            # Q.) Return all the even numbers in a list

# def evenlist(mylist):
#     anslist=[]
#     for item in mylist:
#         if(item%2==0):
#          anslist.append(item)
#         # else:
#         #    pass  ---> Not mandatory to write this else block
#     return anslist


# mylist = [1,2,3,4,5,6,7,8]
# print(evenlist(mylist))            #o/p:- [2, 4, 6, 8]









                          #tupple unpacking with python fns-

              # Q.)return the employee of the month-

# def emp_of_month(work_hours):
#    maxi=0
#    for item,value in work_hours:
#       if value>maxi:
#          maxi=value
#          ans=item
#    print(f'Employee of the month is {ans}')     


# work_hours=[('adi',100),('nandan',200),('ansh',300),('joshi',400)]
# emp_of_month(work_hours)  #o/p:- Employee of the month is joshi

# work_hours=[('adi',100),('nandan',2000),('ansh',300),('joshi',400)]
# emp_of_month(work_hours)  #o/p:- Employee of the month is nandan

    #returning a tupple-
# def emp_of_month(work_hours):
#    maxi=0
#    for item,value in work_hours:
#       if value>maxi:
#          maxi=value
#          ans=item
#    return(ans,maxi) 


# work_hours=[('adi',100),('nandan',200),('ansh',300),('joshi',400)]
# name,workHours = emp_of_month(work_hours)   
# print(f'Employee {name} worked for {workHours} hours')   #o/p:-Employee joshi worked for 400 hours



# def emp_of_month(work_hours):
#    maxi=0
#    for item,value in work_hours:
#       if value>maxi:
#          maxi=value
#          ans=item
#    return(ans,maxi) 

# work_hours=[('adi',100),('nandan',2000),('ansh',300),('joshi',400)]
# name,workHours = emp_of_month(work_hours)   
# print(f'Employee {name} worked for {workHours} hours')   #o/p:-Employee nandan worked for 2000 hours
