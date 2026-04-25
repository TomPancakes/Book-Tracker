#MAIN FILE. 

import database #runs database code and sets up
import tkinter as tk
from tkinter import ttk #import treeview module (to show table)


root = tk.Tk()

root.geometry("1920x1020")
root.title("Book Tracker")

#Functions

def update_table():
    pass
    #get the data from sql (for loop throughout)

    for row in table.get_children(): #Remove current table entries
        table.delete(row)

    books = database.get_entries()

    for book in books: #iterate over list of entries
        table.insert("", "end", values=book) #insert 

def add_book():
    print("pass")
    popup = tk.Toplevel()
    popup.geometry("500x500")
    popup.title("BOOK ADDITION")

    #TITLE
    Title_Text = tk.Label(popup, text="Title: ", width="20")
    Title_Text.grid(row=0, column=0, padx=10, pady=5)
    Title_Entry = tk.Entry(popup)
    Title_Entry.grid(row=0, column=1, padx=10, pady=5)

    #STATUS
    status_text = tk.Label(popup, text="Status: ", width="20")
    status_text.grid(row=1, column=0, padx=10, pady=5)
    status_var = tk.StringVar(value="Reading")
    status_dropdown = tk.OptionMenu(popup, status_var, "Reading", "Completed", "Dropped")
    status_dropdown.grid(row=1, column=1, padx=10, pady=5)

    def submit():
        title = Title_Entry.get()
        status = status_var.get()
        print(f"Inserting title: {title} as {status}")
        database.insert(title, status)
        popup.destroy()
        update_table()

    submit_button = tk.Button(popup, text="Submit Entry", width="20", command=submit)
    submit_button.grid(row="3", column="0")

def delete_selected():
    selected = table.focus() #get the selected row 
    print(f"Deleting Row {selected}")
    title = table.item(selected, "values")[0] #get title of selected
    database.delete(title)
    update_table()
        

title = tk.Label(root, text="Book Tracker", font=("Arial", 18))
title.pack()

#Buttons to Do Stuff
AddBookButton = tk.Button(root, text="Add Entry: ", width="40", command=add_book)
AddBookButton.pack()

#Delete Button
delete = tk.Button(root, text="Delete Selected", command=delete_selected)
delete.pack()

#Bones of Table
table = ttk.Treeview(root, columns=("Title", "Status", "Buttons"), show="headings" )
table.heading("Title", text="Title")
table.heading("Status", text="Status")
table.heading("Buttons", text="Options")
table.pack(fill="both", expand=True)

update_table() #Populate the table on startup

root.mainloop() #Infinite loop to keep app active


#TKINTER WIDGET CHEATSHEET:

# Label - text
# Entry - input
# Button - clickable
# OptionMenu - dropdown
# Checkbutton - checkbox
# Listbox - list
# Frame - container
# Text - multiline
# ttk.Treeview - table
