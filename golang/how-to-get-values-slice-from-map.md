# How to get values slice from map

```go
package main

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  vals := make([]string, 0, len(mp))
  for  _, v := range mp {
     vals = append(vals, v)
  }
}
```

- `package main` - default package declaration
- `make(map[string]string)` - initialize map with string keys and string values
- `len(` - returns length of a given map
- `vals = append(vals, v)` - add each `mp` value to `vals` slice

group: map

## Example: 
```go
package main

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  vals := make([]string, 0, len(mp))
  for  _, v := range mp {
     vals = append(vals, v)
  }
  
  print(vals[0])
  print(vals[1])
}
```
```
Joepresident
```

