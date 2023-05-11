# How to join a thread with a timeout in Rust?
// plain

Joining a thread with a timeout in Rust can be done using the `join_timeout` method of the `std::thread::Thread` type. This method takes a `Duration` as an argument and returns a `Result` indicating whether the thread was joined or not.

## Example code

```rust
use std::thread;
use std::time::Duration;

let handle = thread::spawn(|| {
    // thread code
});

let result = handle.join_timeout(Duration::from_secs(5));
```

## Output example

```
Ok(())
```

## Code explanation

- `thread::spawn`: creates a new thread and returns a handle to it
- `Duration::from_secs`: creates a `Duration` from a number of seconds
- `handle.join_timeout`: attempts to join the thread with a timeout, returns a `Result`
- `Ok(())`: indicates that the thread was successfully joined

## Helpful links
- [std::thread::Thread::join_timeout](https://doc.rust-lang.org/std/thread/struct.Thread.html#method.join_timeout)
- [std::time::Duration](https://doc.rust-lang.org/std/time/struct.Duration.html)