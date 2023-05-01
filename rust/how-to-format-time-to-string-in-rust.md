# How to format time to string in Rust
// plain

Formatting time to string in Rust can be done using the `chrono` crate. This crate provides a `format` method which takes a `DateTime` object and a formatting string as parameters and returns a `String` object.

## Code example:
```
use chrono::{DateTime, Utc};

let now: DateTime<Utc> = Utc::now();
let formatted_time = now.format("%Y-%m-%d %H:%M:%S").to_string();
```

### Output
`formatted_time` will contain a string in the format `YYYY-MM-DD HH:MM:SS`

## Explanation of code parts:
1. `use chrono::{DateTime, Utc};` - This imports the `DateTime` and `Utc` types from the `chrono` crate.
2. `let now: DateTime<Utc> = Utc::now();` - This creates a `DateTime` object with the current time in UTC.
3. `let formatted_time = now.format("%Y-%m-%d %H:%M:%S").to_string();` - This uses the `format` method to format the `DateTime` object to a string with the specified format and then converts it to a `String` object.

## Helpful links:
1. [chrono crate documentation](https://docs.rs/chrono/0.4.11/chrono/)
2. [DateTime formatting documentation](https://docs.rs/chrono/0.4.11/chrono/format/strftime/index.html)