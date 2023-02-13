'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open('employee_data.csv', 'r')
emp_files = csv.reader(infile, delimiter= ',')
next(emp_files)


#create an empty dictionary
new_dict = {}


#use a loop to iterate through the csv file
for row in range (emp_files):
    first_name = emp_files('First Name'[2])
    last_name = emp_files('Last Name'[3])
    cur_pay = emp_files('Salary'[6])
    new_pay = cur_pay * 1.10

    #check if the employee fits the search criteria
    if new_dict ['Title']['CSR'] in emp_files:
        new_dict = emp_files['Title'][row][new_pay]

        
print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
if new_dict ['Title']['CSR'] in emp_files:
    print(new_dict)



          
        

        
    
