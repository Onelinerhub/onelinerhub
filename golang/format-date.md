# How to get current time

```go
package main

import (
  "fmt"
  "time"
)

func main() {
	ct := time.Now()
}

```

- `"time"` - module allows manipulating time
- `time.Now()` - returns current date time

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
	fmt.Println(ct)
}

```
```
2022-02-09 16:11:30.88623962 +0000 UTC m=+0.000039235

```

