# How to get map keys

```go
package main

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  keys := make([]string, 0, len(mp))
  for k := range mp {
    keys = append(keys, k)
  }
}
```

- `package main` - default package declaration
- `make(map[string]string)` - initialize map with string keys and string values
- `mp["name"]` - set value of `name` key
- `len(` - returns length of a given map
- `keys` - slice will contain list of all map keys
- `append(keys, k)` - append each key from `mp` to `keys`

group: map

## Example: 
```go
package main

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  keys := make([]string, 0, len(mp))
  for k := range mp {
    keys = append(keys, k)
  }

  print(keys[0])
  print(keys[1])
}
```
```
nameposition
```

