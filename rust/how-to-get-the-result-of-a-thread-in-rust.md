# How to get the result of a thread in Rust?
// plain

The result of a thread in Rust can be obtained by using the `join` method on the `JoinHandle` returned by the `spawn` method.

## Example code

```rust
use std::thread;

let handle = thread::spawn(|| {
    // thread code
});

let result = handle.join();
```

The `join` method will block the current thread until the thread associated with the `JoinHandle` terminates. The result of the thread is then returned by the `join` method.

## Code explanation

- `thread::spawn`: spawns a new thread and returns a `JoinHandle`
- `JoinHandle::join`: blocks the current thread until the thread associated with the `JoinHandle` terminates and returns the result of the thread

## Helpful links
- [`std::thread`](https://doc.rust-lang.org/std/thread/index.html)
- [`JoinHandle`](https://doc.rust-lang.org/std/thread/struct.JoinHandle.html)