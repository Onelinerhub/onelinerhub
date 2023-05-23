# How to set up a scheduler in Symfony with PHP?
// plain

Symfony provides a powerful way to set up a scheduler with PHP.

```php
// Create a new CronJob instance
$job = new CronJob();

// Set the command to execute
$job->setCommand('php bin/console app:my-task');

// Set the schedule
$job->setSchedule('0 0 * * *');

// Save the job to the database
$job->save();
```

The above code will create a new CronJob instance, set the command to execute, set the schedule and save the job to the database.

The schedule is set using a cron expression, which is a string of five fields separated by spaces. The fields are:

1. Minute (0-59)
2. Hour (0-23)
3. Day of Month (1-31)
4. Month (1-12)
5. Day of Week (0-6)

For more information, please refer to the [Symfony documentation](https://symfony.com/doc/current/components/console/scheduling.html).

onelinerhub: [How to set up a scheduler in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-set-up-a-scheduler-in-symfony-with-php)