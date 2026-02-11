#Use of next() fn


# def simple_gen():
#     for x in range(3):
#         yield x

# for num in simple_gen():
#     print(num)

# '''
# o/p:-
# 0
# 1
# 2
# '''

# g=simple_gen()
# print(next(g))     #o/p:- 0
# print(next(g))     #o/p:- 1
# print(next(g))     #o/p:- 2
# print(next(g))     #o/p:- StopIteration             ---> because 3 was limit here

#Note:- while iterating over a generator, for loop is also using the next() internally, and when it encounters the error, it stops   





                    #iter fn - it is used to convert the objects that are iterable into the iterators themselves-

s='hello'

# for letter in s:
#     print(letter)


#print(next(s))  #o/p:- TypeError: 'str' object is not an iterator


#so now to make this string a generator and iterable-
s_iterable= iter(s)
print(next(s_iterable))   #o/p:- h
print(next(s_iterable))   #o/p:- e
print(next(s_iterable))   #o/p:- l
print(next(s_iterable))   #o/p:- l
print(next(s_iterable))   #o/p:- o

print(s)                  #o/p:-     hello
