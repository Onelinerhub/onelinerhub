# How to diff two CSV files using csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV, the most popular being `csvdiff`. It can be used to compare two CSV files and output the differences between them.

## Example code

```
csvdiff file1.csv file2.csv
```

## Output example

```
+---------+---------+---------+
| Column1 | Column2 | Column3 |
+---------+---------+---------+
| A       | B       | C       |
| D       | E       | F       |
+---------+---------+---------+
```

The code above will compare the two CSV files `file1.csv` and `file2.csv` and output the differences between them. The output will show the columns and the differences between the two files.

## Code explanation


1. `csvdiff`: This is the command used to compare two CSV files.
2. `file1.csv` and `file2.csv`: These are the two CSV files that will be compared.
3. `Column1`, `Column2`, `Column3`: These are the columns that will be compared.
4. `A`, `B`, `C`, `D`, `E`, `F`: These are the values that will be compared.

## Helpful links

- [csvkit Documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvdiff Documentation](https://csvkit.readthedocs.io/en/latest/scripts/csvdiff.html)

onelinerhub: [How to diff two CSV files using csvkit?](https://onelinerhub.com/csvkit/how-to-diff-two-csv-files-using-csvkit)