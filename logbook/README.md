# All Of Part 0

## What programs and files are
- program = set of instructions that are stored in a file
- jupyter notebook = combination of programs and notes
- programs are stored in a file, the format is plain text, meaning it can be edited

## File extensions
- file extensions give clues about the language used for the program
  - .py = python program
  - .rb = ruby program
  - .java = java program
etc etc

## File naming
- putting spaces in file names is a bad idea, underscores are better, an example being test_program.py

## Why plain text matters
- using plain text is efficient as its been around since the start of programming (1960), meaning they should always be able to be opened
- we're able to detect differences between versions of program files meaning we can store versions of them in a version control system (git)

## Python program files
- python programs are plain text files that can be opened in hundreds of applications, different from word files which are specific to one application

## Jupyter notebooks
- jupyter notebooks - contain program code, notes, documentation. the programs are in python, the notes are called markdown, stored together in a format called json
- many tools can use the json to show the contents of the notebook (.ipynb)

## editing notebooks
- a jupyter notebook is a mix of documentation, code, and output
- code is split into cells, which are run one at a time
- cells are executed from top to bottom
- output appears directly under the cell that was run
- notebooks are good for learning and experimenting, not just writing final programs

## tools of the trade
- there are different ways to write and edit jupyter notebooks
- jupyter notebooks run in a browser
- commonly used tools include:
  - jupyter notebook
  - jupyter lab
  - vscode
- vscode can open and edit notebooks like a normal file
- notebooks can contain both code cells and markdown cells
- markdown cells are used for notes and explanations
- code cells are used for actual python code

## just a file
- notebooks are just files stored on your computer
- they can be copied, moved, renamed, and deleted like any other file
- they usually end with the .ipynb extension
- the contents are saved automatically as you work
- because they are files, they can be shared or uploaded

## jupyter notebooks
- jupyter notebooks open in a web browser
- you can add cells above or below
- cells can be:
  - code cells
  - markdown cells
- shift + enter runs the current cell
- notebooks show code and results together

## python
- python code is written inside code cells
- code runs line by line when the cell is executed
- variables stay in memory between cells
- errors appear directly under the cell that caused them

## r code
- notebooks can also contain r code
- r is another programming language, commonly used for statistics
- similar idea to python notebooks, but different language and syntax

## notebooks +
- notebooks are stored as files on disk
- the file contains all code, notes, and outputs
- because of this, notebooks can get large
- outputs like graphs and tables are saved inside the file

## recap
- a jupyter notebook is a file
- it contains code, notes, and output
- it is edited using cells
- cells can be run individually
- notebooks are useful for learning, experimenting, and explaining code

## why use json?
- notebooks are stored using json
- json is a structured text format
- it allows different tools to read the same notebook file
- this is why notebooks can be opened in many editors
- json makes notebooks portable and flexible


# all of part 1

## git and version control
- git is a version control system
- version control helps track changes to files over time
- it lets you go back to older versions of your work
- useful when working alone or with other people
- mainly used for managing source code

## introducing version control
- version control systems manage changes to documents
- they keep a history of edits
- multiple people can work on the same files
- conflicts can be detected and resolved
- git is one of the most widely used systems

## what is git?
- git is a distributed version control system
- it tracks changes to files in a project
- each change is recorded as a snapshot
- you can move backwards and forwards between versions
- works locally on your machine

## versions and repos
- a repository (repo) stores a project and its history
- each version represents a state of the project
- versions are created when changes are saved
- the repo keeps track of all versions over time

## a new version
- a new version is created when changes are committed
- a commit records what changed and when
- commits have messages describing the change
- versions help understand how a project evolved

## staging and the repo
- files are first added to a staging area
- staging lets you choose what will go into the next version
- once staged, changes can be committed
- the repository stores all committed versions

## how it works
- files start in a working directory
- changes are staged
- staged changes are committed
- commits are stored in the repository
- this cycle repeats as you work

