# How to make POST request using HTTP client

```go
package main

import ("net/http"; "os"; "io"; "time")

func main() {
  h := http.Client{Timeout: 3 * time.Second}
  r, _ := h.Get("https://echoof.me/")
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Client{` - creates HTTP client object
- `Timeout:` - sets request timeout
- `3 * time.Second` - timeout is set to `3` seconds
- `.Body` - object to access response body
- `io.Copy(os.Stdout, r.Body)` - output response body to stdout

group: http_client

## Example: 
```go
package main

import ("net/http"; "os"; "io"; "net/url")

func main() {
  h := http.Client{}
  data := url.Values{
    "name": {"John Doe"},
  }
  r, _ := h.Post("https://echoof.me/", "multipart/form-data", data)
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```
```
# command-line-arguments

./test.go:10:40: not enough arguments in call to h.Post
	have (string, url.Values)
	want (string, string, io.Reader)
```

