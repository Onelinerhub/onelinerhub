# Yield generator in Rust
// plain

Yield generator in Rust is a feature that allows a function to pause its execution and return a value to the caller. It is similar to a generator in Python, but with a few differences.

## Example code

```
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


1. `fn generator() -> impl Iterator<Item = i32>`: This declares a function named `generator` that returns an iterator of type `i32`.

2. `let mut i = 0`: This declares a mutable variable `i` and initializes it to `0`.

3. `yield i`: This pauses the execution of the function and returns the value of `i` to the caller.

4. `i += 1`: This increments the value of `i` by `1`.

## Helpful links

- [Rust Documentation - Generators](https://doc.rust-lang.org/stable/book/ch19-06-macros.html#generators)
- [Rust Generators Tutorial](https://rust-lang.github.io/async-book/07_generators/01_introduction.html)

group: rust-generators