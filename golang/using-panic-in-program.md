# Using panic() in program

```go
package main
func main() {
  age := 90
  
  if age > 50 {
    panic("Naah, too old")
  }  
}
```


group: panic

## Example: 
```go
package main
func main() {
  age := 90
  
  if age > 50 {
    panic("Naah, too old")
  }  
}
```
```
panic: Naah, too old

goroutine 1 [running]:
main.main()
	/tmp/test.go:6 +0x27
exit status 2
```

