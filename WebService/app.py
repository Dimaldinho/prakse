import tkinter as tk
from tkinter import messagebox
import conn

def getAnimalById():
    windowData = tk.Toplevel(root)
    id = entry.get()
    data = conn.getAnimalById(id)
    tk.Label(windowData, text=f"Name: {data['name']}, Age: {data['age']}").pack()

def getAllAnimals():
    windowData = tk.Toplevel(root)

    data = conn.getAllAnimals()
   
    for i in data:
        tk.Label(windowData, text=f"Id: {i}, Name: {data[i]['name']}, Age: {data[i]['age']}").pack()
       
        #tk.Button(windowData, text="Delete").pack()
        #tk.Button(windowData, text="Update").pack()

def updateAnimal():
    windowData = tk.Toplevel(root)
    id = entry.get()
    
    data = conn.getAnimalById(id)
    tk.Label(windowData, text=f"Name: {data['name']}, Age: {data['age']}").pack()

    entry2 = tk.Entry(windowData)
    entry2.pack()

    entry3 = tk.Entry(windowData)
    entry3.pack()
    
    def up():
        name = entry2.get()
        age = entry3.get()
        conn.updateAnimal(id,name,age)
    
    a= tk.Button(windowData, text = "update", command= up)
    a.pack(anchor="w")

def createAnimal():
    windowData = tk.Toplevel(root)
    
    entry1 = tk.Entry(windowData)
    entry1.pack()

    entry2 = tk.Entry(windowData)
    entry2.pack()

    entry3 = tk.Entry(windowData)
    entry3.pack()
    
    def up():
        id = entry1.get()
        name = entry2.get()
        age = entry3.get()
        conn.createAnimal(id,name,age)
    
    a= tk.Button(windowData, text = "update", command= up)
    a.pack(anchor="w")



def deleteAnimal():
    id = entry.get()
    conn.deleteAnimal(id)
    
root = tk.Tk()
root.geometry("600x400")

tk.Label(root, text= "Search animal").pack(anchor="w")

entry = tk.Entry(root)
entry.pack(anchor="w")


tk.Button(root, text="Search", command=getAnimalById).pack(anchor="w")
tk.Button(root, text = "All Animals", command=getAllAnimals).pack(anchor="w")
tk.Button(root, text = "Create Animal", command=createAnimal).pack(anchor="w")
tk.Button(root, text = "Update Animal", command=updateAnimal).pack(anchor="w")
tk.Button(root, text = "Delete Animal", command=deleteAnimal).pack(anchor="w")

root.mainloop()


