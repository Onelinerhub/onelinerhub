# How to check if a thread is finished in Rust?
// plain

To check if a thread is finished in Rust, you can use the `join()` method on the thread handle. This will block the current thread until the thread handle is finished.

## Example code

```rust
let handle = thread::spawn(|| {
    println!("Hello from a thread!");
});

handle.join().expect("The thread being joined has panicked");
```

## Output example

```
Hello from a thread!
```

The code above creates a thread handle with the `thread::spawn()` method, and then calls the `join()` method on the handle. This will block the current thread until the thread handle is finished. The `expect()` method is used to handle any panics that may occur in the thread.

## Helpful links

- [Rust Docs - Threads](https://doc.rust-lang.org/std/thread/index.html)