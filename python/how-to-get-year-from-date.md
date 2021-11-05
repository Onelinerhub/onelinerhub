# How to get year from date

```python
import datetime
date = '2022-10-20 10:11:12'
year = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").year
```


group: date_extract

## Example: 
```python
import datetime
date = '2022-10-20 10:11:12'
year = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").year
print(year)
```
```
2022

```
