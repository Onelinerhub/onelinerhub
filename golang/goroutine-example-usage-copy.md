# How to return value from goroutine using channels

```go
func main() {
  c := make(chan int)
  go func(a int) {
    c <- a * 2
  }(2)
	
	select {
    case msg := <-c:
      res := msg
      fmt.Println("received", res)
  } 
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `c := make(chan int)` - declare channel to use for return value from goroutine
- `go func` - call anonymous function in parallel
- `c <- a * 2` - return result from function to channel `c`
- `select {` - handle channel messages
- `case msg := <-c` - check if message is from channel `c`
- `res := msg` - save returned value to `res` variable

group: goroutine

## Example: 
```go
package main
import "fmt"

func main() {
  c := make(chan int)
  go func(a int) {
    c <- a * 2
  }(2)
	
	select {
    case msg := <-c:
      fmt.Println("received", msg)
  } 
}
```
```
received 4

```

