
from django.shortcuts import render
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')


# Create your views here.
def index(request):

    _from = request.GET.get("page")
    size = 20

    if _from == "first":
        _from = 0
    elif _from == "last":
        _from = int(459 / size) * size

    index = "products"
    body = { 
            "from" : _from,
            "size" : size
        }
    
    res = es.search(index=index, body=body)

    product_list = [res.get("_source") for res in res.get("hits").get("hits")]
    page_list = [int(_from) + i for i in range(0, 10)]

    return render(request, "index.html", {"product_list": product_list, "page_list":page_list})

