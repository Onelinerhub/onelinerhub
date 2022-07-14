# How to get response status code of HTTP request

```go
package main

import ("net/http"; "os"; "io")

func main() {
  r, _ := http.Get("https://echoof.me")
  print(r.StatusCode)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Get(` - executes GET request to the specified URL
- `.StatusCode` - will return request status code

group: http_client

## Example: 
```go
package main

import ("net/http")

func main() {
  r, _ := http.Get("https://echoof.me")
  print(r.StatusCode)
}
```
```
200
```

