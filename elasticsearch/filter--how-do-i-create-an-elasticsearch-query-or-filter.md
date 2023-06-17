# filter

How do I create an Elasticsearch query or filter?
// plain

An Elasticsearch query or filter can be created using the Query DSL (Domain Specific Language) which is a JSON-style syntax. The basic structure of a query is composed of a query clause, which indicates what type of query is being performed, and a filter clause, which indicates which documents should be returned.

For example, the following query will return all documents in the index:

```
GET /_search
{
  "query": {
    "match_all": {}
  }
}
```

This query can be modified to filter the results by adding a filter clause. For example, to return documents with a field named "category" equal to "sports", the query would be:

```
GET /_search
{
  "query": {
    "match_all": {}
  },
  "filter": {
    "term": {
      "category": "sports"
    }
  }
}
```

The query clause can also be modified to refine the results. For example, to return documents with a field named "title" containing the word "football", the query would be:

```
GET /_search
{
  "query": {
    "match": {
      "title": "football"
    }
  },
  "filter": {
    "term": {
      "category": "sports"
    }
  }
}
```

The Query DSL is a powerful and flexible way to create queries and filters for Elasticsearch. For more information, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html).

onelinerhub: [filter

How do I create an Elasticsearch query or filter?](https://onelinerhub.com/elasticsearch/filter--how-do-i-create-an-elasticsearch-query-or-filter)