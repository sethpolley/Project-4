import imp
import os.path
import urllib.request
import re
from datetime import datetime

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


def parser_main(x):
    
    regex_parser = re.compile('(.*?) - - \[(.*?):(.*) .*\] \"[A-Z]{3,6} (.*?)( HTTP.*\"|\") ([2-5]0[0-9])')
    
    # define variable to tokenize list objects

    month_list = []
    day_of_week_list = []
    week_list = []
    unsuccessful_list = []
    redirect_list = []
    file_list = []

    # define lists that will be needed to answer questions

    for i in x:

    # for expression allows program to analyze each line of the list of lines individually

        lines_objects = regex_parser.split(i)

        # break each line up into list of individual objects


