

import pandas as pd
import numpy as np
import csv

class charges:
  def __init__(self,lot,buy_price, sell_price):
    self.buy_price=buy_price
    self.sell_price=sell_price
    self.total_buy_price=lot*buy_price
    self.total_sell_price=lot*sell_price
    self.net_price= (sell_price-buy_price)*lot

  def calculate_buy_price(self):
    return  ((0.003/100)+ (0.053/100) + (0.0001/100))* self.total_buy_price + 20 + (18/100)*(( (0.053/100) + (0.0001/100))* self.total_buy_price + 20)
  def calculate_sell_price(self):
    return ((0.05/100)+ (0.053/100) + (0.0001/100))*self.total_sell_price + 20 + (18/100)*(( (0.053/100) + (0.0001/100))*self.total_sell_price + 20)

lot = int(input("Lot size: "))
p=charges(lot,int(input("buy price: ")),int(input("sell price: ")))
PNL=(p.net_price - round(p.calculate_sell_price() + p.calculate_buy_price())) 

rows=[input("name: ") , lot,p.buy_price ,p.sell_price ,PNL]

filename = "trade_history.csv"
with open(filename, 'a') as csvfile:
  csvwriter= csv.writer(csvfile)

  csvwriter.writerow(rows)
