# How to exit a thread in Rust?
// plain

Threads in Rust can be exited using the `std::thread::Thread::join()` method. This method will block the current thread until the thread it is called on has finished executing.

```rust
use std::thread;

let handle = thread::spawn(|| {
    println!("Hello from a thread!");
});

handle.join().unwrap();
```

The code above will create a new thread and execute the closure passed to `thread::spawn()`. The `handle.join().unwrap()` will block the current thread until the thread created by `thread::spawn()` has finished executing.

- `thread::spawn()`: creates a new thread and executes the closure passed to it
- `handle.join()`: blocks the current thread until the thread created by `thread::spawn()` has finished executing
- `unwrap()`: returns the result of the thread, or panics if the thread panicked

## Helpful links
- [std::thread::Thread::join()](https://doc.rust-lang.org/std/thread/struct.Thread.html#method.join)