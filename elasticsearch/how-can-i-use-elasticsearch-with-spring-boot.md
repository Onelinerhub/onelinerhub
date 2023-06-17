# How can I use Elasticsearch with Spring Boot?
// plain

Elasticsearch is a distributed, RESTful search and analytics engine capable of solving a growing number of use cases. It can be used in combination with Spring Boot to build powerful search applications.

To use Elasticsearch with Spring Boot, you need to add the Elasticsearch dependency to your project. For example, if you are using Maven, you can add the following to your pom.xml file:

```
<dependency>
  <groupId>org.elasticsearch</groupId>
  <artifactId>elasticsearch</artifactId>
  <version>6.2.4</version>
</dependency>
```

Once the dependency is added, you can create a configuration class that sets up the Elasticsearch client. The following example code will create an instance of the Elasticsearch client and expose it as a bean:

```
@Configuration
public class ElasticsearchConfig {

    @Bean
    public Client client() throws Exception {
        Settings settings = Settings.builder()
            .put("cluster.name", "my-cluster")
            .build();
        TransportClient client = new PreBuiltTransportClient(settings);
        client.addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("localhost"), 9300));
        return client;
    }

}
```

The configuration class is responsible for creating an instance of the Elasticsearch client and exposing it as a bean. The configuration class also sets up the cluster name and the transport address for the client.

Once the configuration class is set up, you can use the Elasticsearch client in your application. For example, you can use the client to search for documents in an index:

```
SearchResponse response = client.prepareSearch("my-index")
    .setTypes("my-type")
    .setQuery(QueryBuilders.matchQuery("field", "value"))
    .execute()
    .actionGet();
```

The above example code will search for documents in the `my-index` index, with the `my-type` type, that match the `field` field with the `value` value.

By combining Elasticsearch and Spring Boot, you can quickly and easily build powerful search applications.

## Helpful links
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/client/java-api/current/index.html)
- [Spring Boot Documentation](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/)

onelinerhub: [How can I use Elasticsearch with Spring Boot?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-spring-boot)