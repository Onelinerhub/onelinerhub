# How to sort slice of strings

```go
package main
import "sort"

func main() {
	arr := []string{"joe","donald", "angela"}
	sort.Strings(arr)
}

```

- `import` - loads net package which provides a portable interface for network I/O and the fmt to print out the nserver
- `func main() {` - declare `main` function that will be launched automatically
- `[]string{"joe","donald", "angela"}` - create slice with `3` `string` values
- `sort.Strings(` - sorts slice of `string` values

group: slices

## Example: 
```go
package main

import "sort"
import "fmt"

func main() {
	arr := []string{"joe","donald", "angela"}
	sort.Strings(arr)
	fmt.Println(arr)
}

```
```
[angela donald joe]

```

