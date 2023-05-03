# Rust Web server example
// plain

[Rocket](https://rocket.rs/) is a web framework for Rust that makes it simple to write fast web applications without sacrificing flexibility or type safety.

```rust
#[get("/")]
fn index() -> &'static str {
    "Hello, world!"
}
```

## Output example
```
Hello, world!
```

The code above is an example of a simple web server written in Rust using the Rocket framework. It defines a function called `index` that is triggered when a GET request is sent to the root path of the server. The function returns a string literal containing the text "Hello, world!" which is then sent back to the client.

Code parts:
- `#[get("/")]` - This is an attribute macro that tells Rocket to call the `index` function when a GET request is sent to the root path of the server.
- `fn index() -> &'static str` - This is the definition of the `index` function. It takes no arguments and returns a string literal.
- `"Hello, world!"` - This is the string literal that is returned by the `index` function.

## Helpful links
- [Rocket Documentation](https://rocket.rs/v0.4/guide/)
- [Rust Web Development Book](https://rustwasm.github.io/book/)
