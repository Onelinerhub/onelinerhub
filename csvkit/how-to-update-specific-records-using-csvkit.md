# How to update specific records using csvkit?
// plain

Updating specific records using csvkit can be done using the `csvcut` and `csvjoin` commands.

The `csvcut` command can be used to select specific columns from a CSV file. For example, the following command will select the columns `name` and `age` from the file `example.csv`:

```
csvcut -c name,age example.csv
```

The `csvjoin` command can be used to join two CSV files together. For example, the following command will join the file `example.csv` with the file `update.csv` on the column `name`:

```
csvjoin -c name example.csv update.csv
```

The output of this command will be a new CSV file with the columns from both `example.csv` and `update.csv`, with the records from `update.csv` replacing the records from `example.csv` with the same `name` value.

## Helpful links
- [csvkit Documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvcut Documentation](https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html)
- [csvjoin Documentation](https://csvkit.readthedocs.io/en/latest/scripts/csvjoin.html)

onelinerhub: [How to update specific records using csvkit?](https://onelinerhub.com/csvkit/how-to-update-specific-records-using-csvkit)