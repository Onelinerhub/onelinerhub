# How to URL decode value

```go
package main
import "net/url"

func main() {
  decoded, _ := url.QueryUnescape("name+is+Joe+%26+Donald")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `url.QueryUnescape(` - decodes given [URL-encoded value](/golang/golang-url-encode)

group: url_encoding

## Example: 
```go
package main
import "net/url"

func main() {
  decoded, _ := url.QueryUnescape("name+is+Joe+%26+Donald")
  print(decoded)
}
```
```
name is Joe & Donald
```

