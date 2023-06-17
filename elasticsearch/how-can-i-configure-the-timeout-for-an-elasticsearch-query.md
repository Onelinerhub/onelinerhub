# How can I configure the timeout for an Elasticsearch query?
// plain

The timeout for an Elasticsearch query can be configured by setting the `request_timeout` parameter. This parameter is set in the request body of the query and is specified in milliseconds.

For example, the following query sets the timeout to 5 seconds:

```
POST /my_index/_search
{
    "request_timeout": 5000
}
```

The `request_timeout` parameter can also be set globally using the `search.request.timeout` setting in the `elasticsearch.yml` configuration file.

The following list explains the parts of the code example:

* `POST` - The HTTP verb used to send the query.
* `/my_index/_search` - The endpoint of the query.
* `request_timeout` - The parameter used to set the timeout.
* `5000` - The value of the timeout in milliseconds.

For more information, please see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-timeout.html).

onelinerhub: [How can I configure the timeout for an Elasticsearch query?](https://onelinerhub.com/elasticsearch/how-can-i-configure-the-timeout-for-an-elasticsearch-query)