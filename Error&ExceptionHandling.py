
# def add(num1, num2):
#     return num1+num2

# num1=20
# num2=input('provide 2nd number')

# add(num1,num2)        #o/p:- TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print('program executed')  #o/p:- due to above error, this block of code will not get executed


# try except else statement-

# try:
#     result = 10+20

# except:
#     print('hey, it looks like you are not adding compatible data types') 

# else:
#     print('add went well')
#     print(result)                      #o/p:- add went well
#                                        #        30




# try:
#     result = 10+'20'

# except:
#     print('hey, it looks like you are not adding compatible data types') 

# else:
#     print('add went well')
#     print(result)                      
#                                       #o/p:-hey, it looks like you are not adding compatible data types



#try except finally-

# try:
#     f= open('test_file', 'w')
#     f.write('hello this is an update')
# except TypeError:               #---->  # thus we can make our except block run on any specific type of error only
#     print('this is a type error')
# except OSError:                          #this error occurs when we try to open a file to which we dont have the permisssion
#     print('hey, you have an OSerror')
# except:                                  #for all other exceptions
#      print('i encountered an error')
# finally:
#     print('i always run')                  #o/p:-  i always run



# try:
#     f= open('test_file', 'r')
#     f.write('hello this is an update')
# except TypeError:                        # thus we can make our except block run on any specific type of error only
#     print('this is a type error')
# except OSError:                          #this error occurs when we try to open a file to which we dont have the permisssion
#     print('hey, you have have no permissions to write on this file')
# except:                                  #for all other exceptions
#     print('i encountered an error')    
# finally:
#     print('i always run')                 #o/p:- hey, you have have no permissions to write on this file
                                            #      i always run   




# try:
#     f= open('test_file', 'r')
#     f.write('hello this is an update')
# except:                                  #for all other exceptions
#     print('i encountered an error')    
# finally:
#     print('i always run')                  #o/p:- i encountered an error
#                                             #      i always run   







           # try except finally in a fn-



# def ask_for_int():
#       try:
#           num = int(input('please enter a number')) 
#       except:
#           print("whoops! that is not a number")     
#       finally:
#           print('this is the end of program')       

# ask_for_int()            #i/p:- 4
#                          #o/p:- this is the end of program


# def ask_for_int():
#       try:
#           num = int(input('please enter a number')) 
#       except:
#           print("whoops! that is not a number")     
#       finally:
#           print('this is the end of program')       

# ask_for_int()            #i/p:- adi
#                          #o/p:-  whoops! that is not a number
                           #       this is the end of program                         






          # making this program work like this that it will keep asking for a number unless it gets it
          # try except else finally -->
def ask_for_int():
    while True:
      try:
          num = int(input('please enter a number')) 
      except:
          print("whoops! that is not a number")
          #continue --> whether we apply it or not, program will work fine 
      else:
          print('yeah! that is correct')   
          break  
      finally:
          print('this is the end of program')  
               


ask_for_int()                   #i/p:- adi
                                #o/p:- whoops! that is not a number
                                #      this is the end of program
                                #      please enter a number
                                #i/p:- 5
                                #o/p:- yeah! that is correct
                                #      this is the end of program
                            
