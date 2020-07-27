import re

class ReadTextfile():
    """
    Reads in a TextFile, and extracts the headers and saves the main data block
    to an array and the headers to a dictionary
    """
    def __init__(self, filename):
        with open(filename, 'r') as inputfile:
            content = inputfile.read()
        self.content = content
        self.nChars = len(content)
        self.nLines = content.count('\n')
        self.nWords = len(content.split())
        self.headers = self.extract_header()
        self.data_frame = self.save_to_array()

    def extract_all_data(self):
        """
        :return all data from after the first occurrence of the string "Grid-ref"
        """
        return self.content[self.content.index("Grid-ref"):]

    def extract_header(self):
        """
        Use regex and the string.split method to isolate information from within brackets.
        :return: a dict of the header information from the text file
        """
        headers = {}
        string = re.findall(r"\[.*?]", self.content)
        pat = re.compile(r'\d{2,4}-\d{2,4}')
        pat2 = re.compile(r'\d+\.\d{1,2}')
        for s in string:
            s_remove_brackets = s[1:-1]
            s_split = s_remove_brackets.split('=')
            hyphens = re.findall(pat, s_split[1])
            decimals = re.findall(pat2, s_split[1])
            if len(hyphens) > 0 and len(decimals) > 0:
                headers[s_split[0]] = list(map(float, s_split[1].split('-')))
            elif len(hyphens) > 0 and len(decimals) == 0:
                headers[s_split[0]] = list(map(int, s_split[1].split('-')))
            elif len(hyphens) == 0 and len(decimals) > 0:
                headers[s_split[0]] = list(map(float, s_split[1].split(',')))
            else:
                headers[s_split[0]] = list(map(int, s_split[1].split(',')))
            if len(headers[s_split[0]]) == 1:
                headers[s_split[0]] = headers[s_split[0]][0]
        return headers

    def extract_data_block(self):
        """
        Splits all the data at each "Grid-ref" reference, removes trailing new lines and split on \n
        :return: A list of data blocks containing precipitation data and the grid ref.
        """
        data_block = []
        data = self.extract_all_data()
        data_blocks = re.split(r"Grid-ref=  ", data)
        for block in data_blocks:
            block.strip().rstrip()
            if len(block) > 0:
                block_strip = block.strip().rstrip('\n')
                block_split = block_strip.split('\n')
                data_block.append(block_split)
        return data_block

    def extract_data_frame(self):
        """
        Splits the data_block list into the grid ref and then further lists of precipitation data.
        :return: A list of lists
        """
        data_frame = []
        data_block = self.extract_data_block()
        n = 0
        for block in data_block:
            int_block = []
            grid_refs = list(map(int, block[0].split(',')))
            int_block.append(grid_refs)
            for i in range(0, len(block[1:])):
                try:
                    block_split = [int(x) for x in block[1:][i].split()]
                    int_block.append(block_split)
                except:
                    break
            data_frame.append(int_block)
            n += 1
        return data_frame

    def save_to_array(self):
        """
        :return:An array of all the data in the text file, each item contains the "Grid-ref", date and value
        """
        db_array = []
        for block in self.extract_data_frame():
            year = int(self.headers['Years'][0])
            for i in range(1, len(block[1]) - 1):
                for month in range(0, len(block[1])):
                    db_row = []
                    date = str(month+1)+'/'+'1'+'/'+str(year)
                    db_row.append(block[0][0])
                    db_row.append(block[0][1])
                    db_row.append(date)
                    db_row.append(block[i][month])
                    db_array.append(db_row)
                year += 1
        return db_array
