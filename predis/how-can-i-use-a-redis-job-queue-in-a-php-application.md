# How can I use a Redis job queue in a PHP application?
// plain

A Redis job queue can be used in a PHP application to process asynchronous tasks in the background. This can be done by pushing tasks onto a Redis queue, and then having a worker process that pulls tasks off the queue and executes them.

## Example code

```php
// Push a job to the queue
$redis->rpush('queue', json_encode(['task' => 'sendEmail', 'params' => ['to' => 'example@example.com']]));

// Worker process to pull jobs from the queue
while($job = $redis->lpop('queue')) {
    $job = json_decode($job, true);
    switch ($job['task']) {
        case 'sendEmail':
            sendEmail($job['params']['to']);
            break;
    }
}

function sendEmail($to) {
    // Send an email to $to
    echo "Sending an email to $to\n";
}
```

## Output example

```
Sending an email to example@example.com
```

## Code explanation


1. `$redis->rpush('queue', json_encode(['task' => 'sendEmail', 'params' => ['to' => 'example@example.com']]));` - This line pushes a job onto the Redis queue. The job is encoded as JSON and contains two pieces of information - the task to be executed, and the parameters to be passed to the task.

2. `while($job = $redis->lpop('queue')) {` - This line starts an infinite loop that pulls jobs off the queue and executes them.

3. `$job = json_decode($job, true);` - This line decodes the job from JSON.

4. `switch ($job['task']) {` - This line checks the task name in the job and executes the appropriate code based on that.

5. `sendEmail($job['params']['to']);` - This line calls the `sendEmail` function and passes it the `to` parameter from the job.

6. `function sendEmail($to) {` - This is the `sendEmail` function which is called by the code above. It simply prints a message indicating that an email was sent.

## Helpful links

- [Redis Queue - PHP Library](https://github.com/php-enqueue/redis)
- [Redis Queue - Documentation](https://redis.io/commands/rpush)

onelinerhub: [How can I use a Redis job queue in a PHP application?](https://onelinerhub.com/predis/how-can-i-use-a-redis-job-queue-in-a-php-application)