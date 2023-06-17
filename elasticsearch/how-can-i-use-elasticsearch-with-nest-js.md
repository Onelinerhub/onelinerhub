# How can I use Elasticsearch with Nest.js?
// plain

Nest.js is an open source web framework for Node.js that allows developers to quickly build modern server-side applications. It can be used with Elasticsearch to create powerful search and analytics applications.

To use Elasticsearch with Nest.js, you will need to install the `@nestjs/elasticsearch` package. This package provides a simple way to connect to an Elasticsearch cluster and provides the necessary components for interacting with the cluster.

```
npm install @nestjs/elasticsearch
```

Once the package is installed, you can create a service that will be used to connect to the Elasticsearch cluster. This service will need to provide the necessary configuration for connecting to the cluster, such as the host and port.

```
import { Injectable } from '@nestjs/common';
import { Client } from '@elastic/elasticsearch';

@Injectable()
export class ElasticsearchService {
  constructor() {
    this.client = new Client({
      node: 'http://localhost:9200',
    });
  }
}
```

Once the service is created, it can be used to interact with the Elasticsearch cluster. For example, you can use it to create an index, add documents to the index, and perform searches.

```
import { Injectable } from '@nestjs/common';
import { Client } from '@elastic/elasticsearch';

@Injectable()
export class ElasticsearchService {
  constructor() {
    this.client = new Client({
      node: 'http://localhost:9200',
    });
  }

  async createIndex(indexName) {
    const { body } = await this.client.indices.create({
      index: indexName,
    });

    console.log(body);
  }
}
```

## Output example

```
{
  acknowledged: true,
  shards_acknowledged: true,
  index: 'my_index'
}
```

## Code explanation

- `npm install @nestjs/elasticsearch`: Installs the `@nestjs/elasticsearch` package.
- `new Client({ node: 'http://localhost:9200' })`: Creates an instance of the Elasticsearch client with the specified configuration.
- `await this.client.indices.create({ index: indexName })`: Creates an index with the specified name.

## Helpful links
- [Nest.js](https://nestjs.com/)
- [Elasticsearch](https://www.elastic.co/products/elasticsearch)
- [@nestjs/elasticsearch](https://www.npmjs.com/package/@nestjs/elasticsearch)

onelinerhub: [How can I use Elasticsearch with Nest.js?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-nest-js)