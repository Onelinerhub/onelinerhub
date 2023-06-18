# How can I use Sphinx Search with Python to create an example application?
// plain

The Sphinx Search engine is a powerful open-source search engine that can be used with Python to create a powerful search application. To create an example application, you can use the Python API to connect to the Sphinx server and execute queries.

## Example code

```python
import sphinxapi

# create connection to the Sphinx server
client = sphinxapi.SphinxClient()
client.SetServer('localhost', 9312)

# execute a search query
result = client.Query('python')

# print the results
print(result)
```

## Output example

```
{'matches': [{'weight': 1, 'attrs': {}, 'id': 1, 'word': 'python'}], 'total': 1, 'total_found': 1, 'time': '0.000', 'words': [{'docs': 1, 'hits': 1, 'word': 'python'}], 'error': ''}
```

## Code explanation


1. `import sphinxapi`: Imports the SphinxAPI module which provides the interface to the Sphinx server.
2. `client = sphinxapi.SphinxClient()`: Creates a SphinxClient instance and sets up a connection to the Sphinx server.
3. `client.SetServer('localhost', 9312)`: Sets the connection parameters to the Sphinx server.
4. `result = client.Query('python')`: Executes a search query with the keyword 'python'.
5. `print(result)`: Prints the results of the search query.

## Helpful links

- [Sphinx Search Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch Python API](http://sphinxsearch.com/docs/current.html#api-python)

onelinerhub: [How can I use Sphinx Search with Python to create an example application?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinx-search-with-python-to-create-an-example-application)