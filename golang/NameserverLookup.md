# Find the nameserver records of a domain name

```go
package main
import ("net"; "fmt" )

func main() {
  nameserver, _ := net.LookupNS("github.com")
	for _, nserver := range nameserver {
		fmt.Println(nserver)
	}
}
```

- `import` - loads net package which provides a portable interface for network I/O and the fmt to print out the nserver
- `net.LookupNS(` - returns the domain name server for the given web address

## Example: 
```go
package main
import ("net"; "fmt" )

func main() {
  nameserver, _ := net.LookupNS("github.com")
	for _, nserver := range nameserver {
		fmt.Println(nserver)
	}
}
```
```
&{ns-421.awsdns-52.com.}
&{ns-520.awsdns-01.net.}
&{dns1.p08.nsone.net.}
&{dns2.p08.nsone.net.}
&{dns3.p08.nsone.net.}
&{dns4.p08.nsone.net.}
&{ns-1283.awsdns-32.org.}
&{ns-1707.awsdns-21.co.uk.}

```

