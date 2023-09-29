"""
    <Name: Kyle Andre L. Lim>
    <Schedule: M.W 9:00 AM - 10:30 AM>
    <EDP: 13953>
        create a file 'student.txt' read, write and update this file
        for the student list
        Create the student list with a menu provided below
        ---------- Student List --------------
        1. Add Student
        2. Find Student
        3. Delete Student
        4. Update Student
        5. Display All Student
        0. Quit/End
        --------------------------------------
        
        student:dict = {
            idno: '0001',
            lastname: 'alpha'
            firstname: 'bravo'
            course: 'bsit'
            level: '3'
        }
"""

from os import system

def displaymenu()->None: 
    system("cls")
    menuoption:tuple = (
        "--------------- MENU ----------------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All Student",
        "0. Quit/End",
        "--------------------------------------"
    )
    
    [print (menu) for menu in menuoption]
    
def AddName()->None:
    system("cls")
    students = open("student.txt", "a")
    
    idNumber = input("Enter ID NUMBER: ") 
    lastN = input("Enter last name: ") 
    firstN = input("Enter first name: ") 
    course = input("Enter student course: ") 
    level = input("Enter student level: ") 
    
    student:dict = {
        "idno: ": idNumber,
        "lastname: ": lastN,
        "firstname: ": firstN,
        "course: ": course,
        "level: ": level
    }
    
    students.write(f"{student.get('idno: ')},{student.get('lastname: ')},{student.get('firstname: ')},{student.get('course: ')},{student.get('level: ')}\n")
    students.close()
    
def FindName()->None:
    system("cls")
    students = "student.txt"

    name = input("Enter Student Name or ID: ")        

    with open(str(students), "r") as file:
        content = file.read()
        if name in content:
            print(f"{name} is found in the list of enrollees")
        else:
            print(f"{name} is NOT FOUND in the list of enrollees")    
    
def Delete()->None:
    
    system("cls")
    students = open("student.txt", "r")
    content = students.readlines()

    indexId = int(input("Enter index to delete: "))

    if 1 <= indexId <= len(content):
        deleted_student = content.pop(indexId - 1)
        with open("student.txt", "w") as deleteFile:
            deleteFile.writelines(content)
            print(f"{deleted_student.strip()} is deleted from the list")
    else:
        print("Invalid index. No student deleted.")
    # system("cls")
    # students = "student.txt"
    
    # indexId = int(input("Enter index to delete: "))
    
    # with open(str(students), "r") as file:   
    #     content = file.readlines()
        
    #     index = 1 # file index pointer
        
    #     with open(str(students), "w") as deleteFile:
    #         for line in content:
    #             if index != indexId:
    #                 deleteFile.write(line)
    #             index += 1
    #         print(f"{id} is deleted from the list")

def Update()->None:
    system("cls")
    students = open("student.txt", "r")
    content = students.readlines()

    StudentId = int(input("Enter the index of the list that you want to update: "))

    if 1 <= StudentId <= len(content):
        idNumber = input("Enter ID NUMBER: ")
        lastN = input("Enter last name: ")
        firstN = input("Enter first name: ")
        course = input("Enter student course: ")
        level = input("Enter student level: ")

        updated_student = f"{idNumber},{lastN},{firstN},{course},{level}\n"
        content[StudentId - 1] = updated_student

        with open("student.txt", "w") as f:
            f.writelines(content)
            print("Student updated successfully.")
    else:
        print("Invalid index. No student updated.")
    
def Display()->None: 
    system("cls")
    students = open("student.txt", "r")
    contentFile = students.read()
    print(contentFile)

def Exit()->None: 
    system("cls")
    print("Program has been terminated!")

def main()-> None: 
    system("cls")
    menuoption = {
        1:AddName,
        2:FindName,
        3:Delete,
        4:Update,
        5:Display,
        0:Exit
    }
    
    option:int = -1
    
    while option != 0:
        displaymenu()
        option = int(input("Enter option (0..5): "))
        menuoption.get(option)()
        input("Press any key to continue...")
    
if __name__ == "__main__":
    main()