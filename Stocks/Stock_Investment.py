__author__ = 'Ryan'

"""
The point of this program is to gather information from yahoo finance and see if a certain stock is worth investing in.
I will use yahoo_finance to determine the price_book of all stocks and display the top %10 with a favorable
 price_book ratio (less than 1 means stock is undervalued).
"""

import csv
from yahoo_finance import Share
import time

f = open('companylist.csv', 'rt')
g = open('symbol_pb_ratio.csv', 'wt')

tick = 0                #a counter so yahoo finance doesn't time out.  you can only make 2000 queries an hour

try:
    reader = csv.reader(f)
    writer = csv.writer(g)

    writer.writerow(('Stock_Symbol', 'Current_Price', 'P/B_Ratio'))

    for row in reader:

        stock = row[0]

        Share(stock).refresh()

        tick = tick + 1

        if tick == 1500:

            time.sleep(3600)              #when 1500 queries have happened, this will pause 1 hour

        if type(Share(stock).get_price()) == str:         #if stock.get_price() is a string, then yahoo sent back information

            stock_price = float(Share(stock).get_price())
            stock_book_value = float(Share(stock).get_book_value())

            if stock_price != 0 and stock_book_value != 0:      #if either are 0, the pb_ratio can't be calculated

                pb_ratio = round(stock_price / stock_book_value, 2)

                if pb_ratio < 1:                    #all we care about right now is stocks where the ratio is less than 0

                    writer.writerow((stock, stock_price, pb_ratio))

            
finally:
    f.close()
    g.close()
