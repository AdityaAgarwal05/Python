# string formatting
# another way of injecting a variable into the string without using the concatenation


# 1st .format method-
print('hello {}, this is from {}'.format('Aditya', 'Kannu') )

# its another advantage is that we can place anything at any position-
print('the {} {} {}'.format('fox', 'quick', 'brown')) # o/p:- the fox quick brown
print('the {1} {2} {0}'.format('fox', 'quick', 'brown')) # o/p:- the quick brown fox
print('the {0} {0} {0}'.format('fox', 'quick', 'brown')) # o/p:- the fox fox fox
print('the {q} {b} {f}'.format(f='fox', q='quick', b='brown')) # o/p:- the quick brown fox

result=100/777
print (result) # o/p:- 0.1287001287001287
print('the result is {r}'.format(r=result)) # o/p:- the result is 0.1287001287001287
print('the result is {r:1.5f}'.format(r=result)) # o/p:- the result is 0.12870

# {value:width:precison f}
result=777/100
print (result) # o/p:- 7.77
print('the result is {r}'.format(r=result)) # o/p:- the result is 7.77
print('the result is {r:1.5f}'.format(r=result)) # o/p:- the result is 7.77000 




        #formatted strings(f strings)

result=100/777
print (result) # o/p:- 0.1287001287001287
print(f'the result is {result}') # o/p:- the result is 0.1287001287001287

q="quick"
b="brown"
f="fox"
print(f'the {q} {b} {f}') # o/p:- the quick brown fox
