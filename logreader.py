import imp
import os.path
import urllib.request

def import_log():
    local_copy = 'http_access_log.txt'
    # define log file variable
    local_copy, headers = urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log', local_copy)

