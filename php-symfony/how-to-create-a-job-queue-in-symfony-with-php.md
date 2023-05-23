# How to create a job queue in Symfony with PHP?
// plain

Creating a job queue in Symfony with PHP is a simple process.

First, create a job class that implements the `ShouldQueue` interface:

```php
<?php

namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Queue\SerializesModels;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Contracts\Queue\ShouldQueue;

class ProcessPodcast implements ShouldQueue
{
    use InteractsWithQueue, Queueable, SerializesModels;

    /**
     * Create a new job instance.
     *
     * @return void
     */
    public function __construct()
    {
        //
    }

    /**
     * Execute the job.
     *
     * @return void
     */
    public function handle()
    {
        //
    }
}
```

Then, dispatch the job to the queue:

```php
<?php

use App\Jobs\ProcessPodcast;

ProcessPodcast::dispatch();
```

The job will be added to the queue and processed when the queue is ready.

## Helpful links

- [Laravel Queues](https://laravel.com/docs/queues)
- [Symfony Queues](https://symfony.com/doc/current/components/messenger.html)

onelinerhub: [How to create a job queue in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-create-a-job-queue-in-symfony-with-php)