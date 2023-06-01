# How can I use Elastic APM to monitor performance in a Laravel application?
// plain

Elastic APM is a powerful tool for monitoring performance in a Laravel application. It uses real-time data to provide insights into application performance and identify potential issues.

To use Elastic APM in a Laravel application, first install the Elastic APM PHP Agent via Composer:

```
composer require elastic/apm-php-agent
```

Then add the following line to the `bootstrap/app.php` file:

```
$app->register(Elastic\Apm\Laravel\ApmServiceProvider::class);
```

This will enable the agent and start collecting performance data.

Next, configure the agent by adding the following to the `.env` file:

```
ELASTIC_APM_SERVICE_NAME=my-app
ELASTIC_APM_SERVER_URL=http://localhost:8200
ELASTIC_APM_SECRET_TOKEN=my-secret-token
```

Finally, you can use the `elastic-apm` artisan command to view performance data:

```
php artisan elastic-apm:report
```

This will display a report of the performance data collected by the agent.

## Helpful links
- [Elastic APM Documentation](https://www.elastic.co/guide/en/apm/get-started/current/index.html)
- [Elastic APM PHP Agent](https://github.com/elastic/apm-agent-php)

onelinerhub: [How can I use Elastic APM to monitor performance in a Laravel application?](https://onelinerhub.com/php-elastica/how-can-i-use-elastic-apm-to-monitor-performance-in-a-laravel-application)