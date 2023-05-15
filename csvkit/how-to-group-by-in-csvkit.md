# How to group by in csvkit?
// plain

Grouping by in csvkit can be done using the `csvstack` command. This command allows you to stack multiple CSV files on top of each other and group by a specified column.

## Example code

```
csvstack -g <column_name> <csv_file1> <csv_file2>
```

## Output example

```
<column_name>,<csv_file1_column1>,<csv_file1_column2>,<csv_file2_column1>,<csv_file2_column2>
<column_name_value1>,<csv_file1_column1_value1>,<csv_file1_column2_value1>,<csv_file2_column1_value1>,<csv_file2_column2_value1>
<column_name_value2>,<csv_file1_column1_value2>,<csv_file1_column2_value2>,<csv_file2_column1_value2>,<csv_file2_column2_value2>
```

## Code explanation

- `csvstack`: The command used to stack multiple CSV files and group by a specified column.
- `-g`: The flag used to specify the column to group by.
- `<column_name>`: The name of the column to group by.
- `<csv_file1>`: The first CSV file to stack.
- `<csv_file2>`: The second CSV file to stack.

## Helpful links
- [csvkit Documentation](https://csvkit.readthedocs.io/en/latest/)

onelinerhub: [How to group by in csvkit?](https://onelinerhub.com/csvkit/how-to-group-by-in-csvkit)