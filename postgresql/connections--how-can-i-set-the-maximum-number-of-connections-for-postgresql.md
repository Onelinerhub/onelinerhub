# connections

How can I set the maximum number of connections for PostgreSQL?
// plain

The maximum number of connections for PostgreSQL can be set with the `max_connections` parameter in the `postgresql.conf` file. This file is typically located in the `data` directory of the PostgreSQL installation.

Example code block to set the maximum number of connections to 100:
```
max_connections = 100
```

The `max_connections` parameter can be set to any number, but it should be set to a value that is appropriate for the system's hardware and software configuration. Generally, the maximum number of connections should not exceed the number of available memory and processor cores.

Once the `max_connections` parameter has been set, the PostgreSQL server must be restarted in order for the changes to take effect. This can be done with the following command:

```
sudo service postgresql restart
```

The output of the command should look something like this:
```
Stopping PostgreSQL 11 database server: main.
Starting PostgreSQL 11 database server: main.
```

## Code explanation

- `max_connections`: Parameter in the `postgresql.conf` file that sets the maximum number of connections for PostgreSQL
- `postgresql.conf`: Configuration file for PostgreSQL, typically located in the `data` directory of the PostgreSQL installation
- `sudo service postgresql restart`: Command used to restart the PostgreSQL server in order for changes to the `max_connections` parameter to take effect

## Helpful links
- [PostgreSQL Documentation - Configuration File](https://www.postgresql.org/docs/11/runtime-config-file.html)
- [PostgreSQL Documentation - Maximum Number of Connections](https://www.postgresql.org/docs/11/runtime-config-connection.html#RUNTIME-CONFIG-CONNECTION-MAX)

onelinerhub: [connections

How can I set the maximum number of connections for PostgreSQL?](https://onelinerhub.com/postgresql/connections--how-can-i-set-the-maximum-number-of-connections-for-postgresql)