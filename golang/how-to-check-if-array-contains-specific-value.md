# How to check if array contains specific value

```go
func main() {
  arr := [5]int{10,12,50,400,8}
  has := false
  for _, a := range arr {
    if a == 400 {
      has = true
    }
  }
  
  print(has)
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `[5]int{10,12,50,400,8}` - sample array declaration
- `has` - will contain `true` if searched value is in array
- `for _, a := range arr {` - iterate over all values of `arr` array
- `400` - searched value

group: arrays

## Example: 
```go
package main

func main() {
  arr := [5]int{10,12,50,400,8}
  has := false
  for _, a := range arr {
    if a == 400 {
      has = true
    }
  }
  
  print(has)
}
```
```
true
```

