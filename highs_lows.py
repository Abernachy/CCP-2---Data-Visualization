import csv
from datetime import datetime
from matplotlib import pyplot as plt


# Get dates, lows, and high temperatures from file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # create a blank list for each item we are grabbing
    # appending data of those rows to the lists
    
    dates,  highs, lows  = [],  [], []
    for row in reader:
    # Error checking  
        try:
            # Dates are the first row
            current_date = datetime.strptime(row[0],  "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,  'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
        
# plot data
fig = plt.figure(dpi=128,  figsize =(10, 6))
# plots the dates and highs with red
plt.plot(dates,  highs,  c='red',  alpha=0.5)
# plots the dates and lows with blue
plt.plot(dates,  lows,  c='blue',  alpha=0.5)
plt.fill_between(dates,  highs,  lows,  facecolor='blue',  alpha=0.1)

# format plot
title= "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title,  fontsize=20)
plt.xlabel('',  fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",  fontsize=16)
plt.tick_params(axis='both',  which='major',  labelsize=16)

plt.show()
