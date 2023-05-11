# How to catch a panic in a Rust thread?
// plain

Catching a panic in a Rust thread can be done using the `catch_unwind` function. This function will return a `Result` type, with `Ok` if the thread completed successfully, and `Err` if the thread panicked.

```rust
use std::thread;

let result = thread::spawn(|| {
    panic!("Panic!");
}).join();

let unwind_result = result.unwrap_or_else(|_| {
    thread::catch_unwind(|| {
        println!("Caught panic!");
    })
});

match unwind_result {
    Ok(_) => println!("Thread completed successfully"),
    Err(_) => println!("Thread panicked"),
}
```

## Output example

```
Caught panic!
Thread panicked
```

## Code explanation

- `thread::spawn`: creates a new thread and returns a `JoinHandle`
- `panic!`: macro to cause a panic
- `join`: method on `JoinHandle` to wait for the thread to finish
- `unwrap_or_else`: method on `Result` to handle the `Err` case
- `catch_unwind`: function to catch a panic in a thread
- `match`: to handle the `Result` returned by `catch_unwind`

## Helpful links
- [std::thread::catch_unwind](https://doc.rust-lang.org/std/thread/fn.catch_unwind.html)