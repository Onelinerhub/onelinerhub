# How to index XML data

```bash
source text_src
{
  type = xmlpipe2
  xmlpipe_command = cat /path/to/data.xml
}

index text_idx {
  type = plain
  source = text_src
  path = /var/lib/manticore/data/test
}
```

- `text_src` - name of the source block
- `type = xmlpipe2` - let Manticore know that data will have XML format
- `xmlpipe_command` - command to execute to get XML data
- `/path/to/data.xml` - path to the XML file
- `text_idx` - name of the index block and our index
- `source = text_src` - which source to use
- `/var/lib/manticore/data/test` - path to store index files in

group: index_pipe


