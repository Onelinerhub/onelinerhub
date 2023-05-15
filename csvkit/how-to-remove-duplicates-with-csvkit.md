# How to remove duplicates with csvkit?
// plain

csvkit is a suite of command-line tools for working with CSV data. It can be used to remove duplicates from a CSV file.

## Example code

```
csvdedupe input.csv output.csv
```

## Output example

```
Processing input.csv
Writing output.csv
```

The code above will take the input file `input.csv` and remove any duplicate rows, writing the output to `output.csv`.

## Code explanation

- `csvdedupe`: the command to run the deduplication process
- `input.csv`: the input file containing the data to be deduplicated
- `output.csv`: the output file where the deduplicated data will be written

## Helpful links
- [csvkit documentation](https://csvkit.readthedocs.io/en/latest/)
- [csvdedupe documentation](https://csvkit.readthedocs.io/en/latest/scripts/csvdedupe.html)

onelinerhub: [How to remove duplicates with csvkit?](https://onelinerhub.com/csvkit/how-to-remove-duplicates-with-csvkit)