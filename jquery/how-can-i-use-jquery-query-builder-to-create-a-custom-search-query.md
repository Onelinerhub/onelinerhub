# How can I use jQuery Query Builder to create a custom search query?
// plain

jQuery Query Builder is a powerful tool for building custom search queries. It provides a graphical interface for constructing complex search queries without having to write code. To use jQuery Query Builder, you first need to include the library in your HTML page:

```
<script src="jquery.query-builder.js"></script>
```

Then you can create a new Query Builder instance and set up the rules for your search query:

```
var queryBuilder = $('#query-builder').queryBuilder({
  rules: [
    {
      id: 'name',
      operator: 'equal',
      value: 'John'
    },
    {
      id: 'age',
      operator: 'greater_or_equal',
      value: 18
    }
  ]
});
```

This code creates a Query Builder instance with two rules: one to match users with the name "John" and one to match users with age 18 or greater. You can also add additional rules and operators to further refine the search query.

Once you have set up the rules, you can get the resulting search query string using the `getRules()` method:

```
var searchQuery = queryBuilder.getRules();
```

The output of this code will be a JSON string representing the search query:

```
{
  "condition": "AND",
  "rules": [
    {
      "id": "name",
      "operator": "equal",
      "value": "John"
    },
    {
      "id": "age",
      "operator": "greater_or_equal",
      "value": 18
    }
  ]
}
```

You can then use this search query string to perform a custom search in your application.

## Code explanation
**

1. Include jQuery Query Builder library in HTML page: `<script src="jquery.query-builder.js"></script>`
2. Create a new Query Builder instance: `var queryBuilder = $('#query-builder').queryBuilder({ rules: [ ... ] });`
3. Add rules and operators to refine the search query.
4. Get the resulting search query string: `var searchQuery = queryBuilder.getRules();`

**## Helpful links**

- [jQuery Query Builder](https://querybuilder.js.org/)
- [Getting Started with jQuery Query Builder](https://querybuilder.js.org/getting_started.html)

onelinerhub: [How can I use jQuery Query Builder to create a custom search query?](https://onelinerhub.com/jquery/how-can-i-use-jquery-query-builder-to-create-a-custom-search-query)