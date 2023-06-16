# search

How do I use keyword search in Elasticsearch?
// plain

Elasticsearch provides powerful search capabilities through its Query DSL (Domain Specific Language). Keyword search is a type of search that allows you to find documents that contain a specific keyword or phrase.

To perform a keyword search in Elasticsearch, you can use the `match` query. The `match` query will match documents that contain the specified keyword or phrase. For example, the following query will match documents that contain the word “Elasticsearch”:

```
GET /_search
{
    "query": {
        "match": {
            "title": "Elasticsearch"
        }
    }
}
```

The output of the query will be a list of documents that contain the word “Elasticsearch” in their title field.

You can also use the `multi_match` query to search for documents that contain multiple keywords or phrases. The `multi_match` query takes an array of keywords or phrases and will match documents that contain any of them. For example, the following query will match documents that contain either the word “Elasticsearch” or the phrase “search engine”:

```
GET /_search
{
    "query": {
        "multi_match": {
            "query": [
                "Elasticsearch",
                "search engine"
            ]
        }
    }
}
```

The output of the query will be a list of documents that contain either the word “Elasticsearch” or the phrase “search engine”.

In addition to the `match` and `multi_match` queries, Elasticsearch also provides a variety of other query types, such as `term` and `prefix` queries, that can be used to perform keyword searches.

For more information on keyword search in Elasticsearch, see the following links:

- [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
- [Searching Your Data](https://www.elastic.co/guide/en/elasticsearch/reference/current/searching.html)

onelinerhub: [search

How do I use keyword search in Elasticsearch?](https://onelinerhub.com/elasticsearch/search--how-do-i-use-keyword-search-in-elasticsearch)