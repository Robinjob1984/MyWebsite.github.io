#!/usr/bin/env python3


null = 0
emps = [[8369, 'THOMAS', 'SECRETARY', 8902, '17-DEC-1990', 1400, null, 20],
       [8499, 'RICHARD', 'SALESPERSON', 8698,'20-FEB-1991', 2100, 300, 30],
       [8521, 'ANNE', 'SALESPERSON', 8698, '22-FEB-1991',1750, 500, 30],
       [8566, 'MARY', 'MANAGER', 8839, '02-APR-1991',3475, null, 20],
       [8654, 'KEN', 'SALESPERSON', 8698, '28-SEP-1991',1750, 1400, 30],
       [8698, 'EDWARD', 'MANAGER', 8839, '01-MAY-1991',3350, null, 30],
       [8782, 'JAMES', 'MANAGER', 8839, '09-JUN-1991',2450, null, 10],
       [8788, 'WESLEY', 'ANALYST', 8566, '09-NOV-1991',3500, null, 20],
       [8839, 'LARRY', 'PRESIDENT', null, '02-APR-1991',3475, null, 10],
       [8844, 'LINDA', 'SALESPERSON', 8698, '08-SEP-1991',2100, 0, 30],
       [8876, 'TERRY', 'SECRETARY', 8788, '23-SEP-1991',1600, null, 20],
       [8900, 'CRAIG', 'SECRETARY', 8698, '03-DEC-1991',1450, null, 30],
       [8902, 'SEAN', 'ANALYST', 8566, '03-DEC-1991',3500, null, 20],
       [8934, 'SUZANNE', 'SECRETARY', 8782, '23-JAN-1992',1800, null,10]]
for emp in emps:
    for item in emp:
        print(item, end=" | ")
    print()


STARS = "*" * 80
print(STARS)
print("%-20s%-20s%-15s%-15s%-12s%-12s%-15s%s"
      % (
        "EMPLOYEE_NUMBER",
        "EMPLOYEE_NAME",
        "JOB",
        "SUPERVISOR",
        "HIREDATE",
        "SALARY",
        "COMMISSION",
        "DEPARTMENT_NUMBER",
    )
)
for e in emps:
    
    print(
        "%-20s%-20s%-15s%-15s%-12s%-12s%-15s%s"
        % (e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7])
    )
print(STARS)

print(STARS)
print("EMPLOYEES NAME IN ALPHABETICAL ORDER:")
for e in sorted(emps, key=lambda e: e[1]):
    print("  ", e[1])
print(STARS)

print(STARS)
for e in emps:
    if e[1].upper() in ["RICHARD", "MARY", "SEAN"]:
        income = e[5] + e[6]
        print("Income of %s is $%.2f." % (e[1], income))
print(STARS)

table = {}
for e in emps:
    job = e[2].upper()
    salary = e[5]

    
    if job in table:
        
        table[job][0] += salary
        
        table[job][1] += 1
    else:
        
        table[job] = [salary, 1]
print(STARS)

print("%-15s%-20s%-20s" % ("JOB", "TOTAL SALARY", "AVERAGE SALARY"))
print("*************************************************")


for job in table:
    total_salary = table[job][0]
    average_salary = total_salary / table[job][1]
    print("%-15s%-20.2f%-20.2f" % (job, total_salary, average_salary))
print(STARS)

print(STARS)
print("%-20s%s" % ("EMPLOYEE NAME", "SUPERVISOR NAME"))
print("***********************************")

for e in sorted(emps, key=lambda e: e[1]):
    emp_no = e[0]
    supervisor_no = e[3]

    
    print("%-20s" % e[1], end="")

    found = False
    
    for s in sorted(emps, key=lambda e: e[3]):
        
        if s[0] == supervisor_no:
            found = True
            
            print(s[1])
    
    if not found:
        print("------")
print(STARS)
print("Extra-credit")
print(STARS)
print("%-20s%s" % ("EMPLOYEE NAME", "DEPARTMENT NAME"))
print("-----------------------------------")
for e in sorted(emps, key=lambda e: e[1]): 
    if e[7] == 10:
        print("%-20s%s" % (e[1],   'ACCOUNTTING'))
    elif e[7] == 20:
        print("%-20s%s" % (e[1],   'RESEARCH'))
    elif e[7] == 30:
        print("%-20s%s" % (e[1],   'SALES'))
    else:
        print("%-20s%s" % (e[1],   'OPERATIONS'))




