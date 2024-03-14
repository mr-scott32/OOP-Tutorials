import tkinter as tk
from tkinter import ttk
import json

class DogBreed:
    def __init__(self, breed, sub_breeds):
        self.breed = breed
        self.sub_breeds = sub_breeds

def load_data():
    with open('dogs.json', 'r') as file:
        data = json.load(file)
    dog_breeds = []
    for breed, sub_breeds in data['message'].items():
        dog_breed = DogBreed(breed, sub_breeds)
        dog_breeds.append(dog_breed)
    return dog_breeds

def update_sub_breeds(event=None):
    breed = breed_combobox.get()
    sub_breeds = [""]
    for dog_breed in dog_breeds:
        if dog_breed.breed == breed:
            sub_breeds = dog_breed.sub_breeds
            break
    sub_breed_combobox['values'] = sub_breeds
    sub_breed_combobox.current(0)

def main():
    global breed_combobox, sub_breed_combobox, dog_breeds

    # Load data
    dog_breeds = load_data()

    # Create main window
    root = tk.Tk()
    root.title("Dog Breeds")

    # Breed label and combobox
    breed_label = ttk.Label(root, text="Select Breed:")
    breed_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    breed_combobox = ttk.Combobox(root, state="readonly")
    breed_combobox.grid(row=0, column=1, padx=10, pady=10)
    breed_combobox['values'] = [dog_breed.breed for dog_breed in dog_breeds]
    breed_combobox.bind("<<ComboboxSelected>>", update_sub_breeds)

    # Sub-breed label and combobox
    sub_breed_label = ttk.Label(root, text="Select Sub-Breed:")
    sub_breed_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    sub_breed_combobox = ttk.Combobox(root, state="readonly")
    sub_breed_combobox.grid(row=1, column=1, padx=10, pady=10)

    # Call update_sub_breeds initially to populate sub-breed combobox
    update_sub_breeds()

    root.mainloop()

if __name__ == "__main__":
    main()
