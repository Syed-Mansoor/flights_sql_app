import mysql.connector

# Connect to the database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='9596531520',
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print('Connection established')
except mysql.connector.Error as err:
    print(f'Connection error: {err}')



# # create a database on the db_server
# mycursor.execute("CREATE DATABASE IF NOT EXISTS indigo")
# conn.commit()

# create a table
# airpot -> airpot_id|code | name
# try:
#     mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS airport(
#             airport_id INTEGER PRIMARY KEY,
#             code VARCHAR(255) NOT NULL,
#             city VARCHAR(255) NOT NULL,
#             name VARCHAR(255) NOT NULL)
#                     """)
#     conn.commit()
#     print('table creation done')
# except Exception as e:
#     print('some error occured')
#     print(e)


# insert data into the table
# mycursor.execute(

#     """
# INSERT INTO airport values
# (1,'DEL','New Delhi','IDIA'),
# (2,'ccu','kolkata','NSCA'),
# (3,'BOM','MUMBAI','CSMA')
# """)

# conn.commit()

# # search/retrive
# try:
#     mycursor.execute('SELECT * FROM airport where airport_id > 1')
#     print('done')
#     data = mycursor.fetchall()
#     print('data stored')
#     print(data)
#     for i in data:
#         print(i[3])
# except Exception as e:
#     print(e)


# # update
# try:
#     mycursor.execute("""UPDATE airport
#                      SET city = 'bombay'
#                      where airport_id = 3
#                      """)
#     conn.commit()
#     print('name changed done')
#     mycursor.execute('SELECT * FROM airport')
#     print('done')
#     data = mycursor.fetchall()
#     print('data stored')
#     print(data)

# except Exception as e:
#     print(e)


# # delete
# try:
#     mycursor.execute('DELETE FROM airport WHERE airport_id = 3')
#     conn.commit()
#     print('deleted successfully')
# except Exception as e:
#     print(e)