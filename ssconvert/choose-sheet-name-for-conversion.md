# Choose sheet name for conversion

```bash
ssconvert -S file.xls "%s.out.csv"
```

- `ssconvert` - convertion utility
- `file.xls` - input XLS file to export to CSV
- `"%s.out.csv"` - output `csv` files template (`%s` will be substituted with a sheet name)
- `-S` - export all sheets to separate files


