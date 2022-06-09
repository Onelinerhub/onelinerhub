# How to format time in ISO 8601 format

```go
package main

import (
  "fmt"
  "time"
)

func main() {
	ct := time.Now()
	fmt.Println(ct.Format("15:04:05.000"))
}

```

- `time.Now()` - returns current date time
- `Format` - formats datatime
- `time.RFC3339` - RFC3339 format (ISO 8601 standard)

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
	fmt.Println(ct.Format("15:04:05.000"))
}

```
```
14:06:18.532

```

