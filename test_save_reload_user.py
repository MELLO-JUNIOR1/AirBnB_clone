#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

def print_reloaded_objects():
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id, obj in all_objs.items():
print(obj)

def create_and_print_user(first_name, last_name, email, password):
user = User()
user.first_name = first_name
user.last_name = last_name
user.email = email
user.password = password
user.save()
return user

def main():
print_reloaded_objects()

# Create and print the first user
print("-- Create a new User --")
my_user = create_and_print_user("Betty", "Holberton", "airbnb@holbertonschool.com", "root")
print(my_user)

# Create and print the second user
print("-- Create a new User 2 --")
my_user2 = create_and_print_user("John", "", "airbnb2@holbertonschool.com", "root")
print(my_user2)

if __name__ == "__main__":
main()
