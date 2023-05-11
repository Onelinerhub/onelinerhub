# How to use an async generator in Rust?
// plain

Async generators in Rust are a way to create an asynchronous iterator. They are created using the `async move` keyword and the `yield` keyword.

## Example code

```rust
async fn my_async_generator() -> impl Stream<Item = i32> {
    let mut i = 0;
    loop {
        yield i;
        i += 1;
    }
}
```

## Output example

```
0
1
2
3
...
```

## Code explanation

- `async fn`: This is used to declare an asynchronous function.
- `impl Stream<Item = i32>`: This is used to specify the type of the stream that will be returned.
- `let mut i = 0`: This is used to declare a mutable variable that will be used to store the current value of the iterator.
- `loop`: This is used to create an infinite loop that will be used to generate the values of the iterator.
- `yield i`: This is used to yield the current value of the iterator.
- `i += 1`: This is used to increment the current value of the iterator.

## Helpful links
- [Async Generators in Rust](https://rust-lang.github.io/async-book/07_generators/01_introduction.html)
- [Async Generators in Rust Tutorial](https://www.tutorialspoint.com/async_generators_in_rust)

group: rust-generators