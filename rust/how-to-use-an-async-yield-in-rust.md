# How to use an async yield in Rust?
// plain

Async/await is a Rust language feature that allows you to write asynchronous code in a synchronous-like style. It is based on the Future trait, which represents a value that will be available at some point in the future.

```rust
async fn foo() {
    let future = async {
        // Do some work
    };
    let result = await!(future);
    // Do something with the result
}
```

The code above shows a basic example of using async/await. The `async` keyword is used to mark a function as asynchronous, and the `await!` macro is used to wait for a Future to resolve.

## Code explanation


- `async` keyword: marks a function as asynchronous
- `let future = async { ... }`: creates a Future that will be resolved at some point in the future
- `let result = await!(future)`: waits for the Future to resolve and stores the result in the `result` variable

## Helpful links

- [Rust Async Book](https://rust-lang.github.io/async-book/)
- [Rust Async Tutorial](https://rust-lang.github.io/async-book/01_getting_started/01_chapter.html)

group: rust-generators