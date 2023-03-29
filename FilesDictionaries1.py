import csv
null = 0
#Given Data
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

f = open("emps.csv",'w',newline="")

writer = csv.writer(f)
writer.writerows(emps)
f.close()
