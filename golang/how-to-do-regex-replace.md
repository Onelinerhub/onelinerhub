# How to do regex replace

```go
package main
import "regexp"

func main() {
  r := regexp.MustCompile(`[0-9]`)
  res := r.ReplaceAllString("+312-332-1432", "*")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `regexp.MustCompile(` - create regexp object and compile given pattern
- `.ReplaceAllString(` - replaces all substrings found by a regex pattern

group: regex

## Example: 
```go
package main
import "regexp"

func main() {
  r := regexp.MustCompile(`[0-9]`)
  res := r.ReplaceAllString("+312-332-1432", "*")
  print(res)
}
```
```
+***-***-****
```

