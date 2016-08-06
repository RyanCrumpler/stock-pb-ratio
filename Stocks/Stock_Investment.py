__author__ = 'Ryan'

"""
The point of this program is to gather information from yahoo finance and see if a certain stock is worth investing in.
I will use yahoo_finance to determine the price_book of all stocks and display the top %10 with a favorable
 price_book ratio (less than 1 means stock is undervalued).
"""

from googlefinance import getQuotes
from yahoo_finance import Share

stock = input("What stock symbol do you want to look up? ")

Share(stock).refresh()

stock_price = float(Share(stock).get_price())

stock_book_value = float(Share(stock).get_book_value())

print(stock, ": $", stock_price)
print("Book value per share: ", stock_book_value)
print("P/B Ratio Calculated: ", stock_price/stock_book_value)

print("Price Book", Share(stock).get_price_book())
