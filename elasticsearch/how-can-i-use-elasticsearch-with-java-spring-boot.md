# How can I use Elasticsearch with Java Spring Boot?
// plain

Elasticsearch can be used with Java Spring Boot in order to build powerful search applications. The following steps can be used to configure Elasticsearch with Spring Boot:

1. Add the required dependencies to the project's `pom.xml` file:

```xml
<dependency>
  <groupId>org.springframework.data</groupId>
  <artifactId>spring-data-elasticsearch</artifactId>
  <version>4.0.0.RELEASE</version>
</dependency>
```

2. Configure the `application.yml` file with the necessary cluster information:

```yml
spring:
  data:
    elasticsearch:
      cluster-name: my-cluster-name
      cluster-nodes: localhost:9300
```

3. Create an `ElasticsearchTemplate` bean in the Spring configuration class:

```java
@Bean
public ElasticsearchTemplate elasticsearchTemplate() {
    return new ElasticsearchTemplate(client());
}
```

4. Create an `ElasticsearchOperations` bean in the Spring configuration class:

```java
@Bean
public ElasticsearchOperations elasticsearchOperations() {
    return new ElasticsearchTemplate(client());
}
```

5. Use the `ElasticsearchTemplate` and `ElasticsearchOperations` beans to perform search operations.

For more information, please refer to the following links:

- [Spring Data Elasticsearch Reference Guide](https://docs.spring.io/spring-data/elasticsearch/docs/current/reference/html/)
- [Spring Data Elasticsearch Tutorial](https://www.baeldung.com/spring-data-elasticsearch-tutorial)

onelinerhub: [How can I use Elasticsearch with Java Spring Boot?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-java-spring-boot)