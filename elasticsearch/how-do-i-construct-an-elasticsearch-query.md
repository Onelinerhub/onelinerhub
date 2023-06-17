# How do I construct an elasticsearch query?
// plain

To construct an Elasticsearch query, you will need to use the Query DSL (Domain Specific Language). The Query DSL is a JSON-style syntax that allows you to specify the query you want to execute.

For example, to search for documents containing the word "Elasticsearch", you can use the following query:

```
GET /_search
{
    "query": {
        "match" : {
            "message" : "Elasticsearch"
        }
    }
}
```

This query will return all documents that contain the word "Elasticsearch".

The Query DSL consists of several parts:

* `GET`: This denotes the HTTP method used to execute the query.
* `/_search`: This is the endpoint for searching documents.
* `query`: This is the root object for the query.
* `match`: This is the query type used to match documents that contain a specific term.
* `message`: This is the field in the document that will be searched.
* `Elasticsearch`: This is the term that will be searched for.

For more information on constructing queries, please see the [Elasticsearch Query DSL documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html).

onelinerhub: [How do I construct an elasticsearch query?](https://onelinerhub.com/elasticsearch/how-do-i-construct-an-elasticsearch-query)