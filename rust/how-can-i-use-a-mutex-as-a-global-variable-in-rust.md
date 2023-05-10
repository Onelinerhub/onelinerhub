# How can I use a mutex as a global variable in Rust?
// plain

A mutex can be used as a global variable in Rust by creating a `static` mutex and then using the `lazy_static` crate to initialize it.

```rust
use lazy_static::lazy_static;
use std::sync::Mutex;

lazy_static! {
    static ref MUTEX: Mutex<u32> = Mutex::new(0);
}
```

The code above creates a `static` mutex called `MUTEX` and initializes it with the value `0`.

## Code explanation


1. `use lazy_static::lazy_static;` - imports the `lazy_static` crate which provides the `lazy_static!` macro.
2. `use std::sync::Mutex;` - imports the `Mutex` type from the `std::sync` module.
3. `lazy_static! {` - starts the `lazy_static!` macro which is used to create a `static` mutex.
4. `static ref MUTEX: Mutex<u32> = Mutex::new(0);` - creates a `static` mutex called `MUTEX` and initializes it with the value `0`.
5. `}` - ends the `lazy_static!` macro.

## Helpful links

- [lazy_static](https://docs.rs/lazy_static/1.4.0/lazy_static/)
- [Mutex](https://doc.rust-lang.org/std/sync/struct.Mutex.html)

group: rust-variables