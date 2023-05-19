# How to use "explain" in MongoDB?
// plain

MongoDB's `explain()` method is used to provide information about how MongoDB executes a query. It can be used to analyze query performance and identify potential areas of improvement.

## Example

```
db.collection.explain("executionStats")
```

## Output example

```
{
    "queryPlanner" : {
        ...
    },
    "executionStats" : {
        "executionSuccess" : true,
        "nReturned" : 1,
        "executionTimeMillis" : 0,
        "totalKeysExamined" : 0,
        "totalDocsExamined" : 0,
        "executionStages" : {
            ...
        },
        "allPlansExecution" : [ ]
    },
    "serverInfo" : {
        ...
    },
    "ok" : 1
}
```

The output of `explain()` contains the following information:

- `queryPlanner`: The query plan MongoDB used to execute the query.
- `executionStats`: Statistics about the query execution, such as the number of documents examined and the execution time.
- `serverInfo`: Information about the server on which the query was executed.

## Helpful links
- [MongoDB Documentation - explain()](https://docs.mongodb.com/manual/reference/method/db.collection.explain/)

onelinerhub: [How to use "explain" in MongoDB?](https://onelinerhub.com/mongodb/how-to-use--explain--in-mongodb)