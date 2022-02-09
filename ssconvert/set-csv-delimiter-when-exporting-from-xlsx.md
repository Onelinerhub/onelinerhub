# Set CSV delimiter when exporting from XLS(x)

```bash
ssconvert -O 'separator=;' file.xls out.txt && mv out.txt out.csv
```

- `ssconvert` - convertion utility
- `-O` - sets export options
- `separator=;` - use `;` symbol as separator when exporting
- `file.xls` - input XLS file to export
- `out.txt` - we export into temporary `txt` file to use custom separator
- `mv out.txt out.csv` - renames `txt` to `csv` file

group: delimiter


