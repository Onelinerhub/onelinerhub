# How to format datetime string in Rust
// plain

Formatting a datetime string in Rust can be done using the `chrono` crate. This crate provides a `DateTime` type which can be used to parse and format datetime strings.

Below is an example of how to format a datetime string in Rust:

```rust
use chrono::{DateTime, Utc};

let datetime = Utc::now();
let formatted_datetime = datetime.format("%Y-%m-%d %H:%M:%S").to_string();

println!("Formatted datetime: {}", formatted_datetime);
```

### Output
Formatted datetime: 2020-09-17 15:45:12

Explanation:
1. The `chrono` crate is imported to use the `DateTime` type.
2. The `Utc::now()` method is used to get the current datetime in UTC.
3. The `format()` method is used to format the datetime string according to the specified format string.
4. The `to_string()` method is used to convert the formatted datetime string to a `String` type.
5. The formatted datetime string is printed using the `println!` macro.

## Helpful links:
1. https://docs.rs/chrono/0.4.11/chrono/
2. https://docs.rs/chrono/0.4.11/chrono/format/strftime/index.html