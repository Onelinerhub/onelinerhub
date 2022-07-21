# How to generate query string from map

```go
package main
import "net/url"

func main() {
  q := req.URL.Query()
  q.Add("a", 12)
  q.Add("b", "hello")
  print(q)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `url.Parse(` - parses given URL into `url` object
- `url.Query()` - get query string as map

group: query_params

## Example: 
```go
package main
import "net/url"

func main() {
  q := url.Values{}
  q.Add("a", 12)
  q.Add("b", "hello")
  print(q.Encode())
}
```
```
# command-line-arguments
./test.go:6:14: cannot use 12 (untyped int constant) as string value in argument to q.Add
```

