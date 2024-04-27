# booster.py -- Calculate date for vaccine booster.
# Brandon Walters (100599925)
# TPRG1131 Section 12345
# January 25, 2022
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).
# The program calculates the given min and max dates for the booster shoot 
from datetime import datetime, timedelta
Late = timedelta(days=365) #Sets a late date 
today = timedelta(days=1) #sets a minamun starting date
initial = datetime.today() #gives todays date


while True: #first loop mainly calling for the min and max days only loops if min value is more then max
    minstring = input("Minimum number of days before booster?")
    maxstring = input("Maximum number of days before booster?")
    if minstring > maxstring:
        print("try Again")
    else:
        if minstring != "" and maxstring != "": #if something is entered will give the amount of days along with todays date
            print("min_days:", minstring, " max_days:", maxstring)
            print("Today is", initial.strftime("%Y/%m/%d"))
            mind = timedelta(days=int(minstring))
            maxd = timedelta(days=int(maxstring))
            break
        else: #if nothing is entered will give a set days along with todays date
            mind = timedelta(days=60)
            maxd = timedelta(days=90)
            print("min_days: 60 max_days: 90")
            print("Today is", initial.strftime("%Y/%m/%d"))
            break

while True:#secound loop exit out if min or max is out of date or ctrl f2 is hit 
    if mind < today:
        print("Too Early")
        break
    elif maxd >= Late:
        print("Too Late")
        break
    else:
        yearstring = input("\nInitial date year (YYYY) ? ")
        monthstring = input("Initial date month (01-12) ? ")
        daystring = input("Initial date day (01-31) ? ")
        if yearstring != "" and monthstring != "" and daystring != "":
            initial = datetime(year=int(yearstring), month=int(monthstring), day=int(daystring))
            mindate = initial + mind
            maxdate = initial + maxd
            print("Earliest date: ", mindate.strftime("%Y/%m/%d"))
            print("Latest: ", maxdate.strftime("%Y/%m/%d"))
        else: #if nothing is entered wil instead use todays date plus min/max dates
            initial = datetime.today()
            mindate = initial + mind
            maxdate = initial + maxd
            print("Earliest date: ", mindate.strftime("%Y/%m/%d"))
            print("Latest: ", maxdate.strftime("%Y/%m/%d"))
       
        