import tkinter as tk

root = tk.Tk()

def myClick():
    myLabel = tk.Label(root, text='Look! I clicked a Button!')
    myLabel.pack()

myButton = tk.Button(root, text="Click me!", command=myClick)
myButton.pack()


tk.mainloop()