import requests
from bs4 import BeautifulSoup

def scrape_coinmarketcap():
    url = 'https://coinmarketcap.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    coins_data = []

    # Find the table containing the coin data
    table = soup.find('table', class_='sc-ae0cff98-3 ipWPGi cmc-table')
    if not table:
        print("Table not found.")
        return []

    rows = table.find('tbody').find_all('tr')

    for row in rows:
        try:
            rank = row.find('td', class_='cmc-table__cell--sort-by__rank').get_text(strip=True)
            name = row.find('td', class_='cmc-table__cell--sort-by__name').get_text(strip=True)
            symbol = row.find('td', class_='cmc-table__cell--sort-by__symbol').get_text(strip=True)
            price = row.find('td', class_='cmc-table__cell--sort-by__price').get_text(strip=True)
            market_cap = row.find('td', class_='cmc-table__cell--sort-by__market-cap').get_text(strip=True)
            volume = row.find('td', class_='cmc-table__cell--sort-by__volume-24-h').get_text(strip=True)
            circulating_supply = row.find('td', class_='cmc-table__cell--sort-by__circulating-supply').get_text(strip=True)

            coin_data = {
                'rank': rank,
                'name': name,
                'symbol': symbol,
                'price': price,
                'market_cap': market_cap,
                'volume': volume,
                'circulating_supply': circulating_supply
            }

            coins_data.append(coin_data)
            print(coin_data)

        except AttributeError as e:
            print(f"Error parsing row: {e}")

    return coins_data

# Test the function
if __name__ == "__main__":
    coin_data = scrape_coinmarketcap()
    print(coin_data)
