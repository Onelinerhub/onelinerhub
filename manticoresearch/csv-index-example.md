# CSV index example

```bash
source text_src
{
  type = csvpipe
  csvpipe_command = can /path/to/data.csv
  csvpipe_attr_string = name
  csvpipe_field = description
}

index text_idx {
  type = plain
  source = text_src
  path = /var/lib/manticore/data/test
}
```

- `text_src` - name of the source block
- `csvpipe` - let Mantico know that data will have CSV format
- `csvpipe_command` - command to execute to get CSV data
- `/path/to/data.csv` - path to the CSV file
- `csvpipe_attr_string` - sample string attribute declaration (first column in CSV)
- `csvpipe_field` - sample filed declaration (second column in CSV)
- `text_idx` - name of the index block and our index
- `source = text_src` - which source to use
- `/var/lib/manticore/data/test` - path to store index files in

group: index_pipe


