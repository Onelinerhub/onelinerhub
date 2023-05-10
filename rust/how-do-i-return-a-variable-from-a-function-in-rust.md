# How do I return a variable from a function in Rust?
// plain

You can return a variable from a function in Rust by using the `return` keyword.

## Example code

```
fn main() {
    let x = 5;
    let y = add_one(x);
    println!("{} + 1 = {}", x, y);
}

fn add_one(x: i32) -> i32 {
    return x + 1;
}
```

## Output example

```
5 + 1 = 6
```

## Code explanation


1. `let x = 5;` - This line declares a variable `x` with the value of `5`.
2. `let y = add_one(x);` - This line calls the `add_one` function with the argument `x` and assigns the return value to the variable `y`.
3. `fn add_one(x: i32) -> i32 {` - This line declares a function `add_one` which takes an argument `x` of type `i32` and returns a value of type `i32`.
4. `return x + 1;` - This line returns the value of `x + 1` from the `add_one` function.

## Helpful links

- [Rust Documentation - Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)

group: rust-variables