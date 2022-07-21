# How to use range

```go
package main

func main() {
  list := [7]int{3,4,5,2,2,4,5}

  for k, v := range list {
    print(k, ":", v, ";")
  }
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `for k, v := range list` - iterate over `list` array with `range` and having all values in `v` variable and key in `k` variable

group: range

## Example: 
```go
package main

func main() {
  list := [7]int{3,4,5,2,2,4,5}

  for k, v := range list {
    print(k, ":", v, ";")
  }
}
```
```
0:3;1:4;2:5;3:2;4:2;5:4;6:5;
```

