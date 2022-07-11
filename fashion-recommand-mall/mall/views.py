import requests

from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from elasticsearch import Elasticsearch

from account.models import UserDetail
from mall.service.elasticserch_service import make_products_query
from mall.forms import SearchForm

es = Elasticsearch('http://localhost:9200')
deep_learning_server = "http://localhost:3000"

# Create your views here.
def index(request):

    category = request.GET.get("category", "all")
    q = None
    sytle = {}

    if request.user.is_authenticated:
        userDetail = UserDetail.objects.filter(user_id = request.user.id).first()
        for key in userDetail.__dict__:
            if key != "id" and key != "user_id" and key != "_state" and userDetail.__dict__.get(key) != 0:
                sytle[key] = userDetail.__dict__.get(key)
        
        
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['search']
    else:
        form = SearchForm()
        
    index = "products"

    body = make_products_query(category, q, sytle)

    res = es.search(index=index, body=body)

    product_list = [res.get("_source") for res in res.get("hits").get("hits")]

    return render(request, "index.html", {"product_list": product_list, "form" : form})

    