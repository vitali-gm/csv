import mysql.connector

class Db:

    mydb = None

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="csv"
        )

    def all(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM data")
        return mycursor.fetchall()

    def one_without_type(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM data WHERE type IS NULL LIMIT 1")
        return mycursor.fetchone()

    def by_contact(self, contact):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM data WHERE contact_rp = '" + contact + "'")
        return mycursor.fetchall()
    
    def first(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM data LIMIT 1")
        return mycursor.fetchone()
    
    def update_type(self, type, num_rp):
        mycursor = self.mydb.cursor()
        mycursor.execute("UPDATE data SET type='" + type + "' WHERE num_rp='" + num_rp + "'")
        self.mydb.commit()