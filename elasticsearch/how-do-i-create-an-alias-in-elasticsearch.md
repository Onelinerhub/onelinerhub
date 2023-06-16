# How do I create an alias in Elasticsearch?
// plain

An alias in Elasticsearch is a reference to an index or a group of indices. It can be used to simplify complex queries, to switch out indices in a single operation, or to provide a single point of access to multiple indices.

Creating an alias in Elasticsearch is done using the `PUT` command, as shown in the example below:
```
PUT /_aliases
{
    "actions" : [
        { "add" : { "index" : "my_index_1", "alias" : "my_alias" } }
    ]
}
```
The output of this command will be `{"acknowledged":true}`, indicating that the alias has been successfully created.

The `PUT` command consists of two parts:
1. The `actions` parameter, which is an array of objects defining what action should be taken. In this case, the action is `add`, which adds an index to the alias.
2. The `add` parameter, which is an object containing the index to add to the alias and the name of the alias.

For more information on creating and managing Elasticsearch aliases, please refer to the [official documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-aliases.html).

onelinerhub: [How do I create an alias in Elasticsearch?](https://onelinerhub.com/elasticsearch/how-do-i-create-an-alias-in-elasticsearch)