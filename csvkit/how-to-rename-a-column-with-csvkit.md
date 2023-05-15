# How to rename a column with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV, the most popular being `csvcut` and `csvrename`.

To rename a column with csvkit, use the `csvrename` command. For example, to rename the column "Name" to "Full Name" in the file `example.csv`, use the following command:

```
csvrename -c Name,Full Name example.csv
```

This will output the following:

```
Full Name,Age
John,25
Jane,30
```

## Code explanation


- `csvrename`: the command to rename a column
- `-c`: the flag to specify the column to rename
- `Name,Full Name`: the original and new column names
- `example.csv`: the file to be modified

## Helpful links

- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to rename a column with csvkit?](https://onelinerhub.com/csvkit/how-to-rename-a-column-with-csvkit)