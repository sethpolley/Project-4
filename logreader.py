from calendar import weekday
import imp
import os.path
import urllib.request
import re
from datetime import datetime
from datetime import date
import datetime

# import modules

def import_log():
    local_copy = 'http_access_log.txt'
    # define log file variable
    local_copy, headers = urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log', local_copy)

# define import log file function 

logexists = os.path.exists('http_access_log')

if not logexists:
    import_log

# call import_log function if the log file does not exist

with open('http_access_log.txt', 'r') as http_info:
    lines = http_info.readlines()

# open the log file and break the file up into a list of elements in list 'lines'

def create_month_files():
    Jan = open('January.txt', 'x')
    Feb = open('Feburary.txt', 'x')
    Mar = open('March.txt', 'x')
    Apr = open('April.txt', 'x')
    May = open('May.txt', 'x')
    Jun = open('June.txt', 'x')
    Jul = open('July.txt', 'x')
    Aug = open('August.txt', 'x')
    Sep = open('September.txt', 'x')
    Oct = open('Octobe.txt', 'x')
    Nov = open('November.txt', 'x')
    Dec =  open('December.txt', 'x')

    # define function that creates month files

month_files_exist = os.path.exists('January.txt')

if not month_files_exist:
    create_month_files

# call create_month_files if they do not extist

def parser_main(x):
    
    regex_parser = re.compile('(.*?) - - \[(.*?):(.*) .*\] \"[A-Z]{3,6} (.*?)( HTTP.*\"|\") ([2-5]0[0-9])')
    
    # define variable to tokenize list objects

    month_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    day_of_week_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    week_list = []
    unsuccessful_list = []
    redirect_list = []
    file_list = []

    # define lists & dictionaries that will be needed to answer questions

    for i in x:
    
    # for expression allows program to analyze each line of the list of lines individually

        lines_objects = regex_parser.split(i)

        # break each line up into list of individual objects

        timestamp = datetime.strptime(lines_objects[2], '%d/%b/%Y')

        # convert datestring up into date object

        month_dict[timestamp.month] += 1

        # increment month counter

        day_of_week_dict[weekday(timestamp.year,timestamp.month,timestamp.day)] += 1

        # increment day counter 

        

