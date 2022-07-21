# How to use regexp

```go
package main
import "regexp"

func main() {
  mtch, _ := regexp.MatchString(`oh[0-9]`, "oh2f3")
  print(mtch)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `regexp.MatchString(` - match given string with a given pattern
- `mtch` - will contain `true` if regexp matches

group: regex

## Example: 
```go
package main
import "regexp"

func main() {
  mtch, _ := regexp.MatchString(`oh[0-9]`, "oh2f3")
  print(mtch)
}
```
```
true
```

