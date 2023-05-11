# How to delay a thread in Rust?
// plain

Threads can be delayed in Rust using the `std::thread::sleep` function. This function takes a `std::time::Duration` as an argument, which can be created from a number of seconds.

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::sleep(Duration::from_secs(5));
    println!("5 seconds have passed");
}
```

## Output example

```
5 seconds have passed
```

The code above will delay the thread for 5 seconds before printing the message.

## Code explanation

- `use std::thread;` - imports the `thread` module from the `std` library
- `use std::time::Duration;` - imports the `Duration` type from the `std::time` module
- `thread::sleep(Duration::from_secs(5));` - calls the `sleep` function from the `thread` module, passing a `Duration` created from 5 seconds
- `println!("5 seconds have passed");` - prints the message after the thread has been delayed

## Helpful links
- [std::thread::sleep](https://doc.rust-lang.org/std/thread/fn.sleep.html)
- [std::time::Duration](https://doc.rust-lang.org/std/time/struct.Duration.html)