# How do I use Sphinx search to find results based on a specific time zone?
// plain

Sphinx search can be used to find results based on a specific time zone by using an expression-based filter. Expression-based filters are a powerful way to filter search results by specifying conditions on attributes like time zone.

For example, the following code can be used to find results based on a specific time zone:

```
$cl->SetFilterRange('date_field', strtotime('-1 day'), strtotime('+1 day'), false);
```

This code sets a filter range on the `date_field` attribute, which is the time zone field in the search index. The range is set to the current day, which will effectively filter out any results that are not in the specified time zone.

The parts of the code are as follows:

- `$cl->SetFilterRange`: This is the method used to set the filter range.
- `date_field`: This is the attribute that the filter is being applied to.
- `strtotime('-1 day')`: This is the start of the range, which is set to the current day minus one day.
- `strtotime('+1 day')`: This is the end of the range, which is set to the current day plus one day.
- `false`: This is an optional parameter which specifies whether or not the range should be inclusive.

## Helpful links

- [Sphinx Search Documentation](http://sphinxsearch.com/docs/current.html)
- [Expression-based Filters](http://sphinxsearch.com/docs/current.html#expressions-filters)

onelinerhub: [How do I use Sphinx search to find results based on a specific time zone?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinx-search-to-find-results-based-on-a-specific-time-zone)