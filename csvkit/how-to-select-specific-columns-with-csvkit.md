# How to select specific columns with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV, the most popular being `csvcut`. `csvcut` allows you to select specific columns from a CSV file.

## Example code

```
csvcut -c 1,3,4 myfile.csv
```

## Output example

```
column1,column3,column4
value1,value3,value4
value5,value7,value8
```

## Code explanation

- `csvcut`: the command to select specific columns from a CSV file
- `-c`: the flag to specify the columns to select
- `1,3,4`: the columns to select, in this case columns 1, 3, and 4
- `myfile.csv`: the CSV file to select columns from

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvcut documentation](https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html)

onelinerhub: [How to select specific columns with csvkit?](https://onelinerhub.com/csvkit/how-to-select-specific-columns-with-csvkit)