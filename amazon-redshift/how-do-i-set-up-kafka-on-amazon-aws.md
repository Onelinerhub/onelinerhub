# How do I set up Kafka on Amazon AWS?
// plain

1. **Create an EC2 instance**: To set up Kafka on Amazon AWS, the first step is to create an EC2 instance. This can be done by logging into the AWS console and navigating to the EC2 dashboard.

2. **Install Java**: Once the EC2 instance is created, install Java on the instance. This can be done by running the following command:

```
sudo yum install java-1.8.0
```

3. **Download and install Kafka**: Now download the latest Kafka version from the Apache website. Then extract the files and move them to the appropriate directory.

4. **Start the ZooKeeper server**: ZooKeeper is a distributed configuration service and is used by Kafka for coordination. To start the ZooKeeper server, run the following command:

```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

5. **Start the Kafka server**: After the ZooKeeper server is started, start the Kafka server. To do this, run the following command:

```
bin/kafka-server-start.sh config/server.properties
```

6. **Create a topic**: Finally, create a topic in Kafka. This can be done by running the following command:

```
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
```

7. **Test the setup**: To test the setup, you can produce and consume messages from the topic. To do this, run the following commands:

```
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
```

```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```

**## Helpful links**

- [Apache Kafka](https://kafka.apache.org/)
- [AWS EC2](https://aws.amazon.com/ec2/)

onelinerhub: [How do I set up Kafka on Amazon AWS?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-kafka-on-amazon-aws)