# How to delete item from slice

```go
package main

import "fmt"

func main() {
	s := []int{1,2,3}
	s = append(s[:1], s[2:]...)
}

```

- `s := []int{1,2,3}` - declare slice of int with 3 sample elements
- `append` - we'll use append to concatenate parts of given slices without removed element
- `s[:1]` - get part of `s` slice up to second element (`1` position - second element)
- `s[2:]` - get part of `s` slice from third element up to the end (`2` position - third element)

group: slices

## Example: 
```go
package main

import "fmt"

func main() {
	s := []int{1,2,3}
	s = append(s[:1], s[2:]...)
	fmt.Println(s)
}

```
```
[1 3]

```

