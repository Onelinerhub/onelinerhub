# Run multiple goroutines and wait for them to finish

```go
package main

import "fmt"
import "sync"

func hi(idx int) {
  fmt.Println(idx)
}

func main() {
  var wg sync.WaitGroup
  
  for i := 1; i <= 3; i++ {
    i := i
    wg.Add(1)
    go func() {
      defer wg.Done()
      hi(i)
    }()
  }
  
  wg.Wait()
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `func hi` - function that we will call in parallel
- `wg sync.WaitGroup` - declare new wait group
- `i := i` - used not to mix `i` values in closure
- `wg.Add(1)` - increase waiting counter on each iteration by `1`
- `defer wg.Done()` - call `hi()` function in closure
- `wg.Wait()` - will wait for all goroutines to finish

group: goroutine

## Example: 
```go
package main

import "fmt"
import "sync"

func hi(idx int) {
  fmt.Println(idx)
}

func main() {
  var wg sync.WaitGroup
  
  for i := 1; i <= 3; i++ {
    i := i
    wg.Add(1)
    go func() {
      defer wg.Done()
      hi(i)
    }()
  }
  
  wg.Wait()
}
```
```
3
1
2

```

