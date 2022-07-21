# How to parse query string params

```go
package main
import "net/url"

func main() {
  url, _ := url.Parse("https://test.com/?a=1&b=hi")
  a := url.Query()["a"]
  b := url.Query()["b"]
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
import ( "fmt"; "net/url" )

func main() {
  url, _ := url.Parse("https://test.com/?a=1&b=hi")
  a := url.Query()["a"]
  b := url.Query()["b"]
  fmt.Println(a)
  fmt.Println(b)
}
```
```
[1]
[hi]

```

