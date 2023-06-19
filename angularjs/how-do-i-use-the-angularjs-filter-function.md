# How do I use the AngularJS filter function?
// plain

The AngularJS filter function is used to filter an array of items based on a specific criteria. It can be used to filter items by a certain property, or to limit the number of items returned.

## Example code

```
//filter by property
var filteredItems = $filter('filter')(items, {name: "John"});

//limit number of items
var limitedItems = $filter('limitTo')(items, 10);
```

The filter function takes two parameters, the first being the array of items to be filtered, and the second being the filter criteria. If the filter criteria is an object, the filter will return all items that match the specified property values. If the filter criteria is a number, the filter will return the specified number of items.

The filter function can also be used with a custom filter function. This allows you to create a custom filter that will be applied to the array of items. For example, you could create a custom filter that filters items based on a specific date range.

Here is an example of a custom filter function:

```
function dateFilter(item) {
    return item.date >= startDate && item.date <= endDate;
}

var filteredItems = $filter('filter')(items, dateFilter);
```

In this example, the dateFilter function is applied to the items array, and all items with a date between the startDate and endDate are returned.

## Helpful links

- [AngularJS Filter Documentation](https://docs.angularjs.org/api/ng/filter/filter)
- [AngularJS LimitTo Documentation](https://docs.angularjs.org/api/ng/filter/limitTo)

onelinerhub: [How do I use the AngularJS filter function?](https://onelinerhub.com/angularjs/how-do-i-use-the-angularjs-filter-function)