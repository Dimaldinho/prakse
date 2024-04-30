import tkinter as tk
from tkinter import messagebox
import sqlite3
import sqlAlchemy as sqlAlc
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=sqlAlc.engine)
session = Session()

def getAnimalById():
    windowData = tk.Toplevel(root)
    id = entry.get()

    animal = session.query(sqlAlc.User).filter_by(id=id).first()
    tk.Label(windowData, text=f"Name: {animal.name}, Age: {animal.age}").pack()
    

def getAllAnimals():
    windowData = tk.Toplevel(root)
    users = session.query(sqlAlc.User).all()
    for i in users:
        tk.Label(windowData, text=f"Id: {i.id}, Name: {i.name}, Age: {i.age}").pack()

def updateAnimal():
    windowData = tk.Toplevel(root)
    id = entry.get()

    animal = session.query(sqlAlc.User).filter_by(id=id).first()
    
    tk.Label(windowData, text=f"Name: {animal.name}, Age: {animal.age}").pack()

    entry2 = tk.Entry(windowData)
    entry2.pack()

    entry3 = tk.Entry(windowData)
    entry3.pack()
    
    def up():
        name = entry2.get()
        age = entry3.get()
        animal.name = name
        animal.age = age
        session.commit()
    
    a= tk.Button(windowData, text = "update", command= up)
    a.pack(anchor="w")

def createAnimal():
    windowData = tk.Toplevel(root)
    
    # entry1 = tk.Entry(windowData)
    # entry1.pack()

    entry2 = tk.Entry(windowData)
    entry2.pack()

    entry3 = tk.Entry(windowData)
    entry3.pack()
    
    def up():
        
        name = entry2.get()
        age = entry3.get()
        new_animal = sqlAlc.User(name=name, age=age)
        session.add(new_animal)
        session.commit()
    
    a= tk.Button(windowData, text = "update", command= up)
    a.pack(anchor="w")



def deleteAnimal():
    id = entry.get()
    animal = session.query(sqlAlc.User).filter_by(id=id).first()
    if animal:
        session.delete(animal)
        session.commit()
    
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


