# How to use watch in MongoDB?
// plain

MongoDB's `watch` command is used to monitor the performance of a MongoDB instance. It provides real-time statistics on the server's operations, such as the number of operations, the amount of data read and written, and the number of connections.

## Example

```
> db.runCommand({ watch: 1 })
{
	"ok" : 1
}
```

The output of the command will be `{ "ok" : 1 }` which indicates that the command was successful.

The `watch` command has several options that can be used to customize the output. These include:

- `start`: Start the watch command.
- `stop`: Stop the watch command.
- `reset`: Reset the watch command.
- `verbosity`: Set the verbosity level of the output.
- `filter`: Filter the output to only show certain operations.

Detailed explanation of each option can be found in the [MongoDB documentation](https://docs.mongodb.com/manual/reference/command/watch/).

onelinerhub: [How to use watch in MongoDB?](https://onelinerhub.com/mongodb/how-to-use-watch-in-mongodb)