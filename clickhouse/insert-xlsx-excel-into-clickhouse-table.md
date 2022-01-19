# Insert XLSX (Excel) into Clickhouse table

### You'll need [ssconvert installed](/ssconvert/how-to-install-ssconvert-on-ubuntu-ubuntuversion) to insert Excel into Clickhouse:

```bash
ssconvert file.xlsx tmp.csv
cat tmp.csv | clickhouse -q "INSERT INTO tbl FORMAT CSV"
rm tmp.csv
```

- `ssconvert` - will convert `xlsx` to `csv`
- `file.xlsx` - name of the original Excel file to insert into Clickhouse table
- `tmp.csv` - name of the temporary `csv` file which will be fed to Clickhouse
- `tbl` - name of the table to insert data to
- `rm tmp.csv` - remove temporary file after data is inserted


