# golang goroutine usage

```go

```


## Example: 
```go
package main

import "fmt"
import "time"

func hi(name string, sleep int) {
  fmt.Println(time.Millisecond)
  //time.Sleep(time.Duration(sleep) * time.Millisecond)
  fmt.Println("Hi, " + name + "!")
}

func main() {
	hi("Joe", 2)
	go hi("Donald", 1)
}
```
```
# command-line-arguments


./test.go:7:28: invalid operation: sleep * time.Millisecond (mismatched types int and time.Duration)
```

