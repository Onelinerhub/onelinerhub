# How do I decide whether to use a keyword or text field when indexing documents in Elasticsearch?
// plain

When deciding whether to use a keyword or text field when indexing documents in Elasticsearch, it is important to consider the type of data you are indexing and the desired use cases.

For example, if you are indexing a person's name, you should use a keyword field since you will likely want to search for exact matches.

```
PUT my_index
{
  "mappings": {
    "properties": {
      "name": {
        "type": "keyword"
      }
    }
  }
}
```

On the other hand, if you are indexing a description of a product, you should use a text field since you will likely want to search for words and phrases within the text.

```
PUT my_index
{
  "mappings": {
    "properties": {
      "description": {
        "type": "text"
      }
    }
  }
}
```

The main difference between keyword and text fields is that keyword fields are analyzed and indexed as-is, while text fields are tokenized, lower-cased, and indexed as individual words. This means that keyword fields are better for exact matches, while text fields are better for searching words and phrases within a document.

For more information, please refer to the following links:

- [Elasticsearch Field Types](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html)
- [Keyword vs Text Fields](https://www.elastic.co/guide/en/elasticsearch/guide/current/_index_time_search_as_you_type.html)

onelinerhub: [How do I decide whether to use a keyword or text field when indexing documents in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-decide-whether-to-use-a-keyword-or-text-field-when-indexing-documents-in-elasticsearch)