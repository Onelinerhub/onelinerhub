# How do I use Sphinx Search to identify an item?
// plain

Sphinx Search is an open-source full-text search engine used to identify items. It can be used to search through large amounts of data quickly and efficiently.

The following example code shows how to use Sphinx Search to identify an item:

```
// Connect to the Sphinx Search server
$sphinx = new SphinxClient();
$sphinx->setServer("localhost", 9312);

// Define the search query
$query = "item";

// Execute the search query
$result = $sphinx->query($query);

// Output the search results
if ($result !== false) {
    print_r($result);
}
```

## Output example

```
Array
(
    [error] =>
    [warning] =>
    [status] => 0
    [fields] => Array
        (
        )

    [attrs] => Array
        (
        )

    [matches] => Array
        (
            [0] => Array
                (
                    [id] => 1
                    [weight] => 1
                )

            [1] => Array
                (
                    [id] => 2
                    [weight] => 1
                )

            [2] => Array
                (
                    [id] => 3
                    [weight] => 1
                )

        )

    [total] => 3
    [total_found] => 3
    [time] => 0.000
    [words] => Array
        (
            [item] => Array
                (
                    [docs] => 3
                    [hits] => 3
                )

        )

)
```

The code above connects to the Sphinx Search server, defines the search query, executes the search query, and outputs the search results. The output includes the IDs and weights of the items that match the query.

Parts of the code:
* `$sphinx = new SphinxClient();` - creates a new instance of the SphinxClient class
* `$sphinx->setServer("localhost", 9312);` - sets the server and port used for the Sphinx Search server
* `$query = "item";` - defines the search query
* `$result = $sphinx->query($query);` - executes the search query
* `print_r($result);` - outputs the search results

## Helpful links
* [Sphinx Search Documentation](https://sphinxsearch.com/docs/current.html)
* [SphinxClient Class Documentation](https://sphinxsearch.com/docs/current.html#api-func-sphinxclient)

onelinerhub: [How do I use Sphinx Search to identify an item?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinx-search-to-identify-an-item)