# How to get JSON data from HTTP request

```go
package main

import ("net/http"; "os"; "encoding/json")

func main() {
  r, _ := http.Get("https://echoof.me/json")
  defer r.Body.Close()
  
  res := F{}
  json.NewDecoder(r.Body).Decode(res)
  print(res)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Get(` - executes GET request to the specified URL
- `io.Copy(os.Stdout, r.Body)` - output response body to stdout

group: http_client

## Example: 
```go
package main

import ("net/http"; "os"; "encoding/json")

func main() {
  r, _ := http.Get("https://echoof.me/json")
  defer r.Body.Close()
  
  res := F{}
  json.NewDecoder(r.Body).Decode(res)
  print(res)
}
```
```
# command-line-arguments
./test.go:9:10: syntax error: unexpected {, expecting expression
./test.go:10:3: syntax error: non-declaration statement outside function body
```

