# How to yield a thread in Rust?
// plain

Threads can be yielded in Rust using the `yield_now()` function from the `std::thread` module.

```rust
use std::thread;

fn main() {
    thread::yield_now();
}
```

This code will yield the current thread, allowing other threads to run.

The code consists of:

1. `use std::thread;` - imports the `thread` module from the `std` crate.
2. `thread::yield_now();` - calls the `yield_now()` function from the `thread` module, yielding the current thread.

## Helpful links

- [std::thread::yield_now()](https://doc.rust-lang.org/std/thread/fn.yield_now.html)

group: rust-generators