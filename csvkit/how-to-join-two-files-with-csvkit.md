# How to join two files with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV, the most popular being `csvjoin`. It can be used to join two CSV files on a common field.

## Example code

```
csvjoin -c common_field file1.csv file2.csv
```

## Output example

```
common_field,field1,field2,field3
value1,value4,value5,value6
value2,value7,value8,value9
```

## Code explanation

- `csvjoin`: the command to join two CSV files
- `-c`: the flag to specify the common field
- `common_field`: the name of the common field
- `file1.csv`: the first CSV file
- `file2.csv`: the second CSV file

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvjoin documentation](https://csvkit.readthedocs.io/en/latest/scripts/csvjoin.html)

onelinerhub: [How to join two files with csvkit?](https://onelinerhub.com/csvkit/how-to-join-two-files-with-csvkit)