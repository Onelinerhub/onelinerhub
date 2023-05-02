# How to share closure between threads in Rust
// plain

In Rust, closures can be shared between threads by using the `Arc` type from the `std::sync` module. This type allows multiple threads to access the same data without the need for explicit locking. To share a closure between threads, it must first be wrapped in an `Arc` type. Then, the `Arc` type can be passed to the thread that needs access to the closure. An example of this is shown below:
```rust
use std::sync::Arc;

let closure = Arc::new(|| println!("Hello from thread!"));

let handle = std::thread::spawn(move || {
    closure();
});

handle.join().unwrap();
```
In this example, the closure is first wrapped in an `Arc` type. Then, the `Arc` type is passed to the thread that needs access to the closure. The thread can then access the closure by calling the `closure()` method.

The `Arc` type is a type of reference-counted pointer, which allows multiple threads to access the same data without the need for explicit locking. This makes it an ideal choice for sharing closures between threads.

## Helpful links
- [std::sync::Arc](https://doc.rust-lang.org/std/sync/struct.Arc.html)
- [std::thread](https://doc.rust-lang.org/std/thread/index.html)
- [Closures in Rust](https://doc.rust-lang.org/book/ch13-01-closures.html)