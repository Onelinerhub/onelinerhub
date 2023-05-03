# Using now to get current time in Rust
// plain

The `now` function from the `chrono` crate can be used to get the current time in Rust.

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

The code above imports the `DateTime` and `Utc` types from the `chrono` crate, and then uses the `Utc::now()` function to get the current time in UTC. The result is stored in a `DateTime<Utc>` type, which can then be printed using the `println!` macro.

## Code explanation

- `use chrono::{DateTime, Utc};`: imports the `DateTime` and `Utc` types from the `chrono` crate.
- `let now: DateTime<Utc> = Utc::now();`: uses the `Utc::now()` function to get the current time in UTC, and stores it in a `DateTime<Utc>` type.
- `println!("{}", now);`: prints the `DateTime<Utc>` type using the `println!` macro.

## Helpful links
- [chrono crate documentation](https://docs.rs/chrono/0.4.11/chrono/)

group: rust-datetime