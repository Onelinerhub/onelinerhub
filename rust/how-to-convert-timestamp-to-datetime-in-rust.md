# How to convert timestamp to datetime in Rust
// plain

Converting a timestamp to a datetime in Rust can be done using the `chrono` crate.

## Example code

```rust
use chrono::{DateTime, Utc};

let timestamp = 1589717600;
let datetime: DateTime<Utc> = Utc.timestamp(timestamp, 0);
println!("{}", datetime);
```

## Output example

```
2020-05-17T00:00:00Z
```

The code above uses the `chrono` crate to convert a timestamp to a datetime. The `Utc` type is used to represent a datetime in the UTC timezone. The `timestamp` method is then used to convert the timestamp to a `DateTime` type. Finally, the `println!` macro is used to print the datetime.

Parts of the code:
- `use chrono::{DateTime, Utc};`: imports the `DateTime` and `Utc` types from the `chrono` crate.
- `let timestamp = 1589717600;`: creates a variable to store the timestamp.
- `let datetime: DateTime<Utc> = Utc.timestamp(timestamp, 0);`: converts the timestamp to a `DateTime` type in the UTC timezone.
- `println!("{}", datetime);`: prints the datetime.

## Helpful links
- [chrono crate](https://crates.io/crates/chrono)

group: rust-datetime