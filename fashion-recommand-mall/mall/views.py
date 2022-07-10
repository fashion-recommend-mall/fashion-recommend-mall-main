import requests

from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from mall.forms import SearchForm
from elasticsearch import Elasticsearch

from mall.service.elasticserch_service import make_products_query

es = Elasticsearch('http://localhost:9200')
deep_learning_server = "http://localhost:3000"

# Create your views here.
def index(request):

    category = request.GET.get("category", "all")
    
    q = None

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['search']
    else:
        form = SearchForm()
        
    index = "products"

    body = make_products_query(category, q)

    res = es.search(index=index, body=body)

    product_list = [res.get("_source") for res in res.get("hits").get("hits")]

    return render(request, "index.html", {"product_list": product_list, "form" : form})

    