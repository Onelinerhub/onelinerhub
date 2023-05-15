# How to remove columns with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV, the most popular being `csvcut`. `csvcut` can be used to remove columns from a CSV file.

## Example code

```
csvcut -c 1,3,4 input.csv > output.csv
```

This command will remove the second column from the input file and save the result to output.csv.

## Code explanation

- `csvcut`: the command used to remove columns from a CSV file
- `-c`: the flag used to specify which columns to keep
- `1,3,4`: the columns to keep, in this case columns 1, 3, and 4
- `input.csv`: the input file
- `>`: the redirection operator used to save the output to a file
- `output.csv`: the output file

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to remove columns with csvkit?](https://onelinerhub.com/csvkit/how-to-remove-columns-with-csvkit)