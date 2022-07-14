# How to iterate over map

```go
package main

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  for k, v := range mp {
    print(k, ": ", v, "; ")
  }
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `for k, v := range mp` - iterate over `mp` map
- `print(k, ": ", v, "; ")` - `k` will contain current key and `v` will contain current value

group: map

## Example: 
```go
package main

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  for k, v := range mp {
    print(k, ": ", v, "; ")
  }
}
```
```
name: Joe; position: president;
```

