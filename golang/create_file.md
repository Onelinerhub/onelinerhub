# How to create a file

```go
package main

import (
	"log"
	"os"
)

func main() {
	file, err := os.Create("/tmp/go.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
}
```

- `"os"` - include operating-system level library
- `"log"` - packet logging implements a simple log pack. It defines a type of Logger with methods for formatting the output.
- `os.Create("/tmp/go.txt")` - function is used to create file named `file.txt`
- `file.Close()` - Closes the file after file operations are complete.

## Example: 
```go
package main

import (
	"log"
	"os"
	"fmt"
)

func main() {
	file, err := os.Create("/tmp/go.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	
	info, err := os.Stat("/tmp/go.txt")
	fmt.Println(info.ModTime())
}
```
```
2022-07-07 12:14:55.105010013 +0000 UTC

```

