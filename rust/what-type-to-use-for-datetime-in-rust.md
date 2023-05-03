# What type to use for datetime in Rust
// plain

The `chrono` crate is the most popular crate for working with dates and times in Rust. It provides a rich set of types and functions for working with dates, times, and timezones.

## Example code

```rust
use chrono::{DateTime, Utc};

let now: DateTime<Utc> = Utc::now();
println!("{}", now);
```

## Output example

```
2020-09-17T17:45:02.945Z
```

The code above uses the `DateTime` type from the `chrono` crate to get the current time in UTC. The `DateTime` type is a generic type that takes a `TimeZone` as a parameter. In this case, we used the `Utc` type, which represents the UTC timezone.

The `DateTime` type provides a number of methods for working with dates and times, such as `date`, `time`, `timestamp`, `format`, and more.

## Helpful links

- [chrono crate](https://crates.io/crates/chrono)
- [chrono documentation](https://docs.rs/chrono/)

group: rust-datetime