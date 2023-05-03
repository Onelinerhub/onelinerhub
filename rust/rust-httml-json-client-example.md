# Rust HTTP JSON client example
// plain

A Rust HTTP JSON client example is a program that uses the Rust programming language to send an HTTP request and receive a JSON response.

```rust
extern crate reqwest;

fn main() {
    let response = reqwest::get("https://www.example.com/data.json")
        .expect("Failed to send request");

    let json: serde_json::Value = response.json()
        .expect("Failed to parse JSON response");

    println!("{}", json);
}
```

```
{
  "name": "John Doe",
  "age": 42
}
```

Code parts explained in detail:

- `extern crate reqwest`: This line imports the reqwest library, which provides an API for making HTTP requests.
- `reqwest::get("https://www.example.com/data.json")`: This line sends an HTTP GET request to the specified URL.
- `response.json()`: This line parses the response body as JSON.
- `println!("{}", json)`: This line prints the parsed JSON to the console.

Relevant helpful links:

- [reqwest documentation](https://docs.rs/reqwest/0.10.4/reqwest/)
- [serde_json documentation](https://docs.serde.rs/serde_json/)
