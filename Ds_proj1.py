#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:51:29 2021

@author: emmye
"""
import os
import pandas as pd
#os.chdir("/Users/emmye/Desktop")
cd ~/.kaggle
mv ~/Downloads/kaggle.json ./
import kaggle

#Dowload the dataset through Kaggle's api call 
from kaggle.api.kaggle_api_extended import KaggleApi
 api = KaggleApi()
 api.authenticate()
api.dataset_download_file('jeffreybraun/chipotle-locations','chipotle_stores.csv',path = './')

data = pd.read_csv('chipotle_stores.csv')

#Create new column that labels if location is in Virginia
data['near_cville'] =  data['state'] == 'Virginia' 

#Convert the CSV to a JSON file
data.to_json("DSproject.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

#Summarize the number of rows and columns in the dataset
len(data)
len(data.columns)



# Code to push file to s3 (not to run)

#import boto3
#from botocore.exceptions import NoCredentialsError
# pip install boto3

#ACCESS_KEY = 'AKIAS6BSB4KJ3NPLVEGD'
#SECRET_KEY = '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'

#def upload_to_aws(local_file, bucket, s3_file):
#    s3 = boto3.client('s3',aws_access_key_id = ACCESS_KEY,
 #                     aws_secret_access_key= SECRET_KEY)
  #  try:
   #     s3.upload_file(local_file, bucket,s3_file)
    #    print('Upload successful')
     #   return True
    #except FileNotFoundError:
     #   print('The file was not found')
      #  return False
    #except NoCredentialsError:
     #   print("Credentials not available")
      #  return False
    
#uploaded = upload_to_aws('DSproject.json','ds3003project' , s3_file)
        
        
        
        
        