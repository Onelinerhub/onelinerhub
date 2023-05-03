# How to get time from milliseconds in Rust
// plain

To get time from milliseconds in Rust, you can use the `Duration` struct from the `std::time` module. This struct takes a `u64` value representing the number of milliseconds and returns a `Duration` object.

## Example code

```rust
use std::time::Duration;

let milliseconds = 1000;
let duration = Duration::from_millis(milliseconds);
```

## Output example

```
Duration {
    secs: 1,
    nanos: 0
}
```

## Code explanation

- `use std::time::Duration`: imports the `Duration` struct from the `std::time` module.
- `let milliseconds = 1000`: creates a variable `milliseconds` with the value of 1000.
- `let duration = Duration::from_millis(milliseconds)`: creates a `Duration` object from the `milliseconds` variable.

## Helpful links
- [std::time::Duration](https://doc.rust-lang.org/std/time/struct.Duration.html)

group: rust-datetime