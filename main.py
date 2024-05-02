import datetime
class Student:
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country_of_birth):
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__sex = sex
        self.__country_of_birth = country_of_birth

    def get_student_number(self):
        return self.__student_number

    def set_student_number(self, student_number):
        self.__student_number = student_number

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex

    def get_country_of_birth(self):
        return self.__country_of_birth

    def set_country_of_birth(self, country_of_birth):
        self.__country_of_birth = country_of_birth

    def get_age(self):
        today = datetime.date.today()
        birth_date = self.__date_of_birth
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

def save_students_to_file(student_array):
    with open("studentlist.txt", "w") as file:
        for student in student_array:
            file.write(f"{student.get_student_number()},{student.get_first_name()},{student.get_last_name()},"
                       f"{student.get_date_of_birth()},{student.get_sex()},{student.get_country_of_birth()}\n")

def read_students_from_file():
    student_array = []
    try:
        with open("studentlist.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                student = Student(int(data[0]), data[1], data[2], datetime.datetime.strptime(data[3], "%d-%m-%Y").date(), data[4], data[5])
                student_array.append(student)
    except FileNotFoundError:
        pass
    return student_array

def add_student(student_array):
    if len(student_array) >= 100:
        print("CANNOT ADD MORE STUDENTS. THE STUDENT LIST IS FULL.")
    else:
        try:
            student_number = int(input("Enter the student number: "))
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            date_of_birth = datetime.datetime.strptime(input("Enter the date of birth (DD-MM-YYYY): "), "%d-%m-%Y").date()
            sex = input("Enter the sex: ")
            country_of_birth = input("Enter the country of birth: ")
            new_student = Student(student_number, first_name, last_name, date_of_birth, sex, country_of_birth)
            student_array.append(new_student)
            print("Student added successfully.")
        except ValueError:
            print("Invalid input. Please try again.")

def find_student_by_number(student_array, student_number):
    for student in student_array:
        if student.get_student_number() == student_number:
            return student
    return None

def show_all_students(student_array):
    for student in student_array:
        age = student.get_age()
        print(f"Student Number: {student.get_student_number()}, Name: {student.get_first_name()} "
              f"{student.get_last_name()}, Age: {age}, Sex: {student.get_sex()}, "
              f"Country of Birth: {student.get_country_of_birth()}")

def show_students_by_birth_year(student_array, year):
    for student in student_array:
        if student.get_date_of_birth().year == year:
            age = student.get_age()
            print(f"Student Number: {student.get_student_number()}, Name: {student.get_first_name()} "
                  f"{student.get_last_name()}, Age: {age}, Sex: {student.get_sex()}, "
                  f"Country of Birth: {student.get_country_of_birth()}")

def modify_student_info(student_array, student_number):
    student = find_student_by_number(student_array, student_number)
    if student:
        print("1- First Name\n2- Last Name\n3- Date of Birth\n4- Sex\n5- Country of Birth")
        choice = int(input("Select the information you want to change [1-5]:  "))
        if choice == 1:
            new_value = input("Enter the new First Name: ")
            student.set_first_name(new_value)
        elif choice == 2:
            new_value = input("Enter the new Last Name: ")
            student.set_last_name(new_value)
        elif choice == 3:
            new_value = datetime.datetime.strptime(input("Enter the new Date of Birth (DD-MM-YYYY): "), "%d-%m-%Y").date()
            student.set_date_of_birth(new_value)
        elif choice == 4:
            new_value = input("Enter the new Sex: ")
            student.set_sex(new_value)
        elif choice == 5:
            new_value = input("Enter the new Country of Birth: ")
            student.set_country_of_birth(new_value)
        else:
            print("Invalid choice.")
            return
        print("Student information updated successfully.")
    else:
        print("Student not found.")

def delete_student_by_number(student_array, student_number):
    student = find_student_by_number(student_array, student_number)
    if student:
        student_array.remove(student)
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def main():
    student_array = read_students_from_file()

    while True:
        print("\nMenu:")
        print("1- Save students info to file")
        print("2- read students info from file")
        print("3- Add a new student")
        print("4- Find a student by student number and show all information")
        print("5- Show all students")
        print("6- Show all students born in a given year")
        print("7- Modify a student record")
        print("8- Delete a student by student number")
        print("9- Quit")

        choice = int(input("Enter a number between [1-9]: "))
        if choice == 1:
            save_students_to_file(student_array)
            print("Student data saved to file.")
        elif choice == 2:
            student_array = read_students_from_file()
            print("Student data loaded from file.")
        elif choice == 3:
            add_student(student_array)
        elif choice == 4:
            student_number = int(input("Enter the student number to search for: "))
            student = find_student_by_number(student_array, student_number)
            if student:
                age = student.get_age()
                print(f"Student Number: {student.get_student_number()}, First Name: {student.get_first_name()}, "
                      f"Last Name: {student.get_last_name()}, Age: {age}, Sex: {student.get_sex()}, "
                      f"Country of Birth: {student.get_country_of_birth()}")
            else:
                print("Student not found.")
        elif choice == 5:
            show_all_students(student_array)
        elif choice == 6:
            year = int(input("Enter the birth year to search for: "))
            show_students_by_birth_year(student_array, year)
        elif choice == 7:
            student_number = int(input("Enter the student number to modify the information: "))
            modify_student_info(student_array, student_number)
        elif choice == 8:
            student_number = int(input("Enter the student number to delete the information: "))
            delete_student_by_number(student_array, student_number)
        elif choice == 9:
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
