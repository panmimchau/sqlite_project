import sqlite3
from employee import Employee

#conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:') #good for testing. dont have to overwrite db

c = conn.cursor() #we can start running sql commands

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

emp_1 = Employee('adam', 'malysz', 1000)
emp_2 = Employee('patos', 'but', 1000)

#print(emp_1.first)
#print(emp_1.last)
#print(emp_1.pay)


##adding to table method nr 1
c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

conn.commit()

#adding to table method nr 2
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

conn.commit()

#c.execute("SELECT * FROM employees WHERE last='kubica'")
c.execute("SELECT * FROM employees WHERE last=?", ('but',))

#print(c.fetchone())
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'kubica'})

#print(c.fetchone())
print(c.fetchall())

conn.commit()

conn.close() #to close connection to db