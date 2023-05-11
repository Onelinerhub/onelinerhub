# How to drop a thread in Rust?
// plain

Threads can be dropped in Rust using the `drop` method. This method takes ownership of the thread and terminates it.

## Example

```
let handle = thread::spawn(|| {
    println!("Hello from a thread!");
});

drop(handle);
```

The `drop` method takes ownership of the thread, which terminates it. In the example above, the thread is terminated after the `drop` method is called.

## Code explanation

- `let handle = thread::spawn(|| {`: creates a thread and stores it in the `handle` variable.
- `println!("Hello from a thread!");`: prints a message from the thread.
- `drop(handle);`: takes ownership of the thread and terminates it.

## Helpful links
- [Rust Documentation - Threads](https://doc.rust-lang.org/book/ch16-02-threads.html)