# How to create slice

```go
package main
 
func main() {
  arr := [2]string{"a","b"}
  print(arr[1])
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `[2]string{` - create slice of `2` elements of `string` type

## Example: 
```go
package main
 
func main() {
  arr := [2]string{"a","b"}
  print(arr[1])
}
```
```
b
```

