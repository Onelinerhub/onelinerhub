# How to loop every second in Rust
// plain

Looping every second in Rust can be done using the `std::thread::sleep` function. This function takes a `Duration` as an argument, which can be used to specify the amount of time to sleep.

## Example code

```rust
use std::thread::sleep;
use std::time::Duration;

for i in 0..5 {
    println!("Looping every second: {}", i);
    sleep(Duration::from_secs(1));
}
```

## Output example

```
Looping every second: 0
Looping every second: 1
Looping every second: 2
Looping every second: 3
Looping every second: 4
```

## Code explanation

- `use std::thread::sleep`: imports the `sleep` function from the `std::thread` module.
- `use std::time::Duration`: imports the `Duration` type from the `std::time` module.
- `Duration::from_secs(1)`: creates a `Duration` representing 1 second.
- `sleep(Duration::from_secs(1))`: pauses the program for 1 second.

## Helpful links
- [std::thread::sleep](https://doc.rust-lang.org/std/thread/fn.sleep.html)
- [std::time::Duration](https://doc.rust-lang.org/std/time/struct.Duration.html)

group: rust-loops