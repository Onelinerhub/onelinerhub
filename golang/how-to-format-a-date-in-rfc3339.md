# How to format a date in RFC3339

```go
package main

import (
  "fmt"
  "time"
)

func main() {
	ct := time.Now()
	fmt.Println(ct.Format(time.RFC3339))
}

```

- `time.Now()` - returns current date time
- `Format` - formats datatime
- `time.RFC3339` - RFC3339 format

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
	fmt.Println(ct.Format(time.RFC3339))
}

```
```
2022-06-09T14:03:07Z

```

