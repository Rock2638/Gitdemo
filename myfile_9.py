# First we'll import the os module to allow us to create file paths across operating sytems
import os

#import the module for reading the csv files
import csv

csvpath = os.path.join('..', 'Resources', 'contacts.csv')

with open(csvpath) as csvfile:

   # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)