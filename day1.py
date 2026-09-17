def check_salary(salary):

    if salary >= 15000:
        return "High salary"

    elif salary >= 10000:
        return "Medium salary"

    else:
        return "Low salary"


salary = int(input("Enter your salary: "))

result = check_salary(salary)

print(result)