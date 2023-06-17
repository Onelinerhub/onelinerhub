# How can I use PostgreSQL with Zabbix?
// plain

PostgreSQL is a powerful open source relational database system that can be used with Zabbix for storing and managing data. To use PostgreSQL with Zabbix, you need to install the PostgreSQL server and client on your system and create a database for Zabbix.

Once the database is created, you can configure Zabbix by editing the configuration file and setting the database type to PostgreSQL. For example, the following code block can be used to configure Zabbix to use PostgreSQL:
```
DBName=zabbix
DBUser=zabbix
DBPassword=zabbix
DBPort=5432
DBHost=localhost
```

The above code block sets the database name, user, password, port, and host for Zabbix to use with PostgreSQL. After the configuration is complete, you can start the Zabbix server and connect it to the PostgreSQL database.

To access the data stored in the PostgreSQL database, you can use the PostgreSQL command line utility called psql. You can use the psql utility to query the database, create tables, and perform other operations.

For more information on using PostgreSQL with Zabbix, you can refer to the [Zabbix documentation](https://www.zabbix.com/documentation/current/manual/installation/requirements).

## Code explanation


1. `DBName=zabbix` - sets the database name for Zabbix to use with PostgreSQL.
2. `DBUser=zabbix` - sets the database user for Zabbix to use with PostgreSQL.
3. `DBPassword=zabbix` - sets the database password for Zabbix to use with PostgreSQL.
4. `DBPort=5432` - sets the database port for Zabbix to use with PostgreSQL.
5. `DBHost=localhost` - sets the database host for Zabbix to use with PostgreSQL.
6. `psql` - command line utility to query the PostgreSQL database.

onelinerhub: [How can I use PostgreSQL with Zabbix?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-with-zabbix)