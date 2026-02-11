#dunder methods can be used to apply built in operations like len and print on user created objects



                 #print and len works on lists-
# mylist=[1,2,3,4]
# print(len(mylist))      #o/p:- 4
# print(mylist)           #o/p:- [1, 2, 3, 4]


                #but print and len does not work on user defined objects-
# class sample():
#     pass

# mysample=sample()
# #print(len(mysample))     #o/p:- TypeError: object of type 'sample' has no len()
# print(mysample)           #o/p:- <__main__.sample object at 0x000001EF169A86E0>



# class Book():
#     def __init__(self,title,author,pages):
#      self.title=title
#      self.author=author
#      self.pages=pages


# b= Book('python book', 'adi', 500)
# print(b)   #o/p:- <__main__.Book object at 0x000002B0439F86E0>          ---> this is because print fn prints the string representation of the objecj
# print(str(b)) #o/p:- <__main__.Book object at 0x000002B0439F86E0>


               





                # print fn internally uses __str__ dunder method, so here is how we can make the print fn work for our object-

# class Book():
#     def __init__(self,title,author,pages):
#      self.title=title
#      self.author=author
#      self.pages=pages

#     def __str__(self):
#        return f"{self.title} by {self.author}" 


# b= Book('python book', 'adi', 500)
# print(b)      #o/p:- python book by adi
# print(str(b)) #o/p:- python book by adi


                #similarly we can make 'len' fn work, len fn uses __len__ dunder method internally-

# class Book():
#     def __init__(self,title,author,pages):
#      self.title=title
#      self.author=author
#      self.pages=pages

#     def __len__(self):
#        return self.pages 


# b= Book('python book', 'adi', 500)
# print(len(b))    #o/p:- 500

                         



                           # 'del' keyword is used to delete the object

class Book():
    def __init__(self,title,author,pages):
     self.title=title
     self.author=author
     self.pages=pages

    def __str__(self):
       return f"{self.title} by {self.author}" 
    
    def __del__(self):
       print("A book object has been deleted") 


b= Book('python book', 'adi', 500)
print(b)      #o/p:- python book by adi

del b         #o/p:-A book object has been deleted
print(b)      #o/p:- NameError: name 'b' is not defined



 
