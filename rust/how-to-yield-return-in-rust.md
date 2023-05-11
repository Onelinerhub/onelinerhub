# How to yield return in Rust?
// plain

Rust provides the `yield` keyword to allow a function to return multiple values. It is used to create an iterator that can be used to iterate over a collection of values.

## Example code

```rust
fn main() {
    let mut iter = yield_return();
    for i in iter {
        println!("{}", i);
    }
}

fn yield_return() -> impl Iterator<Item = i32> {
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
4
...
```

## Code explanation

- `fn main()`: This is the main function that will be called when the program is executed.
- `let mut iter = yield_return()`: This creates an iterator from the `yield_return` function.
- `for i in iter`: This loop iterates over the values returned by the `yield_return` function.
- `yield i`: This is the `yield` keyword, which returns the value of `i` to the iterator.
- `i += 1`: This increments the value of `i` for the next iteration.

## Helpful links
- [Rust Documentation - Iterators](https://doc.rust-lang.org/stable/book/ch13-02-iterators.html)
- [Rust Documentation - Yield](https://doc.rust-lang.org/stable/book/ch13-02-iterators.html#yield)

group: rust-generators