## why use git?
- keeps a complete history of your project
- makes it easier to recover from mistakes
- supports collaboration
- allows experimentation without breaking everything
- widely used in industry

## git commands
- git is controlled using commands in the terminal
- commands tell git what action to perform
- common commands include:
  - status
  - add
  - commit
  - clone
  - pull
  - push

## status
- shows the current state of the repository
- tells you which files are modified
- shows which files are staged
- useful to check before committing

## add
- adds files to the staging area
- prepares changes to be committed
- you can add specific files or everything
- staging does not save changes permanently

## commit
- creates a new version of the project
- saves staged changes to the repository
- each commit has a message
- messages describe what was changed

## welcome to github
- github is an online service for git repositories
- it hosts repos on the internet
- allows sharing and collaboration
- commonly used for open source projects

## github
- github stores repositories remotely
- provides tools for collaboration
- includes features like issues and pull requests
- works together with git

## using github
- you can push local repos to github
- others can clone or pull your repo
- changes can be shared between machines
- useful for backup and teamwork

## workflow
- create or modify files
- check status
- add changes
- commit changes
- push to github
- repeat as needed

## devices
- git allows working across multiple devices
- changes can be pushed from one device
- pulled onto another device
- keeps work in sync

## git commands (remote)
- some commands work with remote repositories
- used when interacting with github
- require an internet connection

## clone
- creates a local copy of a remote repository
- downloads the full project and history
- used when starting work on an existing repo

## fetch and pull
- fetch downloads changes from a remote repo
- pull fetches and merges changes
- keeps your local repo up to date
- pull is commonly used

## push
- sends local commits to a remote repo
- updates github with your changes
- requires permission to push

## git is distributed
- every copy of a repo has full history
- no single central version is required
- allows offline work
- makes git reliable and flexible

## meet markdown
- markdown is a simple text formatting language
- used for notes and documentation
- easy to read and write
- commonly used in notebooks and github

## markup languages
- markup languages add structure to text
- they use special symbols for formatting
- examples include html and markdown
- markdown is lightweight and simple

## markdown on github
- github uses markdown for documentation
- readme files are written in markdown
- markdown is rendered automatically
- makes repos easier to understand

## learning markdown
- markdown is easy to learn
- small set of rules
- widely supported
- useful for writing notes and documentation

## emojis
- emojis can be used in markdown
- supported on github
- mainly used for visual emphasis
- optional, not required


# all of part 2

## the python interpreter
- python code is run by the python interpreter
- the interpreter reads python instructions and executes them
- you write code, the interpreter runs it
- errors happen when the interpreter can’t understand something

## meet the interpreter
- python runs one instruction at a time
- instructions are read from top to bottom
- if an error occurs, execution stops
- the interpreter shows error messages to help debug

## running the interpreter
- the interpreter can be run from the terminal
- you can type python code directly
- code runs as soon as you press enter
- useful for testing small bits of code

## ipython
- ipython is an enhanced version of the python interpreter
- provides better error messages
- supports extra features like tab completion
- commonly used with notebooks

## using values, doing maths
- python can work with numbers
- supports basic maths operations
- values can be combined using operators
- results are shown immediately

## python3 and ipython3
- python2 and python3 are different versions
- python3 is the modern version
- ipython3 runs using python3
- most systems now use python3 by default

## a quick note on types
- every value in python has a type
- the type defines what you can do with a value
- common types include numbers and text
- types affect how operations behave

## variables and values
- variables store values
- a variable is created when you assign a value
- the variable name refers to the value
- values can be reused by referencing the variable

## variables and input
- variables can store user input
- input is read as text by default
- input can be assigned to a variable
- user input allows interaction

## variables and expressions
- expressions combine values and operators
- variables can be used inside expressions
- expressions are evaluated by the interpreter
- the result can be stored in a variable

## more data types
- python supports many data types
- different types are used for different purposes
- choosing the right type matters
- some types are more flexible than others

