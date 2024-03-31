#Using zip() to zip lists
indexes = [1, 2, 3, 4]
employees = ["david", "Josa", "Franky", "Robin"]
department = ["managment", "Teacher", "Engineer", "Mechanic"]

#zip all three lists together
roster = zip(indexes, employees, department)

#print the contents of each row
for employees in roster:
    print(employees)
