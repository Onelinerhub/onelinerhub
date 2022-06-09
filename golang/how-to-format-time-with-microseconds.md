# How to format time with microseconds

```go
package main

import (
  "fmt"
  "time"
)

func main() {
	ct := time.Now()
	fmt.Println(ct.Format("15:04:05.000000"))
}

```

- `time.Now()` - returns current date time
- `Format` - formats datatime
- `.000000` - Adds microseconds to time format

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
	fmt.Println(ct.Format("15:04:05.000000"))
}

```
```
14:06:36.384663

```

