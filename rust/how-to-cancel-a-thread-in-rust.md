# How to cancel a thread in Rust?
// plain

Threads can be cancelled in Rust using the `std::thread::Thread::cancel` method. This method takes no arguments and returns a `Result<()>` indicating whether the thread was successfully cancelled.

## Example

```rust
let handle = std::thread::spawn(|| {
    println!("Hello from thread!");
});

let result = handle.cancel();

match result {
    Ok(_) => println!("Thread cancelled successfully"),
    Err(_) => println!("Thread could not be cancelled"),
}
```
## Output example

```
Thread cancelled successfully
```

The `Thread::cancel` method works by sending a signal to the thread, which can be handled by the thread itself. If the thread does not handle the signal, it will be terminated.

## Code explanation

- `std::thread::Thread::cancel`: Method to cancel a thread
- `Result<()>`: Return type of the `Thread::cancel` method, indicating whether the thread was successfully cancelled
- `handle.cancel()`: Call the `Thread::cancel` method on the thread handle
- `match`: Check the result of the `Thread::cancel` call

## Helpful links
- [std::thread::Thread::cancel](https://doc.rust-lang.org/std/thread/struct.Thread.html#method.cancel)