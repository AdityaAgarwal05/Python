#strings are immutable ordered sequences that means we can use indexing and slicing to get its subsections
# .len() , .upper() , .lower() , .split()       ---> important methods
# string formatting 



# a='my name is aditya'
# print(a)

# a="I'm going on a walk" 
# print(a)

# print("Hello\nmy\nname\nis\naditya")

# print("Hello\tmy\tname\tis\taditya")

# print(len("a b c"))   #o/p: 5

#indexing for getting a single character and slicing to get a sub section

#indexing-
# a="kannu"
# print(a[0],a[1],a[2],a[3],a[4])
# print(a[0],a[-1],a[-2],a[-3],a[-4])


# a="my name is aditya"
# print(a[11:])    #o/p:- aditya
# print(a[:1])     #o/p:- m
# print(a[:2])     #o/p:- my        --> since "uptil" not included
# print(a[3:7])    #o/p:- name
# print(a[:])      #o/p:- my name is aditya
# print(a[::])     #o/p:- my name is aditya
# print(a[::2])    #o/p:- m aei dta            -->take the entire string a but with a step of 2.
# print(a[::-1])    #o/p:- aytida si eman ym

# print("Hello World"[8])  #o/p:- r



# print('tinker'[1:4])      #o/p:- ink
