
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

- import os/user - Package user allows user account lookups by name or id.
- import log - Packet logging implements a simple log pack. It defines a type of Logger with methods for formatting the output.
- 'Current()' Current returns the current user.
- 'user.Username' Returns the name of the computer user.