## python data types
- common data types include:
  - int (whole numbers)
  - float (decimal numbers)
  - str (text)
  - bool (true or false)
- each type behaves differently

## python lists
- lists store multiple values in one place
- values are ordered
- lists can contain different types
- items are accessed by index

## choosing a collection
- collections store groups of values
- different collections have different features
- lists are good for ordered data
- choice depends on how the data is used

## a list
- a list is written using square brackets
- items are separated by commas
- lists can be modified after creation
- items can be added or removed

## python in notebooks
- python code can be run inside notebooks
- each cell can contain code
- output appears below the cell
- notebooks keep code and output together

## packages
- packages add extra functionality to python
- they are collections of code
- packages can be installed when needed
- allow reuse of existing solutions

## jupyter recap
- jupyter is used to run notebooks
- notebooks open in a web browser
- supports python and other languages
- useful for learning and experimentation

## vs code and pycharm
- vscode and pycharm are code editors
- both can be used for python
- they support notebooks and scripts
- provide tools for writing and debugging code


# all of part 3

## express everything once
- programs often repeat similar actions
- repetition can be handled using loops
- writing the same code multiple times is inefficient
- loops help reduce duplication

## dry code
- dry means "don’t repeat yourself"
- repeated code makes programs harder to change
- repeating logic increases the chance of bugs
- loops and functions help keep code dry

## wet code
- wet code repeats the same logic
- harder to maintain and update
- changes must be made in multiple places
- should generally be avoided

## a note on comments
- comments explain what code is doing
- they are written for humans, not the computer
- comments help with readability
- useful when code is not obvious

## elements of programming
- programming involves:
  - sequence
  - selection
  - repetition
- these elements describe how instructions are executed

## types of repetition
- repetition allows instructions to run multiple times
- different ways to repeat code exist
- loops are used for repetition
- common loop types include for and while

## deterministic logic
- deterministic code always produces the same result
- the same input gives the same output
- behaviour is predictable
- important for reliability

## indeterminate logic
- results may vary
- behaviour can depend on conditions
- output may change between runs
- often used with user input or external data

## iteration
- iteration means repeating a process
- loops iterate over data or ranges
- each loop step is an iteration
- iteration stops when a condition is met

## for
- for loops repeat code a set number of times
- commonly used with ranges
- useful when the number of repetitions is known
- often used to loop through collections

## while
- while loops repeat while a condition is true
- useful when the number of repetitions is unknown
- condition is checked before each iteration
- risk of infinite loops if not careful

## making data tables
- loops can be used to generate tables
- tables store structured data
- values can be calculated repeatedly
- results can be displayed in rows

## a times table
- loops can generate times tables
- values are calculated using multiplication
- each iteration produces a new row
- useful for learning loops

## a times table
- a times table can be built step by step
- each loop iteration adds a value
- results can be stored or printed
- shows repetition clearly

## run again
- code can be re-run easily
- changing values changes output
- loops make experiments quick
- useful for testing

## general times table
- loops can generate more flexible tables
- start and end values can be changed
- allows reuse of the same logic
- demonstrates parameterisation

## repetition patterns
- loops often follow patterns
- understanding patterns helps write better code
- patterns can be reused
- common in problem solving

## just loop
- simple loops repeat a single action
- minimal logic inside the loop
- useful for basic repetition
- easy to understand

## looping is for everyone
- loops are a core programming concept
- used in many languages
- once understood, they are very powerful
- essential for writing efficient programs

## a while pattern
- while loops follow a common pattern
- initialise variables
- check a condition
- update variables
- repeat until condition is false

## making lists
- loops can be used to build lists
- values are added one at a time
- useful for collecting results
- lists grow as the loop runs


# all of part 4

## lists and indexing
- lists store multiple values in order
- each item has a position called an index
- indexing starts at 0, not 1
- items are accessed using square brackets

## accessing list items
- list items are accessed by index
- negative indexes count from the end
- accessing an invalid index causes an error
- indexes are used to read or change values

