# this file has functions to generate the eda for the csv.

import pandas as pd 
import pandas_profiling
import matplotlib
matplotlib.use('Agg') #handling the runtime error for the 2nd instance
import socket
import time
import os
import boto3
from boto3.s3.transfer import S3Transfer


current_time = lambda: int(round(time.time()))
output_file_name = 'eda_profile'+ str(current_time()) + '.html'

credentials = { 
    'aws_access_key_id': 'AKIA4IY2R63BUN2HGB5M',
    'aws_secret_access_key': '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'
}

def eda_csv(file_name, host_val, s3_value):
    """getting the data from the file"""
    result = {}
    file_url = 'o'
    file_name_print = (file_name.split(sep='.')[-2]).split(sep='/')[-1]
    df = pd.read_csv(file_name, error_bad_lines=False, encoding="cp1252")
    # creating the pandas profile and saving the data to the file.

    profile = pandas_profiling.ProfileReport(df, title='Data profile : '+file_name_print, explorative=True)
    profile_file = profile.to_file('media/eda_folder/'+file_name_print+output_file_name)
    profile_link = 'http://'+host_val+'/media/eda_folder/'+file_name_print+output_file_name

    if int(s3_value) == 1:
        #s3 configuration, uploading the data for s3
        filename = file_name_print+output_file_name
        key = filename
        bucket = 'bucketstoredata'
        client = boto3.client('s3', 'ap-south-1', **credentials)
        transfer = S3Transfer(client)
        transfer.upload_file('media/eda_folder/'+file_name_print+output_file_name, bucket, key , extra_args={'ACL': 'public-read', 'ContentType':'text/html'})
        file_url = '%s/%s/%s' % (client.meta.endpoint_url, bucket, key)    
        

    describe = df.describe() #getting the overview of the df
    head = df.head()
    #return (head.to_dict()) # =converting the data to dictionary format 
    result['dimensions'] = df.shape
    result['sample_data'] = head.to_dict()
    result['data_description'] = describe.to_dict()
    result['profile_link'] = profile_link
    result['s3_url'] = file_url
    result['status_code'] = 200 
    result['host'] = socket.gethostbyname(socket.gethostname())
    result['host_val'] = host_val

    return result