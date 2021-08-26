# Fetch the username of the running computer

```Go
package main

import (
	"fmt"
	"log"
	"os/user"
)

func main() {

	user, err := user.Current()
	if err != nil {
		log.Fatalf(err.Error())
	}

	username := user.Username

	fmt.Println(username)
}
```

- "os/user" - Package user allows user account lookups by name or id.
- "log" - packet logging implements a simple log pack. It defines a type of Logger with methods for formatting the output.
- user.Current() - returns the current user.
- user.Username - returns the name of the computer user.
