#import library to make table
from tabulate import tabulate

#create empty lists
name = []
ID_number = []
sold_property = []
commission_rate = 500



#input number of employee
employee_num = int(input("\nEnter number of employee: "))

#This function collects the input data for employee names, ID numbers, and sales, 
#iterating over the specified range of employees, and returns the final iteration variable "i".
def input_employee_data():
    
    for i in range(0, employee_num):
        name.append(input("\nEnter emloyee name: "))
        ID_number.append(int(input("Enter ID number: ")))
        sold_property.append(int(input("Enter sold property: ")))
    return i 

#Calculate  the commission for each sold property using a commission rate
def calculateCommission(sold_property):
    return [x * commission_rate for x in sold_property] 
    



def sortList():
    #sort the list of employees by sold property using the bubble algorithm

    sort = len(sold_property)
    for i in range(sort - 1):
        for j in range(sort - i -1):
            if sold_property[j] < sold_property[j+1]:
                sold_property[j],sold_property[j + 1] = sold_property[j + 1], sold_property[j] 
                name[j], name[j+1] = name[j+1], name[j]
                ID_number[j], ID_number[j+1] = ID_number[j+1], ID_number[j]

    
#This function sorts the data and tabulates employee details with specified headers using the "tabulate" function.
def listt():
    sortList()   
    data = list(zip(name, ID_number, sold_property))
    headers  =["Employee name", "ID number" , "Sold properties"]
    print(tabulate(data, headers=headers))

    
#Calculate sales commission for each employee with 2 decimal places
def assessEarnings ():
    commission = calculateCommission(sold_property)
    
    data = list(zip(name, ID_number, sold_property,commission) )
    headers  =["Employee name", "ID number" , "Sold properties", "Commissions"]
    print(tabulate(data, headers=headers, floatfmt=".2f"))
    
    

#Calculate total sales commission for the week with 2 decimal places
def weeklyCommission():
    commission = calculateCommission(sold_property)
    total_commission = sum(commission)
    print("\nTotal sales commission for a week: %.2f" % total_commission)
    

#Calculate total number of properties sold in the week
def totalProperties():
    total_num = sum(sold_property)
    print(f"\nThe total number of properties sold in the week: {total_num}")


#This function identifies the Employee of the Week by sorting and tabulating the top performer's data.
def weekAwardEmployee():
    sortList()
    data = [(name[0], ID_number[0], sold_property[0] )]
    header = ["Name", "ID Number", "Sold Property"]
    print("\nEmployee of the Week Award")
    print(tabulate(data, headers=header))


#This function calculates and awards a bonus to the Employee of the Week based on sales
def award():
    sortList()
    commission = calculateCommission(sold_property)
    maxNum = commission[0]
    bonus = (maxNum * 15)/100

    data = [(name[0], ID_number[0], sold_property[0], bonus )]
    header = ["Name", "ID Number", "Sold Property", "Bonus"]
    print("\nEmployee of the Week Award And Received Bonus\n")
    print(tabulate(data, headers=header))
    

#This function processes the user's menu choice (1-6) and calls the corresponding function
def menu(choice):
    if choice == "1":
        listt()
    elif choice == "2":
        assessEarnings()
    elif choice == "3":
        weeklyCommission()
    elif choice == "4":
        totalProperties()
    elif choice == "5":
        weekAwardEmployee()
    elif choice == "6":
        award()
    else:
        print("Invalid choice. Please enter a number from 1 to 6")
        
        
       
#This function displays a menu, processes the user's choice, and prompts for further use, 
#ensuring a valid response before repeating or exiting.
def options():
    print("""
1. List employee in order of the number of properties sold
2. Sales commission for each employee
3. Total sales commission for the week
4. The total number of properties sold in the week
5. Employee of the week award
6. Bonus amount received by the employee of the week.
    """)
    choice = input("Please chose one of these options: ") 
    menu(choice)
    

    use_again = input("\nWould you like to use menu again(Y/N)?: ")
    if use_again == "y" or use_again == "Y":
        options()
    elif use_again == "n" or use_again == "N":
        print("Thank you for using menu!")
    else:
        print("Invalid choice. Please try again")
        


#call inputt() function
input_employee_data()

#call options() function
options()