# How can I use Laravel Queue to process jobs in PHP?
// plain

Laravel Queue provides a unified API across a variety of different queue backends. It can be used to process jobs in PHP in the following way:

1. Create a job class that extends the `Illuminate\Bus\Queueable` class. This class contains the logic to be performed by the job.

2. Create a job handler class that implements the `Illuminate\Contracts\Queue\ShouldQueue` interface. This class will receive the job instance when it is dispatched.

3. Dispatch the job using the `dispatch` method.

```php
use App\Jobs\ProcessJob;

ProcessJob::dispatch();
```

4. The job will be added to the queue and processed by the queue worker.

5. Once the job is processed, the job handler class will be called and the job logic will be executed.

6. The job can be monitored using the queue dashboard provided by Laravel.

7. Further information can be found in the [Laravel Documentation](https://laravel.com/docs/7.x/queues).

**## Helpful links**
- [Laravel Documentation](https://laravel.com/docs/7.x/queues)

onelinerhub: [How can I use Laravel Queue to process jobs in PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-laravel-queue-to-process-jobs-in-php)