# the file conatins the list of queries 

import pandas as pd 
from django.db import connection

def all_customers():
	query = "select id,company, last_name, job_title, business_phone, city from customers"
	data = (pd.read_sql(query, connection))
	return(data)