# How to use Prometheus with PHP Symfony?
// plain

Prometheus can be used with PHP Symfony to monitor application performance.

To use Prometheus with Symfony, you need to install the [PrometheusBundle](https://github.com/Innmind/PrometheusBundle) package.

Once installed, you can configure the bundle in your `config/bundles.php` file:

```php
return [
    // ...
    Innmind\PrometheusBundle\InnmindPrometheusBundle::class => ['all' => true],
];
```

Then, you can add the Prometheus routes to your `config/routes.yaml` file:

```yaml
innmind_prometheus:
    resource: "@InnmindPrometheusBundle/Resources/config/routing.yaml"
```

Finally, you can start collecting metrics in your application by using the provided `Metrics` class:

```php
use Innmind\Prometheus\Metrics;

$metrics = new Metrics;
$metrics->counter('my_counter')->increment();
```

This will create a counter metric called `my_counter` and increment it by one.

For more information, please refer to the [PrometheusBundle documentation](https://github.com/Innmind/PrometheusBundle/blob/master/README.md).

onelinerhub: [How to use Prometheus with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-prometheus-with-php-symfony)