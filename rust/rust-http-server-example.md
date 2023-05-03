# Rust HTTP server example
// plain

A basic Rust HTTP server example can be written using the [hyper](https://hyper.rs/) library. The following ## Code example creates a server that listens on port 8080 and responds with a "Hello World" message when a request is received:
```rust
use hyper::{Body, Request, Response, Server};
use hyper::rt::{self, Future};
use hyper::service::service_fn_ok;

fn hello_world(_req: Request<Body>) -> Response<Body> {
    Response::new(Body::from("Hello, World!"))
}

fn main() {
    let addr = ([127, 0, 0, 1], 8080).into();

    let server = Server::bind(&addr)
        .serve(|| service_fn_ok(hello_world))
        .map_err(|e| eprintln!("server error: {}", e));

    println!("Listening on http://{}", addr);

    rt::run(server);
}
```

The ## Code example creates a server that listens on port 8080 and responds with a "Hello World" message when a request is received. The `Server::bind` method is used to bind the server to the given address, and the `serve` method is used to specify the service that should be used to handle requests. The `service_fn_ok` function is used to create a service that will handle requests and return a response. Finally, the `run` method is used to start the server.

Output example:
```
Listening on http://127.0.0.1:8080
```

## Explanation
 The ## Code example creates a server that listens on port 8080 and responds with a "Hello World" message when a request is received. The `Server::bind` method is used to bind the server to the given address, and the `serve` method is used to specify the service that should be used to handle requests. The `service_fn_ok` function is used to create a service that will handle requests and return a response. Finally, the `run` method is used to start the server.

## Helpful links
- [Hyper Documentation](https://hyper.rs/guides/server/hello-world/)
- [Rust HTTP Server Tutorial](https://www.joshmcguigan.com/blog/rust-http-server-tutorial/)
- [Rust HTTP Server Example](https://github.com/rust-lang-nursery/rust-cookbook/blob/master/src/network/http-server.rs)