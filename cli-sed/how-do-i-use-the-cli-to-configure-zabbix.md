# How do I use the CLI to configure Zabbix?
// plain

The Zabbix Command Line Interface (CLI) is a powerful tool for managing and configuring Zabbix. It can be used to perform a variety of tasks, such as creating and managing hosts, users, and groups.

Below is an example of how to use the CLI to configure Zabbix.

First, connect to the Zabbix server:
```
zabbix_cli -s server_name -u username -p password
```

Then, create a new host:
```
zabbix_cli add host name="hostname" ip="127.0.0.1"
```

This will create a new host on the Zabbix server with the specified name and IP address.

Next, create a new user:
```
zabbix_cli add user name="username" password="password"
```

This will create a new user on the Zabbix server with the specified username and password.

Finally, create a new group:
```
zabbix_cli add group name="groupname"
```

This will create a new group on the Zabbix server with the specified name.

The Zabbix CLI can also be used to modify existing hosts, users, and groups, as well as to delete them. For more information on using the Zabbix CLI, please refer to the [Zabbix documentation](https://www.zabbix.com/documentation/4.4/manual/cli).

onelinerhub: [How do I use the CLI to configure Zabbix?](https://onelinerhub.com/cli-sed/how-do-i-use-the-cli-to-configure-zabbix)