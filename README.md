0x00. AirBnB clone - The console
Welcome to the AirBnB clone project!
Before starting, please read the AirBnB concept page.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

Description of Project
For this task, we are tasked to build our first full web application:
the Airbnb clone. This task is crucial as the knowledge gained here will help
build the following projects: HTML/CSS templating, database storage, API, front-end integration…

We were assigned to:
Create a parent class (called BaseModel) which will take care of the
initialization, serialization, and deserialization of your future instances.
Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
Create the first abstracted storage engine of the project: File storage.
Create all unittests to validate all our classes and storage engin


Description of Command Line Interpreter:
A command interpreter, often referred to as a command-line interpreter (CLI)
or shell, is a text-based interface that allows users to interact with a computer
or software by entering commands.

How to Start a Command Interpreter:
Windows:
On Windows, you can use the Command Prompt (cmd) or PowerShell.
Press Win + R to open the Run dialog, type cmd or powershell, and press Enter.
Linux/Unix:

On Linux or Unix-based systems, you can use the Terminal.
You can typically find it in the system applications menu, or use a keyboard shortcut like Ctrl + Alt + T.
macOS:

On macOS, you can use the Terminal.
You can find it in the Utilities folder within the
Applications folder, or use Spotlight (Cmd + Space) to search for it.

How to Use a Command Interpreter:
Enter Commands:

Once the command interpreter is open, you can type commands directly into the terminal or command prompt.
Navigate Directories:

Use commands like cd to change directories.
Execute Programs:

Run executable programs by typing their names.
View and Edit Files:

Use commands like cat, ls, dir, nano, or vim to view or edit files.
Manage Files and Directories:

Use commands like mkdir to create directories, rm or del to remove files, and cp or copy to copy files.
Get Help:

Use --help or -h with commands to get information on how to use them.

Examples:
Navigate Directories: cd Documents

List Files:ls - # On Linux/Unix, dir - # On Windows

Create a Directory: mkdir NewDirectory

Copy Files: cp file.txt backup/

Run a Python Script: python script.py

View File Content:cat readme.txt - # On Linux/Unix, type readme.txt - # On Windows

Remove a File: rm file.txt - # On Linux/Unix, del file.txt - # On Windows
