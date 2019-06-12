import mysql.connector

#TO CHANGE ENCRYPTION OF PASSWORD
# ALTER USER 'yourusername'@'localhost' IDENTIFIED WITH mysql_native_password BY 'youpassword';

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="471-my-root",
    database= "mysocial"
)

mycursor = mydb.cursor()

insert_to_logged = "INSERT INTO LOGGED_IN (Email_address, Password, Name, ID, IP_Address) VALUES (%s, %s, %s, %s, %s)"

#user_log = ("steven@", "123qwe", "steven", 123, "111")

insert_to_user = "INSERT INTO USER (Name, ID, IP_Address) VALUES (%s, %s, %s)"
#user = ("anon", 471, 147)

#mycursor.execute(sqlFormula, user)

#mydb.commit()