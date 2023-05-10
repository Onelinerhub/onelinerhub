# How do I determine the type of a variable in Rust?
// plain

The type of a variable in Rust can be determined using the `std::any::type_name` function. This function takes a reference to a variable and returns a string containing the type of the variable.

```rust
let x = 5;
println!("x is of type {}", std::any::type_name::<&x>());
```

## Output example

```
x is of type i32
```

The code above consists of the following parts:

1. `let x = 5;` - This declares a variable `x` with the value `5`.
2. `std::any::type_name::<&x>()` - This is a function call to `std::any::type_name` which takes a reference to the variable `x` as an argument.
3. `println!("x is of type {}", std::any::type_name::<&x>());` - This prints the type of the variable `x` to the console.

## Helpful links

- [std::any::type_name](https://doc.rust-lang.org/std/any/fn.type_name.html)

group: rust-variables