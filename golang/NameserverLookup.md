#Find the nameserver records of a domain name

```Go
import (
        "net"
        "fmt"
        )

nameserver, _ := net.LookupNS("github.com")
	for _, nserver := range nameserver {
		fmt.Println(nserver)
	}
  
- import the net package which provides a portable interface for network I/O and the fmt to print out the nserver
- net.LookupNS() returns the domain name server for the given web address
