# How to format time in ISO 8601 format

```go
package main

import (
  "fmt"
  "time"
)

func main() {
	fmt.Println(time.Now().Format(time.RFC3339))
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
	fmt.Println(time.Now().Format(time.RFC3339))
}

```
```
2022-06-09T14:09:15Z

```

