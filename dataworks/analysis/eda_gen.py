# this file has functions to generate the eda for the csv.

import pandas as pd 
#import matplotbib.pyplot as plt 

def eda_csv(file_name):
    """getting the data from the file"""
    df = pd.read_csv(file_name)
    describe = df.describe() #getting the overview of the df
    head = df.head()
    return (head.to_dict()) # =converting the data to dictionary format 
