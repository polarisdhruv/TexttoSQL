# import sqlite3


# ##Connect to sqlite
# connection = sqlite3.connect("student.db")


# ## Create a cursor object to insert record, create table , retreieve

# cursor =  connection.cursor()


# ## create the table 

# table_info = """
# Create table Student(Name varchar(25), CLASS varchar(25), SECTION varchar(25), MARKS INT)
# """

# cursor.execute(table_info)


# # Insert data into the table


# cursor.execute(''' Insert Into Student values('krish', 'Data Science', 'A', 90)''')
# cursor.execute(''' Insert Into Student values('Abhay', 'Data Science', 'B', 90)''')
# cursor.execute(''' Insert Into Student values('Rohit', 'Development', 'C', 90)''')
# cursor.execute(''' Insert Into Student values('Vikas', 'Devops', 'A', 80)''')
# cursor.execute(''' Insert Into Student values('Vayu', 'Devops', 'A', 86)''')


# ## Display all the records 

# print("The inserted records are:")

# data = cursor.execute(''' SELECT * From STUDENT''')

# for row in data:
#     print(row)

# ### Close the connection
# connection.commit()

# connection.close()



