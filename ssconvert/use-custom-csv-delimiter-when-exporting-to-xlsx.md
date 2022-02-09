# Use custom CSV delimiter when exporting to XLS(x)

```bash
mv file.csv tmp.txt && ssconvert tmp.txt tmp.csv && ssconvert tmp.csv out.xls
```

- `ssconvert` - convertion utility
- `mv file.csv tmp.txt` - renames `csv` to temporary `txt` file to use `ssconvert` automatic delimiter detection
- `ssconvert tmp.txt tmp.csv` - convert temporary file with custom delimiter to temporary `csv` file
- `out.xls` - final `xls` file

group: delimiter


