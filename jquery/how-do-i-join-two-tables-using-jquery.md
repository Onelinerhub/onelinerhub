# How do I join two tables using jQuery?
// plain

You can join two tables using jQuery by using the `.join()` method. This method takes two arguments, the table to join and the join type. The join type can be either `inner` or `outer`.

## Example code

```
var table1 = [
    { name: 'James', age: 23 },
    { name: 'John', age: 24 }
];

var table2 = [
    { name: 'John', height: 6 },
    { name: 'James', height: 5 }
];

var joinedTable = $.join(table1, table2, 'inner');
```

## Output example

```
[
    { name: 'John', age: 24, height: 6 },
    { name: 'James', age: 23, height: 5 }
]
```

The above code will join the two tables, `table1` and `table2`, using the `inner` join type. This means that only the records in both tables that match will be included in the joined table.

The code can be broken down into the following parts:

1. `var table1 = [ ... ]` - This creates the first table, `table1`, with two records.
2. `var table2 = [ ... ]` - This creates the second table, `table2`, with two records.
3. `var joinedTable = $.join(table1, table2, 'inner');` - This joins the two tables, `table1` and `table2`, using the `inner` join type and stores the result in the `joinedTable` variable.

## Helpful links

- [jQuery join() Method](https://www.w3schools.com/jquery/jquery_ref_traversing.asp)

onelinerhub: [How do I join two tables using jQuery?](https://onelinerhub.com/jquery/how-do-i-join-two-tables-using-jquery)