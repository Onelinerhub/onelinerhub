# How do I pass a variable as an argument to a function in Rust?
// plain

Passing a variable as an argument to a function in Rust is done by using the `&` operator. This operator allows the function to borrow the variable, rather than taking ownership of it.

## Example

```
fn main() {
    let x = 5;
    print_value(x);
}

fn print_value(value: &i32) {
    println!("The value is {}", value);
}
```
## Output example

```
The value is 5
```

The code above passes the variable `x` to the function `print_value` by using the `&` operator. This allows the function to borrow the variable, rather than taking ownership of it.

## Code explanation

- `let x = 5;`: This declares a variable `x` with the value `5`.
- `print_value(x);`: This passes the variable `x` to the function `print_value`.
- `fn print_value(value: &i32)`: This declares the function `print_value` which takes a parameter `value` of type `i32` and borrows it.
- `println!("The value is {}", value);`: This prints the value of the parameter `value`.

## Helpful links
- [Rust Reference - Functions](https://doc.rust-lang.org/reference/functions.html)
- [Rust Reference - Ownership](https://doc.rust-lang.org/reference/ownership.html)

group: rust-variables