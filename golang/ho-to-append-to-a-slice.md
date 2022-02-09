# Ho to append to a slice

```go
package main

import "fmt"

func main() {
	var s []int
	s = append(s, 1)
}

```

- `var s []int` - declare `s` slice
- `append(s, 1)` - append `1` value to `s slice`

group: slices

## Example: 
```go
package main

import "fmt"

func main() {
	var s []int
	s = append(s, 1)
	s = append(s, 2)
	fmt.Println(s)
}

```
```
[1 2]

```

