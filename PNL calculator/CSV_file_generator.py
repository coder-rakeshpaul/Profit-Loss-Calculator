
# creating csv file to store trade history
import csv
fields = ['Name', 'lot size', 'buy price', 'sell price', 'PNL']
filename = "trade_history.csv"
with open(filename, 'w') as csvfile:
  csvwriter= csv.writer(csvfile)
  csvwriter.writerow(fields)
