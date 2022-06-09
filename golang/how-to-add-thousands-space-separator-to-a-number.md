# How to add thousands space separator to a number

### We use a hack here to localize our number to English standard (uses comma as thousands separator) and then replace commas with spaces:

```go
package main

import "golang.org/x/text/language"
import "golang.org/x/text/message"
import "fmt"
import "strings"

func main() {
  p := message.NewPrinter(language.English)
  s := strings.Replace(p.Sprintf("%d", 12398712983),","," ",-1)
  fmt.Println(s)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `golang.org/x/text` - enables localization capabilities
- `message.NewPrinter(language.English)` - create localized English printer
- `12398712983` - sample number to add thousands separator to
- `strings.Replace(` - replaces found substring to the specified string given amount of times
- `","," ",-1` - replace `,` (comma) to ` ` (space), all found entities (`-1`)
- `fmt.Println` - prints specified string

group: int_format

## Example: 
```go
package main

import "golang.org/x/text/language"
import "golang.org/x/text/message"
import "fmt"
import "strings"

func main() {
  p := message.NewPrinter(language.English)
  s := strings.Replace(p.Sprintf("%d", 12398712983),","," ",-1)
  fmt.Println(s)
}
```
```
12 398 712 983

```

