# How to get length of map

```go
package main

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  length := len(mp)
}
```

- `package main` - default package declaration
- `make(map[string]string)` - initialize map with string keys and string values
- `mp["name"]` - set value of `name` key
- `len(` - returns length of a given map
- `length` - variable will contain length value

group: map

## Example: 
```go
package main

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  length := len(mp)
  print(length)
}
```
```
2
```

