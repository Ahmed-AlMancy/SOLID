from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, emp_id: int):
        self._name = name
        self._id = emp_id

    @property
    def name(self):
        return self._name

    @property
    def emp_id(self):
        return self._id

    def display_details(self):
        print(f"Employee Name: {self._name}, ID: {self._id}")

class Manager(Employee):
    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting.")

class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is writing code.")

class SalaryCalculator(ABC):
    @abstractmethod
    def calculate_salary(self, employee: Employee) -> float:
        pass

class ManagerSalaryCalculator(SalaryCalculator):
    def calculate_salary(self, employee: Employee) -> float:
        return 40000.0

    def calculate_bonus(self):
        print("Calculating bonus for a manager.")

class DeveloperSalaryCalculator(SalaryCalculator):
    def calculate_salary(self, employee: Employee) -> float:
        return 75000.0

    def calculate_overtime_pay(self):
        print("Calculating overtime pay for a developer.")

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, employee: Employee) -> str:
        pass

class SimpleReportGenerator(ReportGenerator):
    def generate_report(self, employee: Employee) -> str:
        return f"Report for Employee: {employee.name} (ID: {employee.emp_id})"

    def generate_summary(self):
        print("Generating a simple summary report.")

class EmployeeService:
    def __init__(self, salary_calculator: SalaryCalculator, report_generator: ReportGenerator):
        self.salary_calculator = salary_calculator
        self.report_generator = report_generator

    def process_employee(self, employee: Employee):
        employee.display_details()
        print(self.report_generator.generate_report(employee))
        print(f"Salary: ${self.salary_calculator.calculate_salary(employee)}")

    def send_notification(self, employee: Employee):
        print(f"Sending notification to: {employee.name}")
########################################################################################################################
manager = Manager(name="Sobhy", emp_id=101)
developer = Developer(name="Ahmed", emp_id=102)

manager_salary_calculator = ManagerSalaryCalculator()
developer_salary_calculator = DeveloperSalaryCalculator()

simple_report_generator = SimpleReportGenerator()

manager_service = EmployeeService(salary_calculator=manager_salary_calculator, report_generator=simple_report_generator)
developer_service = EmployeeService(salary_calculator=developer_salary_calculator, report_generator=simple_report_generator)

print("Processing Manager:")
manager_service.process_employee(manager)
manager.conduct_meeting()
print()

print("Processing Developer:")
developer_service.process_employee(developer)
developer.write_code()
print()
########################################################################################################################
