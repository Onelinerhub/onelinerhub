# How can I increase the maximum number of connections allowed in PostgreSQL?
// plain

In order to increase the maximum number of connections allowed in PostgreSQL, there are several steps you can take.

1. Set the `max_connections` parameter in the `postgresql.conf` configuration file. This parameter sets the maximum number of concurrent connections allowed. For example, to set the maximum number of connections to 100:

```
max_connections = 100
```

2. You can also set the `superuser_reserved_connections` parameter in the `postgresql.conf` configuration file. This parameter sets the number of connections reserved for superusers. For example, to set the number of reserved connections to 10:

```
superuser_reserved_connections = 10
```

3. You can also increase the `max_prepared_transactions` parameter in the `postgresql.conf` configuration file. This parameter sets the maximum number of prepared transactions that can be active at any given time. For example, to set the maximum number of prepared transactions to 20:

```
max_prepared_transactions = 20
```

4. Finally, you can also increase the `shared_buffers` parameter in the `postgresql.conf` configuration file. This parameter sets the amount of memory dedicated to shared memory buffers. Increasing this parameter can help improve performance and allow more connections. For example, to set the shared memory buffer size to 8GB:

```
shared_buffers = 8GB
```

After making any changes to the `postgresql.conf` configuration file, you will need to restart the PostgreSQL server for the changes to take effect.

## Helpful links
* [PostgreSQL Documentation: Connection Settings](https://www.postgresql.org/docs/current/runtime-config-connection.html)
* [PostgreSQL Documentation: Server Configuration](https://www.postgresql.org/docs/current/runtime-config.html)

onelinerhub: [How can I increase the maximum number of connections allowed in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-increase-the-maximum-number-of-connections-allowed-in-postgresql)