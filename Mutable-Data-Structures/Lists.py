#Lists are mutable ordred sequence that can hold variety of object types
#Lists can be nested
#Lists supports indexing and slicing
#Lists are mutable

# len(), concatenation(+),  .append(),  .extend(), .pop(),  .pop(position),  .sort(), sorted(), .reverse(), Nested lists 
               
                        #len() fn-
# my_list =[1, 'adi', 0.5]
# print(len(my_list))


# my_list =['one', 'two', 'three']
# print(my_list[0])
# print(my_list[1:]) #o/p:- ['two', 'three']


                 #Concatenation of lists-
# another_list= ['four', 'five']
# print(my_list+another_list)   #['one', 'two', 'three', 'four', 'five']
  
 
                  #list is mutable
# my_list[0]='six'
# print(my_list) #o/p:- ['six', 'two', 'three']    --> since list is mutable

                  #append()  adds at last
# my_list.append('seven')
# print(my_list) #o/p:- ['six', 'two', 'three', 'seven']


# my_list=['a','b','c']
# my_list2=[1,2,3]
#append-
# my_list.append(my_list2)    
# print(my_list)               # o/p:- ['a','b','c',[1,2,3]]

                       
                    #extend-
# my_list.extend(my_list2)    
# print(my_list)                 # o/p:- ['a','b','c',1,2,3]

                  


                      #.pop() removes from the end-
# my_list = ['six', 'two', 'three', 'seven']
# my_list.pop()
# print(my_list) #o/p:- ['six', 'two', 'three']

   #it returns popped item-
# popped_item= my_list.pop()
# print(popped_item) #three

  #removing from specific position-
# another_list= ['four', 'five']
# another_list.pop(1)  # by default this index in pop() fn is -1
# print(another_list) #o/p:-['four']  

                #.sort() fn --> sorts in place

# a = ['h','s','y','a','b']
# a.sort()
# print(a) #o/p:- ['a', 'b', 'h', 's', 'y']

# b = [10,4,1,7,5]
# my_sorted_list = b.sort()
# print(my_sorted_list)  #o/p:- none       --> because sort does not return, it sorts in place
# type(my_sorted_list)   #o/p:- none

# c = [10,4,1,7,5]
# c.sort()
# d=c
# print(d) #o/p:- [1, 4, 5, 7, 10]

                        # soted() fn  --> but it is not in place, it returns a new sorted list

# my_list=[5,3,8,19,6,3,2]
# print(sorted(my_list)) #o/p:-[2, 3, 3, 5, 6, 8, 19]
# print(my_list)         #o/p:-[5,3,8,19,6,3,2]


                        # .reverse() fn-
# e = [10,4,1,7,5]
# f = e.reverse()
# print(e)  #o/p:- [5, 7, 1, 4, 10]
# print(f)  #o/p:- none             -------> it reverses in place, and does not return a new reversed list



                       #Nested lists-

# a = [1,2,[3,4]]
# print(a[2][0]) #o/p:-3
# print(a[2][1]) #o/p:-4


# my_list = [0]*3
# print(my_list) #[0, 0, 0]


# mystring ='Aditay'
# mylist =[]

# for letter in mystring:
#     mylist.append(letter)

# print(mylist)               #o/p:- ['A', 'd', 'i', 't', 'a', 'y']


#abc= [1,2,3]
# print(*abc)                 #o/p:-  1 2 3
