from tkinter import*

import sqlite3

root=Tk()
root.title('MyCRUDProject')
root.geometry("500x500")

conn=sqlite3.connect('my_data.db')
c=conn.cursor()


def submit ():
    conn=sqlite3.conect('"C:/Users/STUDENTS\Documents/my_data.db"')
    c=coon.curso()
    c.excute("INSERT INTO studentinfo VALUES(:f_name,;age,:adrress,:email)",
             {
                 'f_name':f_name.get(),
                 'l_name':l_name.get(),
                 'Age':age.get(),
                 'address':address.get(),
                 'email':email.get(),

                 })
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    email.delete(0,END)

def query():
    conn=sqlite3.connect('"C:/Users/STUDENTS\Documents/my_data.db"')
    c=conn.cursor()
    c.execute("SELECT ', oid FROM my_data")
    records=c.fetchall()

    print_record=''
    for record in records:
        print_records+=str(records[0])+" "+str(records[1])+""+str(records[2])+" "+str(records[3])+" "+(records[4])+" "+"/t"+str(records[5])+"/n"
        query_label=Label(root,text=print_records)
        query_label.grid(row=30,column=0,columnspan=2)

    conn.commit()
    conn.close()

'''
c.execute("""CREATE TABLE "my_data" (
	"f_name"	TEXT,
	"l_name"	TEXT,
	"Age"	INTEGER,
	"address"	TEXT,
	"email"	TEXT
)
)""")
'''

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
Age=Entry(root,width=30)
Age.grid(row=2,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)
email=Entry(root,width=30)
email.grid(row=4,column=1,padx=20)
delete_box=Entry(root,width=30)
delete_box.grid(row=10,column=1,padx=30)


f_name_label=Label(root,text="First name")
f_name_label.grid(row=0,column=0)
l_name_label=Label(root,text="last name")
l_name_label.grid(row=1,column=0)
Age_label=Label(root,text="Age")
Age_label.grid(row=2,column=0)
address_label=Label(root,text="Address")
address_label.grid(row=3,column=0)
email_label=Label(root,text="email")
email_label.grid(row=4,column=0)

def delete():
    conn=sqlite3.connect('"C:/Users/STUDENTS\Documents/my_data.db"')
    c=conn.cursor()

    c.execute("DELETE from customerinfo WFERE oid="+delete_box.get())

    delete_box.delete(0,END)

    conn.commit()
    conn.close()


delete_box_label=Label(root,text="Select ID No.")
delete_box_label.grid(row=10,column=0)

submit_btn=Button(root,text="add record to database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,ipadx=100)

query_btn=Button(root,text= "Show records", command=query)
query_btn.grid (row=7,column=0,columnspan=2, pady=10, padx=10, ipadx=137)

query_btn=Button(root,text="Delete Record",command=delete)
query_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

update_btn=Button(root,text="Edit Record",command=exit)
update_btn.grid(row=13,column=0,columnspan=2,pady=10,padx=10,ipadx=140)

conn.commit()
conn.close()

root.mainloop()
