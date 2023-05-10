# How do I share a variable between threads in Rust?
// plain

Sharing variables between threads in Rust can be done using the `Arc` type from the `std::sync` module. `Arc` stands for atomic reference counting and allows multiple threads to access the same data.

```rust
use std::sync::Arc;

let data = Arc::new(vec![1, 2, 3]);

let thread_1 = std::thread::spawn(move || {
    let data = data.clone();
    println!("Thread 1 data: {:?}", data);
});

let thread_2 = std::thread::spawn(move || {
    let data = data.clone();
    println!("Thread 2 data: {:?}", data);
});

thread_1.join().unwrap();
thread_2.join().unwrap();
```

## Output example

```
Thread 1 data: [1, 2, 3]
Thread 2 data: [1, 2, 3]
```

The code above creates a vector of numbers and stores it in an `Arc` type. Then two threads are spawned, each of which clones the `Arc` and prints the data.

## Code explanation


1. `let data = Arc::new(vec![1, 2, 3]);` - creates a vector of numbers and stores it in an `Arc` type.
2. `let thread_1 = std::thread::spawn(move || {` - spawns a thread.
3. `let data = data.clone();` - clones the `Arc` so that the thread can access the data.
4. `println!("Thread 1 data: {:?}", data);` - prints the data.

## Helpful links

- [std::sync::Arc](https://doc.rust-lang.org/std/sync/struct.Arc.html)

group: rust-variables