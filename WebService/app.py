import tkinter as tk
import conn

root = tk.Tk()
root.geometry("600x400")
tk.Label(root, text= "Search animal").pack(anchor="w")

id_userInput = tk.Entry(root)
id_userInput.pack(anchor="w")


def get_Animal_By_Id():
    window_two = tk.Toplevel(root)
    retrieved_data = conn.getAnimalById(id_userInput.get())

    tk.Label(window_two, text=f"Name: {retrieved_data['name']}, Age: {retrieved_data['age']}").pack()

def get_All_Animals():
    window_two = tk.Toplevel(root)
    retrieved_data = conn.getAllAnimals()

    for data in retrieved_data:
        tk.Label(window_two, text=f"Id: {data['id']}, Name: {data['name']}, Age: {data['age']}").pack()

def update_Animal():
    window_two = tk.Toplevel(root)

    search_id = id_userInput.get()
    retrieved_data = conn.getAnimalById(search_id)

    tk.Label(window_two, text=f"Name: {retrieved_data['name']}, Age: {retrieved_data['age']}").pack()

    name_userInput = tk.Entry(window_two)
    name_userInput.pack()
    age_userInput = tk.Entry(window_two)
    age_userInput.pack()
    
    def send_data():
        updated_name = name_userInput.get()
        updated_age = age_userInput.get()
        conn.updateAnimal(search_id,updated_name,updated_age)
    
    tk.Button(window_two, text = "update", command= send_data).pack(anchor="w")

def create_Animal():
    window_two = tk.Toplevel(root)

    name_userInput = tk.Entry(window_two)
    name_userInput.pack()
    age_userInput = tk.Entry(window_two)
    age_userInput.pack()
    
    def send_data():
        new_animal_name = name_userInput.get()
        new_animal_age = age_userInput.get()

        conn.createAnimal(new_animal_name,new_animal_age)
    
    tk.Button(window_two, text = "update", command = send_data).pack(anchor="w")


def delete_Animal():
    animal_id = id_userInput.get()

    conn.deleteAnimal(animal_id)


def main():

    tk.Button(root, text="Search", command=get_Animal_By_Id).pack(anchor="w")
    tk.Button(root, text = "All Animals", command=get_All_Animals).pack(anchor="w")
    tk.Button(root, text = "Create Animal", command=create_Animal).pack(anchor="w")
    tk.Button(root, text = "Update Animal", command=update_Animal).pack(anchor="w")
    tk.Button(root, text = "Delete Animal", command=delete_Animal).pack(anchor="w")

    root.mainloop()


if __name__ == "__main__":
    main()

