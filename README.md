# AirBnB clone
## Project Description
This a clone of the AirBnB application. The current implementation consists only of a **command interpreter** that allows us to manipulate our objects.

### The Command Interpreter
This feature will allow us to:
- create a new object
- retrieve an object from a file or database
- perform operations on an object
- update attributes of an object
- destroy an object

To use it, clone the repository to your local machine:
```git clone https://github.com/Fredasante/AirBnB_clone.git```

To start it, run the command:
```./console.py```
You are now ready to use the console to manipulate your AirBnB objects.

#### Operations
The table below shows some operations you can perform on the command interpreter:

Command | Description | Usage
-------- | ------------- | --------|
**help** or **?** | Displays the documented commands | `help`
**quit** or **EOF** | exit the program | `quit` or `EOF`
**create** | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id | `create <class name>`
**show** | Prints the string representation of an instance based on the class name and id | `show <class name> <id>`
**destroy** | Deletes an instance based on the class name and id and saves the change into the JSON file | `destroy <classname> <id>`
**all** | Prints all string representation of all instances based or not on the class name | `all <classname>` or `all`
**update** | Updates an instance based on the class name and id by adding or updating attribute and saves the change into the JSON file | `update <classname> <id> <attributename> <attributevalue>`
***count** |  Retrieves the number of instances of a class | `<classname>.count()`
***show** | Retrieves an instance based on its ID | `<classname>.show(<id>)`
***destroy#2** | Destroys an instance based on its ID | `classname>.destroy(<id>)`
***update#2** | Updates an instance based on its ID | `<classname>.update(<id>, <attributename>, <attributevalue>)`
***update#3** | Updates an instance based on its ID with a dictionary | `<classname>.update(<id>, <dictionary representation>)`

*Note*: The commands marked with an asterisk are WIP

### Tests
If you wish to run the tests for this application all of the test are located under the **test/** folder.
Execute them by running the command:
```python3 -m unittest discover tests```

from the root directory.

#### ENJOY :)

