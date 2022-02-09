# How to concatenate two slices

```go
package main

import "fmt"

func main() {
	var s []int
	s = append([]int{1,2}, []int{3,4}...)
}

```

- `var s []int` - declare `s` slice
- `append` - appends given slices
- `[]int{1,2}` - first sample slice
- `[]int{3,4}` - second sample slice

group: slices

## Example: 
```go
package main

import "fmt"

func main() {
	var s []int
	s = append([]int{1,2}, []int{3,4}...)
	fmt.Println(s)
}

```
```
[1 2 3 4]

```

