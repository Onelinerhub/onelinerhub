# How to skip the first line with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV files. It can be used to skip the first line of a CSV file with the `csvcut` command.

## Example code

```
csvcut -n -K 1 input.csv
```

## Output example

```
column1,column2,column3
value1,value2,value3
```

## Code explanation

- `csvcut`: the command to cut columns from a CSV file
- `-n`: the flag to skip the header line
- `-K 1`: the flag to skip the first line
- `input.csv`: the input CSV file

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to skip the first line with csvkit?](https://onelinerhub.com/csvkit/how-to-skip-the-first-line-with-csvkit)