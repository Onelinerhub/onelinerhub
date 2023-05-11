# How to create a thread in Rust?
// plain

Creating a thread in Rust is easy and straightforward. The `std::thread` module provides the `spawn` function to create a new thread.

```rust
use std::thread;

let handle = thread::spawn(|| {
    println!("Hello from a thread!");
});
```

The `spawn` function takes a closure as an argument and returns a `JoinHandle` which can be used to join the thread and wait for its completion.

1. `use std::thread`: imports the `thread` module from the standard library.
2. `thread::spawn`: creates a new thread and takes a closure as an argument.
3. `JoinHandle`: returned by the `spawn` function, can be used to join the thread and wait for its completion.

## Helpful links

- [std::thread](https://doc.rust-lang.org/std/thread/)
- [Rust Book - Threads](https://doc.rust-lang.org/book/ch16-02-threads.html)