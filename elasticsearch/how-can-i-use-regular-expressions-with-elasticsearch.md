# How can I use regular expressions with Elasticsearch?
// plain

Regular expressions (regex) can be used in Elasticsearch to search for patterns in strings. The regexp query can be used to match a regular expression against all fields in a document or against a specific field.

Example code block:
```
GET /_search
{
    "query": {
        "regexp": {
            "title": ".*Elastic.*"
        }
    }
}
```

This example will return all documents that contain the string "Elastic" in the title field.

The regexp query has several parameters that can be used to refine the search:

* `flags` - This parameter allows you to set flags for the regular expression. For example, `flags` can be set to `"ALL"` to enable case-insensitive matching.
* `max_determinized_states` - This parameter allows you to set the maximum number of states that can be generated for the regular expression.
* `rewrite` - This parameter allows you to specify how the regular expression should be rewritten.

## Helpful links

* [Elasticsearch Documentation - Regexp Query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-regexp-query.html)
* [Regular Expressions Cheat Sheet](https://www.rexegg.com/regex-quickstart.html)

onelinerhub: [How can I use regular expressions with Elasticsearch?](https://onelinerhub.com/elasticsearch/how-can-i-use-regular-expressions-with-elasticsearch)