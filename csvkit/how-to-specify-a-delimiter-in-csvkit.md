# How to specify a delimiter in csvkit?
// plain

csvkit is a suite of command-line tools for converting to and working with CSV, the comma-separated values format. It can be used to specify a delimiter in csvkit.

## Example code

```
csvcut -d '|' input.csv
```

## Output example

```
column1|column2|column3
value1|value2|value3
```

## Code explanation

- `csvcut`: the command to specify a delimiter
- `-d`: the flag to indicate the delimiter
- `'|'`: the delimiter to be used
- `input.csv`: the input file

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to specify a delimiter in csvkit?](https://onelinerhub.com/csvkit/how-to-specify-a-delimiter-in-csvkit)