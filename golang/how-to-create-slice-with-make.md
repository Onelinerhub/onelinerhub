# How to create slice with make()

```go
package main

func main() {
	a := make([]int, 5)
}
```

- `package main` - default package declaration
- `make(` - creates zero-filled array and returns slice referencing this array
- `[]int, 5` - we're creating array of 5 integers

group: make

## Example: 
```go
package main
import "fmt"

func main() {
	a := make([]int, 5)
	fmt.Println(a)
}
```
```
[0 0 0 0 0]

```

