# How can I use wildcards in Elasticsearch queries?
// plain

Wildcards in Elasticsearch queries allow for the use of pattern matching to search for specific strings of text. To use wildcards, the `wildcard` query should be used. For example, to search for documents containing the string `hello` with any character before and after, the following query can be used:

```
GET /_search
{
  "query": {
    "wildcard" : {
      "content" : "*hello*"
    }
  }
}
```

This query will return any documents containing the string `hello` with any other characters before and after.

The wildcard query supports two types of wildcards: `*` and `?`. `*` is a wildcard for any number of characters, while `?` is a wildcard for a single character. For example, to search for documents containing the string `hello` with any single character before and after, the following query can be used:

```
GET /_search
{
  "query": {
    "wildcard" : {
      "content" : "?hello?"
    }
  }
}
```

This query will return any documents containing the string `hello` with any single character before and after.

Wildcards can also be used with the `fuzzy` query. The `fuzzy` query allows for fuzzy matching, which means that it will match documents that are similar to the given string. For example, to search for documents containing similar strings to `hello`, the following query can be used:

```
GET /_search
{
  "query": {
    "fuzzy" : {
      "content" : "hello"
    }
  }
}
```

This query will return any documents containing strings similar to `hello`.

Wildcards can be a powerful tool for searching for specific strings of text in Elasticsearch.

### Parts of code and explanation

- `GET /_search`: This is the endpoint used to query the Elasticsearch cluster.
- `wildcard`: This is the query type used to search for documents containing strings with wildcards.
- `content`: This is the field in the documents that is being searched.
- `*`: This is a wildcard for any number of characters.
- `?`: This is a wildcard for a single character.
- `fuzzy`: This is the query type used to search for documents containing strings similar to the given string.

### Relevant links

- [Elasticsearch Wildcard Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-wildcard-query.html)
- [Elasticsearch Fuzzy Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-fuzzy-query.html)

onelinerhub: [How can I use wildcards in Elasticsearch queries?](https://onelinerhub.com/elasticsearch/how-can-i-use-wildcards-in-elasticsearch-queries)