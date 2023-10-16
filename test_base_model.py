#!/usr/bin/python3
from models.base_model import BaseModel

def print_model_info(model):
print(model)
model.save()
print(model)

def print_json_info(model_json):
print("JSON of my_model:")
for key, value in model_json.items():
print(f"\t{key}: ({type(value)}) - {value}")

def main():
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89

# Print information about the original model
print_model_info(my_model)

my_model_json = my_model.to_dict()
print_json_info(my_model_json)

if __name__ == "__main__":
main()
