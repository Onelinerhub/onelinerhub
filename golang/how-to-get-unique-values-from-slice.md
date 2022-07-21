# How to get unique values from slice

```go
package main

import "fmt"

func main() {
  arr := []int{3,7,4,7,3,7,2,6,7,3,7,4}
  fmt.Println(arr)
  
  keys := make(map[int]bool)
  uniq := []int{}	
  for _, entry := range arr {
    if _, value := keys[entry]; !value {
      keys[entry] = true
      uniq = append(uniq, entry)
    }
  }
  
  fmt.Println(uniq)
}
```

- `import` - loads net package which provides a portable interface for network I/O and the fmt to print out the nserver
- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `arr` - sample int slice with duplicate values
- `for _, entry := range arr` - iterate over `arr` items
- `if _, value := keys[entry]; !value {` - check if we have seen this value already
- `append(uniq, entry)` - append new entries to `uniq` slice

group: slices

## Example: 
```go
package main

import "fmt"

func main() {
  arr := []int{3,7,4,7,3,7,2,6,7,3,7,4}
  fmt.Println(arr)
  
  keys := make(map[int]bool)
  uniq := []int{}	
  for _, entry := range arr {
    if _, value := keys[entry]; !value {
      keys[entry] = true
      uniq = append(uniq, entry)
    }
  }
  
  fmt.Println(uniq)
}
```
```
[3 7 4 7 3 7 2 6 7 3 7 4]
[3 7 4 2 6]

```

