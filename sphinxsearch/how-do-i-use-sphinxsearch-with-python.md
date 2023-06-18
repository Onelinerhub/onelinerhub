# How do I use SphinxSearch with Python?
// plain

SphinxSearch is an open source full-text search engine written in C++. It can be used with Python through the [SphinxClient](http://sphinxsearch.com/docs/current.html#sphinxclient-py) module.

The following example code searches the index for the term "python":
```
import sphinxapi

# Create the SphinxClient object
client = sphinxapi.SphinxClient()

# Set the server, port, and search query
client.SetServer('localhost', 9312)
client.SetMatchMode(sphinxapi.SPH_MATCH_ANY)
client.Query('python')

# Get the results
results = client.GetResults()

# Print the results
for r in results['matches']:
    print(r['attrs'])
```
The output of the example code is a list of attributes associated with the search term:
```
{'title': 'Python', 'description': 'A programming language'}
```

The code consists of the following parts:
1. Import the SphinxClient module
2. Create a SphinxClient object
3. Set the server, port, and search query
4. Get the results
5. Print the results

For more information, see the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I use SphinxSearch with Python?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-with-python)