# Using Template format to output data in custom format

```bash
echo 'My name is ${col:CSV} and I am ${age:CSV}' > tmp.tpl
clickhouse-client -q "INSERT INTO tbl FORMAT Template SETTINGS format_template_row = 'tmp.tpl'"
```

- `tmp.tpl` - save custom format description to the temporary file
- `${col:CSV}` - placeholder to pick value for `col` column, escaped using CSV rules ([more details](https://clickhouse.com/docs/en/interfaces/formats/#format-template))
- `${age:CSV}` - placeholder to pick value for `age` column
- `My name is Donald and I am 125` - example string to insert using custom format
- `clickhouse-client -q` - execute given query through client interface
- `INSERT INTO tbl` - insert given data into `tbl` table
- `FORMAT Template` - use Template format
- `format_template_row` - set path to our template format file

group: Template_format

## Example: 
```bash
SELECT * FROM tbl FORMAT JSONEachRow
```
```
{"date":"2022-01-07","col":"Donald","val":0,"age":0}
{"date":"2022-01-10","col":"Donald","val":0,"age":0}
{"date":"2022-01-11","col":"Donald","val":0,"age":0}

```

