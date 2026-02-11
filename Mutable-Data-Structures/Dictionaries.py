#Dictionaries are muttable unordered key value pair mapping for storing the objects, it can not be sorted
#in dictionary object is retrieved by key only, not like list where we can access object by location
#dictionary is mutable
# dict.keys()         dict.values()     dict.items()


my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key2'])

my_dict = {'oranges':10, 'apples':5.5}
print(my_dict['oranges'])

# dictionary can hold multiple data types

my_dict = {'k1':123, 'k2':[4,5,6], 'k3': {'k4':7, 'k5':8}}
print(my_dict['k3']) #o/p:- {'k4': 7, 'k5': 8}
print(my_dict['k3']['k4']) #o/p:- 7
print(my_dict['k2'][2]) #o/p:- 6
print(my_dict) #{'k1': 123, 'k2': [4, 5, 6], 'k3': {'k4': 7, 'k5': 8}}

#adding new key value pair in dictionary-
my_dict['k4']= 100.00
print(my_dict) #{'k1': 123, 'k2': [4, 5, 6], 'k3': {'k4': 7, 'k5': 8}, 'k4': 100.0}

#we can associate new value also-
my_dict['k4']= 99
print(my_dict) #{'k1': 123, 'k2': [4, 5, 6], 'k3': {'k4': 7, 'k5': 8}, 'k4': 99}
print(my_dict.keys()) #dict_keys(['k1', 'k2', 'k3', 'k4'])
print(my_dict.values()) #dict_values([123, [4, 5, 6], {'k4': 7, 'k5': 8}, 99])
print(my_dict.items()) #dict_items([('k1', 123), ('k2', [4, 5, 6]), ('k3', {'k4': 7, 'k5': 8}), ('k4', 99)])


# Keys can be any immutable type, such as:
# str (strings)
# int (integers)
# float (floats)
# tuple (as long as the tuple itself contains only immutable elements)
# frozenset

# Keys cannot be mutable types, like:
# list
# dictionary
# set


# Valid keys
my_dict = {
    "name": "Alice",
    42: "Answer",
    (1, 2): "Tuple key"
}

print(my_dict[42]) # o/p:- Answer

# Invalid key (will raise TypeError)
#my_dict[[1, 2]] = "List key"  # ❌ lists are mutable



#Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary but you would like ordering as well, check out the ordereddict object


