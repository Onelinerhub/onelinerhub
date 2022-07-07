# Using FOR range loop

```go
package main
import "fmt"

func main() {
  nums := [5]int{1,2,3,4,5}
  for i, item := range nums {
    fmt.Printf("nums[%d] = %d \n", i, item)
  }
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `nums` - array with 5 numbers we plan to iterate over
- `i, item := range nums` - iterate over `nums` while saving index to `i` and value to `item` on each iteration

group: for

## Example: 
```go
package main
import "fmt"

func main() {
  nums := [5]int{1,2,3,4,5}
  for i, item := range nums {
    fmt.Printf("nums[%d] = %d \n", i, item)
  }
}
```
```
nums[0] = 1 
nums[1] = 2 
nums[2] = 3 
nums[3] = 4 
nums[4] = 5 

```

