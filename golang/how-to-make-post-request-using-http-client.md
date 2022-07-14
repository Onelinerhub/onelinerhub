# How to make POST (form data) request using HTTP client

```go
package main

import ("net/http"; "os"; "io"; "net/url")

func main() {
  data := url.Values{ "name": {"John Doe"} }
  r, _ := http.PostForm("https://echoof.me", data)
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `url.Values` - prepares data to post
- `http.PostForm` - post given form data to the specified URL
- `io.Copy(os.Stdout, r.Body)` - output response body to stdout

group: http_client

## Example: 
```go
package main

import ("net/http"; "os"; "io"; "net/url")

func main() {
  data := url.Values{ "name": {"John Doe"} }
  r, _ := http.PostForm("https://echoof.me", data)
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```
```
IP:                           135.181.98.214

ACCEPT_ENCODING:              gzip
CONTENT_TYPE:                 application/x-www-form-urlencoded
CONTENT_LENGTH:               13
USER_AGENT:                   Go-http-client/1.1

DATA name:                    John Doe

https://echoof.me
```

