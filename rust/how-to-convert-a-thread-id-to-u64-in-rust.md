# How to convert a thread ID to u64 in Rust?
// plain

To convert a thread ID to u64 in Rust, you can use the `thread::id()` method. This method returns a `ThreadId` struct, which can be converted to a u64 using the `as_u64()` method.

## Example code

```
let thread_id = std::thread::current().id();
let u64_id = thread_id.as_u64();
```

## Output example

```
u64_id = 123456789
```

## Code explanation

- `std::thread::current()`: This method returns the current thread.
- `.id()`: This method returns the `ThreadId` struct of the current thread.
- `.as_u64()`: This method converts the `ThreadId` struct to a u64.

## Helpful links
- [std::thread::current()](https://doc.rust-lang.org/std/thread/fn.current.html)
- [std::thread::ThreadId](https://doc.rust-lang.org/std/thread/struct.ThreadId.html)