# How do I configure Sphinxsearch on a specific port?
// plain

1. Install Sphinxsearch as per the [official documentation](http://sphinxsearch.com/docs/current.html).
2. Open the configuration file `sphinx.conf` located in the `etc/` directory.
3. Add the following line to the configuration file to specify the port: `listen = 0.0.0.0:<port>`
4. Save the file.
5. Start Sphinxsearch with the `searchd` command.
6. Check whether the port has been set correctly with the command `netstat -an | grep <port>`.
7. If the port is set correctly, the output should be similar to the following:
```
tcp        0      0 0.0.0.0:<port>           0.0.0.0:*               LISTEN
```

For more information, see the [Sphinxsearch Configuration Manual](http://sphinxsearch.com/docs/current.html#conf-listen).

onelinerhub: [How do I configure Sphinxsearch on a specific port?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-sphinxsearch-on-a-specific-port)