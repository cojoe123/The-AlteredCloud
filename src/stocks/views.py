from django.shortcuts import render

from .forms import SearchForm

import stocks.service as services


# Create your views here.
def home_view(request):
    mostactive = services.get_top_active()
    gainers = services.get_gainers()
    losers = services.get_losers()

    return render(request, 'stocks/index.html', {'active':mostactive, 'gainers':gainers, 'losers':losers})

def search_result_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            search = form.cleaned_data['search']
    else:
        form = SearchForm()

    book = services.get_stock_book_details(company=search)
    company = services.get_stock_company_details(company=search)

    return render(request, 'stocks/company.html', {'book':book, 'company_info':company })

def stock_info_view(request, ticker):
    book = services.get_stock_book_details(company=ticker)
    company = services.get_stock_company_details(company=ticker)

    return render(request, 'stocks/company.html', {'book':book, 'company_info':company })
