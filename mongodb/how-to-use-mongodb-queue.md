# How to use MongoDB queue?
// plain

MongoDB queue is a queue system that uses MongoDB as its backend. It is a distributed queue system that allows for asynchronous processing of tasks.

## Example code

```
from mongodb_queue import MongoDBQueue

# Create a queue
queue = MongoDBQueue('localhost', 27017, 'my_queue')

# Add a task to the queue
queue.put('my_task')

# Get a task from the queue
task = queue.get()
```

## Output example

```
my_task
```

## Code explanation

- `from mongodb_queue import MongoDBQueue`: imports the MongoDBQueue class from the mongodb_queue module.
- `queue = MongoDBQueue('localhost', 27017, 'my_queue')`: creates a MongoDBQueue instance with the given parameters.
- `queue.put('my_task')`: adds a task to the queue.
- `task = queue.get()`: gets a task from the queue.

## Helpful links
- [MongoDB Queue Documentation](https://mongodb-queue.readthedocs.io/en/latest/)
- [MongoDB Queue GitHub Repository](https://github.com/mongodb-labs/mongodb-queue)

onelinerhub: [How to use MongoDB queue?](https://onelinerhub.com/mongodb/how-to-use-mongodb-queue)