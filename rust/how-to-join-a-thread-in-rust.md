# How to join a thread in Rust?
// plain

Joining a thread in Rust is done using the `join()` method. This method blocks the current thread until the thread it is called on has completed its execution.

## Example

```rust
use std::thread;

let handle = thread::spawn(|| {
    println!("Hello from a thread!");
});

handle.join().unwrap();
```

## Output example

```
Hello from a thread!
```

The code above creates a new thread using the `thread::spawn()` method and stores the thread handle in the `handle` variable. The `join()` method is then called on the `handle` variable, which blocks the current thread until the thread it is called on has completed its execution.

Parts of the code:
- `thread::spawn()`: creates a new thread and returns a handle to it
- `handle.join()`: blocks the current thread until the thread it is called on has completed its execution

## Helpful links
- [Rust Documentation - Threads](https://doc.rust-lang.org/book/ch16-02-threads.html)
- [Rust Documentation - Threads - Joining Threads](https://doc.rust-lang.org/book/ch16-02-threads.html#joining-threads)