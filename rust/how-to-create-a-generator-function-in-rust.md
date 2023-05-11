# How to create a generator function in Rust?
// plain

A generator function in Rust is a function that can be used to generate a sequence of values. It is defined using the `yield` keyword.

## Example

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

- `fn generator() -> impl Iterator<Item = i32>`: This is the function signature, which defines the return type as an iterator of type `i32`.
- `let mut i = 0`: This declares a mutable variable `i` and initializes it to `0`.
- `yield i`: This is the `yield` keyword, which is used to return a value from the generator.
- `i += 1`: This increments the value of `i` by `1`.

## Helpful links
- [Rust Generators](https://doc.rust-lang.org/stable/book/ch19-06-macros.html#generators)
- [Rust Iterators](https://doc.rust-lang.org/stable/book/ch13-02-iterators.html)

group: rust-generators