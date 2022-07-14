# How to get request body from HTTP server

```go
import ( "fmt"; "net/http"; "io" )

func hi(w http.ResponseWriter, req *http.Request) {
  defer req.Body.Close()
  b, _ := io.ReadAll(req.Body)
  fmt.Fprintf(w, string(b))
}

func main() {
  http.HandleFunc("/hi", hi)
  http.ListenAndServe(":8222", nil)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `io.ReadAll(req.Body)` - reads entire body into `b` variable (and then printed back to client)
- `"/hi", hi` - handle `/hi` request with `hi()` function
- `http.ListenAndServe` - launch HTTP server
- `8222` - port to listen HTTP server on

group: http_server

## Example: 
```go
import ( "fmt"; "net/http"; "io" )

func hi(w http.ResponseWriter, req *http.Request) {
  defer req.Body.Close()
  b, _ := io.ReadAll(req.Body)
  fmt.Fprintf(w, string(b))
}

func main() {
  http.HandleFunc("/hi", hi)
  http.ListenAndServe(":8222", nil)
}
```
```
# returns "123" on "localhost:8222/hi?test=123" request
```

