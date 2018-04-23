# import sqlite3
# connection=sqlite3.connect('SUNNY')

# connection.close()


# # creating  a table in my data base

# import sqlite3
# connection=sqlite3.connect('SUNNY')
# connection.execute(''' CREATE TABLE  CHERRY
# 					 (ID INT PRIMARY KEY NOT NULL,
# 					  NAME TEXT NOT NULL,
# 					  AGE INT NOT NULL,
# 					  ADDRESS CHAR (100) NOT NULL,
# 					  PROOF TEXT NOT NULL);''')
# print('the table has been successfully created')



import sqlite3

connection = sqlite3.connect('SUNNY')
connection.execute("INSERT INTO CHERRY  (ID,NAME,AGE,ADDRESS,PROOF) \
						values(1,'himan55',23,'gachibowli','aadhar')")

connection.execute("INSERT INTO CHERRY  (ID,NAME,AGE,ADDRESS,PROOF) \
 						values(2,'batman',22,'gachibowli','aadhar')")

connection.execute("INSERT INTO CHERRY  (ID,NAME,AGE,ADDRESS,PROOF) \
 						values(3,'superman',21,'gachibowli','aadhar')")

connection.execute("INSERT INTO CHERRY  (ID,NAME,AGE,ADDRESS,PROOF) \
						values(4,'Iornman',18,'gachibowli','aadhar')")

connection.execute("INSERT INTO CHERRY (ID,NAME,AGE,ADDRESS,PROOF) \
 						values(5,'wonderwomen',23,'gachibowli','aadhar')")

connection.execute("INSERT INTO CHERRY  (ID,NAME,AGE,ADDRESS,PROOF) \
 						values(6,'tonystark',23,'gachibowli','aadhar')")

connection.execute("INSERT INTO CHERRY (ID,NAME,AGE,ADDRESS,PROOF) \
 						values(7,'himan',23,'gachibowli','aadhar')")

connection.execute("INSERT INTO CHERRY  (ID,NAME,AGE,ADDRESS,PROOF) \
 						values(8,'himan1',23,'gachibowli','aadhar')")

connection.execute("INSERT INTO CHERRY  (ID,NAME,AGE,ADDRESS,PROOF) \
 						values(9,'himan2',23,'gachibowli','aadhar')")
connection.execute("INSERT INTO CHERRY  (ID,NAME,AGE,ADDRESS,PROOF) \
 						values(10,'himan3',23,'gachibowli','aadhar')")

connection.commit()

connection.close()

