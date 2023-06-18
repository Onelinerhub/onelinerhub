# What is the default port for SphinxSearch?
// plain

The default port for SphinxSearch is **9312**.

Example code for connecting to the SphinxSearch server:
```
$client = new SphinxClient();
$client->SetServer('localhost', 9312);
```

The code above creates a new SphinxClient object and sets the server to localhost on port 9312.

## Code explanation

1. `$client = new SphinxClient();` - creates a new SphinxClient object.
2. `$client->SetServer('localhost', 9312);` - sets the server to localhost on port 9312.

## Helpful links
- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxClient Reference](http://sphinxsearch.com/docs/current.html#php-api-reference)

onelinerhub: [What is the default port for SphinxSearch?](https://onelinerhub.com/sphinxsearch/what-is-the-default-port-for-sphinxsearch)