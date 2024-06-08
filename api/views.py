from django.shortcuts import render
from .utils import scrape_coinmarketcap

def coin_list(request):
    # Call the scrape_coinmarketcap function to get cryptocurrency data
    coins_data = scrape_coinmarketcap()
    print(coins_data)
    # Pass the data to the template for rendering
    return render(request, 'scraped_data.html', {'scraped_data': coins_data})

