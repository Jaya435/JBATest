import unittest
from save_file.read_file import ReadTextfile
import sqlite3
from save_file.create_db import Input

class TestReadFileSuccess(unittest.TestCase):

    def setUp(self):
        self.test_data = 'test/test_data.pre'
        self.file = ReadTextfile(self.test_data)

    def testReadHeaderSuccessfully(self):
        self.assertEqual(4, int(self.file.headers['Boxes']), "Function did not return  the correct number of boxes")

    def testExtractDataFrameSuccessfully(self):
        self.assertGreater(len(self.file.data_frame), 0, "Dataframe was not created successfully")

    def testDataFrameContainsCorrectData(self):
        first_line_jan = [3, 318, '1/1/1991', 249]
        fifth_line_march = [3, 318, '3/1/1994', 113]
        self.assertEqual(first_line_jan, self.file.data_frame[0], "January 1991 value is incorrect")
        self.assertEqual(fifth_line_march, self.file.data_frame[38], "March 1994 line is incorrect")

    def testDateColumnInCorrectFormat(self):
        june_date = '6/1/1998'
        self.assertEqual(june_date, self.file.data_frame[89][2], '1st June 1998 is incorrect')


class TestSaveTestFiletoDB(unittest.TestCase):
    def setUp(self):
        self.test_data = 'test/test_data.pre'
        self.file = ReadTextfile(self.test_data)
        self.input = Input('temp.db')
        self.input.setting()

    def test_sqlite3_create_table_success(self):
        conn = sqlite3.connect('temp.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PRECIPITATION';")
        tb_name = cursor.fetchone()[0]
        self.assertEqual('PRECIPITATION', tb_name, "Precipitation table was not created")

    def test_sqlite3_insert_success(self):
        self.input.submit(self.file.data_frame)
        self.assertEqual(self.input.count('after'), 480, "There are not the correct number of rows in the table")


if __name__ == '__main__':
    unittest.main()