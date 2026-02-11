# # temp = 10
# # print(temp)

# def add(a, b):
#     return a+b
# x=input("enter 1st number")  # i/p:-5
# y=input("enter 2nd number")  # i/p:-4

# print(add(x,y))  #o/p:- 54

# def add(a, b):
#     return a+b
# x=int(input("enter 1st number"))  # i/p:-5
# y=int(input("enter 2nd number"))  # i/p:-4

# print(add(x,y))  #o/p:- 9
    
# x, y = 20, 10
# y, x = x, y
# print(x, y)


# a = [1,2,3,5,6,7,8]
# print(a[::-1])
#a.reverse()
#print(a)
# t = (1,2,3)
# x = list(reversed(t))
# print(x)
# m = {'a': 1, 'b':2}
# print(m['a'])
# a.sort(reverse=True)


# class Student:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.li = [id, id*id]
#     def __eq__(self, value):
#         return self.id == value.id
    
#     def __ne__(self, value):
#         return not self == value
    
#     # def isEqual(self, value):
#     #     return self.id == value.id
    
#     def __contains__(self, value):
#        return ''
    
#     def __mul__(self, value):
#         return "xyz"
    
#     def __str__(self):
#         return f"{self.id} - {self.name}"

# s1 = Student(2, "A")
# s2 = Student(10, "B")
# s3 = Student(5, "A")
# s1.isEqual()


# print(s1 == s3)
# print(4 in s1.li)
# print(40 in s1)
# print(s1 * s2)
# print(s1)

# print(25 ** 0.5)



# from platform import python_version
# print(python_version())                #o/p:-    3.14.2
