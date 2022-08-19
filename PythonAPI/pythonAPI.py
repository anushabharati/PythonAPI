#Repl.it link: https://replit.com/join/lrdrnwdjzo-anushabharati85

import sqlite3
# Define DBOperation class to manage all data into the database.
#Class to manage all data into the database. 
class DBOperations:
  sql_create_table = "CREATE table EmployeeUoB (employeeID int, empTitle varchar(10), forename varchar(50), surname varchar(50), email varchar(50), salary float)"

  sql_insert = "INSERT INTO EmployeeUoB (employeeID, empTitle, forename, surname, email, salary) VALUES (?,?,?,?,?,?)"
 
  sql_select_all = "select * from EmployeeUoB"
  sql_search = "select * from EmployeeUoB where EmployeeID = ?"

  sql_delete_data = "DELETE FROM EmployeeUoB WHERE EmployeeID = ?"

  sql_delete_data1 = "DELETE FROM EmployeeUoB"

  sql_search_high_sal = "SELECT employeeID, empTitle, forename, surname, email, MAX(salary) FROM EmployeeUoB "

  sql_drop_table = "DROP TABLE EmployeeUoB"
  
#function to connect to the database  
  def __init__(self):
    try:
      self.conn = sqlite3.connect("DBUoB.db")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

#function to get the connection and setting up the database.
  def get_connection(self):
    self.conn = sqlite3.connect("DBName.db")
    self.cur = self.conn.cursor()

#function to create table if it does not exist in the database and commit
  def create_table(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_create_table)
      print("\nTable created!")
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

#function to insert data in the table and commit
  def insert_data(self):
    try:
      self.get_connection()
      emp = Employee()
      emp.set_employee_id(int(input("Enter Employee ID: ")))
      emp.set_employee_title(input("Enter Employee Title: "))
      emp.set_forename(input("Enter Employee Forename: "))
      emp.set_surname(input("Enter Employee Surname: "))
      emp.set_email(input("Enter Employee Email: "))
      emp.set_salary(input("Enter Employee Salary: "))
     
      self.cur.execute(self.sql_insert,tuple(str(emp).split("\n")))

      self.conn.commit()
      print("\nInserted data successfully!")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

#function to select all data in the table and display the details
  def select_all(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all)
      results = self.cur.fetchall()
      print("\nPrinting each row\n")
      for row in results:
        print ("----------------------------------")
        print("Employee:        ", row[0])
        print("Employee Title:  ", row[1])
        print("Forename:        ", row[2])
        print("Surname:         ", row[3])
        print("Email:           ", row[4])
        print("Salary:          ", row[5])
        print ("----------------------------------")
        print("\n")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

#function to drop the entire table
  def drop_table(self):
      try:
        self.get_connection()
        self.cur.execute(self.sql_drop_table)
        print ("\nTable dropped!")
        self.conn.commit()
      except Exception as e:
        print(e)
      finally:
        self.conn.close()

#function to search data by employee id in the table and display the details
  def search_data(self):
    try:
      self.get_connection()
      employeeID = int(input("Enter Employee ID: "))
      self.cur.execute(self.sql_search,tuple(str(employeeID)))
      result = self.cur.fetchone()
      print("\nPrinting details for the employee\n")
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("Employee ID: " + str(detail))
          elif index == 1:
            print("Employee Title: " + detail)
          elif index == 2:
            print("Employee Name: " + detail)
          elif index == 3:
            print("Employee Surname: " + detail)
          elif index == 4:
            print("Employee Email: " + detail)
          else:
            print("Salary: "+ str(detail))
      else:
        print ("No Record")
           
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

#function to search data by highest salary among all employee id entered in the table and display the details
  def search_high_sal_data(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_search_high_sal)
      result = self.cur.fetchone()
      print("\nPrinting details for the employee with highest salary.\n")
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("Employee ID: " + str(detail))
          elif index == 1:
            print("Employee Title: " + detail)
          elif index == 2:
            print("Employee Name: " + detail)
          elif index == 3:
            print("Employee Surname: " + detail)
          elif index == 4:
            print("Employee Email: " + detail)
          else:
            print("Salary: "+ str(detail))
      else:
        print ("No Record")
           
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

