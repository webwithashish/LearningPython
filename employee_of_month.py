
work_hours = [("ashish", 100), ("ganesh", 150), ("smith",140), ("billy", 350), ("akash", 344)]
def empolyee_of_month(work_hours):
    max_hours = 0
    employee_name = ''
    for name,hours in  work_hours:
        if hours > max_hours:
            max_hours = hours
            employee_name = name
        else:
            pass
    return (employee_name, max_hours)


winner = empolyee_of_month(work_hours)
name, working_hours = winner
print(f"the winner is '{name}' with {working_hours} hours")
