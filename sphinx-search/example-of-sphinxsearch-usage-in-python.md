# Example of sphinxsearch usage in Python
// plain

SphinxSearch is a powerful full-text search engine written in C++. It can be used in Python applications to provide fast and accurate search results.

## Example code

```
import sphinxapi

# Create a SphinxClient object
client = sphinxapi.SphinxClient()

# Set the server, port, and search query
client.SetServer('localhost', 9312)
client.SetMatchMode(sphinxapi.SPH_MATCH_EXTENDED2)
client.Query('python')

# Get the results
results = client.GetMatches()

# Print the results
for result in results:
    print(result)
```

## Output example

```
{'weight': 1, 'attrs': {}, 'id': 1, 'matches': [{'weight': 1, 'id': 1, 'word': 'python'}]}
```

The code above creates a SphinxClient object, sets the server, port, and search query, and then gets the results. The results are then printed.

Parts of the code:
- `import sphinxapi`: imports the SphinxSearch API for Python
- `client = sphinxapi.SphinxClient()`: creates a SphinxClient object
- `client.SetServer('localhost', 9312)`: sets the server and port
- `client.SetMatchMode(sphinxapi.SPH_MATCH_EXTENDED2)`: sets the search query
- `client.Query('python')`: sets the search query
- `results = client.GetMatches()`: gets the results
- `for result in results:`: iterates through the results
- `print(result)`: prints the results

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch Python API](https://pypi.org/project/sphinxapi/)

onelinerhub: [Example of sphinxsearch usage in Python](https://onelinerhub.com/sphinx-search/example-of-sphinxsearch-usage-in-python)