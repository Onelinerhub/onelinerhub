# How can I index XML data in Elasticsearch?
// plain

The XML data can be indexed in Elasticsearch using the Ingest Node. The Ingest Node can be used to parse and index XML data into Elasticsearch.

## Example code

```
PUT _ingest/pipeline/xml_pipeline
{
  "description" : "A pipeline for ingesting XML data",
  "processors" : [
    {
      "xml" : {
        "field" : "message"
      }
    }
  ]
}
```

This example code creates a pipeline called `xml_pipeline` that will parse the `message` field as XML data.

Then, the XML data can be indexed into Elasticsearch by using the `_bulk` API with the `xml_pipeline` pipeline.

## Example code

```
POST _bulk
{ "index" : { "_index" : "my_index", "_type" : "_doc", "_pipeline" : "xml_pipeline" } }
{ "message" : "<data><name>John Doe</name><age>30</age></data>" }
```

## Output example

```
{
  "took" : 0,
  "errors" : false,
  "items" : [
    {
      "index" : {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "1",
        "_version" : 1,
        "_shards" : {
          "total" : 2,
          "successful" : 1,
          "failed" : 0
        },
        "result" : "created",
        "_seq_no" : 0,
        "_primary_term" : 1
      }
    }
  ]
}
```

The `xml` processor in the `xml_pipeline` pipeline will parse the `message` field in the indexed document as XML data and store it as fields in the document.

## Code explanation

- `PUT _ingest/pipeline/xml_pipeline`: Creates a pipeline called `xml_pipeline`
- `"xml" : { "field" : "message" }`: Configures the `xml` processor to parse the `message` field as XML data
- `POST _bulk`: Indexes the document with the `xml_pipeline` pipeline

## Helpful links
- [Ingest Node](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html)
- [XML Processor](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest-xml.html)

onelinerhub: [How can I index XML data in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-index-xml-data-in-elasticsearch)