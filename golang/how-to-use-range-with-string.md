# How to use range with string

```go
package main

func main() {
  str := "joe"

  for k, v := range str {
    print(k, ":", string(v), ";")
  }
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `for k, v := range str` - iterate over `str` string characters with `range` and having all chars in `v` variable and index in `k` variable
- `string(v)` - return character from its code

group: range

## Example: 
```go
package main

func main() {
  str := "joe"

  for k, v := range str {
    print(k, ":", string(v), ";")
  }
}
```
```
0:j;1:o;2:e;
```

