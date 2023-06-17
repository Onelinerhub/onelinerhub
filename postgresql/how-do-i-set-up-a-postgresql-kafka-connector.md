# How do I set up a PostgreSQL Kafka Connector?
// plain

1. Install the [Confluent Platform](https://www.confluent.io/product/confluent-platform/) to your machine.

2. Create a Kafka Connector configuration file. The following example uses a file named `postgres-sink.properties`:
```
name=postgres-sink
connector.class=io.confluent.connect.jdbc.JdbcSinkConnector
tasks.max=1
connection.url=jdbc:postgresql://<hostname>:<port>/<database>
connection.user=<username>
connection.password=<password>
topics=<topic1>,<topic2>
auto.create=true
insert.mode=upsert
```

3. Run the Kafka Connector with the configuration file:
```
$ confluent load postgres-sink -d postgres-sink.properties
```

4. Verify that the connector is running:
```
$ confluent status connectors
```
## Output example

```
postgres-sink               RUNNING
```

5. Create a PostgreSQL table for the topics you specified:
```
CREATE TABLE <topic1> (
  id SERIAL,
  key VARCHAR(255),
  value VARCHAR(255)
);
```

6. Publish messages to the topics you specified in the configuration file.

7. Verify that the messages have been successfully sent to your PostgreSQL database.

## Helpful links

- [Confluent Platform Documentation](https://docs.confluent.io/current/connect/index.html)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

onelinerhub: [How do I set up a PostgreSQL Kafka Connector?](https://onelinerhub.com/postgresql/how-do-i-set-up-a-postgresql-kafka-connector)