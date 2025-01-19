#Introductory Interface, that shows the user options.
def Interface():
    print("-"*50)
    print("Employees:")
    print("-"*50)
    print("Select one of the following:")
    print("1) Add a new employee")
    print("2) Search for an employee")
    print("3) Remove an employee")
    print("4) Display employees")
    print("5) Exit")
    print("-"*50)

#displays all the employees in the database
def DisplayDB():
    try:
        with open("database.txt", "r") as myFile:
            for line in myFile:
                fields = line.strip().split(":")
                print(f"{fields[0]}:{fields[1]}:{fields[2]}:{fields[3]}")
    except FileNotFoundError:
        print("No employee database found.")
    print("-"*50)

#remove the employee with a specified user input ID
def RemoveEmployee():
    emp_id = input("Enter the Employee ID to remove: ")
    found = False
    updated_list = []
    with open("database.txt", "r") as myFile:
        for line in myFile:
            fields = line.strip().split(":")
            if fields[0] == emp_id:
                found = True
            else:
                updated_list.append(line.strip())
    
    if found:
        with open("database.txt", "w") as myFile:
            for record in updated_list:
                myFile.write(record + "\n")
        print("Employee removed successfully.")
        print("-"*50)
    else:
        print("The ID does not exist!")
        print("-"*50)

# Check if the input ID already exists in the database, if it does ask the user to retry another ID

def id_exists(emp_id):
    with open("database.txt", "r") as myFile:
        for line in myFile:
            fields = line.strip().split(":")
            if fields[0] == emp_id:
                return True
    return False

# Check if department exists in the department file

def department_exists(department):
    try:
        with open("department.txt", "r") as myFile:
            for line in myFile:
                if line.strip() == department:  
                    return True
        return False  # Department not found
    except FileNotFoundError:
        print("Department file not found.")
        return False
    
#search for the Input ID if it exists and then displays the employee 

def SearchID():
    emp_id = input("Enter the Employee ID to search: ")
    with open("database.txt", "r") as myFile:
        for line in myFile:
            fields = line.strip().split(":")
            if fields[0] == emp_id:
                print(f"Employee found: ID = {fields[0]}, Name = {fields[1]} {fields[2]}, Department = {fields[3]}")
                print("-"*50)
                return
    print("The ID does not exist!")
    print("-"*50)

#adds a new employee with a unique ID to the database

def AddNew():
    emp_id = input("Enter the Employee's ID: ").strip()
    id = emp_id.isnumeric()  #check to make sure the user enters numeric value only
    if not id:
        print("Wrong Input, Please enter a numeric value.")
        emp_id = input("Enter the Employee's ID: ").strip()

    if id_exists(emp_id):
        print("ID already exists! Employee not added. Please retry.")
        return

    while True:
        department = input("Enter the Employee's Department: ").strip()
        emp_department = department.isalpha() #check to make sure the user enters alphabets only
        if not emp_department:
            print("Wrong Input.")
            department = input("Enter the Employee's Department: ").strip()
            continue

#Makes sure user enters a valid department from the department.txt file.
        if department_exists(department):
            break
        print("Department does not exist. Please retry.")

    firstname = input("Enter the Employee's First Name: ").strip()
    emp_Firstname = firstname.isalpha()  #check to make sure the user enters alphabets only

    if not emp_Firstname:    
        print("Wrong Input.")
        firstname = input("Enter the Employee's First Name: ").strip()

    lastname = input("Enter the Employee's Last Name: ").strip()
    emp_Lastname = lastname.isalpha()   #check to make sure the user enters alphabets only
    if not emp_Lastname:
        print("Wrong Input.")
        lastname = input("Enter the Employee's Last Name: ").strip()

    with open("database.txt", "a") as outfile:
        outfile.write(f"{emp_id}:{firstname}:{lastname}:{department}\n")
    #writes to the file in the format above.

    print("Employee added successfully.")
    print("-"*50)

#loop to continue the Database running
def Continue():
    while True:
        val = input("Enter your value: ")
        if val == "1":
            AddNew()
        elif val == "2":
            SearchID()
        elif val == "3":
            RemoveEmployee()
        elif val == "4":
            DisplayDB()
        elif val == "5":
            DisplayDB()
            print("Exited!!")
            break #exit the loop once 5 has been entered.
        else:
            print("Invalid choice. Please try again.Enter numbers in the range (1 - 5)") #forces users to enter numbers in the range(1-5)
