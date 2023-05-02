# Example of closure that returns future in Rust
// plain

A closure in Rust that returns a future can be written as follows:
```rust
fn closure_returning_future() -> impl Future<Output = i32> {
    async {
        // Do some asynchronous work here
        42
    }
}
```
This closure returns a future that resolves to the value `42`. The `async` block is used to define the asynchronous work that the future will perform. The `impl Future<Output = i32>` syntax is used to specify that the closure returns a future that resolves to the type `i32`.

## Helpful links
- [Rust Closures](https://doc.rust-lang.org/book/ch13-01-closures.html)
- [Rust Futures](https://rust-lang.github.io/async-book/01_getting_started/02_why_futures.html)
- [Rust Async/Await](https://doc.rust-lang.org/book/ch13-02-async-await.html)