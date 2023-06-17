# How can I use Elasticsearch with Node.js?
// plain

****

Using Elasticsearch with Node.js is relatively straightforward. To get started, you'll need to install the Elasticsearch JavaScript client library. This can be done with the following command:

```
npm install elasticsearch
```

Once the library is installed, you can use it to connect to an Elasticsearch cluster. An example of how to do this is shown below:

```javascript
const { Client } = require('elasticsearch');
const client = new Client({
  host: 'localhost:9200',
  log: 'trace'
});
```

Once the connection is established, you can use the client library to perform operations such as indexing, searching, and aggregations. For example, the following code snippet shows how to index a document:

```javascript
client.index({
  index: 'my-index',
  body: {
    title: 'My first document',
    content: 'This is my first document in Elasticsearch'
  }
}, (err, resp, status) => {
  console.log(resp);
});
```

The output of this code will be a JSON object containing the details of the indexed document.

To learn more about using Elasticsearch with Node.js, the following resources are helpful:
- [Elasticsearch Node.js Client Documentation](https://www.elastic.co/guide/en/elasticsearch/client/javascript-api/current/index.html)
- [Node.js and Elasticsearch Tutorial](https://www.codementor.io/@mayowa.a/how-to-setup-elasticsearch-on-ubuntu-and-use-it-with-nodejs-du107yb1c)
- [Elasticsearch Node.js Tutorial](https://www.elastic.co/blog/getting-started-with-elasticsearch-and-node-js)

onelinerhub: [How can I use Elasticsearch with Node.js?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-node-js)