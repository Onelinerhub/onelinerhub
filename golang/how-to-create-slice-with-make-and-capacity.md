# How to create slice with make() and capacity

```go
package main

func main() {
	a := make([]int, 5, 10)
}
```

- `package main` - default package declaration
- `make(` - creates zero-filled array and returns slice referencing this array
- `[]int, 5, 10` - we're creating array of 10 integers and return a slice of 5 elements from this array

group: make

## Example: 
```go
package main
import "fmt"

func main() {
	a := make([]int, 5, 10)
	fmt.Println(len(a))
	fmt.Println(cap(a))
}
```
```
5
10

```

