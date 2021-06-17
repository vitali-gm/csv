import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="csv"
)


mycursor = mydb.cursor()

sql = "INSERT INTO data (num_rp, date_rp, amount_rp, contact_rp, type) VALUES (%s, %s, %s, %s, %s)"

with open('contacts_mshara_17-21.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for i, row in enumerate(csv_reader):
        print(i)
        if i > 0:
            val = (row[0], row[1], row[2], row[3], 'new')
            mycursor.execute(sql, val)
            mydb.commit()
