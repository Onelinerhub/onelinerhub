# Rust library usage example
// plain

An example of using a Rust library is the [`reqwest`](https://docs.rs/reqwest/0.10.4/reqwest/) library for making HTTP requests.

```rust
use reqwest;

let res = reqwest::get("https://www.rust-lang.org")
    .await
    .unwrap();

assert!(res.status().is_success());
```

The code above uses the `reqwest` library to make an HTTP request to the Rust website. The `get` method is used to make the request, and the `await` keyword is used to wait for the response. The `unwrap` method is used to get the response from the request. Finally, the `status` method is used to check if the response was successful.

- `use reqwest`: imports the `reqwest` library
- `reqwest::get`: makes an HTTP request
- `await`: waits for the response
- `unwrap`: gets the response from the request
- `status`: checks if the response was successful

## Helpful links
- [`reqwest` Documentation](https://docs.rs/reqwest/0.10.4/reqwest/)

group: rust-examples