# How to format a date in "MM/DD/YYYY"

```go
package main

import (
  "fmt"
  "time"
)

func main() {
	ct := time.Now()
	fmt.Println(ct.Format("02/01/2006"))
}

```

- `time.Now()` - returns current date time
- `Format` - formats datatime
- `"02/01/2006"` - will format date in MM/DD/YYYY

group: date

## Example: 
```go
package main

import (
  "fmt"
  "time"
)

func main() {
	ct := time.Now()
	fmt.Println(ct.Format("02/01/2006"))
}

```
```
09/06/2022

```

