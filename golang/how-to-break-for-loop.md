# How to break FOR loop

```go
package main
import "fmt"

func main() {
  nums := [5]int{1,2,3,4,5}
  for i, item := range nums {
    fmt.Printf("nums[%d] = %d \n", i, item)
    if ( i >= 1 ) {
      break
    }
  }
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `nums` - array with 5 numbers we plan to iterate over
- `i, item := range nums` - iterate over `nums` while saving index to `i` and value to `item` on each iteration
- `if ( i >= 1 ) {` - sample condition to break loop on
- `break` - breaks current loop

group: for

## Example: 
```go
package main
import "fmt"

func main() {
  nums := [5]int{1,2,3,4,5}
  for i, item := range nums {
    fmt.Printf("nums[%d] = %d \n", i, item)
    if ( i >= 1 ) {
      break
    }
  }
}
```
```
nums[0] = 1 
nums[1] = 2 

```

