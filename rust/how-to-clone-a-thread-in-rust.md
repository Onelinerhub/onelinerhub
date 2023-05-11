# How to clone a thread in Rust?
// plain

Cloning a thread in Rust is done using the `thread::spawn` method. This method takes a closure as an argument and returns a `JoinHandle` which can be used to join the thread.

```rust
let handle = thread::spawn(|| {
    println!("Hello from a thread!");
});
```

The code above will create a new thread and execute the closure passed to `thread::spawn`. The `handle` variable will contain a `JoinHandle` which can be used to join the thread.

## Code explanation


1. `thread::spawn` - method used to create a new thread
2. Closure - argument passed to `thread::spawn` which will be executed in the new thread
3. `JoinHandle` - returned by `thread::spawn` which can be used to join the thread

## Helpful links

- [Rust Docs - thread::spawn](https://doc.rust-lang.org/std/thread/fn.spawn.html)