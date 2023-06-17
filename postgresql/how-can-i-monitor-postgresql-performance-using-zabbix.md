# How can I monitor PostgreSQL performance using Zabbix?
// plain

Zabbix is a powerful monitoring tool that can be used to monitor the performance of PostgreSQL databases. The following steps outline how to set up Zabbix for PostgreSQL monitoring:

1. Install the Zabbix Agent on the PostgreSQL server.
2. Create a Zabbix user on the PostgreSQL server.
3. Configure the Zabbix Agent to connect to the PostgreSQL server.
4. Create a Zabbix template for PostgreSQL monitoring.
5. Create a Zabbix item to monitor PostgreSQL performance.

Example code for creating a Zabbix item to monitor PostgreSQL performance:

```
UserParameter=postgresql.performance[*],psql -U zabbix_user -d postgres -c "SELECT * FROM pg_stat_activity WHERE state='active'"
```

The code above creates a Zabbix item that will query the pg_stat_activity table in the PostgreSQL database and return the active connections.

## Helpful links

- https://www.zabbix.com/documentation/4.2/manual/config/items/itemtypes/zabbix_agent
- https://www.zabbix.com/documentation/4.2/manual/config/items/itemtypes/user_parameter
- https://www.postgresql.org/docs/current/monitoring-stats.html

onelinerhub: [How can I monitor PostgreSQL performance using Zabbix?](https://onelinerhub.com/postgresql/how-can-i-monitor-postgresql-performance-using-zabbix)