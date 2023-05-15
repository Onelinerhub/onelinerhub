# How to split a csv file with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV, the most popular being `csvcut` and `csvsplit`.

`csvcut` can be used to select specific columns from a CSV file, while `csvsplit` can be used to split a CSV file into multiple files based on a given column.

## Example code

```
csvcut -c 1,2,3 input.csv > output.csv
csvsplit -c 3 input.csv
```

Output of example code:
```
input.csv
1,2,3
4,5,6
7,8,9

output.csv
1,2,3
4,5,6
7,8,9

input_3_1.csv
1,2,3
4,5,6

input_3_2.csv
7,8,9
```

## Code explanation

- `csvcut`: used to select specific columns from a CSV file
- `-c`: used to specify the columns to be selected
- `csvsplit`: used to split a CSV file into multiple files based on a given column
- `-c`: used to specify the column to split on

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvcut usage](https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html)
- [csvsplit usage](https://csvkit.readthedocs.io/en/latest/scripts/csvsplit.html)

onelinerhub: [How to split a csv file with csvkit?](https://onelinerhub.com/csvkit/how-to-split-a-csv-file-with-csvkit)