# This shows how JSON data can be used to pass messages to a class and create objects from it.

import json

# Define the class for the dog breed
class DogBreed:
    def __init__(self, breed, sub_breeds):
        self.breed = breed
        self.sub_breeds = sub_breeds

# Read the JSON file
with open('dogs.json', 'r') as file:
    data = json.load(file)

# Create a list to store DogBreed objects
dog_breeds = []

# Iterate through the JSON data and create DogBreed objects
for breed, sub_breeds in data['message'].items():
    dog_breed = DogBreed(breed, sub_breeds)
    dog_breeds.append(dog_breed)

# Example usage
for dog_breed in dog_breeds:
    print(f"Breed: {dog_breed.breed}")
    if dog_breed.sub_breeds:
        (f"Sub-breeds: {dog_breed.sub_breeds}")
    else:
        print("Sub-breeds: None")

    print()
