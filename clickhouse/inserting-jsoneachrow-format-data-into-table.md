# Inserting JSONEachRow format data into table

```bash
cat json_rows.txt | clickhouse-client -q "INSERT INTO tbl FORMAT JSONEachRow"
```

- `json_rows.txt` - file with JSONEachRow formatted data (separate JSON on each line)
- `clickhouse-client -q` - execute given query through client interface 
- `INSERT INTO tbl` - insert given data into `tbl` table
- `FORMAT JSONEachRow` - set format of input data to `JSONEachRow`

group: Template_format

## Example: 
```bash
cat json_rows.txt
```
```
{"date":"2022-01-07","col":"Donald","val":0,"age":0}
{"date":"2022-01-10","col":"Donald","val":0,"age":0}
{"date":"2022-01-11","col":"Donald","val":0,"age":0}

```

