# How to format datetime in Rust
// plain

Rust provides a powerful library for formatting and manipulating dates and times called `chrono`. It is a feature-rich library that supports a wide range of operations.

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

The code above uses the `chrono` library to get the current date and time in UTC and then formats it using the `format` method. The format string `%Y-%m-%d %H:%M:%S` specifies the desired output format.

Parts of the code:
- `use chrono::{DateTime, Utc};`: imports the `DateTime` and `Utc` types from the `chrono` library.
- `let now: DateTime<Utc> = Utc::now();`: creates a `DateTime` object representing the current date and time in UTC.
- `println!("{}", now.format("%Y-%m-%d %H:%M:%S"));`: prints the `DateTime` object in the specified format.

## Helpful links
- [chrono documentation](https://docs.rs/chrono/0.4.11/chrono/)
- [chrono format strings](https://docs.rs/chrono/0.4.11/chrono/format/strftime/index.html)

group: rust-datetime