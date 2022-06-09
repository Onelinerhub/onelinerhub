# How to add thousands separators commas to a number 

```go
package main

import "fmt"

func main() {
  setlocale(LC_ALL, "");
  printf("%'d\n", 1000);
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `%08d` - pads given number to 8 zeros on the left
- `123` - sample integer value to format
- `res` - variable will contain formatted value

group: int_format

```
/tmp/test.go:3:8: no required module provides package golang.org/x/text/language: go.mod file not found in current directory or any parent directory; see 'go help modules'
```

