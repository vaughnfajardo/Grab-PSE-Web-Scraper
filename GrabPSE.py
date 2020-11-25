import requests
from bs4 import BeautifulSoup
import pandas as pd

# The getPSEStockData function scrapes data of off Investagrams.com,
# converts the data into a dataframe,
# and exports it as a CSV file.

def getPSEStockData(ticker):
    # Data is scraped of off Investagrams.com depending on specified ticker symbol
    url = ('https://www.investagrams.com/Stock/PSE:' + ticker)
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    table = soup.find('table', {"class": "table table-hover"})
    data_frame = pd.read_html(str(table))[0]
    data_frame.drop(data_frame.tail(1).index, inplace=True)

    # Date column in DataFrame is converted to DateTime objects
    data_frame['Date'] = pd.to_datetime(data_frame['Date'], format='%b %d, %Y')

    # DataFrame is saved to a CSV file
    data_frame.to_csv(str(ticker) + '.csv')

    rows = len(data_frame.index)

    return rows


def main():
    while True:
        try:
            print('===================================')
            ticker = input('Ticker Symbol: ')
            print('===================================')
            print('PROCESSING')
            print('===================================')
            rows = getPSEStockData(ticker)
            break
        except:
            print('Please enter a valid ticker symbol.')
    print('===================================')
    print('File has been saved as ' + ticker + '.csv.')
    print('===================================')
    print('Days Exported: ' + str(rows))
    print('===================================')


if __name__ == "__main__":
    main()
