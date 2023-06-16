# How can I use ElasticSearch to highlight search results?
// plain

ElasticSearch provides a powerful and flexible way to highlight search results. To do this, you can use the [`highlight`](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-highlighting.html) parameter in your search query.

For example, to highlight the words “ElasticSearch” in the results, you could use the following query:

```
GET /_search
{
    "query": {
        "match": {
            "text": "ElasticSearch"
        }
    },
    "highlight": {
        "fields": {
            "text": {}
        }
    }
}
```

The output of this query would look something like this:

```
{
    "hits": {
        "total": 1,
        "max_score": 0.2876821,
        "hits": [
            {
                "_index": "test",
                "_type": "_doc",
                "_id": "1",
                "_score": 0.2876821,
                "_source": {
                    "text": "This is a test document about ElasticSearch"
                },
                "highlight": {
                    "text": [
                        "This is a test document about <em>ElasticSearch</em>"
                    ]
                }
            }
        ]
    }
}
```

The `highlight` parameter has several components:

- `fields`: The fields to highlight.
- `pre_tags`: The HTML tags to wrap the highlighted terms in.
- `post_tags`: The HTML tags to wrap the highlighted terms in.
- `order`: The order of the highlighted fragments.
- `encoder`: The encoding type for the highlighted terms.

For more information, see the [ElasticSearch Highlighting Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-highlighting.html).

onelinerhub: [How can I use ElasticSearch to highlight search results?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-to-highlight-search-results)