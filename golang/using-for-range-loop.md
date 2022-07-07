# Using FOR range loop

```go

```


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

