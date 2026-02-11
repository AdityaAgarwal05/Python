#Creating the generator-

# def create_cubes(n):  
#     mylist=[]
#     for i in range(n):  # it means- for i in range(0,n)
#         mylist.append(i**3)
#     return mylist    

# print(create_cubes(10))        #o/p:- [0,1, 8, 27, 64, 125, 216, 343, 512, 729]
# for x in create_cubes(10):
#     print(x)                   #o/p:- 0 1 8 27 64 125 216 343 512 729 



    #so to make our memory more utilised, we can avoid creating a list and storing it into the memory like this-

def create_cubes(n):  
    for i in range(n):  # it means- for i in range(0,n)   --> n not included
        yield i**3
 
print(create_cubes(10))        #o/p:-   <generator object create_cubes at 0x000001E1A5939490>

for x in create_cubes(10):
    print(x)                   #o/p:- 0 1 8 27 64 125 216 343 512 729            --> thus we can see that we can utilise the functionality withot using any memory

print(list(create_cubes(10)))     #o/p:-        [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]












        
