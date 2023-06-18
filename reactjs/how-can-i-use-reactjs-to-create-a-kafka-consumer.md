# How can I use ReactJS to create a Kafka consumer?
// plain

ReactJS can be used to create a Kafka consumer by leveraging the [KafkaJS](https://kafkajs.org/) library. To do this, first install the library:

```
npm install kafkajs
```

Then, create a consumer for the desired topic:

```javascript
const { Kafka } = require('kafkajs')

const kafka = new Kafka({
  clientId: 'my-app',
  brokers: ['kafka1:9092', 'kafka2:9092']
})

const consumer = kafka.consumer({ groupId: 'test-group' })

await consumer.connect()
await consumer.subscribe({ topic: 'topic-name' })

await consumer.run({
  eachMessage: async ({ topic, partition, message }) => {
    console.log({
      value: message.value.toString(),
    })
  },
})
```

This code will create a consumer for the `topic-name` topic, and log the values of each message that is received.

To stop the consumer, simply call `consumer.disconnect()`.

## Helpful links

- [KafkaJS Documentation](https://kafkajs.org/docs)
- [ReactJS Documentation](https://reactjs.org/docs/getting-started.html)

onelinerhub: [How can I use ReactJS to create a Kafka consumer?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-to-create-a-kafka-consumer)