# How to add thousands comma separator to a number

```go
package main

import "golang.org/x/text/language"
import "golang.org/x/text/message"
import "fmt"

func main() {
  p := message.NewPrinter(language.English)
  s := p.Sprintf("%d", 12398712983)
  fmt.Println(s)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `golang.org/x/text` - enables localization capabilities
- `message.NewPrinter(language.English)` - create localized English printer
- `12398712983` - sample number to add thousands separator to
- `fmt.Println` - prints specified string

group: int_format

## Example: 
```go
package main

import "golang.org/x/text/language"
import "golang.org/x/text/message"
import "fmt"

func main() {
  p := message.NewPrinter(language.English)
  s := p.Sprintf("%d", 12398712983)
  fmt.Println(s)
}
```
```
12,398,712,983

```

