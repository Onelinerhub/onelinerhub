# How to format time in "HH:MM:SS"

```go
package main

import (
  "fmt"
  "time"
)

func main() {
	ct := time.Now()
	fmt.Println(ct.Format("15:04:05"))
}

```

- `time.Now()` - returns current date time
- `Format` - formats datatime
- `"15:04:05"` - will format date in HH:MM:SS

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
	fmt.Println(ct.Format("15:04:05"))
}

```
```
16:16:56

```

