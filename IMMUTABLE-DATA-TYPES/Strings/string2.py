#string properties and methods

# string is immutable, that means it can not be changed
#Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)


# a= "kannu"
# a[0]="g"
# print(a) #Error: 'str' object does not support item assignment

# new_name="g"+a[1:]    # this is callled string concatenation
# print(new_name)  #o/p:-gannu

# b= "hello " + new_name 
# print(b)


        #  .upper() --> returns uppercase string, but does not change original string(ofcourse, string is immutable, but since list is mutable so we have to take care of these things in case of lists)
# x= "kannu"
# print(x.upper) #<built-in method upper of str object at 0x0000026230861230>
# print(x.upper()) #KANNU ,  this is not in place, it is a new string that is created original string still remained unchanged
# print(x) #O/p:- kannu

#if you want to change the original string then reassignment is the only option-
# x = x.upper()
# print(x) #o/p:- KANNU

# b= b+ " myself kannu" # reassignment is possible
# print(b) 


# string multiplication
# a = "kannu"
# print(a * 10)  #o/p:- kannukannukannukannukannukannukannukannukannukannu


# a='2'
# b='3'
# print(a+b) o/p:- 23, that is why we have to take care of these things in dynamic typing



#split method-
# a= "Hi this is string"
# print(a.split())  #o/p:-['Hi', 'this', 'is', 'string']
# my_list = a.split()
# print(my_list)    #o/p:-['Hi', 'this', 'is', 'string']


    #by default it is spliting based on white space, let say you want it to split based on character 'i' -
#print(a.split('i'))  #o/p:-['H', ' th', 's ', 's str', 'ng'] #look, in this split white spaces are included






