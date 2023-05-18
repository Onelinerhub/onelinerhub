# How to get categories in WordPress using PHP?
// plain

You can get categories in WordPress using PHP with the `get_categories()` function. This function returns an array of category objects.

## Example code

```
$categories = get_categories();
foreach($categories as $category) {
    echo $category->name;
}
```

## Output example

```
Category 1
Category 2
Category 3
```

The `get_categories()` function takes an array of arguments as its parameter. The arguments can be used to filter the categories returned.

## Code explanation

- `get_categories()`: This is the function used to get categories in WordPress using PHP.
- `$categories`: This is the array of category objects returned by the `get_categories()` function.
- `foreach`: This is a loop used to iterate through the array of category objects.
- `echo $category->name`: This is used to output the name of each category.

## Helpful links
- [get_categories() Function Reference](https://developer.wordpress.org/reference/functions/get_categories/)

onelinerhub: [How to get categories in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-get-categories-in-wordpress-using-php)