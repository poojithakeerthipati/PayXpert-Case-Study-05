from DAO import EmployeeService, FinancialService, TaxService, PayrollService
from Entity import Employee, Payroll, Tax, FinancialRecord


class MainMenu:
    employee_service = EmployeeService()
    payroll_service = PayrollService()
    tax_service = TaxService()
    financial_service = FinancialService()

    def employee_menu(self):
        while True:
            print(
                """
                1.Read employee By ID
                2. Read All employees
                3.Add an Employee
                4.Update an employee
                5.Delete an employee
                6.EXIT"""
            )
            choice = int(input("Please Choose from above options: "))

            if choice == 1:
                employee_id = int(input("Enter the EmployeeID: "))
                self.employee_service.get_employee_by_id(employee_id)
            elif choice == 2:
                self.employee_service.get_all_employees()
            elif choice == 3:
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                gender = input("Enter gender: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                address = input("Enter address: ")
                position = input("Enter position: ")
                joining_date = input("Enter joining date (YYYY-MM-DD): ")
                termination_date = input(
                    "Enter termination date (YYYY-MM-DD, if any): "
                )
                new_employee = Employee(
                    first_name,
                    last_name,
                    date_of_birth,
                    gender,
                    email,
                    phone_number,
                    address,
                    position,
                    joining_date,
                    termination_date,
                )
                self.employee_service.add_employee(new_employee)
            elif choice == 4:
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                gender = input("Enter gender: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                address = input("Enter address: ")
                position = input("Enter position: ")
                joined_date = input("Enter joining date (YYYY-MM-DD): ")
                termination_date = input(
                    "Enter termination date (YYYY-MM-DD, if any): "
                )
                employee_id = int(input("Enter the Employee ID: "))
                updated_employee = Employee(
                    first_name,
                    last_name,
                    date_of_birth,
                    gender,
                    email,
                    phone_number,
                    address,
                    position,
                    joined_date,
                    termination_date,
                )
                self.employee_service.update_employee(updated_employee, employee_id)

            elif choice == 5:
                employee_id = int(input("Enter employee Id: "))
                self.employee_service.remove_employee(employee_id)
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def payroll_menu(self):

        while True:
            print(
                """
                1. Generate payroll
                2. Get payroll by ID
                3. Get payrolls for an Employee
                4. Get payrolls for a Period
                5. EXIT"""
            )
            choice = int(input("Please Choose from above options: "))

            if choice == 1:
                employee_id = int(input("Enter EmployeeID: "))
                start_date = input("Enter Pay Period Start Date (YYYY-MM-DD): ")
                end_date = input("Enter Pay Period End Date (YYYY-MM-DD): ")
                self.payroll_service.generate_payroll(employee_id, start_date, end_date)
            elif choice == 2:
                payroll_id = int(input("Enter PayrollID: "))
                self.payroll_service.get_pay_roll_by_id(payroll_id)
            elif choice == 3:
                employee_id = int(input("Enter EmployeeID: "))
                self.payroll_service.get_pay_rolls_for_employee(employee_id)
            elif choice == 4:
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                self.payroll_service.get_pay_rolls_for_period(start_date, end_date)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def tax_menu(self):
        while True:
            print(
                """
                1. Calculate tax
                2. Get tax by ID
                3. Get taxes for an Employee
                4. Get taxes for a Year
                5. EXIT"""
            )
            choice = int(input("Please Choose from above options: "))

            if choice == 1:
                employee_id = int(input("Enter EmployeeID: "))
                tax_year = input("Enter Tax Year: ")
                self.tax_service.calculate_tax(employee_id, tax_year)
            elif choice == 2:
                tax_id = int(input("Enter TaxID: "))
                self.tax_service.get_tax_by_id(tax_id)
            elif choice == 3:
                employee_id = int(input("Enter EmployeeID: "))
                self.tax_service.get_tax_for_employee(employee_id)
            elif choice == 4:
                tax_year = input("Enter Tax Year: ")
                self.tax_service.get_tax_for_year(tax_year)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def financial_record_menu(self):

        while True:
            print(
                """
                  1. Add a financial record
                  2. Get financial record by ID
                  3. Get financial records for an Employee
                  4. Get financial records for a Date
                  5. EXIT"""
            )
            choice = int(input("Please Choose from above options: "))

            if choice == 1:
                employee_id = int(input("Enter EmployeeID: "))
                description = input("Enter description: ")
                amount = float(input("Enter amount: "))
                record_type = input("Enter record type: ")
                self.financial_service.add_financial_record(
                    employee_id, description, amount, record_type
                )
            elif choice == 2:
                record_id = int(input("Enter RecordID: "))
                self.financial_service.get_financial_record_by_id(record_id)
            elif choice == 3:
                employee_id = int(input("Enter EmployeeID: "))
                self.financial_service.get_financial_records_for_employee(employee_id)
            elif choice == 4:
                record_date = input("Enter Record Date (YYYY-MM-DD): ")
                self.financial_service.get_financial_records_for_date(record_date)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please enter a valid option.")


def main():
    main_menu = MainMenu()
    while True:
        print("Main Menu:")
        print(
            """
              1. Employee Management
              2. Payroll Management
              3. Tax Management
              4. Financial Record Management
              5. Exit"""
        )
        choice = int(input("Please Choose from above options: "))

        if choice == 1:
            main_menu.employee_menu()
        elif choice == 2:
            main_menu.payroll_menu()
        elif choice == 3:
            main_menu.tax_menu()
        elif choice == 4:
            main_menu.financial_record_menu()
        elif choice == 5:
            main_menu.employee_service.close()
            main_menu.payroll_service.close()
            main_menu.tax_service.close()
            main_menu.financial_service.close()
            print("Goodbye! Come back soon")
            break


if __name__ == "__main__":
    print("Welcome to the Pay Xpert 🎉")
    main()
