# How to reload the configuration in SphinxSearch?
// plain

SphinxSearch can be reloaded using the `reload` command. This command will re-read the configuration file and apply any changes.

## Example

```
$ searchd --reload
```

## Output example

```
Sphinx 2.2.11-id64-release (r5161)
Copyright (c) 2001-2018, Andrew Aksyonoff
Copyright (c) 2008-2016, Sphinx Technologies Inc (http://sphinxsearch.com)

using config file '/usr/local/etc/sphinx.conf'...
reloading index 'test1'...
reloaded successfully.
```

The `reload` command has the following parts:
- `searchd`: The search daemon that runs in the background and handles search requests.
- `--reload`: The command to reload the configuration.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How to reload the configuration in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-reload-the-configuration-in-sphinxsearch)