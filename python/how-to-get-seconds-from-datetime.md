# How to get seconds from datetime

```python
import datetime
date = '2022-10-20 10:11:12'
second = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").second
```

- `datetime` - module to manipulate dates/times
- `date = ` - example date to extract part from
- `datetime.datetime.strptime` - parses given string  with the given format
- `"%Y-%m-%d %H:%M:%S"` - format of the datetime string to parse
- `.second` - returns second part of the datetime

group: date_extract

## Example: 
```python
import datetime
date = '2022-10-20 10:11:12'
second = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").second
printsecond
```
```
11

```

## Additional keywords
- parse
- datetime
- extract
- date
