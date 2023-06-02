# How can I configure TLS encryption for a connection between PHP and Redis?
// plain

TLS encryption can be configured for a connection between PHP and Redis using the `tls` connection option. For example,

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379, null, null, null, null, [
    'tls' => [
        'ca_cert_path' => '/path/to/ca_cert.pem',
        'cert_path' => '/path/to/cert.pem',
        'key_path' => '/path/to/key.pem',
    ]
]);
```

The `ca_cert_path` option is the path to the certificate authority's certificate. The `cert_path` option is the path to the client's certificate. The `key_path` option is the path to the client's private key.

Once the connection is established, you can check the TLS encryption status using the `Redis::getTlsVersion()` method:

```
$tlsVersion = $redis->getTlsVersion();
echo $tlsVersion; // Outputs "TLSv1.2"
```

For more information, see the [PHP Redis documentation](https://redis.io/clients/php).

onelinerhub: [How can I configure TLS encryption for a connection between PHP and Redis?](https://onelinerhub.com/predis/how-can-i-configure-tls-encryption-for-a-connection-between-php-and-redis)