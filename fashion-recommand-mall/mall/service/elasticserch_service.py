

def make_products_query(category, q, style) -> dict:
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

    if style is not None:
      should_list = []

      for key in style:
        target = {
          "rank_feature": {
                      "field":f'style.{key}',
                      "boost" : 1 + style[key] / 10
            }
        }

        should_list.append(target)
      
      body["query"]["bool"]["should"] = should_list

      print(body)
    return body