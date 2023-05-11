# Example of yield_now in Rust?
// plain

`yield_now` is a function in Rust that allows a thread to voluntarily give up its time slice and allow other threads to run. It is part of the `std::thread` module.

## Example code

```rust
use std::thread;

fn main() {
    thread::yield_now();
}
```

This code will cause the current thread to give up its time slice and allow other threads to run.

## Code explanation

- `use std::thread`: This imports the `thread` module from the `std` library.
- `thread::yield_now()`: This is the function call that causes the current thread to give up its time slice.

## Helpful links
- [Rust Documentation - std::thread](https://doc.rust-lang.org/std/thread/)

group: rust-generators