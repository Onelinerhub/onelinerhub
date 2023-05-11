# How to use a callback with a Rust thread?
// plain

Using a callback with a Rust thread is a great way to ensure that a task is completed before continuing with the main thread. To do this, you can use the `thread::spawn` function to create a new thread and pass a closure as an argument. The closure will be executed in the new thread and can be used to call a callback when the task is finished.

## Example code

```rust
use std::thread;

fn main() {
    let handle = thread::spawn(|| {
        // Do some work
        // Call the callback when done
    });

    // Wait for the thread to finish
    handle.join().unwrap();
}
```

## Output example

```
No output
```

## Code explanation

- `thread::spawn`: This function creates a new thread and takes a closure as an argument. The closure will be executed in the new thread.
- `handle.join().unwrap()`: This line waits for the thread to finish before continuing with the main thread.

## Helpful links
- [Rust thread documentation](https://doc.rust-lang.org/std/thread/index.html)