# text search

How can I use elasticsearch to perform a free text search?
// plain

Elasticsearch is a powerful search engine that can be used to perform free text search. To use Elasticsearch for free text search, you will first need to create an index and define the mapping for the fields that you want to search. This mapping will tell Elasticsearch how to tokenize the text and how to index it.

Once the index is created, you can query it using the `query_string` query. For example, the following query searches for documents that contain the word "Elasticsearch":

```
GET /my_index/_search
{
    "query" : {
        "query_string" : {
            "query" : "Elasticsearch"
        }
    }
}
```

This query will return all documents that contain the word "Elasticsearch".

You can also use the `multi_match` query to search multiple fields at once. For example, the following query searches for documents that contain the word "Elasticsearch" in the `title` and `content` fields:

```
GET /my_index/_search
{
    "query" : {
        "multi_match" : {
            "query" : "Elasticsearch",
            "fields" : ["title", "content"]
        }
    }
}
```

This query will return all documents that contain the word "Elasticsearch" in either the `title` or `content` fields.

To learn more about free text search with Elasticsearch, please refer to the [official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html).

**Parts of Code Explained:**

* `query_string` query: This query allows you to search for documents that contain a specific word or phrase.

* `multi_match` query: This query allows you to search multiple fields at once for a specific word or phrase.

**## Helpful links**

* [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
* [Elasticsearch Query String Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html)

onelinerhub: [text search

How can I use elasticsearch to perform a free text search?](https://onelinerhub.com/elasticsearch/text-search--how-can-i-use-elasticsearch-to-perform-a-free-text-search)