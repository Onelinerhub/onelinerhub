# How to format a date in "YYYY-MM-DD"

```go
package main

import (
  "fmt"
  "time"
)

func main() {
	ct := time.Now()
	fmt.Println(ct.Format("2006-02-01"))
}

```

- `time.Now()` - returns current date time
- `Format` - formats datatime
- `"2006-02-01"` - will format date in YYYY-MM-DD

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
	fmt.Println(ct.Format("2006-02-01"))
}

```
```
2022-09-02

```