## list length
- lists have a length
- length is the number of items in the list
- length can change as items are added or removed
- knowing the length helps control loops

## looping over lists
- lists can be looped through using for loops
- each iteration accesses one item
- avoids manual indexing
- common pattern in python

## modifying lists
- lists are mutable
- items can be changed after creation
- values can be updated by index
- changes affect the original list

## adding items
- items can be added to a list
- append adds an item to the end
- extend adds multiple items
- insert adds an item at a specific position

## removing items
- items can be removed from a list
- remove deletes a specific value
- pop removes by index
- clear removes all items

## lists and functions
- lists can be passed into functions
- functions can modify lists
- changes affect the original list
- useful for processing data

## lists in practice
- lists are used everywhere in python
- useful for storing collections of data
- often combined with loops
- core data structure to understand

## common list mistakes
- forgetting indexing starts at 0
- accessing out-of-range indexes
- modifying a list while looping
- confusing lists with other data types


# all of part 5

## good code is dry is important
- good code should be easy to read and change
- repeating code makes changes harder
- if you need to update something, you should only have to do it once
- dry code helps avoid mistakes

## dry code
- dry means "don’t repeat yourself"
- repeated code increases the chance of bugs
- repetition makes programs longer than they need to be
- dry code keeps logic in one place

## standard library
- python comes with a standard library
- the standard library contains pre-written code
- it solves common problems
- using it avoids rewriting code that already exists

## beyond the standard
- there are libraries beyond the standard library
- extra libraries can be installed when needed
- they extend what python can do
- using libraries helps keep code dry

## some terminology
- code reuse means using existing code instead of rewriting it
- libraries are collections of reusable code
- functions help reuse logic
- dry is a principle, not a rule

## not being wet
- wet code repeats the same logic
- changes must be made in multiple places
- this increases the risk of errors
- wet code is harder to maintain

## not being wet (again)
- avoiding wet code saves time
- dry code is easier to test
- dry code improves clarity
- following dry makes programs more reliable


# all of part 6

## making decisions
- programs often need to choose between different actions
- decisions depend on conditions
- conditions are checked while the program runs
- different code runs depending on the result

## conditions
- a condition is something that can be true or false
- conditions control which parts of code execute
- they are used to guide program flow
- conditions are evaluated by python

## boolean values
- boolean values are true or false
- they represent the result of a condition
- many operations produce boolean values
- booleans are used in decision making

## comparison operators
- comparisons check relationships between values
- common operators include:
  - ==
  - !=
  - <
  - >
  - <=
  - >=
- comparisons always return true or false

## if statements
- if statements run code only when a condition is true
- the condition is checked once
- code inside the if block must be indented
- indentation defines what belongs to the if

## else
- else runs when the if condition is false
- ensures one path always runs
- used for alternative behaviour
- pairs directly with if

## elif
- elif allows multiple conditions to be checked
- conditions are tested in order
- the first true condition runs
- remaining conditions are skipped

## combining conditions
- multiple conditions can be combined
- and requires all conditions to be true
- or requires at least one condition to be true
- allows more complex decisions

## logical flow
- decision statements change how code flows
- only certain blocks run depending on conditions
- helps programs react to different situations
- core concept in programming


# all of part 7

## strings
- strings are used to store text
- text is written inside quotes
- strings can contain letters, numbers, and symbols
- very commonly used in programs

## working with strings
- strings can be combined together
- text can be built up from smaller pieces
- operations on strings create new strings
- strings themselves do not change

## string indexing
- strings are ordered sequences
- each character has an index
- indexing starts at 0
- characters can be accessed individually

## string slicing
- parts of a string can be extracted
- slicing returns a new string
- useful for working with sections of text
- indexes control which part is selected

## string methods
- strings have built-in methods
- methods perform actions on strings
- common methods include:
  - lower
  - strip
  - upper
  - replace
- these methods will return new strings

