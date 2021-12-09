import tkinter as tk

root = tk.Tk()

#Creating a Label Widget
myLabel1 = tk.Label(root, text="Hello World!")
myLabel2 = tk.Label(root, text="My name is Liam Thompson")

#Putting it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=4)


#myLabel.pack()

tk.mainloop()