<h1> Employee Profile Generator </h1>

first_name = "Mickey"
last_name = "Chan"

full_name = first_name + ' ' + last_name 

address = "123 Main Street" 
address += ", Apartment 4B"

empolyee_age = 28

employee_info = full_name + " is "  + str(employee_age) + " years old"
print(employee_info) 

experience_years = 5
experience_info = "Experience: " + str(experience_years) + " years"
print(experience_info)

position = "Data Analyst" 
salary = 75000

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)g


