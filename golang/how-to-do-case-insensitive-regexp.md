# How to do case-insensitive regexp

```go
package main
import "regexp"

func main() {
  mtch, _ := regexp.MatchString(`(?i)oh[0-9]`, "OH2f3")
  print(mtch)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `regexp.MatchString(` - match given string with a given pattern
- `(?i)` - this will make regex search case-insensitive

group: regex

## Example: 
```go
package main
import "regexp"

func main() {
  mtch, _ := regexp.MatchString(`(?i)oh[0-9]`, "OH2f3")
  print(mtch)
}
```
```
true
```

