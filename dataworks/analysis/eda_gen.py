# this file has functions to generate the eda for the csv.

import pandas as pd 
import pandas_profiling
import matplotlib
matplotlib.use('Agg') #handling the runtime error for the 2nd instance
import socket
import time
import os
from django.core.files.storage import FileSystemStorage


current_time = lambda: int(round(time.time()))
output_file_name = 'eda_profile'+ str(current_time()) + '.html'

def eda_csv(file_name, host_val):
    """getting the data from the file"""
    result = {}
    file_name_print = (file_name.split(sep='.')[-2]).split(sep='/')[-1]
    df = pd.read_csv(file_name, error_bad_lines=False, encoding="cp1252")
    profile = pandas_profiling.ProfileReport(df, title='Data profile : '+file_name_print, explorative=True)
    folder = 'eda_profile/'
    profile_file = profile.to_file('media/eda_folder/'+file_name_print+output_file_name)

    describe = df.describe() #getting the overview of the df
    head = df.head()
    #return (head.to_dict()) # =converting the data to dictionary format 
    result['dimensions'] = df.shape
    result['sample_data'] = head.to_dict()
    result['data_description'] = describe.to_dict()
    result['profile_link'] = {'file_path':'http://'+host_val+'/media/eda_folder/'+file_name_print+output_file_name}
    result['status_code'] = 200 
    result['host'] = socket.gethostbyname(socket.gethostname())
    result['host_val'] = host_val

    return result