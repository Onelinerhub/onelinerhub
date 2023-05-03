# How to format date in Rust
// plain

Rust provides a number of ways to format dates.

The most common way is to use the `chrono` crate. This crate provides a number of functions to format dates and times.

## Example code

```rust
use chrono::{DateTime, Utc};

let now: DateTime<Utc> = Utc::now();
let formatted_date = now.format("%Y-%m-%d %H:%M:%S").to_string();

println!("Formatted date: {}", formatted_date);
```

## Output example

```
Formatted date: 2020-09-17 15:45:12
```

The code above uses the `chrono` crate to get the current date and time in UTC and then formats it using the `format` function. The format string `%Y-%m-%d %H:%M:%S` specifies the format of the output.

## Code explanation

- `use chrono::{DateTime, Utc};`: imports the `DateTime` and `Utc` types from the `chrono` crate.
- `let now: DateTime<Utc> = Utc::now();`: gets the current date and time in UTC.
- `let formatted_date = now.format("%Y-%m-%d %H:%M:%S").to_string();`: formats the date and time using the `format` function and converts it to a string.
- `println!("Formatted date: {}", formatted_date);`: prints the formatted date.

## Helpful links
- [chrono crate](https://crates.io/crates/chrono)
- [chrono documentation](https://docs.rs/chrono/0.4.11/chrono/)

group: rust-datetime