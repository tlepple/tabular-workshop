from faker import Faker
from datagenerator import DataGenerator
import datetime
import time
import sys
import csv
import boto3
import os
import argparse
import re

#########################################################################################
#       Define variables
#########################################################################################
dg = DataGenerator()
fake = Faker() # <--- Don't Forgot this
parser = argparse.ArgumentParser()

# define our required arguments to pass in:
parser.add_argument("startingCustomerID", help="Enter int value to assign to the first customerID field", type=int)
parser.add_argument("recordCount", help="Enter int value for desired number of records per group", type=int)
parser.add_argument("s3Bucket", help="Enter string to S3 bucket name to write files into", type=ascii)

# parse these args
args = parser.parse_args()

# assign args to vars:
startKey = int(args.startingCustomerID)
stopVal = int(args.recordCount)
s3BucketDest = re.sub("'", "",str(args.s3Bucket))
#s3BucketDest2 = re.sub("'", "",s3BucketDest)

# other variables:
now = datetime.datetime.now()
dir_location = "/tmp/"
prefix = 'customer_csv'
tname = now.strftime("%Y-%m-%d-%H-%M-%S")
suffix = '.csv'
fname = dir_location + prefix + tname + suffix
s3 = boto3.resource('s3')
# new items for txn
txn_prefix = 'txn_csv'
txn_fname = dir_location + txn_prefix + tname + suffix
cust_bucket_location = "customers/" + prefix + tname + suffix
txn_bucket_location = "transactions/" + txn_prefix + tname + suffix


#print("input bucket name --> " + s3BucketDest)
#print("cust_bucket_location --> " + cust_bucket_location)
#print("txn_bucket_location --> " + txn_bucket_location)
#print("s3BucketDest2 --> " + s3BucketDest2)
try:
         # customer starts here:
         try:
              #  open file to write csv
              with open(fname, 'w', newline='') as csvfile:
                   # create the header row
                   fpgheader = dg.fake_person_generator(1, 1, fake)
                   for h in fpgheader:
                           writer = csv.DictWriter(csvfile, fieldnames=h.keys() , delimiter='|', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                           writer.writeheader()
                   # create the data rows
                   fpg = dg.fake_person_generator(startKey, stopVal, fake)
                   for person in fpg:
                           writer = csv.DictWriter(csvfile, fieldnames=person.keys() , delimiter='|', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                           writer.writerow(person)
              csvfile.close()
              #Upload to S3
              s3.meta.client.upload_file(fname, s3BucketDest, cust_bucket_location)

         except:
              print("failing in person generator")
              producer.flush()

         # transaction starts here:
         try:
              #  open file to write csv
              with open(txn_fname, 'w', newline='') as csvfile:
                   # create the header row
                   fpgheader = dg.fake_txn_generator(1, 0, fake)
                   for h in fpgheader:
                           writer = csv.DictWriter(csvfile, fieldnames=h.keys() , delimiter='|', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                           writer.writeheader()
                   # create the data rows
                   fpg = dg.fake_txn_generator(startKey, stopVal, fake)
                   for tranx in fpg:
                           writer = csv.DictWriter(csvfile, fieldnames=tranx.keys() , delimiter='|', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                           writer.writerow(tranx)
              csvfile.close()
              #Upload to S3
              s3.meta.client.upload_file(txn_fname, s3BucketDest, txn_bucket_location)

         except:
              print("failing in transaction generator")
              producer.flush()

except:
     print("failed to create csv files.")
finally:
     print("script complete")
