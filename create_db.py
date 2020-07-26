import sqlite3
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class Input:
    """Saves an array of data into an sqlite3 database named by filename."""
    def __init__(self, filename):
        self.filename = filename

    def setting(self):
        """
        Creates a table in the database called PRECIPITATION and drops one if it already exists
        :return:
        """
        conn = sqlite3.connect('/db/' + self.filename)
        logging.info("Opened database successfully")
        try:
            conn.execute('''DROP TABLE IF EXISTS PRECIPITATION;''')
            conn.execute('''CREATE TABLE PRECIPITATION (
                            Xref INTEGER,
                            Yref INTEGER,
                            Date TEXT,
                            Value INTEGER
                            );'''
                         )
            self.count('before')
        except:
            pass
        conn.close()

    def submit(self,db_array):
        '''
        :param db_array: An array of data to be inserted
        :return: Insert values into precipiation table
        '''
        self.db_array = db_array
        try:
            sqliteConnection = sqlite3.connect(self.filename)
            cursor = sqliteConnection.cursor()
            logging.info("Successfully Connected to SQLite")

            cursor.executemany("INSERT INTO PRECIPITATION VALUES (?,?,?,?)", self.db_array)
            sqliteConnection.commit()
            cursor.close()
            self.count('after')
            logging.info("Successfully inserted PRECIPITATION data into sqlite table")

        except sqlite3.Error as error:
            logging.info("Failed to insert PRECIPITATION data into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()

    def select(self):
        '''
        :return: all rows in table PRECIPITATION
        '''
        conn = sqlite3.connect(self.filename)
        cursor = conn.cursor()
        for row in cursor.execute('SELECT * from PRECIPITATION'): logging.info(row)

    def count(self, time):
        '''
        :param time: when the count was taken
        :return: the maximum row number in the table
        '''
        conn = sqlite3.connect(self.filename)
        cursor = conn.cursor()
        cursor.execute('SELECT max(rowid) from PRECIPITATION')
        n = cursor.fetchone()[0]
        logging.info("Database rows {} upload: {}".format(time, n))