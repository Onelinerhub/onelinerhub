# How can I use elasticsearch to manage transactions?
// plain

Elasticsearch can be used to manage transactions with the help of the [_bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html). This API allows you to send multiple documents in a single request. The documents can be of any type, including transactions.

For example, the following code block can be used to create two transactions in a single request:

```
curl -X POST "localhost:9200/_bulk?pretty" -H 'Content-Type: application/json' -d'
{ "index": { "_id": 1 } }
{ "transaction_type": "credit", "amount": 500 }
{ "index": { "_id": 2 } }
{ "transaction_type": "debit", "amount": 100 }
'
```

The output of the above code would be:
```
{
  "took" : 4,
  "errors" : false,
  "items" : [
    {
      "index" : {
        "_index" : "_bulk",
        "_type" : "_doc",
        "_id" : "1",
        "_version" : 1,
        "result" : "created",
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "status" : 201
      }
    },
    {
      "index" : {
        "_index" : "_bulk",
        "_type" : "_doc",
        "_id" : "2",
        "_version" : 1,
        "result" : "created",
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "status" : 201
      }
    }
  ]
}
```

The code consists of the following parts:

1. `curl -X POST "localhost:9200/_bulk?pretty" -H 'Content-Type: application/json' -d'`: This is the command used to send a request to the Elasticsearch server.

2. `{ "index": { "_id": 1 } }`: This is the first document that will be indexed. It contains an `index` property with an `_id` property set to `1`.

3. `{ "transaction_type": "credit", "amount": 500 }`: This is the second document that will be indexed. It contains a `transaction_type` property set to `credit` and an `amount` property set to `500`.

4. `{ "index": { "_id": 2 } }`: This is the third document that will be indexed. It contains an `index` property with an `_id` property set to `2`.

5. `{ "transaction_type": "debit", "amount": 100 }`: This is the fourth document that will be indexed. It contains a `transaction_type` property set to `debit` and an `amount` property set to `100`.

6. `'`: This is the end of the request.

This code will create two transactions in a single request, which can be used to manage transactions with Elasticsearch.

onelinerhub: [How can I use elasticsearch to manage transactions?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-to-manage-transactions)