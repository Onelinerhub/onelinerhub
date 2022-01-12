# Using Template format to output data in custom format

```bash
echo 'My name is ${col:CSV} and I am ${age:CSV}' > tmp.tpl
clickhouse-client -q "SELECT * FROM tbl FORMAT Template SETTINGS format_template_row = 'tmp.tpl'"
```

- `tmp.tpl` - save custom format description to the temporary file
- `${col:CSV}` - placeholder to pick value for `col` column, escaped using CSV rules ([more details](https://clickhouse.com/docs/en/interfaces/formats/#format-template))
- `${age:CSV}` - placeholder to pick value for `age` column
- `clickhouse-client -q` - execute given query through client interface
- `tbl` - table to select data from
- `FORMAT Template` - use Template format for output
- `format_template_row` - set path to our template format file

group: Template_format

## Example: 
```bash
echo 'My name is ${col:CSV} and I am ${age:CSV}' > tmp.tpl
clickhouse-client -q "SELECT * FROM tbl FORMAT Template SETTINGS format_template_row = 'tmp.tpl'"
```
```
Query id: ef3a3c26-5db4-4d09-9d58-39ba6f80f41b

My name is "Donald" and I am 125
...
```

