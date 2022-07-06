
from django.shortcuts import render
from mall.forms import SearchForm
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')


# Create your views here.
def index(request):
    
    _from = request.GET.get("page")
    _category = request.GET.get("category")
    size = 20

    if _from == "first" or _from is None:
        _from = 0
    elif _from == "last":
        _from = int(459 / size) * size

    index = "products"
    body = { 
            "from" : _from,
            "size" : size,
            "query" :{
              "bool": {

              }
            }
        }
    if _category is not None and _category != "all":
      body["query"]["bool"]["filter"] = [
                {
                  "match": {
                    "category": _category
                  }
                }
              ]
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            body["query"]["bool"]["must"] = [
                  {
                    "query_string": {
                      "query": form.cleaned_data['search']
                    }
                  }
                ]
    else:
        form = SearchForm()

    res = es.search(index=index, body=body)

    product_list = [res.get("_source") for res in res.get("hits").get("hits")]
    page_list = [int(_from) + i for i in range(0, 10)]

    return render(request, "index.html", {"product_list": product_list, "page_list":page_list, "form" : form})

