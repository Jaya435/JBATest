# JBA Code Challenge

Repository contains python project that can read in a text file then extract the headers and main body of data. The header is transformed into a dictionary and the main data body is transformed into an array to be inserted into an sqlite3 database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to run this programme using Python3. You can do this by creating a virtual environment as below:

```
python3 -m venv /path/to/new/virtual/environment
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repository onto your local machine
```
https://github.com/Jaya435/JBATest.git
```
Then run
```
python save_file_to_db.py --input cru-ts-2-10.1991-2000-cutdown.pre --output test.db
```
The --output flag is optional and defines the name of the database that will be created when the programme is run.

Once the programme is run, you can view the data stored in the system either by using an sqlite3 application. Or by opening a python interpreter and running:
```
import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
for row in cursor.execute('SELECT * from PRECIPITATION LIMIT 36'): print(row)
```
This prints out the first 3 years of precipitation data from the first datablock.

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Authors

* **Tom Richmond** - *Initial work* - [Jaya435](https://github.com/Jaya435/)
