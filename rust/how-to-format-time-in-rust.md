# How to format time in Rust
// plain

Rust provides a number of ways to format time.

The most common way is to use the `chrono` crate. This crate provides a number of types and functions to work with dates and times.

## Example code

```rust
use chrono::{DateTime, Utc};

let now: DateTime<Utc> = Utc::now();
println!("{}", now.format("%Y-%m-%d %H:%M:%S"));
```

## Output example

```
2020-09-17 11:45:00
```

The code above uses the `chrono` crate to get the current time in UTC and then formats it using the `format` function. The format string `%Y-%m-%d %H:%M:%S` specifies the format of the output.

The `chrono` crate also provides other types and functions to work with dates and times, such as `DateTime` and `Duration`.

## Helpful links
- [chrono crate](https://crates.io/crates/chrono)
- [chrono documentation](https://docs.rs/chrono/0.4.11/chrono/)

group: rust-datetime