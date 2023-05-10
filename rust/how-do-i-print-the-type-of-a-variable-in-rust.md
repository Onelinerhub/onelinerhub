# How do I print the type of a variable in Rust?
// plain

You can print the type of a variable in Rust using the `std::any::type_name` function. This function takes a reference to a variable and returns a `&str` containing the type name.

## Example code

```rust
let x = 5;
println!("x is of type {}", std::any::type_name::<decltype(x)>());
```

## Output example

```
x is of type i32
```

## Code explanation

- `let x = 5;`: This declares a variable `x` with the value `5`.
- `std::any::type_name`: This is the function used to print the type of a variable.
- `<decltype(x)>()`: This is a type parameter that specifies the type of the variable `x`.
- `println!("x is of type {}", ...)`: This prints the type of the variable `x` to the console.

## Helpful links
- [std::any::type_name](https://doc.rust-lang.org/std/any/fn.type_name.html)

group: rust-variables