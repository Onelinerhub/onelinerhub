# How can I use PHP Elastica and Zabbix together to monitor application performance?
// plain

PHP Elastica and Zabbix can be used together to monitor application performance. This can be done by creating a script that sends the performance metrics from your application to Zabbix. This script can be written in PHP and use the Elastica library to send the metrics to Zabbix.

## Example code

```php
<?php

use Elastica\Client;

$client = new Client(['host' => 'localhost']);

$zabbix = $client->getIndex('zabbix');

$params = [
    'metric' => 'cpu_usage',
    'value' => '0.5',
];

$zabbix->sendMetric($params);
```

The code above creates an Elastica client, gets an index for the Zabbix server, and sends a metric with the name `cpu_usage` and value `0.5` to the Zabbix server.

The parts of the code are as follows:

1. `use Elastica\Client;` - This imports the Elastica Client class.
2. `$client = new Client(['host' => 'localhost']);` - This creates an Elastica client and sets the host to `localhost`.
3. `$zabbix = $client->getIndex('zabbix');` - This gets an index for the Zabbix server.
4. `$params = [` - This sets up the parameters for the metric.
5. `'metric' => 'cpu_usage',` - This sets the name of the metric to `cpu_usage`.
6. `'value' => '0.5',` - This sets the value of the metric to `0.5`.
7. `$zabbix->sendMetric($params);` - This sends the metric to the Zabbix server.

## Helpful links

- [Elastica Documentation](https://elastica.io/docs/)
- [Zabbix Documentation](https://www.zabbix.com/documentation)

onelinerhub: [How can I use PHP Elastica and Zabbix together to monitor application performance?](https://onelinerhub.com/php-elastica/how-can-i-use-php-elastica-and-zabbix-together-to-monitor-application-performance)