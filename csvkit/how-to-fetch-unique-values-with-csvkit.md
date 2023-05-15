# How to fetch unique values with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV, the most popular being `csvcut` and `csvgrep`.

`csvcut` can be used to fetch unique values from a CSV file. For example, to fetch the unique values from the "Name" column of a CSV file named "example.csv":

```
csvcut -c Name example.csv | sort | uniq
```

The output of this command will be a list of unique values from the "Name" column:

```
Alice
Bob
John
```

The command consists of three parts:

1. `csvcut -c Name example.csv`: This part of the command uses `csvcut` to select the "Name" column from the "example.csv" file.

2. `sort`: This part of the command sorts the output of the `csvcut` command.

3. `uniq`: This part of the command filters out any duplicate values from the sorted output.

For more information about csvkit, see the [csvkit documentation](https://csvkit.readthedocs.io/en/latest/).

onelinerhub: [How to fetch unique values with csvkit?](https://onelinerhub.com/csvkit/how-to-fetch-unique-values-with-csvkit)