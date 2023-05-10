# How do I get the name of a variable in Rust?
// plain

You can get the name of a variable in Rust by using the `std::any::type_name` function. This function takes a reference to a type and returns a `&'static str` containing the name of the type.

## Example code

```rust
let x = 5;
let type_name = std::any::type_name::<&x>();
println!("Type of x is {}", type_name);
```

## Output example

```
Type of x is i32
```

## Code explanation

- `let x = 5;`: This declares a variable `x` with the value `5`.
- `let type_name = std::any::type_name::<&x>();`: This uses the `std::any::type_name` function to get the type name of the variable `x`. The `<&x>` syntax is used to specify the type of the variable.
- `println!("Type of x is {}", type_name);`: This prints the type name of the variable `x` to the console.

## Helpful links
- [std::any::type_name](https://doc.rust-lang.org/std/any/fn.type_name.html)

group: rust-variables