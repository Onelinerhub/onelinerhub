# How do I configure PHP Elastica using YML?
// plain

To configure PHP Elastica using YML, you first need to create a YML file with the desired configuration. The most basic configuration includes the following:

```
elastica:
    connections:
        default:
            host: localhost
            port: 9200
```

This configures the default connection to the localhost on port 9200. To add more connections, you can use the `connections` key and add additional connection configurations. For example:

```
elastica:
    connections:
        default:
            host: localhost
            port: 9200
        staging:
            host: staging.example.com
            port: 9200
        production:
            host: production.example.com
            port: 9200
```

This configures three connections, the default connection to the localhost on port 9200, a staging connection to staging.example.com on port 9200, and a production connection to production.example.com on port 9200.

You can also configure additional options such as `timeout`, `retries`, `connections`, `headers`, `proxy`, and `transport`. For example:

```
elastica:
    connections:
        default:
            host: localhost
            port: 9200
            timeout: 5
            retries: 3
            headers:
                Authorization: 'Basic QWxhZGRpbjpPcGVuU2VzYW1l'
```

This configures the default connection to the localhost on port 9200 with a timeout of 5 seconds, 3 retries, and an Authorization header.

For more information on configuring PHP Elastica using YML, see the [official documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-en/current/configuration.html).

onelinerhub: [How do I configure PHP Elastica using YML?](https://onelinerhub.com/php-elastica/how-do-i-configure-php-elastica-using-yml)