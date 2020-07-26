#!/usr/bin/python

import argparse
from create_db import Input
import read_file
import datetime
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class SaveTextFiletoDB():
    """
    Saves input file into a database file, using the read_file method.
    """

    def __init__(self, file, filename):
        self.file = read_file.ReadTextfile(file)
        self.input = Input(filename)
        self.header = self.file.headers
        self.data_frame = self.file.save_to_array()

    def save_to_db(self):
        '''
        :return: a .db file with data extracted from the input file
        '''
        self.input.setting()
        start_time = datetime.datetime.now()
        self.input.submit(self.data_frame)
        logging.info("Data uploaded in {} seconds".format(datetime.datetime.now() - start_time))


if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(description='Process a .pre file and save to a .db')

    # add arguments to the parser
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name, default is rainfall.db', default="rainfall.db")

    # parse the arguments
    args = parser.parse_args()
    db = SaveTextFiletoDB(args.input, args.output)
    db.save_to_db()
