# How to sleep in Rust
// plain

Sleeping in Rust is done using the `std::thread::sleep` function. This function takes a `Duration` as an argument, which is a type representing a span of time.

```rust
use std::thread::sleep;
use std::time::Duration;

// Sleep for 2 seconds
sleep(Duration::from_secs(2));
```

The code above will sleep for 2 seconds.

## Code explanation


1. `use std::thread::sleep`: imports the `sleep` function from the `std::thread` module.
2. `use std::time::Duration`: imports the `Duration` type from the `std::time` module.
3. `Duration::from_secs(2)`: creates a `Duration` representing 2 seconds.
4. `sleep(Duration::from_secs(2))`: calls the `sleep` function with the `Duration` representing 2 seconds.

## Helpful links

- [std::thread::sleep](https://doc.rust-lang.org/std/thread/fn.sleep.html)
- [std::time::Duration](https://doc.rust-lang.org/std/time/struct.Duration.html)

group: rust-datetime