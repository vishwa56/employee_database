import json
import os
from datetime import datetime

DATA_FILE = "employees.json"

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def write_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)

def display_employees(employees):
    print("\nEmployee List:")
    for employee in employees:
        print(f"ID: {employee['id']}, Full Name: {employee['full_name']}, Age: {employee['age']}, Date of Birth: {employee['date_of_birth']}, Salary: {employee['salary']}, Department: {employee['department']}")

def filter_employees(criteria, value):
    employees = read_data()
    filtered_employees = [employee for employee in employees if str(employee.get(criteria, '')) == value]
    display_employees(filtered_employees)

def search_employee(search_query):
    employees = read_data()
    filtered_employees = [employee for employee in employees if search_query.lower() in employee.get('full_name', '').lower()]
    display_employees(filtered_employees)

def update_employee(employee_id):
    employees = read_data()
    employee = next((e for e in employees if e["id"] == employee_id), None)

    if employee:
        print(f"\nUpdating Employee with ID {employee_id}")
        employee["full_name"] = input("Enter new full name: ")
        employee["age"] = int(input("Enter new age: "))
        employee["date_of_birth"] = input("Enter new date of birth (YYYY-MM-DD): ")
        employee["salary"] = int(input("Enter new salary: "))
        employee["department"] = input("Enter new department: ")

        write_data(employees)
        print("Employee updated successfully!")
    else:
        print("Employee not found.")

def delete_employee(employee_id):
    employees = read_data()
    employees = [e for e in employees if e["id"] != employee_id]

    write_data(employees)
    print("Employee deleted successfully!")

def add_employee():
    employees = read_data()

    new_employee = {
        "id": len(employees) + 1,
        "full_name": input("Enter full name: "),
        "age": int(input("Enter age: ")),
        "date_of_birth": input("Enter date of birth (YYYY-MM-DD): "),
        "salary": int(input("Enter salary: ")),
        "department": input("Enter department: ")
    }

    employees.append(new_employee)
    write_data(employees)
    print("Employee added successfully!")

def main():
    while True:
        print("\nEmployee Management Application")
        print("1. Show all Employees")
        print("2. Filter Employees")
        print("3. Search for an Employee")
        print("4. Update an Employee's Record")
        print("5. Delete an Employee")
        print("6. Add Employee")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            employees = read_data()
            display_employees(employees)
        elif choice == '2':
            criteria = input("Enter criteria to filter (e.g., age, salary, department): ")
            value = input(f"Enter value for {criteria} to filter: ")
            filter_employees(criteria, value)
        elif choice == '3':
            search_query = input("Enter search query for employee: ")
            search_employee(search_query)
        elif choice == '4':
            employee_id = int(input("Enter the ID of the employee to update: "))
            update_employee(employee_id)
        elif choice == '5':
            employee_id = int(input("Enter the ID of the employee to delete: "))
            delete_employee(employee_id)
        elif choice == '6':
            add_employee()
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
