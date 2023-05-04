# Rust function example
// plain

A Rust function is a block of code that performs a specific task. It can take parameters, and can return a value. Here is an example of a Rust function that takes two parameters and returns the sum of them:

```
fn add_two_numbers(x: i32, y: i32) -> i32 {
    x + y
}
```

The output of this function would be the sum of the two parameters, for example:

```
add_two_numbers(2, 3) // Output: 5
```

The ## Code explanation


- `fn add_two_numbers(x: i32, y: i32) -> i32 {` - This is the function declaration, which includes the function name, parameters, and return type.
- `x + y` - This is the body of the function, which contains the code that will be executed when the function is called.
- `add_two_numbers(2, 3)` - This is an example of calling the function, passing in two parameters.

## Helpful links

- [Rust Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
- [Rust Function Syntax](https://doc.rust-lang.org/book/ch03-04-complex-types.html#function-syntax)

group: rust-examples