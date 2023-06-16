# How can I use Elasticsearch and Hunspell to add Russian language support to my software?
// plain

To add Russian language support to your software using Elasticsearch and Hunspell, you need to do the following:

1. Install the Elasticsearch [Russian Language Analyzer](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-lang-analyzer.html#analysis-lang-plugin-russian) plugin.

2. Install the [Hunspell Russian dictionary](https://github.com/wooorm/dictionaries/blob/master/dictionaries/ru/index.dic) on your system.

3. Configure the Elasticsearch index to use the Russian language analyzer and Hunspell dictionary. This can be done using the following example code:

```
PUT /myindex
{
  "settings": {
    "analysis": {
      "filter": {
        "my_russian_hunspell": {
          "type": "hunspell",
          "locale": "ru_RU",
          "dedup": true
        }
      },
      "analyzer": {
        "my_russian_analyzer": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "my_russian_hunspell"
          ]
        }
      }
    }
  }
}
```

4. Create a mapping for the fields in your index that should be analyzed using the Russian language analyzer. This can be done using the following example code:

```
PUT /myindex/_mapping
{
  "properties": {
    "title": {
      "type": "text",
      "analyzer": "my_russian_analyzer"
    }
  }
}
```

5. Index documents in your Elasticsearch index using the Russian language analyzer. This can be done using the following example code:

```
POST /myindex/_doc
{
  "title": "Это тестовый документ"
}
```

6. Query the indexed documents using the Russian language analyzer. This can be done using the following example code:

```
GET /myindex/_search
{
  "query": {
    "match": {
      "title": "тестовый"
    }
  }
}
```

The output of this query should be the document you indexed in step 5.

For more information, please refer to the following links:

- [Elasticsearch Russian Language Analyzer](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-lang-analyzer.html#analysis-lang-plugin-russian)
- [Hunspell Russian Dictionary](https://github.com/wooorm/dictionaries/blob/master/dictionaries/ru/index.dic)
- [Elasticsearch Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)

onelinerhub: [How can I use Elasticsearch and Hunspell to add Russian language support to my software?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-and-hunspell-to-add-russian-language-support-to-my-software)