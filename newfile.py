import tkinter as tk
import sqlite3
#
def a():
	
	db=sqlite3.connect('artists. db')
	cursor=db.cursor()
	
	cursor.execute('''SELECT name from artists''')
	
	name = cursor.fetchall()
	
	print(name)
	
	for i in name:
		if i[0] == 'Timati':
			print(i[0])
	
db=sqlite3.connect('db. db')
cursor=db.cursor()

cursor.execute('''SELECT name from artists''')

name = cursor.fetchall()

print(name)

for i in name:
	if i[0] == 'Timati':
		print(i[0])

window=tk.Tk()
window.config(bg='blue')

name = tk.Label(text='name')
name.pack()

entry = tk.Entry()
entry.pack()

but=tk.Button(text='Search')
but.pack()

window.mainloop()