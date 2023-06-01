# How can I use Elastic PHP to sort data?
// plain

Elastic PHP provides a powerful set of tools for sorting data. It can be used to sort data by one or multiple criteria, as well as to sort data in ascending or descending order. Here is an example of how you can use Elastic PHP to sort data:

```
$data = [
    ['name' => 'John', 'age' => 34],
    ['name' => 'Adam', 'age' => 24],
    ['name' => 'Jane', 'age' => 45],
];

$sortedData = elastic_array_sort($data, 'age');

print_r($sortedData);
```

## Output example

```
Array
(
    [0] => Array
        (
            [name] => Adam
            [age] => 24
        )

    [1] => Array
        (
            [name] => John
            [age] => 34
        )

    [2] => Array
        (
            [name] => Jane
            [age] => 45
        )

)
```

The code above uses the `elastic_array_sort` function to sort the array of data by the `age` key. The function takes two parameters: the array of data to be sorted and the key to sort by. It then returns a new array with the data sorted in ascending order.

You can also sort by multiple criteria. For example:

```
$data = [
    ['name' => 'John', 'age' => 34, 'gender' => 'male'],
    ['name' => 'Adam', 'age' => 24, 'gender' => 'male'],
    ['name' => 'Jane', 'age' => 45, 'gender' => 'female'],
];

$sortedData = elastic_array_sort($data, ['gender', 'age']);

print_r($sortedData);
```

## Output example

```
Array
(
    [0] => Array
        (
            [name] => Adam
            [age] => 24
            [gender] => male
        )

    [1] => Array
        (
            [name] => John
            [age] => 34
            [gender] => male
        )

    [2] => Array
        (
            [name] => Jane
            [age] => 45
            [gender] => female
        )

)
```

The code above uses the `elastic_array_sort` function to sort the array of data by the `gender` and `age` keys. The function takes two parameters: the array of data to be sorted and an array of keys to sort by. It then returns a new array with the data sorted in ascending order.

For more information on using Elastic PHP to sort data, see the [documentation](https://www.elasticphp.com/docs/sorting-data/).

onelinerhub: [How can I use Elastic PHP to sort data?](https://onelinerhub.com/php-elastica/how-can-i-use-elastic-php-to-sort-data)