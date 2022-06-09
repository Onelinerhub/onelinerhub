# How to format time with milliseconds

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
- `.000` - Adds milliseconds to time format

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

