# How to detach a thread in Rust?
// plain

Threads in Rust can be detached using the `detach()` method on a `JoinHandle` instance. This method will return a `Result<()>` indicating whether the thread was successfully detached.

```rust
use std::thread;

let handle = thread::spawn(|| {
    println!("Hello from a thread!");
});

handle.detach();
```

The code above will create a new thread and detach it immediately.

1. `use std::thread;` - imports the `thread` module from the standard library.
2. `let handle = thread::spawn(|| {` - creates a new thread and stores a `JoinHandle` instance in the `handle` variable.
3. `println!("Hello from a thread!");` - prints a message from the thread.
4. `handle.detach();` - detaches the thread.

## Helpful links

- [Rust Documentation - Threads](https://doc.rust-lang.org/std/thread/index.html)
- [Rust Documentation - JoinHandle](https://doc.rust-lang.org/std/thread/struct.JoinHandle.html)