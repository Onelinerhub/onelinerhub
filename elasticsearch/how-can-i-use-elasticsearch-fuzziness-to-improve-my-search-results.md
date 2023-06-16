# How can I use elasticsearch fuzziness to improve my search results?
// plain

Elasticsearch fuzziness provides a way to improve search results by allowing inexact matching of search terms. Fuzziness is expressed as a value between 0 and 1, with 0 being exact match and 1 being completely fuzzy.

For example, if you have a search query for "sport car", and you want to return results that match "sports car" or "sportscar", you can use fuzziness to increase the likelihood of matching those results.

## Example code

```
GET /_search
{
  "query": {
    "match": {
      "title": {
        "query": "sport car",
        "fuzziness": "0.5"
      }
    }
  }
}
```

## Output example

```
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 4,
      "relation": "eq"
    },
    "max_score": 0.9808291,
    "hits": [
      {
        "_index": "my_index",
        "_type": "my_type",
        "_id": "1",
        "_score": 0.9808291,
        "_source": {
          "title": "Sports car"
        }
      },
      {
        "_index": "my_index",
        "_type": "my_type",
        "_id": "2",
        "_score": 0.9808291,
        "_source": {
          "title": "Sportscar"
        }
      },
      {
        "_index": "my_index",
        "_type": "my_type",
        "_id": "3",
        "_score": 0.8180921,
        "_source": {
          "title": "Fast car"
        }
      },
      {
        "_index": "my_index",
        "_type": "my_type",
        "_id": "4",
        "_score": 0.68203986,
        "_source": {
          "title": "Family car"
        }
      }
    ]
  }
}
```

## Code explanation

- `GET /_search`: This is the endpoint used to send a search query to Elasticsearch.
- `query`: This is the query object that contains the search query.
- `match`: This is the query type used to perform a fuzzy match.
- `query`: This is the actual search query, in this case "sport car".
- `fuzziness`: This is the fuzziness value, which is set to 0.5 in this example.

## Helpful links
- [Elasticsearch Fuzziness Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-fuzzy-query.html)
- [Elasticsearch Query DSL Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

onelinerhub: [How can I use elasticsearch fuzziness to improve my search results?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-fuzziness-to-improve-my-search-results)