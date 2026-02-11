#for the files which are located in the same folder 

""" In write mode (w), the file is opened for writing, and any new data written to the file will overwrite 
the existing content. This is useful when you want to create a new file or replace the entire content
of an existing file. """

"""In contrast, append mode (a) is used to add new data to the end of the file without overwriting the 
existing content. This is ideal for maintaining a log or a list of tasks where you want to add new
entries without losing the previous ones."""

#my_file = open('sample.txt')
# print(my_file.read()) #o.p:- Hello, myself aditya, i am a software engineer
# print(my_file.read())  #o/p:- ''   --> because curser went at the end
# my_file.seek(0)  # to reset the file
# print(my_file.read())  #o.p:- Hello, myself aditya, i am a software engineer
# print(my_file.read())  #o/p:- ''   --> because curser went at the end
# my_file.seek(0)  # to reset the file
# print(my_file.read())  #o.p:- Hello, myself aditya, i am a software engineer

# print(my_file.readlines() ) #each line as a sepearate object in the list

# my_file.close()  #best to do at the end to prevent errors, like while deleting it is saying that "python is still using this file"

                

                      #new way to access and open the files-

# with open ('sample.txt') as my_file:
#     contents=my_file.read()

# print(contents)    #o.p:- Hello, myself aditya, i am a software engineer



                       #for read only-

# with open ('sample.txt', mode='r') as f:  
#     print(f.read())  #o/p:- Hello, myself aditya, i am a software engineer

      

                       #append-will add more lines into the file-
                       
# with open ('sample.txt', mode='a') as f: 
#     f.write('i am from jaipur')       
# with open ('sample.txt', mode='r') as f:  
#      print(f.read())  #o/p:- Hello, myself aditya, i am a software engineer i am from jaipur    




         #write mode- will overwrite or create new


          #write mode- overwrite

# with open ('sample.txt', mode='w') as f:  
#     f.write('i created this file')
# with open ('sample.txt', mode='r') as f:  
#      print(f.read())  #o/p:- i created this file


         #write mode- create new

# with open ('sample2.txt', mode='w') as f:  
#     f.write('i have created this file')
# with open ('sample2.txt', mode='r') as f:  
#      print(f.read())  #o/p:- sample2.txt has been created in this folder having the content - i have created this file

# with open ('sample3.txt', mode='w') as f:  
#     f.write('i have created this file also')
# with open ('sample3.txt', mode='r') as f:  
#      print(f.read())  #o/p:- sample3.txt has been created in this folder having the content - i have created this file also

