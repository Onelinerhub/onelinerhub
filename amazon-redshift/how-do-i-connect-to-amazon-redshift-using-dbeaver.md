# How do I connect to Amazon Redshift using DBeaver?
// plain

1. First, install [DBeaver](https://dbeaver.io/download/) and open it.
2. Go to Database > New Connection.
3. Select Amazon Redshift from the list of Database Drivers.
4. Enter the connection information, such as host, port, username and password.
5. Click Test Connection to make sure the connection is successful.
6. Click OK to save the connection.
7. You can now connect to Amazon Redshift using DBeaver.

## Example code


```
$ psql -h <host> -p <port> -U <username> -d <database_name>
```

## Output example

```
psql (9.4.5, server 8.0.2)
SSL connection (cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

<database_name>=#
```

## Code explanation

- `psql`: the PostgreSQL command line interface
- `-h <host>`: the hostname or IP address of the server
- `-p <port>`: the port number of the server
- `-U <username>`: the username for the server
- `-d <database_name>`: the name of the database to connect to

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [DBeaver Documentation](https://dbeaver.io/documentation/)

onelinerhub: [How do I connect to Amazon Redshift using DBeaver?](https://onelinerhub.com/amazon-redshift/how-do-i-connect-to-amazon-redshift-using-dbeaver)