## formatting strings
- strings can include values, meaning they could include numbers
- formatting makes output clearer
- variables can be inserted into text
- useful for printing results

## user input
- input allows users to enter data, which can be numerical or text
- input is always read as text
- input can be stored in variables
- often used with strings

## strings in practice
- strings are used when messages and prompts are used
- common in user interaction
- they are also used in practice when reading and writing files
- essential data type to understand



# all of part 8

## files
- programs can work with files
- files allow data to be stored permanently
- data can be saved and reused later
- useful for working with larger amounts of information

## opening files
- files must be opened before they can be used
- opening a file tells python how it will be used
- common modes include reading and writing
- the file must exist when opening for reading

## reading files
- files can be read line by line
- file contents are read as strings
- reading allows data to be processed
- often used for analysing stored data

## writing files
- programs can write data to files
- writing can overwrite existing content
- new files can be created if they don’t exist
- useful for saving output or results

## closing files
- files should be closed after use
- closing frees system resources
- prevents data corruption
- some tools close files automatically

## file paths
- files are stored in directories
- a path tells python where the file is located
- paths can be relative or absolute
- incorrect paths cause errors

## files in practice
- files are commonly used for data storage
- often combined with loops and strings
- allow programs to work beyond a single run
- important for real-world programs



# all of part 9

## errors
- errors happen when something goes wrong in a program
- errors stop code from running correctly
- python shows messages when errors occur
- error messages help identify the problem

## types of errors
- syntax errors happen when code is written incorrectly
- runtime errors happen while the program is running
- logic errors happen when code runs but gives the wrong result
- different errors need different fixes

## error messages
- error messages describe what went wrong
- they often point to the line causing the issue
- reading them carefully helps debugging
- they are meant to help, not punish you

## debugging
- debugging is the process of finding and fixing errors
- testing small sections of code helps
- checking values while code runs is useful
- debugging is a normal part of programming

## common mistakes
- incorrect indentation
- misspelt variable names
- using the wrong data type
- forgetting how values change

## testing code
- testing checks if code behaves as expected
- code should be tested with different inputs
- edge cases should be considered
- testing improves reliability

## writing better programs
- keep code simple
- use clear variable names
- comment where necessary
- structure code logically



# all of part 10

## wrapping things up
- this part is more of a big-picture wrap up
- less about learning new syntax
- more about understanding where python fits and where this could go next
- stuff you don’t need to fully understand yet, just be aware of

## classes (very briefly)
- python uses classes, even if we haven’t really focused on them
- we’ve already been using objects without realising it
- things like ints, strings, lists are all objects
- classes are just a way of grouping data and behaviour together

## objects everywhere
- in modern python, basically everything is an object
- numbers, strings, lists, etc all come from classes
- you don’t need to worry about this deeply yet
- it just explains why some things have methods attached to them

## not something to stress about
- you can write perfectly good python without knowing oop properly
- that’s what we’ve been doing so far
- oop becomes more important in bigger projects
- for now it’s just useful context

## python vs other languages
- python and java are both very popular
- python is quicker to write and easier to read
- java is more verbose but very structured
- different languages are better for different jobs

## typing differences
- python figures out types as you go
- java forces you to define types up front
- python is faster to prototype with
- java is stricter but can catch errors earlier

## which is better?
- there isn’t really a “best” language
- python is good for learning, scripting, data, quick systems
- java is good for large, structured, long-term systems
- once you know one language, others are easier to learn

## final takeaway
- the core ideas matter more than the language
- things like dry code, loops, decisions, and structure carry over
- python is a good starting point
- this course is about fundamentals, not mastering everything




## completed

# apologies if it's too long or doesn't make much sense, all my notes were in a PowerPoint document before this week until I realisd they had to be in a markdown file and formatting.
# converting it to that was very last minute so the numbered slides which we had to make note of underneath each 'part' might not be in the right order
## however after proofreading it i believe all the notes are at least under the correct 'part', just possibly not in the right order as they should've been on the site