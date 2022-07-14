# How to get response body of HTTP request

```go
package main

import ("net/http"; "os"; "io")

func main() {
  r, _ := http.Get("https://echoof.me/")
  defer r.Body.Close()
  
  b, _ := io.ReadAll(r.Body)
  body := string(b)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Get(` - executes GET request to the specified URL
- `io.ReadAll(r.Body)` - reads entire buffer (response body) into `b` bytes var
- `string(b)` - converts bytes to string and writes result to `body` var

group: http_client

## Example: 
```go
package main

import ("net/http"; "io")

func main() {
  r, _ := http.Get("https://echoof.me/")
  defer r.Body.Close()
  
  b, _ := io.ReadAll(r.Body)
  body := string(b)
  
  print(body)
}
```
```
IP:                           135.181.98.214

ACCEPT_ENCODING:              gzip
USER_AGENT:                   Go-http-client/1.1

https://echoof.me
```

