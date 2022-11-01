## AirBnB clone - The console
# Descripton
The AirBnB is a website which presents a digital platform to access the services of a privately owned lodging available for rents and you could sort through the listings by location - by state and city as well as amenities available at each AirBnB.<br>

This project is to build a structural basis for data access, manipulation and database storage behind the hood of this website

# Concepts
Command interpreter<br>
Data Structures/Model<br>
Storage Engine<br>
JSON format<br>
# Command interpreter
A command interpreter is the part of a computer operating system that understands and executes commands that are entered interactively by a human being or from a program. In some operating systems, the command interpreter is called the shell.<br>

Our shell is limited to a specific use case which enable us to manage the objects of our project:<br>

-> Create a new object (ex: a new User or a new Place)

-> Retrieve an object from a file, a database etc…

-> Do operations on objects (count, compute stats, etc…)

-> Update attributes of an object

-> Destroy an object

With our command line interpreter, we are creating a base for future projects such as HTML/CSS templating, database storage, API, front-end integration…

# How to start the Command interpreter
we created a program called 'console.py' that contains the entry point of the command interpreter. Running this program on the command line starts up the shell. This shell was built using the python Cmd module with the class definition class HBNBCommand(cmd.Cmd):

# How to use the Shell interpreter
The following features are built in our command interpreter:

1. quit and EOF to exit the program<br>

2. help (this action is provided by default by cmd but you should keep it 
    updated and documented as you work through tasks)<br>

3. a custom prompt: (hbnb)<br>

4. an empty line + ENTER shouldn’t execute anything<br>

5. create: Creates a new instance of our BaseModel, saves it (to the JSON file)
   and prints the id. Ex: $ create BaseModel<br>

6. show: Prints the string representation of an 
   instance based on the class name and id<br>

7. destroy: Deletes an instance based on the 
   class name and id (save the change into the JSON file).<br>

8. all: Prints all string representation of all instances
   based or not on the class name.<br>

9. update: Updates an instance based on the class name and id 
   by adding or updating attribute (save the change into the JSON file).<br>
# Examples
1. $ create BaseModel
    If the class name is missing, print ** class name missing ** (ex: $ create)
    If the class name doesn’t exist, print ** class doesn't exist 
    ** (ex: $ create MyModel)
2. $ show BaseModel 1234-1234-1234.
    If the class name is missing, print ** class name missing ** (ex: $ show)
    If the class name doesn’t exist, print 
        ** class doesn't exist ** (ex: $ show MyModel)
    If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
    If the instance of the class name doesn’t exist for the id, print 
        ** no instance found ** (ex: $ show BaseModel 121212)
3.  $ destroy BaseModel 1234-1234-1234.
      If the class name is missing, print ** class name missing ** (ex: $ destroy)
      If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
      If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
      If the instance of the class name doesn’t exist for the id, print ** no instance found ** 
        (ex: $ destroy BaseModel 121212)
4.  $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
      Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        You can assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type
      If the class name is missing, print ** class name missing ** (ex: $ update)
      If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ update MyModel)
      If the id is missing, print ** instance id missing ** (ex: $ update BaseModel)
      If the instance of the class name doesn’t exist for the id, print ** no instance found ** 
        (ex: $ update BaseModel 121212)
      If the attribute name is missing, print ** attribute name missing ** (ex: $ update BaseModel existing-id)
      If the value for the attribute name doesn’t exist, print ** value missing ** 
        (ex: $ update BaseModel existing-id first_name)
    All other arguments should not be used (Ex: $ update BaseModel 1234-1234-1234 email 
    "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com")
    id, created_at and updated_at cant’ be updated. You can assume they won’t be passed in the update command
    Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to 
    update list of ids or datetime
# Data Structures/Model
A base model defines a class which suffices for our website methods 'foundation'. Most functions and fields in our overall framework would inherit this class. Essentially, this class renders all data inputs into their appropriate structures and format.

# Storage Engine
For this stage, our basic storages are simple python modules. These modules accepts JSON strings and allows for deserialization to class instances.

# JSON format
JSON stands for Javascript Object Notation and is a convenient and human-readable way to represent data. In this project mosts and the data structure packets are rendered to JSON format for ease of file storage.

# Bugs
No Bugs

# Authors
@Josh-121<br>

@FrancisOkolo<br>
'
