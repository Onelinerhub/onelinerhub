# How can I increase the memory limit for Sphinx Search?
// plain

1. Increase the memory limit for Sphinx Search by editing the configuration file.

```
# Open sphinx.conf
$ sudo nano /etc/sphinx/sphinx.conf

# Find the line that reads "max_matches = 1000"
# Change the value to whatever you need
max_matches = 10000

# Save the file
$ sudo service sphinxsearch restart
```

2. Increase the memory limit for Sphinx Search by setting the SPH_MAX_MATCHES environment variable.

```
# Set the SPH_MAX_MATCHES environment variable
$ export SPH_MAX_MATCHES=10000

# Check the value of the environment variable
$ echo $SPH_MAX_MATCHES
10000
```

3. Increase the memory limit for Sphinx Search by setting the max_matches directive in the SphinxQL command.

```
# Set the max_matches directive
$ SET max_matches=10000;

# Check the value of the directive
$ SHOW VARIABLES LIKE 'max_matches';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| max_matches  | 10000 |
+---------------+-------+
```

The above methods can be used to increase the memory limit for Sphinx Search. The configuration file and environment variable can be used to set the memory limit globally, while the SphinxQL command can be used to set the memory limit for a particular query.

## Helpful links

- [Sphinx Documentation - max_matches](http://sphinxsearch.com/docs/current.html#conf-max-matches)
- [Sphinx Documentation - Environment Variables](http://sphinxsearch.com/docs/current.html#envvars)
- [Sphinx Documentation - SphinxQL](http://sphinxsearch.com/docs/current.html#sphinxql-set-variable)

onelinerhub: [How can I increase the memory limit for Sphinx Search?](https://onelinerhub.com/sphinxsearch/how-can-i-increase-the-memory-limit-for-sphinx-search)