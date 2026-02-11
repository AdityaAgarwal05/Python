import csv
data = open('csvfiles\sample_data.csv', encoding='utf-8')    #since emails have '@' symbol, so it needs utf-8 to get recognised
csv_data = csv.reader(data)
datalines=list(csv_data)
print(datalines)         #o/p is a list of lists, will print entire csv as list, each row as a list into a list




#print(datalines[0])  #o/p:- ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_adds', 'city']    ---> columns name 
#to check the number of rows in csv file-
#print(len(datalines))                     #o/p:- 9

# for line in datalines[:5]:
#     print(line)                #o/p:- ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_adds', 'city']
#                                #      ['1', 'Aditya', 'Agarwal', 'aditya.agarwal@example.com', 'Male', '192.168.1.1', 'Navi Mumbai']
#                                #      ['2', 'Aditi', 'Pawar', 'aditi.pawar@example.com', 'Female', '192.168.1.2', 'Mumbai']       
#                                #      ['3', 'Helen', 'Joseph', 'helen.joseph@example.com', 'Female', '192.168.1.3', 'Pune']       
#                                #      ['4', 'Ayush', 'Gahlot', 'ayush.gahlot@example.com', 'Male', '192.168.1.4', 'Delhi']



#let say you want to extract the email of ayush-
#print(datalines[4][3])           #o/p:- ayush.gahlot@example.com

#let say you want to extract all the emails-
# for item in datalines:
#     print(item[3])

#let say you want to extract only initial 5 persons emails-
# for item in datalines[:6]:  # datalines[1:6]  --> yh bhi same hi kaam krta, since first row has "Email"
#     print(item[3])    



# as first name and last name are seperated, let say you want full name-
# full_names=[]
# for item in datalines[1:]:
#     full_names.append(item[1]+ ' '+item[2] )
# print(full_names)                              #o/p:- ['Aditya Agarwal', 'Aditi Pawar', 'Helen Joseph', 'Ayush Gahlot', 'Nikhil Rathore', 'Nehal Jain', 'Divyansh Sharma', 'Nishant Dhupia']











                            #writing to a csv-
#let say you want to create a file named as "to_save_file.csv"  or you want to overwrite a file that is named as  "to_save_file.csv"   

# file_to_output = open('to_save_file.csv', mode='w', newline='')
# csv_writer = csv.writer(file_to_output, delimiter=',')       
# #let say you want to write a single row-
# csv_writer.writerow(['a','b','c'])           
# #or you can add multiple rows-
# csv_writer.writerows([['1','2','3'],['d','e','f'],['4','5','6']])   

# run here, and you will see that 'to_save_file.csv' has been generated in this folder, having this content-
'''
a,b,c
1,2,3
d,e,f
4,5,6

'''

# file_to_output.close()



# #now let say you want to append something in this file-
# f = open('to_save_file.csv', mode='a', newline='')
# csv_writer = csv.writer(f, delimiter=',') 
# #let say you want to append a single row-
# csv_writer.writerow(['g','h','i']) 
# #or you can add multiple rows-
# csv_writer.writerows([['7','8','9'],['j','k','l'],['10','11','12']])  

''' 
a,b,c
1,2,3
d,e,f
4,5,6
g,h,i
7,8,9
j,k,l
10,11,12

'''

# f.close()


