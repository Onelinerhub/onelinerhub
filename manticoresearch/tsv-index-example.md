# How to index TSV data

```bash
source text_src
{
  type = tsvpipe
  tsvpipe_command = cat /path/to/data.tsv
  tsvpipe_attr_string = name
  tsvpipe_field = description
}

index text_idx {
  type = plain
  source = text_src
  path = /var/lib/manticore/data/test
}
```

- `text_src` - name of the source block
- `type = tsvpipe` - let Manticore know that data will have TSV format
- `tsvpipe_command` - command to execute to get TSV data
- `/path/to/data.tsv` - path to the TSV file
- `tsvpipe_attr_string` - sample string attribute declaration (first column in TSV)
- `tsvpipe_field` - sample filed declaration (second column in TSV)
- `text_idx` - name of the index block and our index
- `source = text_src` - which source to use
- `/var/lib/manticore/data/test` - path to store index files in

group: index_pipe


