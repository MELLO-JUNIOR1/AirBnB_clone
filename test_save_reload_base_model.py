#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

def print_reloaded_objects():
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id, obj in all_objs.items():
print(obj)

def create_and_print_object():
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print(my_model)

def main():
print_reloaded_objects()
create_and_print_object()

if __name__ == "__main__":
main()
