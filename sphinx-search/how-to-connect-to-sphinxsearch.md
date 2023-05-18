# How to connect to SphinxSearch?
// plain

To connect to SphinxSearch, you need to use the SphinxAPI.

```python
import sphinxapi

conn = sphinxapi.SphinxClient()
conn.SetServer('localhost', 9312)
```

The code above will create a connection to the SphinxSearch server running on `localhost` on port `9312`.

1. `import sphinxapi` - imports the SphinxAPI library
2. `conn = sphinxapi.SphinxClient()` - creates a SphinxClient object
3. `conn.SetServer('localhost', 9312)` - sets the server and port to connect to

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxAPI Documentation](http://sphinxsearch.com/docs/sphinxapi.html)

onelinerhub: [How to connect to SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-connect-to-sphinxsearch)