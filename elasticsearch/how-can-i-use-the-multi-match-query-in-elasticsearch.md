# How can I use the multi_match query in Elasticsearch?
// plain

The multi_match query in Elasticsearch allows you to search for multiple fields in a single query. It works by combining the query terms with OR operators. It also has the capability to boost certain fields or query terms.

Example of multi_match query code:
```
GET /_search
{
    "query": {
        "multi_match" : {
            "query":    "quick brown fox",
            "fields": [ "title^5", "content" ]
        }
    }
}
```
## Output example

```
{
    "took": 3,
    "timed_out": false,
    "_shards": {
        "total": 5,
        "successful": 5,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 2,
            "relation": "eq"
        },
        "max_score": 0.5753642,
        "hits": [
            {
                "_index": "test",
                "_type": "_doc",
                "_id": "1",
                "_score": 0.5753642,
                "_source": {
                    "title": "The quick brown fox",
                    "content": "The quick brown fox jumps over the lazy dog"
                }
            },
            {
                "_index": "test",
                "_type": "_doc",
                "_id": "2",
                "_score": 0.2876821,
                "_source": {
                    "title": "The quick brown fox jumps",
                    "content": "The quick brown fox jumps over the lazy dog"
                }
            }
        ]
    }
}
```

## Code explanation

- **GET /_search** - This is the search endpoint of Elasticsearch.
- **query** - This is the query clause where the multi_match query is specified.
- **multi_match** - This is the multi_match query.
- **query** - This is the query string that we want to search for.
- **fields** - This is the list of fields that we want to search in.
- **title^5** - This is the title field with a boost of 5.
- **content** - This is the content field.

## Helpful links
- [Multi_match query documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-multi-match-query.html)
- [Elasticsearch search endpoint documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html)

onelinerhub: [How can I use the multi_match query in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-use-the-multi-match-query-in-elasticsearch)