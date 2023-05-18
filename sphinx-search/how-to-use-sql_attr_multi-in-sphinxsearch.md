# How to use SQL_ATTR_MULTI in SphinxSearch?
// plain

SQL_ATTR_MULTI is a SphinxSearch attribute that allows for multiple queries to be executed in a single call. This can be useful for optimizing search performance when multiple queries need to be executed.

## Example code

```
$cl->SetServer('localhost', 9312);
$cl->SetConnectTimeout(1);
$cl->SetArrayResult(true);
$cl->SetMatchMode(SPH_MATCH_EXTENDED);
$cl->SetLimits(0, 10);
$cl->SetRankingMode(SPH_RANK_PROXIMITY_BM25);
$cl->SetSortMode(SPH_SORT_EXTENDED, '@weight DESC');
$cl->SetFieldWeights(array('title' => 10, 'content' => 1));
$cl->SetSelect('*, WEIGHT() as weight');
$cl->SetArrayResult(true);
$cl->SetFilter('status', array(1));
$cl->SetFilter('type', array(1,2,3));
$cl->SetFilter('date_added', array(time()-86400, time()));
$cl->SetGroupBy('id', SPH_GROUPBY_ATTR);
$cl->SetGroupDistinct('title');

$queries = array(
    array('query' => 'test', 'index' => 'index1'),
    array('query' => 'example', 'index' => 'index2')
);

$cl->SetSqlParamsMulti($queries, SPH_ATTR_MULTI);

$result = $cl->Query('', 'index1,index2');
```

## Output example

```
Array
(
    [status] => 0
    [fields] => Array
        (
            [0] => title
            [1] => content
            [2] => weight
        )

    [attrs] => Array
        (
            [weight] => uint
        )

    [matches] => Array
        (
            [0] => Array
                (
                    [weight] => 4
                    [attrs] => Array
                        (
                            [weight] => 4
                        )

                )

            [1] => Array
                (
                    [weight] => 3
                    [attrs] => Array
                        (
                            [weight] => 3
                        )

                )

        )

    [total] => 2
    [total_found] => 2
    [time] => 0.001
    [words] => Array
        (
            [test] => Array
                (
                    [docs] => 1
                    [hits] => 1
                )

            [example] => Array
                (
                    [docs] => 1
                    [hits] => 1
                )

        )

)
```

## Code explanation


- `$cl->SetServer('localhost', 9312);`: Sets the server and port to connect to.
- `$cl->SetConnectTimeout(1);`: Sets the connection timeout in seconds.
- `$cl->SetArrayResult(true);`: Sets the result format to an array.
- `$cl->SetMatchMode(SPH_MATCH_EXTENDED);`: Sets the match mode to extended.
- `$cl->SetLimits(0, 10);`: Sets the limits for the number of results to return.
- `$cl->SetRankingMode(SPH_RANK_PROXIMITY_BM25);`: Sets the ranking mode to proximity BM25.
- `$cl->SetSortMode(SPH_SORT_EXTENDED, '@weight DESC');`: Sets the sort mode to extended and sorts by weight in descending order.
- `$cl->SetFieldWeights(array('title' => 10, 'content' => 1));`: Sets the field weights for the title and content fields.
- `$cl->SetSelect('*, WEIGHT() as weight');`: Sets the fields to select and adds a weight field.
- `$cl->SetArrayResult(true);`: Sets the result format to an array.
- `$cl->SetFilter('status', array(1));`: Sets a filter for the status field.
- `$cl->SetFilter('type', array(1,2,3));`: Sets a filter for the type field.
- `$cl->SetFilter('date_added', array(time()-86400, time()));`: Sets a filter for the date_added field.
- `$cl->SetGroupBy('id', SPH_GROUPBY_ATTR);`: Sets the group by field to id and the group by mode to attribute.
- `$cl->SetGroupDistinct('title');`: Sets the group distinct field to title.
- `$queries = array(array('query' => 'test', 'index' => 'index1'), array('query' => 'example', 'index' => 'index2'));`: Sets up an array of queries to execute.
- `$cl->SetSqlParamsMulti($queries, SPH_ATTR_MULTI);`: Sets the SQL parameters to execute multiple queries.
- `$result = $cl->Query('', 'index1,index2');`: Executes the queries and returns the result.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [SphinxSearch PHP API Documentation](http://sphinxsearch.com/docs/current.html#api-reference)

onelinerhub: [How to use SQL_ATTR_MULTI in SphinxSearch?](https://onelinerhub.com/sphinx-search/how-to-use-sql_attr_multi-in-sphinxsearch)