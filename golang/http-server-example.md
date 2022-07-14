# HTTP server example

```go
package main
import ( "fmt"; "net/http" )

func hi(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, "Oh hi!\n")
}

func main() {
  http.HandleFunc("/hi", hi)
  http.ListenAndServe(":8222", nil)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.HandleFunc` - add handler to specified request URI
- `"/hi", hi` - handle `/hi` request with `hi()` function
- `http.ListenAndServe` - launch HTTP server
- `8222` - port to listen HTTP server on

group: http_server

## Example: 
```go
package main
import ( "fmt"; "net/http" )

func hi(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, "Oh hi!\n")
}

func main() {
  http.HandleFunc("/hi", hi)
  http.ListenAndServe(":8222", nil)
}
```
```
# returns "hi" on "localhost:8222/hi" request
```

