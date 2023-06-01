# How can I integrate PHP Elastica with NestJS?
// plain

Integrating PHP Elastica with NestJS is relatively straightforward. The first step is to install the PHP Elastica library with Composer.

```
composer require elastica/elastica
```

Next, create a service in NestJS to make use of the PHP Elastica library. The service should inject the Elastica client and use it to interact with the Elasticsearch cluster.

```typescript
import { Injectable } from '@nestjs/common';
import { Client } from 'elastica';

@Injectable()
export class ElasticsearchService {
  private readonly client: Client;

  constructor(client: Client) {
    this.client = client;
  }

  async search(query: any): Promise<any> {
    return await this.client.search(query);
  }
}
```

Finally, register the service in the NestJS application module.

```typescript
import { Module } from '@nestjs/common';
import { ElasticsearchModule } from '@nestjs/elasticsearch';
import { ElasticsearchService } from './elasticsearch.service';

@Module({
  imports: [
    ElasticsearchModule.register({
      node: 'http://localhost:9200',
    }),
  ],
  providers: [ElasticsearchService],
})
export class AppModule {}
```

Now the service can be injected into any other module and used to interact with the Elasticsearch cluster.

## Code explanation


1. `composer require elastica/elastica` - This command installs the PHP Elastica library with Composer.
2. `@Injectable()` - This decorator marks the `ElasticsearchService` as an injectable NestJS service.
3. `constructor(client: Client)` - This constructor injects an `Elastica` client into the service.
4. `async search(query: any): Promise<any>` - This method uses the injected `Elastica` client to send a search query to the Elasticsearch cluster.
5. `ElasticsearchModule.register()` - This registers the `ElasticsearchModule` with the NestJS application module, providing it with the necessary configuration to interact with the Elasticsearch cluster.

## Helpful links

- [PHP Elastica Documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html)
- [NestJS Elasticsearch Module](https://docs.nestjs.com/techniques/elasticsearch)

onelinerhub: [How can I integrate PHP Elastica with NestJS?](https://onelinerhub.com/php-elastica/how-can-i-integrate-php-elastica-with-nestjs)