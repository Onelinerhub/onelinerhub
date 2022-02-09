# Convert multiple sheets

```bash
ssconvert -S file.xls "%s.out.csv"
```

- `ssconvert` - convertion utility
- `file.xls` - input XLS file to export
- `-S` - export all sheets to separate files
- `"%s.out.csv"` - output `csv` files template (`%s` will be substituted with a sheet name)

group: sheet_names


