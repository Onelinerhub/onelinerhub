# How to use CLI sed to modify data in a Kafka topic?
// plain

Using `sed` in the command line interface (CLI) to modify data in a Kafka topic requires the following steps:

1. Create a Kafka topic with the command `bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic <topic_name>`

2. Use `bin/kafka-console-producer.sh` to produce messages to the topic. For example, `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic <topic_name>`

3. Use `bin/kafka-console-consumer.sh` to consume the messages from the topic. For example, `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic_name> --from-beginning`

4. Use `sed` to modify the data. For example, `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic_name> --from-beginning | sed 's/old_text/new_text/g'`

5. Use `bin/kafka-console-producer.sh` to produce the modified messages to the topic. For example, `bin/kafka-console-producer.sh --broker-list localhost:9092 --topic <topic_name> < modified_message`

6. Use `bin/kafka-console-consumer.sh` to consume the modified messages from the topic. For example, `bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic_name> --from-beginning`

7. Verify that the messages have been modified correctly.

Example code block:
```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic_name> --from-beginning | sed 's/old_text/new_text/g'
```

Output (if any):
```
modified_message
```

## Helpful links
- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [sed Documentation](https://www.gnu.org/software/sed/manual/sed.html)

onelinerhub: [How to use CLI sed to modify data in a Kafka topic?](https://onelinerhub.com/cli-sed/how-to-use-cli-sed-to-modify-data-in-a-kafka-topic)