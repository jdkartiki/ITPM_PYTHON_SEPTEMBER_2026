from abc import ABC, abstractmethod

# ============================================================
# ABSTRACT BASE CLASS
# ============================================================

class Employee(ABC):

    total_employees = 0

    def __init__(self, employee_id, name, email, department, basic_salary):

        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department

        # Encapsulation
        self.__basic_salary = basic_salary

        Employee.total_employees += 1

    # ========================================================
    # GETTER
    # ========================================================

    @property
    def salary(self):
        return self.__basic_salary

    # ========================================================
    # SETTER
    # ========================================================

    @salary.setter
    def salary(self, value):

        if value > 0:
            self.__basic_salary = value
        else:
            print("Salary must be greater than 0.")

    # ========================================================
    # ABSTRACT METHOD
    # ========================================================

    @abstractmethod
    def calculate_salary(self):
        pass

    # ========================================================
    # COMMON METHOD
    # ========================================================

    def display_employee(self):

        print("\n----------------------------------------")
        print("Employee ID   :", self.employee_id)
        print("Name          :", self.name)
        print("Email         :", self.email)
        print("Department    :", self.department)
        print("Employee Type :", self.__class__.__name__)
        print("Basic Salary  :", self.salary)
        print("Final Salary  :", self.calculate_salary())
        print("----------------------------------------")

    # ========================================================
    # STATIC METHOD
    # ========================================================

    @staticmethod
    def validate_employee_id(employee_id):

        if employee_id.startswith("EMP") and employee_id[3:].isdigit():
            return True

        return False

    @staticmethod
    def validate_email(email):

        if "@" in email and "." in email:
            return True

        return False


# ============================================================
# FULL TIME EMPLOYEE
# ============================================================

class FullTimeEmployee(Employee):

    def __init__(
        self,
        employee_id,
        name,
        email,
        department,
        basic_salary,
        allowance,
        annual_bonus
    ):

        super().__init__(
            employee_id,
            name,
            email,
            department,
            basic_salary
        )

        self.allowance = allowance
        self.annual_bonus = annual_bonus

    # Method Overriding

    def calculate_salary(self):

        return (
            self.salary
            + self.allowance
            + self.annual_bonus
        )


# ============================================================
# PART TIME EMPLOYEE
# ============================================================

class PartTimeEmployee(Employee):

    def __init__(
        self,
        employee_id,
        name,
        email,
        department,
        basic_salary,
        hours_worked,
        hourly_rate
    ):

        super().__init__(
            employee_id,
            name,
            email,
            department,
            basic_salary
        )

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    # Method Overriding

    def calculate_salary(self):

        return self.hours_worked * self.hourly_rate


# ============================================================
# INTERN
# ============================================================

class Intern(Employee):

    def __init__(
        self,
        employee_id,
        name,
        email,
        department,
        basic_salary,
        internship_duration,
        stipend
    ):

        super().__init__(
            employee_id,
            name,
            email,
            department,
            basic_salary
        )

        self.internship_duration = internship_duration
        self.stipend = stipend

    # Method Overriding

    def calculate_salary(self):

        return self.stipend


# ============================================================
# MANAGER
# ============================================================

class Manager(FullTimeEmployee):

    def __init__(
        self,
        employee_id,
        name,
        email,
        department,
        basic_salary,
        allowance,
        annual_bonus,
        team_size,
        management_bonus
    ):

        super().__init__(
            employee_id,
            name,
            email,
            department,
            basic_salary,
            allowance,
            annual_bonus
        )

        self.team_size = team_size
        self.management_bonus = management_bonus

    # Method Overriding

    def calculate_salary(self):

        return (
            self.salary
            + self.allowance
            + self.annual_bonus
            + self.management_bonus
        )


# ============================================================
# EMPLOYEE MANAGEMENT SYSTEM
# ============================================================

