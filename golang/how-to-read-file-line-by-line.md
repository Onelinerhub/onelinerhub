# How to read file line by line

```go
package main

import (
  "bufio"
  "fmt"
	"os"
)

func main() {
  f, _ := os.Open("/var/www/examples/data.csv")
  defer f.Close()
  
  scn := bufio.NewScanner(f)
  for scn.Scan() {
    fmt.Println(scn.Text())
  }
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `os.Open` - opens specified file handler
- `/var/www/examples/data.csv` - path to sample file with multiple lines
- `defer f.Close()` - deferred file handler close
- `bufio.NewScanner` - create new scanning buffer from our file handler
- `scn.Scan()` - iterate over scanning buffer
- `scn.Text()` - get buffer content on each iteration

group: file

## Example: 
```go
package main

import (
  "bufio"
  "fmt"
	"os"
)

func main() {
  f, _ := os.Open("/var/www/examples/data.csv")
  defer f.Close()
  
  scn := bufio.NewScanner(f)
  for scn.Scan() {
    fmt.Println(scn.Text())
  }
}
```
```
a,b
1,4
2,3
3,6

```

