# How to borrow a thread in Rust?
// plain

Threads in Rust are created using the `std::thread::spawn` function. This function takes a closure as an argument and returns a `std::thread::JoinHandle` which can be used to join the thread.

```rust
use std::thread;

let handle = thread::spawn(|| {
    println!("Hello from a thread!");
});
```

The code above creates a thread which prints "Hello from a thread!" when it is executed.

1. `use std::thread`: imports the `thread` module from the `std` crate.
2. `thread::spawn`: creates a thread and returns a `JoinHandle` which can be used to join the thread.
3. `|| { ... }`: a closure which is passed to the `spawn` function. This closure is executed in the thread.
4. `handle`: a `JoinHandle` which can be used to join the thread.

## Helpful links

- [std::thread](https://doc.rust-lang.org/std/thread/index.html)
- [Rust Book - Threads](https://doc.rust-lang.org/book/ch16-02-threads.html)