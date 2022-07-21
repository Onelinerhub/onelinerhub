# How to sort slice

```go
package main
import "sort"

func main() {
	arr := []int{3,1,7,2}
	sort.Ints(arr)
}

```

- `import` - loads net package which provides a portable interface for network I/O and the fmt to print out the nserver
- `func main() {` - declare `main` function that will be launched automatically
- `[]int{3,1,7,2}` - create slice with `4` `int` values
- `sort.Ints(` - sorts slice of `int` values

group: slices

## Example: 
```go
package main

import "sort"
import "fmt"

func main() {
	arr := []int{3,1,7,2}
	sort.Ints(arr)
	fmt.Println(arr)
}

```
```
[1 2 3 7]

```

