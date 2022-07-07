# How to continue in FOR loop

```go
package main
import "fmt"

func main() {
  nums := [5]int{1,2,3,4,5}
  for i, item := range nums {
    if ( i < 3 ) {
      continue
    }
    
    fmt.Printf("nums[%d] = %d \n", i, item)
  }
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `nums` - array with 5 numbers we plan to iterate over
- `i, item := range nums` - iterate over `nums` while saving index to `i` and value to `item` on each iteration
- `if ( i < 3 ) {` - sample condition to skip loop (continue) execution on
- `continue` - skips execution to next loop iteration

group: for

## Example: 
```go
package main
import "fmt"

func main() {
  nums := [5]int{1,2,3,4,5}
  for i, item := range nums {
    if ( i < 3 ) {
      continue
    }
    
    fmt.Printf("nums[%d] = %d \n", i, item)
  }
}
```
```
nums[3] = 4 
nums[4] = 5 

```

