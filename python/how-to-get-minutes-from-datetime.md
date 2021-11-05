# How to get minutes from datetime

```python
import datetime
date = '2022-10-20 10:11:12'
minute = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").minute
```

- `datetime` - module to manipulate dates/times
- `date = ` - example date to extract part from
- `datetime.datetime.strptime` - parses given string  with the given format
- `"%Y-%m-%d %H:%M:%S"` - format of the datetime string to parse
- `.minute` - returns minute part of the datetime

group: date_extract

## Example: 
```python
import datetime
date = '2022-10-20 10:11:12'
minute = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").minute
print(minute)
```
```
11

```

## Additional keywords
- parse
- datetime
- extract
- date
