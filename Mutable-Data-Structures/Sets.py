#unordered collection of unique elements


"""a set is a mutable data type in Python. 
This means you can modify the contents of a set after it has been created by adding or removing elements from it,
without creating a new set object. 
Key Characteristics of Python SetsMutable: 
You can use methods like add(), remove(), pop(), and update() to change the set's elements after creation.
"""

# .add() method
myset = set()
myset.add(5)
myset.add(5)
myset.add(5)
myset.add(4)
myset.add(4)

print(myset) #o/p:- {4, 5}


a =[1,1,1,2,2,3,3,4,4,4,4,5,5]
print(set(a)) #o/p:- {1, 2, 3, 4, 5},  --> although here it came in order, but sets are unordrerd

print(set('Mississippi')) #o/p:-{'s', 'p', 'M', 'i'}
