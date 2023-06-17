# How can I use Elasticsearch with Zammad?
// plain

Elasticsearch is an open source search engine that can be used with Zammad to provide powerful search capabilities. It can be used to index and search Zammad tickets, users, organizations, and more.

To use Elasticsearch with Zammad, you will need to install and configure the [Elasticsearch Zammad Plugin](https://github.com/zammad/zammad-elasticsearch-plugin). This plugin allows you to index and search Zammad data using Elasticsearch.

You can then use the Elasticsearch API to query the indexed data. For example, the following code snippet will query for all tickets with the keyword "test":

```
GET /_search
{
  "query": {
    "query_string": {
      "query": "test"
    }
  }
}
```

The output of the above query will be a JSON array of all tickets that contain the keyword "test".

You can also use Elasticsearch to perform more complex searches. For example, the following code snippet will query for all tickets with the keyword "test" that were created by a specific user:

```
GET /_search
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query": "test"
          }
        },
        {
          "term": {
            "created_by_id": 123
          }
        }
      ]
    }
  }
}
```

The output of the above query will be a JSON array of all tickets that contain the keyword "test" and were created by the user with ID 123.

Using Elasticsearch with Zammad provides powerful search capabilities that can be used to quickly find the information you need.

onelinerhub: [How can I use Elasticsearch with Zammad?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-zammad)