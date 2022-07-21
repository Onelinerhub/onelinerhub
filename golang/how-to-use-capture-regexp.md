# How to use capture regexp

```go
package main
import "regexp"

func main() {
  r := regexp.MustCompile(`o(h[0-9])`)
  captures := r.FindStringSubmatch("oh2f3")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `regexp.MustCompile(` - create regexp object and compile given pattern
- `.FindStringSubmatch(` - returns found capture groups from a given string
- `captures` - will contain list of captured values

group: regex

## Example: 
```go
package main
import "regexp"

func main() {
  r := regexp.MustCompile(`o(h[0-9])`)
  captures := r.FindStringSubmatch("oh2f3")
  print(captures[1])
}
```
```
h2
```

