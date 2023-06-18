# How can I use SphinxSearch to expand keywords?
// plain

SphinxSearch is a powerful open source search engine that can be used to expand keywords. It uses a special algorithm to look for related words and phrases to the input keywords. This can be useful for finding related topics and keywords to a given query.

Example code to expand keywords using SphinxSearch:

```
import sphinxapi

# Create a SphinxClient object
client = sphinxapi.SphinxClient()

# Set the keyword to expand
keyword = "sphinx"

# Get the related keywords
results = client.BuildExcerpts([keyword], "index", "search engine, open source")

# Print the related keywords
print(results)
```

## Output example


```
['<b>Sphinx</b> search engine', '<b>Sphinx</b> open source']
```

The code above does the following:

1. Imports the `sphinxapi` library.
2. Creates a `SphinxClient` object.
3. Sets the keyword to expand.
4. Gets the related keywords using the `BuildExcerpts` method.
5. Prints the related keywords.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxAPI Python Documentation](https://pypi.org/project/SphinxAPI/)

onelinerhub: [How can I use SphinxSearch to expand keywords?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinxsearch-to-expand-keywords)