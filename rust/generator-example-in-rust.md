# Generator example in Rust
// plain

Generators are a powerful tool in Rust for creating iterators. Generators are functions that can be paused and resumed, allowing them to yield values one at a time.

## Example code

```rust
fn generator() -> impl Iterator<Item = i32> {
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

- `fn generator() -> impl Iterator<Item = i32>`: This declares a function named `generator` that returns an iterator of type `i32`.
- `let mut i = 0`: This declares a mutable variable `i` and initializes it to `0`.
- `yield i`: This pauses the function and returns the value of `i`.
- `i += 1`: This increments `i` by `1`.
- `loop { ... }`: This creates an infinite loop that will keep yielding values until it is manually stopped.

## Helpful links
- [Rust Generators](https://doc.rust-lang.org/stable/book/ch19-06-macros.html#generators)
- [Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-generators