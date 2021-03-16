import mysql.connector as mysql

from tkinter import *
import tkinter.messagebox as MessageBox



def insert():
    id = input_id.get()
    item = input_item.get()
    price = input_price.get()

    if(id=="" or item=="" or price==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="student expense")
        cursor = con.cursor()
        cursor.execute("insert into expense values('"+ id +"','"+ item +"','"+ price +"') ")
        cursor.execute("commit");

        input_id.delete(0, 'end')
        input_item.delete(0, 'end')
        input_price.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully!");
        con.close();

def delete():
    if(input_id.get() == ""):
        MessageBox.showinfo("Delete Status", "Please enter an ID to delete")
    else:

        con = mysql.connect(host="localhost", user="root", password="", database="student expense")
        cursor = con.cursor()
        cursor.execute("delete from expense where id='"+ input_id.get() +"'")
        cursor.execute("commit");

        input_id.delete(0, 'end')
        input_item.delete(0, 'end')
        input_price.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted Successfully!");
        con.close();

def update():
    id = input_id.get()
    item = input_item.get()
    price = input_price.get()

    if (id == "" or item == "" or price == ""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:

        con = mysql.connect(host="localhost", user="root", password="", database="student expense")
        cursor = con.cursor()

        cursor.execute("select item, price from expense where id ='" + id + "'")
        dataFound = cursor.fetchone()

        if not dataFound:
            MessageBox.showinfo("Update Status", "No such item ID found! Try again.")
        else:
            cursor.execute("update expense set item='" + item + "', price='"+ price +"' where id='"+ id +"'")
            cursor.execute("commit");

            input_id.delete(0, 'end')
            input_item.delete(0, 'end')
            input_price.delete(0, 'end')
            show()
            MessageBox.showinfo("Update Status", "Updated Successfully!");

        con.close();

def get():
    if(input_id.get() == ""):
        MessageBox.showinfo("Fetch Status", "Please enter an ID to fetch")
    else:

        con = mysql.connect(host="localhost", user="root", password="", database="student expense")
        cursor = con.cursor()
        cursor.execute("select * from expense where id='"+ input_id.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            input_id.insert(0, row[0])
            input_item.insert(0, row[1])
            input_price.insert(0, row[2])


        con.close();

def show():
    con = mysql.connect(host="localhost", user="root", password="", database="student expense")
    cursor = con.cursor()
    cursor.execute("select * from expense")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertdata = str(row[0])+'        '+ row[1]+'        '+ str(row[2])
        list.insert(list.size()+1, insertdata)

    con.close();


root = Tk()
mycolor = '#a0dde8'
root.configure(background=mycolor)
root.geometry("600x300")
root.title("Student Expense Tracker (Python+MySQL)")

id = Label(root, text='Enter ID', font=('bold', 10))
id.place(x = 20, y = 30);

item_name = Label(root, text='Enter item name', font=('bold', 10))
item_name.place(x = 20, y = 60);

price = Label(root, text='Enter price', font=('bold', 10))
price.place(x = 20, y = 90);

input_id = Entry()
input_id.place(x=150, y = 30)

input_item = Entry()
input_item.place(x=150, y = 60)

input_price = Entry()
input_price.place(x=150, y = 90)

insertbtn = Button(root, text="Insert", font=("italic", 10), bg="white", command=insert)
insertbtn.place(x = 20, y = 140)

deletebtn = Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
deletebtn.place(x = 70, y = 140)

updatebtn = Button(root, text="Update", font=("italic", 10), bg="white", command=update)
updatebtn.place(x = 130, y = 140)

getbtn = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
getbtn.place(x = 190, y = 140)

list = Listbox(root)
list.place(x=290, y = 30)
show()

root.mainloop()
