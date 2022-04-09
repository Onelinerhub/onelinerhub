# Get current year and month

```python
from datetime import datetime

currentYearMonth = "{month}/{year}".format(
  month = datetime.now().month,
  year = datetime.now().year
)

print(currentYearMonth)
```

- `from datetime import datetime` - import datetime utility to operate with time
- `datetime.now()` - returns current date object
- `.year` - attribute returns year
- `.month` - attribute returns month
- `"{month}/{year}".format` - format resulting month/year string in a given way
- `currentYearMonth` - will contain final formatted month/year string

group: date

## Example: 
```python
from datetime import datetime

currentYearMonth = "{month}/{year}".format(
  month = datetime.now().month,
  year = datetime.now().year
)

print(currentYearMonth)
```
```
4/2022

```

