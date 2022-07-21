# golang url encode

```go
package main
import "net/url"

func main() {
  escaped := url.QueryEscape("name is Joe & Donald")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `url.QueryEscape(` - encodes given value based on URL encoding standard
- `name is Joe & Donald` - sample value to encode

## Example: 
```go
package main
import "net/url"

func main() {
  escaped := url.QueryEscape("name is Joe & Donald")
  print(escaped)
}
```
```
name+is+Joe+%26+Donald
```

