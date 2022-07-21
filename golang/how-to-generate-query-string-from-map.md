# How to generate query string from map

```go
package main
import "net/url"

func main() {
  q := url.Values{}
  q.Add("a", "12")
  q.Add("b", "hello")
  
  encoded := q.Encode()
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `url.Values{}` - create new `Values` object to generate query string
- `.Add(` - adds new param to query string object
- `.Encode()` - generate query string from given values

group: query_params

## Example: 
```go
package main
import "net/url"

func main() {
  q := url.Values{}
  q.Add("a", "12")
  q.Add("b", "hello")
  
  encoded := q.Encode()
  print(encoded)
}
```
```
a=12&b=hello
```

