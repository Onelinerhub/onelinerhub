# How do I set up an elasticsearch ingest pipeline?
// plain

1. Firstly, you need to create an ingest pipeline in elasticsearch. This can be done by sending a `PUT` request to the `_ingest/pipeline` endpoint with the pipeline definition in the body. For example:
```
PUT _ingest/pipeline/my_pipeline
{
  "description" : "my pipeline",
  "processors" : [
    {
      "set" : {
        "field": "field_1",
        "value": "value_1"
      }
    }
  ]
}
```
2. The response of the request will be a `201 Created` status, if the pipeline was created successfully.
3. The next step is to index documents into Elasticsearch. This can be done by sending a `POST` request to the `_bulk` endpoint with the documents in the body. For example:
```
POST _bulk
{ "index" : { "_index" : "my_index", "_type" : "my_type" } }
{ "field_1" : "value_1" }
```
4. To enable the ingest pipeline, you need to add the `pipeline` parameter to the `_bulk` request. For example:
```
POST _bulk?pipeline=my_pipeline
{ "index" : { "_index" : "my_index", "_type" : "my_type" } }
{ "field_1" : "value_1" }
```
5. The response of the request will be a `200 OK` status, if the documents were indexed successfully.
6. The documents that were indexed will have the fields that were set in the ingest pipeline.
7. For more information, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html).

onelinerhub: [How do I set up an elasticsearch ingest pipeline?](https://onelinerhub.com/elasticsearch/how-do-i-set-up-an-elasticsearch-ingest-pipeline)