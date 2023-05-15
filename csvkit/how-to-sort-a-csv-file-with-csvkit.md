# How to sort a csv file with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV files. It can be used to sort a csv file.

## Example code

```
csvsort -c column_name input.csv > output.csv
```

## Output example

```
column_name1,column_name2,column_name3
value1,value2,value3
value4,value5,value6
value7,value8,value9
```

## Code explanation

- `csvsort`: command to sort a csv file
- `-c`: flag to specify the column to sort by
- `column_name`: the name of the column to sort by
- `input.csv`: the name of the input csv file
- `>`: redirects the output to a file
- `output.csv`: the name of the output csv file

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to sort a csv file with csvkit?](https://onelinerhub.com/csvkit/how-to-sort-a-csv-file-with-csvkit)