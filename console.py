#!/usr/bin/python3
'''Method Command Interpreter'''
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
prompt = '(hbnb) '
__classes = [
"Amenity",
"BaseModel",
"City",
"Place",
"Review",
"State",
"User"
]

def do_create(self, args):
'''Create a new instance of BaseModel, save it, and print the id
Usage: create <class name>
'''
args = args.split()
if not args:
print("** class name missing **")
elif args[0] not in HBNBCommand.__classes:
print("** class doesn't exist **")
else:
new_creation = eval(args[0] + '()')
storage.save()
print(new_creation.id)

def do_show(self, args):
'''Print the string representation of a specific instance
Usage: show <class name> <id>
'''
strings = args.split()
if not strings:
print("** class name missing **")
elif strings[0] not in HBNBCommand.__classes:
print("** class doesn't exist **")
elif len(strings) == 1:
print("** instance id missing **")
else:
obj = storage.all()
key_value = strings[0] + '.' + strings[1]
print(obj.get(key_value, "** no instance found **"))

def do_destroy(self, args):
'''Delete an instance
Usage: destroy <class name> <id>
'''
args = args.split()
objects = storage.all()

if not args:
print('** class name missing **')
elif args[0] not in HBNBCommand.__classes:
print("** class doesn't exist **")
elif len(args) == 1:
print('** instance id missing **')
else:
key_find = args[0] + '.' + args[1]
objects.pop(key_find, None)
storage.save()

def do_all(self, args):
'''Print a string representation of all instances
Usage: all <class name>
'''
args = args.split()
objects = storage.all()
new_list = []

if not args:
for obj in objects.values():
new_list.append(obj.__str__())
print(new_list)
elif args[0] not in HBNBCommand.__classes:
print("** class doesn't exist **")
else:
for obj in objects.values():
if obj.__class__.__name__ == args[0]:
new_list.append(obj.__str__())
print(new_list)

def do_update(self, args):
'''Update an instance
Usage: update <class name> <id> <attribute name> "<attribute value>"
'''
objects = storage.all()
args = args.split(" ")

if not args:
print("** class name missing **")
elif args[0] not in HBNBCommand.__classes:
print("** class doesn't exist **")
elif len(args) == 1:
print("** instance id missing **")
elif len(args) == 2:
print("** attribute name missing **")
elif len(args) == 3:
print("** value missing **")
else:
key_find = args[0] + '.' + args[1]
obj = objects.get(key_find, None)

if not obj:
print("** no instance found **")
return

setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
storage.save()

# Other methods remain unchanged

def emptyline(self):
'''Don't execute anything when the user presses enter on an empty line'''
pass

if __name__ == '__main__':
HBNBCommand().cmdloop()
