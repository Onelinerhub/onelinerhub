# How to copy slice elements

```go
package main

import "fmt"

func main() {
	s1 := []int{1, 2, 3}
	s2 := []int{4, 5}
  copy(s1, s2)
}

```

- `s1 := []int{1, 2, 3}` - first slice to copy items to
- `s2 := []int{4, 5}` - second slice to copy items from
- `copy(s1, s2)` - copies elements from `s2` slice to `s1` slice

group: slices

## Example: 
```go
package main

import "fmt"

func main() {
	s1 := []int{1, 2, 3}
	s2 := []int{4, 5}
  copy(s1, s2)
	fmt.Println(s1)
}

```
```
[4 5 3]

```

