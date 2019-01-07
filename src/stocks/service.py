import requests

def get_top_active():
    url = 'https://api.iextrading.com/1.0/stock/market/list/mostactive'
    response = requests.get(url)
    info = response.json()
    return info

def get_gainers():
    url = 'https://api.iextrading.com/1.0/stock/market/list/gainers'
    response = requests.get(url)
    info = response.json()
    return info

def get_losers():
    url = 'https://api.iextrading.com/1.0/stock/market/list/losers'
    response = requests.get(url)
    info = response.json()
    return info

def get_stock_company_details(company):
    url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(company)
    response = requests.get(url)
    info = response.json()
    return info

def get_stock_book_details(company):
    url = 'https://api.iextrading.com/1.0/stock/{}/book'.format(company)
    response = requests.get(url)
    info = response.json()
    return info


def get_stock_chart(company):
    url = 'https://api.iextrading.com/1.0/stock/{}/chart'.format(company)
    response = requests.get(url)
    info = response.json()
    return info
