# Creating a folder

```Go
package main

import (
	"log"
	"os"
)

func main() {
	file, err := os.Create("file.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
}
```

- "os" - include operating-system level library
- "log" - packet logging implements a simple log pack. It defines a type of Logger with methods for formatting the output.
- os.Create("file.txt") - function is used to create file named `file.txt`
- file.Close() - Closes the file after file operations are complete.
