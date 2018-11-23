import unittest
import Python_coding_Assignment_Clootrack

sample_file_names_list = ['Sample1.txt']

class TestingProgram(unittest.TestCase):
    def testing_function(self, input_from_file):
        input_from_file = self.input_from_file
        required_index = input_from_file.index('Input')
        Python_coding_Assignment_Clootrack.number_of_inputs = input_from_file[0]
        Python_coding_Assignment_Clootrack.no_of_tweets = input_from_file[1]

def text_fixtures():
    input_output_list = []
    with open(f'.\{sample_file_names_list}','r') as sf1:
        input_output_list.append(sf1.readlines())
    