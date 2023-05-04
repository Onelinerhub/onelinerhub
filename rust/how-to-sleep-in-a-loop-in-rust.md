# How to sleep in a loop in Rust
// plain

Sleeping in a loop in Rust can be done using the `std::thread::sleep` function. This function takes a `std::time::Duration` as an argument, which can be used to specify the amount of time to sleep.

## Example code

```rust
use std::thread;
use std::time::Duration;

loop {
    thread::sleep(Duration::from_secs(1));
    println!("Sleeping for 1 second");
}
```

## Output example

```
Sleeping for 1 second
Sleeping for 1 second
Sleeping for 1 second
...
```

## Code explanation


1. `use std::thread;`: This imports the `thread` module from the `std` crate, which contains the `sleep` function.
2. `use std::time::Duration;`: This imports the `Duration` type from the `std::time` module, which is used to specify the amount of time to sleep.
3. `thread::sleep(Duration::from_secs(1));`: This calls the `sleep` function, passing in a `Duration` representing 1 second.

## Helpful links

- [std::thread::sleep](https://doc.rust-lang.org/std/thread/fn.sleep.html)
- [std::time::Duration](https://doc.rust-lang.org/std/time/struct.Duration.html)

group: rust-loops