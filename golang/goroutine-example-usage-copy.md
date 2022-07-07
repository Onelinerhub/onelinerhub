# Goroutine channel usage

```go
func main() {
  go func() {
    // do something in background
  }()
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `go ` - execute given function in parallel
- `func() {` - anonymous function to execute in background

group: goroutine

## Example: 
```go
package main

import "fmt"
import "time"

func hi(name string, sleep int) {
  time.Sleep(time.Duration(sleep) * 1000 * time.Millisecond)
  fmt.Println("Hi, " + name + "!")
}

func main() {
  go hi("Donald", 2)
	hi("Joe", 1)
	time.Sleep(time.Second)
}
```
```
Hi, Joe!
Hi, Donald!

```

