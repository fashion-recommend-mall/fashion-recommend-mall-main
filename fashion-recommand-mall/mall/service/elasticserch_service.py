

def make_products_query(category, q) -> dict:
    body = { 
            "size" : 1000,
            "query" :{
              "bool": {

              }
            }
        }

    if category != "all":
        body["query"]["bool"]["filter"] = [
                {
                  "match": {
                    "category": category
                  }
                }
              ]
    
    if q is not None:
        body["query"]["bool"]["must"] = [
                  {
                    "query_string": {
                      "query": q
                    }
                  }
                ]

    return body