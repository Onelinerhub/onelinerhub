# What is an environment variable in Rust?
// plain

An environment variable in Rust is a global variable that can be accessed from any part of the program. It is used to store information that can be used by multiple parts of the program. Environment variables are set using the `std::env::set_var` function.

## Example code

```rust
use std::env;

fn main() {
    env::set_var("MY_VAR", "my_value");
    println!("MY_VAR is set to: {}", env::var("MY_VAR").unwrap());
}
```

## Output example

```
MY_VAR is set to: my_value
```

## Code explanation


1. `use std::env;`: This imports the `env` module from the `std` library, which provides functions for setting and getting environment variables.
2. `env::set_var("MY_VAR", "my_value");`: This sets the environment variable `MY_VAR` to the value `my_value`.
3. `env::var("MY_VAR").unwrap();`: This retrieves the value of the environment variable `MY_VAR`. The `unwrap()` function is used to convert the `Option` type returned by `env::var` into a `String`.

## Helpful links

- [std::env](https://doc.rust-lang.org/std/env/index.html)

group: rust-variables