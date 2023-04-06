import csv
from dateutil.parser import *
from datetime import *

def settlementDate(id):
    with open('transactions.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (str(id) == row['Transfer ID']):
                if("FAILED" == row['Status']):
                    print("Failed")
                elif(not row['Posted At']):
                    helper(row['Scheduled Date'])
                else: 
                    helper(row['Posted At'])

def helper(startDate):
    posted_at_date = parse(startDate).date()
    posted_at_day = posted_at_date.day
    settlement_date = posted_at_date + timedelta(days=4)
    print(settlement_date)

settlementDate(5319)