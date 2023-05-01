# How to format date string in Rust
// plain

Formatting date strings in Rust can be done using the `chrono` crate. This crate provides a wide range of formatting options for dates and times.

Below is an example of how to format a date string in Rust:

```rust
use chrono::{DateTime, Utc};

let now: DateTime<Utc> = Utc::now();
let formatted_date = now.format("%Y-%m-%d %H:%M:%S").to_string();

println!("Formatted date: {}", formatted_date);
```

### Output
Formatted date: 2020-09-17 13:45:12

Explanation:
1. The `chrono` crate is imported with `use chrono::{DateTime, Utc};`
2. The current date and time is obtained with `let now: DateTime<Utc> = Utc::now();`
3. The date is formatted with `let formatted_date = now.format("%Y-%m-%d %H:%M:%S").to_string();`
4. The formatted date is printed with `println!("Formatted date: {}", formatted_date);`

## Helpful links:
1. https://docs.rs/chrono/0.4.11/chrono/
2. https://docs.rs/chrono/0.4.11/chrono/format/strftime/index.html