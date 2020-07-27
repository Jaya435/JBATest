import unittest

import unittest
from read_file import ReadTextfile

class TestReadFileSuccess(unittest.TestCase):

    def setUp(self):
        self.test_data = 'test_data.pre'
        self.file = ReadTextfile(self.test_data)

    def testReadHeaderSuccessfully(self):

        self.assertEqual(4, int(self.file.headers['Boxes']), "Function did not return  the correct number of boxes")

    def testExtractDataFrameSuccessfully(self):
        self.assertGreater(len(self.file.data_frame), 0, "Dataframe was not created successully")

    def testDataFrameContainsCorrectData(self):
        first_line_jan = [3, 318, '1/1/1991', 249]
        fifth_line_march = [3, 318, '3/1/1994', 113]
        self.assertEqual(first_line_jan, self.file.data_frame[0], "January 1991 value is incorrect")
        self.assertEqual(fifth_line_march, self.file.data_frame[38], "March 1994 line is incorrect")

class TestSaveFileToDB(unittest.TestCase):
    def setUp(self):
        self.test_data = 'test_data.pre'
        self.file = ReadTextfile(self.test_data)


if __name__ == '__main__':
    unittest.main()