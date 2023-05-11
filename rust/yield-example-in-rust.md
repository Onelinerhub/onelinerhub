# Yield example in Rust
// plain

Yield is a feature of Rust that allows a function to pause its execution and return a value to the caller. It is similar to the return statement, but instead of returning a single value, it can return multiple values over time.

## Example code

```rust
fn main() {
    let mut counter = 0;
    let result = counter_generator(3);

    for x in result {
        println!("{}", x);
    }
}

fn counter_generator(x: i32) -> impl Iterator<Item = i32> {
    (0..x).map(|x| {
        counter += 1;
        counter
    })
}
```

## Output example

```
1
2
3
```

## Code explanation

- `fn main()`: This is the main function, which is the entry point of the program.
- `let mut counter = 0`: This declares a mutable variable `counter` and initializes it to 0.
- `let result = counter_generator(3)`: This calls the `counter_generator` function with the argument `3` and stores the result in the `result` variable.
- `for x in result`: This loop iterates over the values returned by the `counter_generator` function.
- `fn counter_generator(x: i32) -> impl Iterator<Item = i32>`: This is the `counter_generator` function, which takes an `i32` argument and returns an `Iterator` of `i32` values.
- `(0..x).map(|x| { counter += 1; counter })`: This uses the `map` method to iterate over the range `0..x` and increment the `counter` variable each time. The `counter` variable is then yielded to the caller.

## Helpful links
- [Rust Documentation - Yield](https://doc.rust-lang.org/book/ch13-01-closures.html#yielding-values-from-closures)

group: rust-generators