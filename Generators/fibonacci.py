def fib(n):
    a=1
    b=1
    result=[]
    for i in range(n):
        result.append(a)
        a,b = b, a+b
    return result    
    
    
for num in fib(10):
    print(num) 
'''
o/p:-
1
1
2
3
5
8
13
21
34
55
'''





#Fibonacci sequence using the generators-

def fib(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b, a+b
    
    
for num in fib(10):
    print(num) 
'''
o/p:-
1
1
2
3
5
8
13
21
34
55
'''


     
