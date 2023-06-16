# How can I use elasticsearch facets to filter search results?
// plain

Elasticsearch facets provide an easy way to filter search results. Facets are used to group results by a certain field. For example, you can use facets to group results by product category or price range.

To use facets, you need to specify the `facets` parameter in the search query. Here is an example code block:

```
GET /products/_search
{
  "query": {
    "match_all": {}
  },
  "facets": {
    "categories": {
      "terms": {
        "field": "category"
      }
    }
  }
}
```

The output of this query will be something like this:

```
{
  ...
  "facets": {
    "categories": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "phones",
          "doc_count": 10
        },
        {
          "key": "tablets",
          "doc_count": 5
        }
      ]
    }
  }
  ...
}
```

The code consists of the following parts:
* `GET /products/_search` - the search query
* `query` - the search query itself
* `facets` - the parameter for specifying the facets
* `categories` - the name of the facet
* `terms` - the type of facet (terms facet)
* `field` - the field to group the results by

Here are some ## Helpful links
* [Elasticsearch Facets](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-facets.html)
* [Elasticsearch Terms Facet](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-facets-terms-facet.html)

onelinerhub: [How can I use elasticsearch facets to filter search results?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-facets-to-filter-search-results)