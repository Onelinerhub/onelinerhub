# How can I use Elasticsearch with JavaScript?
// plain

Elasticsearch can be used with JavaScript in a variety of ways.

First, you can use the Elasticsearch JavaScript client library to interact with an Elasticsearch cluster from a web browser or a Node.js application. The library provides a rich set of APIs for creating, updating, and deleting documents, as well as performing searches and aggregations.

For example, the following code snippet uses the Elasticsearch JavaScript client library to search for documents in an Elasticsearch index:

```javascript
const { Client } = require('@elastic/elasticsearch')
const client = new Client({ node: 'http://localhost:9200' })

const { body } = await client.search({
  index: 'my-index',
  body: {
    query: {
      match: {
        title: 'foo'
      }
    }
  }
})

console.log(body.hits.hits)
```

This example will output an array of documents matching the query:

```
[
  {
    _index: 'my-index',
    _type: '_doc',
    _id: '1',
    _score: 1,
    _source: {
      title: 'foo'
    }
  },
  {
    _index: 'my-index',
    _type: '_doc',
    _id: '2',
    _score: 1,
    _source: {
      title: 'foo bar'
    }
  }
]
```

You can also use the Elasticsearch REST API directly from JavaScript. This is useful if you want to perform more complex queries or if you want to use the Elasticsearch query DSL. For example, the following code snippet uses the Elasticsearch REST API to search for documents in an Elasticsearch index:

```javascript
const axios = require('axios')

const { data } = await axios.get('http://localhost:9200/my-index/_search', {
  params: {
    q: 'title:foo'
  }
})

console.log(data.hits.hits)
```

This example will output an array of documents matching the query:

```
[
  {
    _index: 'my-index',
    _type: '_doc',
    _id: '1',
    _score: 1,
    _source: {
      title: 'foo'
    }
  },
  {
    _index: 'my-index',
    _type: '_doc',
    _id: '2',
    _score: 1,
    _source: {
      title: 'foo bar'
    }
  }
]
```

You can also use the Elasticsearch JavaScript client library or the Elasticsearch REST API to create visualizations using JavaScript libraries such as D3.js.

## Helpful links

- [Elasticsearch JavaScript Client](https://www.elastic.co/guide/en/elasticsearch/client/javascript-api/current/index.html)
- [Elasticsearch REST API](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [D3.js](https://d3js.org/)

onelinerhub: [How can I use Elasticsearch with JavaScript?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-javascript)