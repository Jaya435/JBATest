# JBA Code Challenge

This Repository contains a python project that can read in a file, extract the headers, and transform the main body of data. The header is transformed into a dictionary and the main data body is transformed into an array to be inserted into an sqlite3 database.

## Getting Started

These instructions will let you get a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to run this programme using Python3. You can follow a guide here to install Python3 on your local machine https://installpython3.com/. Once Python3 is installed, you can run this programme from within a virtual environment. You can do this by creating a virtual environment as below:

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
python save_file/save_file_to_db.py --input cru-ts-2-10.1991-2000-cutdown.pre --output db/test.db
```
The --output flag is optional and defines the name of the database that will be created when the programme is run.\

The --input flag is mandatory and relates to the file you would like to be read.

```
usage: save_file_to_db.py [-h] -i INPUT [-o OUTPUT]

Process a .pre file and save to a .db

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file name
  -o OUTPUT, --output OUTPUT
                        Output file name, default is rainfall.db
```

Once the programme is run, you can view the data stored in the system either by using an sqlite3 application, or by opening a python interpreter and running:
```
import sqlite3
conn = sqlite3.connect("db/test.db")
cursor = conn.cursor()
for row in cursor.execute('SELECT * from PRECIPITATION LIMIT 36'): print(row)
```
This prints out the first 3 years of precipitation data from the first datablock.

## Running the tests

The automated tests can be run using the below command:
```
python3 -m unittest discover
```

## Authors

* **Tom Richmond** - *Initial work* - [Jaya435](https://github.com/Jaya435/)
