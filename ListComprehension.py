# mystring ='Aditay'
# mylist =[]

# for letter in mystring:
#     mylist.append(letter)

# print(mylist)               #o/p:- ['A', 'd', 'i', 't', 'a', 'y']



            # short way to do it-
# mystring ='Aditay'
# mylist =[letter for letter in mystring]
# print(mylist)                 #o/p:- ['A', 'd', 'i', 't', 'a', 'y']


# mylist =[x for x in 'kannu']
# print(mylist)                 #o/p:- ['k', 'a', 'n', 'n', 'u']


# mylist =[num for num in range(0,10)]
# print(mylist)                 #o/p:-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mylist =[num**2 for num in range(0,10)]
# print(mylist)                 #o/p:-[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# mylist =[num for num in range(0,10) if num%2==0]
# print(mylist)                 #o/p:-[0, 2, 4, 6, 8]

# celcius = [5,34,20,12,8]
# fahrenheit = [((9/5)*temp +32) for temp in celcius ]
# print(fahrenheit)             #o/p:-[41.0, 93.2, 68.0, 53.6, 46.4]


# mylist=[]
# for x in [1,2,3]:
#     for y in [10,100,1000]:
#         mylist.append(x*y)
# print(mylist)                #o/p:-  [10, 100, 1000, 20, 200, 2000, 30, 300, 3000]



# mylist=[x*y for x in [1,2,3] for y in [10,100,1000]]
# print(mylist)                #o/p:-  [10, 100, 1000, 20, 200, 2000, 30, 300, 3000]



  # my experiments-
# a= [5,6,7,8] 
# b= [1,2,3,4]

# my_list = [x**y for x in a for y in b]
# print(my_list)          #o/p:- [5, 25, 125, 625, 6, 36, 216, 1296, 7, 49, 343, 2401, 8, 64, 512, 4096]


# table of any number
x = int(input('Enter a number'))
a= [1,2,3,4,5,6,7,8,9,10]
my_list= [x*multiplier for multiplier in a]
print(my_list)



