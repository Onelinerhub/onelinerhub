# How to use Apache Kafka with Symfony and PHP?
// plain

Using Apache Kafka with Symfony and PHP is relatively straightforward.

First, you need to install the [php-rdkafka](https://github.com/arnaud-lb/php-rdkafka) library. This library provides an interface for PHP to communicate with Apache Kafka.

Once the library is installed, you can use the following code to connect to Apache Kafka:

```php
$conf = new RdKafka\Conf();
$conf->set('group.id', 'myConsumerGroup');

$rk = new RdKafka\Consumer($conf);
$rk->addBrokers("localhost:9092");

$topic = $rk->newTopic("myTopic");
```

The code above creates a new consumer group, adds a broker to the consumer group, and creates a new topic.

You can then use the `$topic` object to produce and consume messages from Apache Kafka. For example, to produce a message:

```php
$topic->produce(RD_KAFKA_PARTITION_UA, 0, "Message payload");
```

And to consume a message:

```php
$msg = $topic->consume(RD_KAFKA_PARTITION_UA, 1000);
echo $msg->payload;
```

## Helpful links

- [php-rdkafka](https://github.com/arnaud-lb/php-rdkafka)
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)

onelinerhub: [How to use Apache Kafka with Symfony and PHP?](https://onelinerhub.com/php-symfony/how-to-use-apache-kafka-with-symfony-and-php)