class EmployeeManagementSystem:

    def __init__(self):

        # Dictionary
        # employee_id -> employee object

        self.employees = {}

    # ========================================================
    # ADD EMPLOYEE
    # ========================================================

    def add_employee(self):

        print("\n========== ADD EMPLOYEE ==========")

        employee_id = input(
            "Enter Employee ID (EMP101): "
        ).upper()

        if employee_id in self.employees:

            print("Employee ID already exists.")

            return

        if not Employee.validate_employee_id(employee_id):

            print("Invalid Employee ID.")
            print("Example: EMP101")

            return

        name = input("Enter Name: ")

        email = input("Enter Email: ")

        if not Employee.validate_email(email):

            print("Invalid Email.")

            return

        department = input("Enter Department: ")

        print("\nSelect Employee Type")

        print("1. Full Time Employee")
        print("2. Part Time Employee")
        print("3. Intern")
        print("4. Manager")

        choice = input("Enter choice: ")

        # ----------------------------------------------------
        # FULL TIME EMPLOYEE
        # ----------------------------------------------------

        if choice == "1":

            basic_salary = float(
                input("Enter Basic Salary: ")
            )

            allowance = float(
                input("Enter Allowance: ")
            )

            annual_bonus = float(
                input("Enter Annual Bonus: ")
            )

            employee = FullTimeEmployee(
                employee_id,
                name,
                email,
                department,
                basic_salary,
                allowance,
                annual_bonus
            )

        # ----------------------------------------------------
        # PART TIME EMPLOYEE
        # ----------------------------------------------------

        elif choice == "2":

            basic_salary = float(
                input("Enter Basic Salary: ")
            )

            hours_worked = float(
                input("Enter Hours Worked: ")
            )

            hourly_rate = float(
                input("Enter Hourly Rate: ")
            )

            employee = PartTimeEmployee(
                employee_id,
                name,
                email,
                department,
                basic_salary,
                hours_worked,
                hourly_rate
            )

        # ----------------------------------------------------
        # INTERN
        # ----------------------------------------------------

        elif choice == "3":

            basic_salary = float(
                input("Enter Basic Salary: ")
            )

            internship_duration = int(
                input("Enter Internship Duration: ")
            )

            stipend = float(
                input("Enter Monthly Stipend: ")
            )

            employee = Intern(
                employee_id,
                name,
                email,
                department,
                basic_salary,
                internship_duration,
                stipend
            )

        # ----------------------------------------------------
        # MANAGER
        # ----------------------------------------------------

        elif choice == "4":

            basic_salary = float(
                input("Enter Basic Salary: ")
            )

            allowance = float(
                input("Enter Allowance: ")
            )

            annual_bonus = float(
                input("Enter Annual Bonus: ")
            )

            team_size = int(
                input("Enter Team Size: ")
            )

            management_bonus = float(
                input("Enter Management Bonus: ")
            )

            employee = Manager(
                employee_id,
                name,
                email,
                department,
                basic_salary,
                allowance,
                annual_bonus,
                team_size,
                management_bonus
            )

        else:

            print("Invalid employee type.")

            return

        self.employees[employee_id] = employee

        print("\nEmployee added successfully.")

    # ========================================================
    # DISPLAY ALL EMPLOYEES
    # ========================================================

    def display_all_employees(self):

        print("\n========== ALL EMPLOYEES ==========")

        if len(self.employees) == 0:

            print("No employees found.")

            return

        for employee in self.employees.values():

            employee.display_employee()

    # ========================================================
    # SEARCH EMPLOYEE
    # ========================================================

    def search_employee(self):

        print("\n========== SEARCH EMPLOYEE ==========")

        employee_id = input(
            "Enter Employee ID: "
        ).upper()

        if employee_id in self.employees:

            employee = self.employees[employee_id]

            employee.display_employee()

        else:

            print("Employee not found.")

    # ========================================================
    # UPDATE SALARY
    # ========================================================

    def update_salary(self):

        print("\n========== UPDATE SALARY ==========")

        employee_id = input(
            "Enter Employee ID: "
        ).upper()

        if employee_id not in self.employees:

            print("Employee not found.")

            return

        new_salary = float(
            input("Enter New Basic Salary: ")
        )

        employee = self.employees[employee_id]

        employee.salary = new_salary

        print("Salary updated successfully.")

    # ========================================================
    # DELETE EMPLOYEE
    # ========================================================

    def delete_employee(self):

        print("\n========== DELETE EMPLOYEE ==========")

        employee_id = input(
            "Enter Employee ID: "
        ).upper()

        if employee_id in self.employees:

            del self.employees[employee_id]

            Employee.total_employees -= 1

            print("Employee deleted successfully.")

        else:

            print("Employee not found.")

    # ========================================================
    # SALARY REPORT
    # ========================================================

    def salary_report(self):

        print("\n==============================================")
        print("             EMPLOYEE SALARY REPORT")
        print("==============================================")

        if len(self.employees) == 0:

            print("No employees found.")

            return

        print(
            f"{'ID':<10}"
            f"{'NAME':<15}"
            f"{'TYPE':<25}"
            f"{'SALARY':>12}"
        )

        print("-" * 65)

        total_salary = 0

        for employee in self.employees.values():

            salary = employee.calculate_salary()

            total_salary += salary

            employee_type = employee.__class__.__name__

            print(
                f"{employee.employee_id:<10}"
                f"{employee.name:<15}"
                f"{employee_type:<25}"
                f"{salary:>12.2f}"
            )

        print("-" * 65)

        print(
            "Total Employees :",
            len(self.employees)
        )

        print(
            "Total Salary    :",
            total_salary
        )

        print(
            "Average Salary  :",
            total_salary / len(self.employees)
        )

        print("==============================================")

    # ========================================================
    # HIGHEST SALARY
    # ========================================================

    def highest_salary_employee(self):

        print("\n========== HIGHEST SALARY EMPLOYEE ==========")

        if len(self.employees) == 0:

            print("No employees found.")

            return

        highest_employee = None
        highest_salary = 0

        for employee in self.employees.values():

            salary = employee.calculate_salary()

            if salary > highest_salary:

                highest_salary = salary
                highest_employee = employee

        highest_employee.display_employee()

    # ========================================================
    # EMPLOYEE COUNT
    # ========================================================

    def employee_count(self):

        print(
            "\nTotal Employees:",
            Employee.total_employees
        )

    # ========================================================
    # MAIN MENU
    # ========================================================

    def menu(self):

        while True:

            print("\n")
            print("========================================")
            print("       EMPLOYEE MANAGEMENT SYSTEM")
            print("========================================")

            print("1. Add Employee")
            print("2. Display All Employees")
            print("3. Search Employee")
            print("4. Update Salary")
            print("5. Delete Employee")
            print("6. Salary Report")
            print("7. Highest Salary Employee")
            print("8. Employee Count")
            print("9. Exit")

            print("========================================")

            choice = input(
                "Enter your choice: "
            )

            if choice == "1":

                self.add_employee()

            elif choice == "2":

                self.display_all_employees()

            elif choice == "3":

                self.search_employee()

            elif choice == "4":

                self.update_salary()

            elif choice == "5":

                self.delete_employee()

            elif choice == "6":

                self.salary_report()

            elif choice == "7":

                self.highest_salary_employee()

            elif choice == "8":

                self.employee_count()

            elif choice == "9":

                print(
                    "\nThank you for using Employee Management System."
                )

                break

            else:

                print(
                    "Invalid choice. Please try again."
                )


# ============================================================
# PROGRAM START
# ============================================================

system = EmployeeManagementSystem()

system.menu()