# How to add second to time in Rust
// plain

Adding seconds to a time in Rust can be done using the `add_secs` method of the `std::time::SystemTime` struct. This method takes a `u64` representing the number of seconds to add to the time.

## Example code

```rust
use std::time::{SystemTime, UNIX_EPOCH};

let start = SystemTime::now();
let ten_seconds_later = start.add_secs(10);
```

## Output example

```
ten_seconds_later = SystemTime { tv_sec: 1599450090, tv_nsec: 845005050 }
```

## Code explanation

- `use std::time::{SystemTime, UNIX_EPOCH};`: imports the `SystemTime` and `UNIX_EPOCH` structs from the `std::time` module.
- `let start = SystemTime::now();`: creates a `SystemTime` object representing the current time.
- `let ten_seconds_later = start.add_secs(10);`: adds 10 seconds to the `start` `SystemTime` object and stores the result in the `ten_seconds_later` variable.

## Helpful links
- [std::time::SystemTime](https://doc.rust-lang.org/std/time/struct.SystemTime.html)

group: rust-datetime