#!/usr/bin/python3
from models.base_model import BaseModel

def print_model_info(model):
print(f"ID: {model.id}")
print(model)
print(f"Type of created_at: {type(model.created_at)}")

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89

# Print information about the original model
print_model_info(my_model)

print("--")

my_model_json = my_model.to_dict()
print("JSON of my_model:")
for key, value in my_model_json.items():
print(f"\t{key}: ({type(value)}) - {value}")

print("--")

# Create a new model using the JSON representation
my_new_model = BaseModel(**my_model_json)
print_model_info(my_new_model)

print("--")
print(f"Is my_model the same as my_new_model? {my_model is my_new_model}")
