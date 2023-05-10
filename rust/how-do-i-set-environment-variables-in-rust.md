# How do I set environment variables in Rust?
// plain

Environment variables can be set in Rust using the `std::env::set_var` function.

```rust
use std::env;

fn main() {
    env::set_var("MY_VAR", "my_value");
}
```

This code sets the environment variable `MY_VAR` to the value `my_value`.

## Code explanation


- `use std::env;`: imports the `env` module from the `std` library.
- `env::set_var("MY_VAR", "my_value");`: sets the environment variable `MY_VAR` to the value `my_value`.

## Helpful links

- [std::env::set_var](https://doc.rust-lang.org/std/env/fn.set_var.html)

group: rust-variables