#function to update specific rows in the table according to the user and commit
  def update_data(self):
    try:
      self.get_connection()
      print ("\nUpdate menu")
      print ("*************************************")
      print (" 1. Employee Title")
      print (" 2. Employee Forename")
      print (" 3. Employee Surname")
      print (" 4. Employee Email")
      print (" 5. Employee Salary")
      print (" 6. Exit")
      print ("*************************************")
      employeeID = (int(input("\nEnter Employee ID for which you want to update: ")))
      choice = int(input("Enter the field that you want to be updated:  "))
      if choice > 0 and choice < 6:
        choose = choice 
        if choose == 1:
          field = 'empTitle'
        elif choose == 2:
          field = 'forename'
        elif choose == 3:
          field = 'surname'
        elif choose == 4:
          field = 'email'
        elif choose == 5:
          field = 'salary'
      elif choice == 6:
        exit(0)
      else:
        print ("Invalid Choice")

      update_value = (input("Enter the value to be updated: "))
      if choose > 0 and choose < 6:
        result = self.cur.execute("UPDATE EmployeeUoB SET " + str(field) + " = " + "'"+str(update_value)+"'"+" WHERE employeeID = " + str(employeeID))
      self.conn.commit()
      if result.rowcount != 0:
        print (str(result.rowcount)+ "Row(s) affected.")
      else:
        print ("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

#function to 
#1.  Delete specific rows from the table according to the employee id entered by the user and commit
#2.  Delete entire rows from the table and commit
  def delete_data(self):
    try:
      self.get_connection()
      print("\nDelete menu")
      print ("*************************************")
      print(" 1. Delete entire record")
      print(" 2. Delete the Employee ID specific data")
      print(" 3. Exit")
      print ("*************************************")
      choice = int(input("\nEnter if you want to delete all the data in record or specific column:  "))
      if choice == 1:
        result = self.cur.execute(self.sql_delete_data1)
        self.conn.commit()
      elif choice == 2:
        employeeID = (int(input("Enter Employee ID for which you want to delete: ")))
        result = self.cur.execute(self.sql_delete_data,tuple(str(employeeID)))
        self.conn.commit()
      elif choice == 3:
        exit(0)
      else:
        print ("Invalid Choice")
      self.conn.commit()
      if result.rowcount != 0:
        print (str(result.rowcount)+ " Row(s) affected.")
      else:
        print ("Cannot find this record in the database")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

#Class to manage all employee data into the database. 
class Employee:
  def __init__(self):
    self.employeeID = 0
    self.empTitle = ''
    self.forename = ''
    self.surname = ''
    self.email = ''
    self.salary = 0.0

  def set_employee_id(self, employeeID):
    self.employeeID = employeeID

  def set_employee_title(self, empTitle):
    self.empTitle = empTitle

  def set_forename(self,forename):
   self.forename = forename
 
  def set_surname(self,surname):
    self.surname = surname

  def set_email(self,email):
    self.email = email
 
  def set_salary(self,salary):
    self.salary = salary
 
  def get_employee_id(self):
    return self.employeeId

  def get_employee_title(self):
    return self.empTitle
 
  def get_forename(self):
    return self.forename
 
  def get_surname(self):
    return self.surname
 
  def get_email(self):
    return self.email
 
  def get_salary(self):
    return self.salary

  def __str__(self):
    return str(self.employeeID)+"\n"+self.empTitle+"\n"+ self.forename+"\n"+self.surname+"\n"+self.email+"\n"+str(self.salary)


# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.
 
while True:
  print ("\n Menu:")
  print ("*************************************")
  print (" 1. Create table EmployeeUoB")
  print (" 2. Insert data into EmployeeUoB")
  print (" 3. Select all data into EmployeeUoB")
  print (" 4. Search an employee")
  print (" 5. Update data (to update a record)")
  print (" 6. Delete data (to delete the entire data or Employee ID specific data)")
  print (" 7. Search data by highest salary among all Employee ID")
  print (" 8. Drop table (to delete a table)")
  print (" 9. Exit")
  print ("*************************************")

  __choose_menu = int(input("\nEnter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.create_table()
  elif __choose_menu == 2:
    db_ops.insert_data()
  elif __choose_menu == 3:
    db_ops.select_all()
  elif __choose_menu == 4:
    db_ops.search_data()
  elif __choose_menu == 5:
    db_ops.update_data()
  elif __choose_menu == 6:
    db_ops.delete_data()
  elif __choose_menu == 7:
    db_ops.search_high_sal_data()
  elif __choose_menu == 8:
    db_ops.drop_table()
  elif __choose_menu == 9:
    exit(0)
  else:
    print ("Invalid Choice")