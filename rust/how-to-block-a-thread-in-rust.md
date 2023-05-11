# How to block a thread in Rust?
// plain

Threads can be blocked in Rust using the `thread::park()` function. This function will block the current thread until it is unparked.

```rust
use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        println!("Thread is running");
    });

    thread::park();

    println!("Thread is blocked");
}
```

## Output example

```
Thread is running
Thread is blocked
```

The code above creates a new thread using `thread::spawn()` and then blocks it using `thread::park()`. The thread will remain blocked until it is unparked.

- `thread::spawn()`: creates a new thread
- `thread::park()`: blocks the current thread

## Helpful links
- [Rust Docs - Threads](https://doc.rust-lang.org/std/thread/index.html)