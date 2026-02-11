#many objects in python are iterable, and we can iterate over them by the use of for loop, we can iterate over list, string and keys in dictionaries
#dict.items()  ---> for accessing key value pair of dictionary
#dict.keys()  ---> for accessing keys of dictionary
#dict.values()  ---> for accessing values of dictionary




   # lists are iterable-
# abc= [1,2,3]
# for item in abc:
#     print(item)       #o/p:-  1
                        #       2
                        #       3

# for item in abc:
#     print(item, end = '')  #o/p:-123

# print(*abc)                 #o/p:-  1 2 3

# for num in abc:
#     if num%2==0:
#      print(num)
#     else:
#        print(f'the number {num} is odd')


# list_sum=0
# for num in abc:
#    list_sum=list_sum+num

# print(list_sum)   # if i put this statement under the expression then it will print the running tally of sum, thus indentation in python is very important





  # strings are iterable-
# abc= 'kannu'
# for item in abc:
#     print(item)
 



  # tupples are iterable-
# abc= (1,2,3)
# for item in abc:
#     print(item)



   #tupple unpacking
# abc = [(1,2), (3,4), (5,6), (7,8)]
# for (a,b) in abc:       # for a,b in abc:       -> would also work
#     print(a)
#     print (b)           #o/p:- 1,2,3,4,5,6,7,8



# abc = [(1,2,3), (4,5,6), (7,8,9)]
# for a,b,c in abc:       # for a,b in abc:       -> would also work
#     print(a)
#     print (b)           
#     print (c)   #o/p:- 1,2,3,4,5,6,7,8,9




#for loop in dictionary

     #by default it prints keys-
# abc = {'k1':1, 'k2':2, 'k3':3}
# for item in abc:
#     print(item)  #o/p:- k1,k2,k3

     
  


    #key unpacking-
# abc = {'k1':10, 'k2':20, 'k3':30}
# for key,value in abc:
#     print(value)  #o/p:- 1,2,3 

# abc = {'k1':1, 'k2':2, 'k3':3}
# for key,value in abc:
#     print(key)  #o/p:- k,k,k  

"""Iterating directly over a dict (for x in abc) yields keys only: 'k1', 'k2', 'k3'.
But you wrote for key, value in abc: — this tries to unpack each key into two variables.
Each key is a string (e.g., 'k1'). When Python unpacks a string into two variables, it splits it into its first two characters:

'k1' → 'k', '1'
'k2' → 'k', '2'
'k3' → 'k', '3'

So key becomes 'k' each time, hence the output: k, k, k.
(If a key weren’t exactly 2 characters long, you’d get a ValueError: too many/few values to unpack.)

"""

 #Correct way to get key–value pairs: use .items()

# abc = {'k1':1, 'k2':2, 'k3':3} 
# for key, value in abc.items():
#     print(key, value)   # k1 1, k2 2, k3 


# for item in abc.items():
#     print(item)  #o/p:- ('k1', 1) ('k2', 2) ('k3', 3)




  #for seperately accessing the values-
# abc = {'k1':10, 'k2':20, 'k3':30}
# for value in abc.values():
#     print(value)  #o/p:- 10,20,30      



   #If you want k1, k2, k3, iterate the dict (or use .keys()):
# abc = {'k1':10, 'k2':20, 'k3':30}   
# for key in abc:          # or: for key in abc.keys():
#     print(key)           # k1, k2, k3



"""
Quick reference

abc = {'k1': 1, 'k2': 2, 'k3': 3}

# Keys
for key in abc:              # or abc.keys()
    print(key)               # k1, k2, k3

# Values
for value in abc.values():
    print(value)             # 1, 2, 3

# Key–Value pairs
for key, value in abc.items():
    print(key, value)        # k1 1, k2 2, k3 3
"""




  #interview question-
# Print following if age > 30
# {person} is from {country}


a = {  'tom': {  'age': 50,  'country': 'USA'  },  'sahil': {  'age': 26,  'country': 'INDIA'  },  'jack': {  'age': 28,  'country': 'CHINA'  },  'leo': {  'age': 35,  'country': 'SPAIN'  }, }

for key, value in a.items():
    if value['age']>30:
       print(f'{key} is from {value['country']}') 







"""
NOTE-
although in these examples o/p was coming in ordered sequence because these are very small,
but dictionaries are unordered it is not mandatory that we will get first what we inserted first

but From Python 3.7+, dictionaries preserve insertion order, so iteration will follow the order you created the dict.
"""
