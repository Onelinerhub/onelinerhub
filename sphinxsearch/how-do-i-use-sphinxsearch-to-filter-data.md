# How do I use SphinxSearch to filter data?
// plain

SphinxSearch is a powerful search engine designed to quickly and efficiently filter data. It can be used to search through large databases and return results quickly and accurately.

Here is an example of how to use SphinxSearch to filter data:

```
# Connect to SphinxSearch
$sphinx = new SphinxClient();
$sphinx->setServer("localhost", 9312);

# Set the query
$sphinx->setLimits(0, 10);
$sphinx->setQuery("keyword");

# Execute the query
$result = $sphinx->query();

# Process the result
if (!empty($result['matches'])) {
    foreach ($result['matches'] as $match) {
        echo $match['id'] . "\n";
    }
}
```

This code will connect to the SphinxSearch server, set a query and limits, then execute the query and process the result. The output of this code will be a list of ids matched by the query.

## Code explanation


1. `$sphinx = new SphinxClient();`: This creates a new SphinxClient object.
2. `$sphinx->setServer("localhost", 9312);`: This sets the server and port to connect to.
3. `$sphinx->setLimits(0, 10);`: This sets the limits of the query, in this case 0 to 10.
4. `$sphinx->setQuery("keyword");`: This sets the query to search for.
5. `$result = $sphinx->query();`: This executes the query.
6. `if (!empty($result['matches'])) {`: This checks if the query returned any results.
7. `foreach ($result['matches'] as $match) {`: This loops through the results.
8. `echo $match['id'] . "\n";`: This prints out the ids of the results.

For more information on SphinxSearch, please see the [official documentation](http://sphinxsearch.com/docs/).

onelinerhub: [How do I use SphinxSearch to filter data?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinxsearch-to-filter-data)