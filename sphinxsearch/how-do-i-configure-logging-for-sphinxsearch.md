# How do I configure logging for SphinxSearch?
// plain

1.  First, you need to configure SphinxSearch to enable logging. This can be done by setting the ```log``` directive in the Sphinx configuration file. For example:
```
log = /var/log/sphinx/searchd.log
```
2. You can also specify the log verbosity by setting the ```query_log``` directive. For example:
```
query_log = /var/log/sphinx/query.log
```
3. You can also specify the log level by setting the ```log_level``` directive. For example:
```
log_level = warning
```
The available log levels are ```fatal```, ```error```, ```warning```, ```info```, ```debug```, ```debugv```, and ```debugvv```.
4. You can also specify the log format by setting the ```log_format``` directive. For example:
```
log_format = query
```
The available log formats are ```plain```, ```sphinxql```, and ```query```.
5. Once the configuration is complete, you can start the SphinxSearch daemon with the ```searchd``` command. For example:
```
searchd --config /etc/sphinx/sphinx.conf
```
6. You can then view the log files to see the output of your searches. For example:
```
tail -f /var/log/sphinx/searchd.log
```
7. You can also use a logging library such as [log4cpp](https://sourceforge.net/projects/log4cpp/) to customize the logging output.

## Helpful links

- [SphinxSearch Logging Documentation](http://sphinxsearch.com/docs/current.html#conf-log)
- [log4cpp Homepage](https://sourceforge.net/projects/log4cpp/)

onelinerhub: [How do I configure logging for SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-configure-logging-for-sphinxsearch)