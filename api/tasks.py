from celery import shared_task
from .utils import scrape_coinmarketcap

@shared_task
def start_scraping_task():
    scrape_coinmarketcap()
