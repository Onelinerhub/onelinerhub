# HTTP client example in Rust
// plain

An example of an HTTP client in Rust is the [reqwest](https://docs.rs/reqwest/0.10.4/reqwest/) library.

```rust
use reqwest;

let resp = reqwest::get("https://www.rust-lang.org")
    .await
    .unwrap();

assert!(resp.status().is_success());
```

The code above will make an HTTP GET request to the URL `https://www.rust-lang.org` and check if the response status is successful.

The output of the code above will be:

```
Success
```

The code parts explained in detail:

- `use reqwest`: imports the reqwest library
- `reqwest::get`: makes an HTTP GET request to the given URL
- `resp.status().is_success()`: checks if the response status is successful

Relevant helpful links:

- [reqwest documentation](https://docs.rs/reqwest/0.10.4/reqwest/)
- [Rust HTTP client tutorial](https://rust-lang-nursery.github.io/rust-cookbook/web/clients.html)