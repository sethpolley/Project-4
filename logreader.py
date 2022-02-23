from calendar import weekday
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
    Feb = open('February.txt', 'x')
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

    global total_count, month_dict, day_of_week_dict, week_dict, unsuccessful_count, redirect_count, file_list
    total_count = 0
    month_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    day_of_week_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    week_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: 0, 47: 0, 48: 0, 49: 0, 50: 0, 51: 0, 52: 0, }
    unsuccessful_count = 0
    redirect_count = 0
    file_list = []

    # define global lists & dictionaries that will be needed to answer questions

    month_file_ref = ['','January.txt', 'February.txt', 'March.txt', 'April.txt', 'May.txt', 'June.txt', 'July.txt', 'August.txt', 'September.txt', 'October.txt', 'November.txt', 'December.txt']

    # create a list that each element position (1:'January.txt') matches the # of the month
    # so that the '.month' attribute can be used to specify which file a new line will be added to

    for i in x:
    
    # for expression allows program to analyze each line of the list of lines individually

        total_count += 1

        # increment total count 
        
        lines_objects = regex_parser.split(i)
        if len(lines_objects) != 8:
            continue
    
        # break each line up into list of individual objects, continue if line has error of some sort

        timestamp = datetime.strptime(lines_objects[2], '%d/%b/%Y')

        # convert datestring up into date object

        month_dict[timestamp.month] += 1

        # increment month counter

        day_of_week_dict[weekday(timestamp.year,timestamp.month,timestamp.day)] += 1

        # increment day of the week counter 

        week_dict[((timestamp.isocalendar)[1])] += 1

        # increment week counter 

        if lines_objects[5] >= 400:
            unsuccessful_count += 1
        if lines_objects[5] >= 300 and lines_objects < 400:
            redirect_count += 1
        
        # increment unsuccessful & redirect counts based on value of lines_objects[5]

        file_list.append(lines_objects[4])

        # add file name to new file_list

        month_file = open(month_file_ref[timestamp.month], 'a')
        log_entry = i + ' \n'
        month_file.write(log_entry)
        month_file.close

        # open month-specific file, write line to it, close it

