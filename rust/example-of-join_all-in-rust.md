# Example of join_all in Rust
// plain

The `join_all` method in Rust is used to wait for multiple threads to finish executing before continuing with the main thread. It takes a vector of `JoinHandle`s as an argument and returns a `Result<Vec<T>, E>` where `T` is the type of the return value of the threads and `E` is the type of the error.

## Code example:

```rust
use std::thread;

fn main() {
    let handles: Vec<_> = (0..10).map(|_| {
        thread::spawn(|| {
            // thread code
        })
    }).collect();

    let results = thread::join_all(handles).unwrap();
    // do something with the results
}
```

### Output

No output.

## Explanation of code parts:

1. `use std::thread;`: This imports the `thread` module from the standard library, which provides functions for creating and managing threads.

2. `let handles: Vec<_> = (0..10).map(|_| {`: This creates a vector of `JoinHandle`s, which are used to manage the threads. The `map` function is used to create 10 threads, each of which will execute the code in the closure.

3. `thread::spawn(|| {`: This creates a new thread and passes the closure to it. The closure contains the code that will be executed by the thread.

4. `let results = thread::join_all(handles).unwrap();`: This waits for all of the threads to finish executing and returns a `Result<Vec<T>, E>` where `T` is the type of the return value of the threads and `E` is the type of the error. The `unwrap` method is used to get the `Vec<T>` from the `Result`.

5. `// do something with the results`: This is where you can do something with the results of the threads.

## Helpful links:

1. [Rust Documentation - Threads](https://doc.rust-lang.org/std/thread/)
2. [Rust Documentation - JoinHandle](https://doc.rust-lang.org/std/thread/struct.JoinHandle.html)