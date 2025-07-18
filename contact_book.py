
import mysql.connector
from mysql.connector import Error
from contact import Contact
class ContactBook:
    def __init__(self):
        self.connection=self.create_connection()

    def create_connection(self):
        try:
          Connection=mysql.connector.connect(host='localhost',database='contact_book',user='root',password='suvidha123')
          if Connection.is_connected():
            return Connection
        except Error as e:
          print(f"Error:{e}")
        return None

    def add_contact(self,contact):
       cursor=self.connection.cursor()
       query="insert into contacts (name,phone,email) values(%s,%s,%s)"
       values=(contact.name,contact.phone,contact.email)
       cursor.execute(query,values)
       self.connection.commit()
       print("contact added successfully")

    def display_all_contacts(self):
        cursor=self.connection.cursor(dictonary=True)
        query="select * from contacts"
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
          Contact=Contact(row['name'],row['phone'],row['email'])
          Contact.display_contact()
          print("--------")

    def search_contacts(self,name):
      cursor=self.connection.cursor(dictonary=True)
      query="select * from contacts where name= %s"
      cursor.execute(query,(name))
      result=cursor.fetchone()
      if result:
        return Contact(result['name'],result['phone'],result['email'])
        return none

    def close_connection(self):
      if self.connection.is_connected():
        self.connection.close()
        print("MySql connection closed")