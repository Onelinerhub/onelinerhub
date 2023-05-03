# How to get current date in Rust
// plain

Getting the current date in Rust is easy with the `chrono` crate.

```rust
use chrono::{Local, DateTime};

let now: DateTime<Local> = Local::now();
println!("{}", now);
```

The code above will print the current date and time in the local timezone.

## Code explanation


- `use chrono::{Local, DateTime};` - imports the `Local` and `DateTime` types from the `chrono` crate
- `let now: DateTime<Local> = Local::now();` - creates a `DateTime` object with the current date and time in the local timezone
- `println!("{}", now);` - prints the `DateTime` object

## Helpful links

- [chrono crate documentation](https://docs.rs/chrono/0.4.11/chrono/)

group: rust-datetime