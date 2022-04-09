# Get current year

```python
from datetime import datetime

currentYear = datetime.now().year
```

- `from datetime import datetime` - import datetime utility to operate with time
- `datetime.now()` - returns current date object
- `.year` - attribute returns year
- `currentYear` - will contain current year

group: date

## Example: 
```python
from datetime import datetime

currentYear = datetime.now().year
print(currentYear)
```
```
2022

```

