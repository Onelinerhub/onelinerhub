# How to convert datetime to timestamp in Rust
// plain

Converting a `datetime` to a `timestamp` in Rust is a simple process. The `chrono` crate provides a `Timestamp` type which can be used to convert a `DateTime` to a `timestamp`.

## Example code

```rust
use chrono::{DateTime, Timestamp};

let dt = DateTime::parse_from_rfc3339("2020-01-01T12:00:00+00:00").unwrap();
let ts = Timestamp::from_datetime(&dt);
```

## Output example

```
1577836800
```

The code above:
- `use chrono::{DateTime, Timestamp};`: imports the `DateTime` and `Timestamp` types from the `chrono` crate.
- `let dt = DateTime::parse_from_rfc3339("2020-01-01T12:00:00+00:00").unwrap();`: parses a `DateTime` from an RFC 3339 string.
- `let ts = Timestamp::from_datetime(&dt);`: converts the `DateTime` to a `timestamp`.

## Helpful links
- [chrono crate](https://crates.io/crates/chrono)
- [RFC 3339](https://tools.ietf.org/html/rfc3339)

group: rust-datetime