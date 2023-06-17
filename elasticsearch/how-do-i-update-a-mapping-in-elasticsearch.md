# How do I update a mapping in Elasticsearch?
// plain

Updating a mapping in Elasticsearch is a two-step process. First, you need to delete the existing mapping, and then you can add the new mapping.

## Example code

```
# Delete existing mapping
curl -X DELETE localhost:9200/my_index

# Add new mapping
curl -X PUT localhost:9200/my_index -H 'Content-Type: application/json' -d '
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text"
      }
    }
  }
}'
```
## Output example

```
{"acknowledged":true}
```

- `curl -X DELETE localhost:9200/my_index`: This command sends an HTTP DELETE request to the Elasticsearch server running on localhost:9200 for the index named my_index.
- `curl -X PUT localhost:9200/my_index`: This command sends an HTTP PUT request to the Elasticsearch server running on localhost:9200 for the index named my_index.
- `-H 'Content-Type: application/json'`: This specifies the content type of the request body as JSON.
- `-d '<mapping>'`: This specifies the mapping to be added to the index.

## Helpful links
- [Elasticsearch Documentation - Updating Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-update.html)
- [Elasticsearch Documentation - cURL](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-command-line.html#_using_curl)

onelinerhub: [How do I update a mapping in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-update-a-mapping-in-elasticsearch)