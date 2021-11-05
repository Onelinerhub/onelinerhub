# How to get month from date

```python
import datetime
date = '2022-10-20 10:11:12'
month = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").month
```

- `datetime` - module to manipulate dates/times
- `date = ` - example date to extract part from
- `datetime.datetime.strptime` - parses given string  with the given format
- `"%Y-%m-%d %H:%M:%S"` - format of the datetime string to parse
- `.month` - returns month part of the date

group: date_extract

## Example: 
```python
import datetime
date = '2022-10-20 10:11:12'
month = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").month
print(month)
```
```
10

```

## Additional keywords
- parse
- datetime
- extract
