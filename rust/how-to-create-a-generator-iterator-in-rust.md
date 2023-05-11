# How to create a generator iterator in Rust?
// plain

Creating a generator iterator in Rust is a simple process. To create a generator iterator, you must first define a function that returns a `yield` expression. The `yield` expression will return a value each time the generator is called.

## Example code

```
fn generator() -> impl Iterator<Item = i32> {
    let mut i = 0;
    loop {
        yield i;
        i += 1;
    }
}

let mut gen = generator();
println!("{}", gen.next().unwrap());
```

## Output example

```
0
```

## Code explanation


1. `fn generator() -> impl Iterator<Item = i32>`: This line defines a function called `generator` that returns an iterator of type `i32`.
2. `let mut i = 0`: This line declares a mutable variable `i` and sets its initial value to `0`.
3. `loop {`: This line starts an infinite loop.
4. `yield i`: This line yields the value of `i` each time the generator is called.
5. `i += 1`: This line increments the value of `i` by `1` each time the loop is executed.
6. `let mut gen = generator()`: This line creates a mutable variable `gen` and assigns it the value returned by the `generator` function.
7. `println!("{}", gen.next().unwrap())`: This line prints the value returned by the `next` method of the `gen` variable.

## Helpful links

- [Rust Generators](https://doc.rust-lang.org/stable/book/ch19-06-macros.html#generators)
- [Rust Iterators](https://doc.rust-lang.org/stable/book/ch13-02-iterators.html)

group: rust-generators