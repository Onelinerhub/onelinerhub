# How do I use SphinxSearch functions?
// plain

SphinxSearch is a powerful full-text search engine that can be used to quickly search and retrieve data from large datasets. It is written in C and can be used from a variety of programming languages, including PHP, Python, and Ruby.

The basic syntax of SphinxSearch is relatively simple, and can be used to query data from a single table or multiple tables. To use SphinxSearch functions, you will need to include the `sphinxapi.php` library in your code.

For example, to search a table called `articles` for the term `sphinx`, you could use the following code:
```
$cl = new SphinxClient();
$cl->SetMatchMode(SPH_MATCH_ALL);
$cl->Query('sphinx', 'articles');
$results = $cl->Get();
```
The code above will search the `articles` table for all documents containing the term `sphinx` and return a list of matching results.

## Code explanation

- `$cl = new SphinxClient()`: This creates a new SphinxClient object.
- `$cl->SetMatchMode(SPH_MATCH_ALL)`: This sets the match mode to SPH_MATCH_ALL, which means that all documents containing the search term will be returned.
- `$cl->Query('sphinx', 'articles')`: This performs the search using the `sphinx` term and the `articles` table.
- `$cl->Get()`: This returns the results of the search query.

For more information about using SphinxSearch, please refer to the [official documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I use SphinxSearch functions?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-functions)